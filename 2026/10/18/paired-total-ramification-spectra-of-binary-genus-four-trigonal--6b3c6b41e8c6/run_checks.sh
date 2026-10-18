#!/bin/sh
set -eu
mkdir -p data
g++ -O3 -std=c++17 code/count_singular.cpp -o ./bidegree33_singular_enum
./bidegree33_singular_enum
python3 code/verify_negative.py
python3 code/branch_census.py
python3 code/verify_positive.py
python3 code/verify_sharp_bound.py
python3 code/verify_zeta_collision.py
rm -f ./bidegree33_singular_enum
