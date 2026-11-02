#!/bin/sh
set -eu
cd "$(dirname "$0")"
PYTHONPATH=. python3 tree3_symbolic.py
c++ -O3 -std=c++17 tree3_direct.cpp -o /tmp/rooted_ancestor_direct_check
/tmp/rooted_ancestor_direct_check
