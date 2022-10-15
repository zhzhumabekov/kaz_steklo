from django.conf import settings
from django.urls import path

from .views import index 

app_name = 'create_order'

urlpatterns = [
    path('', index, name='index'),
]