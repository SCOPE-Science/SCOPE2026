#!/usr/bin/env python3
"""Supplementary finite sanity checks; full proof is analytical."""
from fractions import Fraction
from math import gcd, cos, pi, isclose
n, k, epsilon, delta = 9, 1, 1, -1
N, S = n+k, n*n+n*k+k*k
assert Fraction(N*N-S, N**3) == Fraction(9,1000)
assert Fraction(N*N-2*S, N**3) == Fraction(-41,500)
g = gcd(n,k)
L = (n-k)//g
levels = sorted((-2*delta*cos(2*pi*q/L) for q in range(L)), reverse=True)
positive = [t for t in levels if t > 1e-10]
assert len(positive) == 3
assert isclose(positive[0], 2.0, rel_tol=0, abs_tol=1e-12)
assert all(isclose(t, 2**0.5, rel_tol=0, abs_tol=1e-12) for t in positive[1:])
def signed_index(s):
    return g*sum(sigma > s for sigma in levels)
assert (signed_index(1),signed_index(1.5),signed_index(2.1)) == (3,1,0)
print('PASS: exact rational jets, candidate wall multiplicities, and index example')
