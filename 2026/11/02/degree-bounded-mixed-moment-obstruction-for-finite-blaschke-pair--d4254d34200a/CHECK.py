#!/usr/bin/env python3
"""Reproducible finite checks for the degree-bounded mixed-moment result.

The all-positive-degree theorem is proved analytically in RESULT.md.
"""
from math import gcd

for d in range(1, 31):
    for e in range(1, 31):
        maximum = max(j*(d-k)+(e-j)*k
                      for j in range(e+1) for k in range(d+1))
        assert maximum == d*e, (d, e, maximum)
        if gcd(d, e) == 1:
            solutions = [(m,n) for m in range(1,e+1)
                         for n in range(1,d+1) if d*m == e*n]
            assert solutions == [(e,d)], (d,e,solutions)
        if d == e == 1:
            assert 1 / (d*e) == 1

print("PASS: 900 rectangular-degree and coprime-monomial finite checks")
