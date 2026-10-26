#!/bin/sh
# Run in a clean writable directory with the supplied scripts available.
set -eu
SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
CXX=${CXX:-g++}
"$CXX" -std=c++17 -O3 "$SCRIPT_DIR/incidence_scan.cpp" -o ./incidence_scan
"$CXX" -std=c++17 -O3 "$SCRIPT_DIR/jacobian_rank.cpp" -o ./jacobian_rank
"$CXX" -std=c++17 -O3 "$SCRIPT_DIR/hermitian_orbit.cpp" -o ./hermitian_orbit
./incidence_scan
./jacobian_rank
./hermitian_orbit
python "$SCRIPT_DIR/independent_scan.py"
cmp tangent_noline_codes.txt tangent_noline_python.txt
printf 'Independent incidence and orbit checks agree.\n'
