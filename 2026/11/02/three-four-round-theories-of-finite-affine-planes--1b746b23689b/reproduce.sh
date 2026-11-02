#!/bin/sh
set -eu
g++ -std=c++17 -O3 -o affine_types affine_types.cpp
./affine_types 2 3 4 5 7
python3 affine_independent.py
python3 affine_atlas.py
