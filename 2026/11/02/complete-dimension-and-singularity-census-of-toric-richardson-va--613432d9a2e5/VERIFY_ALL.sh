#!/bin/sh
# Reproduce the complete finite combinatorial census with two independent mathematical tests.
set -eu
cd "$(dirname "$0")"
c++ -O3 -std=c++17 VERIFY_RPOLY.cpp -o verify_rpoly
c++ -O3 -std=c++17 VERIFY_CROWN.cpp -o verify_crown
./verify_rpoly 7 > rpoly_check.txt
./verify_crown 7 > crown_check.txt
grep -q '^VERIFY_OK$' rpoly_check.txt
grep -q '^VERIFY_OK$' crown_check.txt
printf 'VERIFY_OK\n'
