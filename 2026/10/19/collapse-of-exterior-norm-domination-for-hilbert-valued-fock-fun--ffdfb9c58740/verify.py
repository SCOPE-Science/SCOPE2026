#!/usr/bin/env python3
"""Exact supplementary checks for the exterior Hilbert-valued Fock witnesses."""
from fractions import Fraction as F
from math import factorial


def multiply(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai*bj
    return c


def witness(s, A):
    q = multiply([-s, F(1)], multiply([-A, F(1)], [-A, F(1)]))
    direct = [-(s*A*A), A*A + 2*A*s, -(2*A+s), F(1)]
    assert q == direct
    assert all(t >= s and sum(q[i]*t**i for i in range(4)) >= 0 for t in [s, s+1, s+2, s+A])
    norm_diff = sum(v*factorial(k) for k, v in enumerate(q))
    split = [max(F(0), v) for v in q], [max(F(0), -v) for v in q]
    assert all(a-b==v for a,b,v in zip(*split, q))
    assert norm_diff == (1-s)*A*A + (2*s-4)*A+6-2*s
    return norm_diff

assert witness(F(1),F(3)) == -2
for s, A in [(F(1),F(3)),(F(2),F(3)),(F(4),F(8)),(F(9),F(8))]:
    assert witness(s,A)<0
print('VERIFY_OK 4 exact exterior witnesses; factorial moments and coefficient signs')
