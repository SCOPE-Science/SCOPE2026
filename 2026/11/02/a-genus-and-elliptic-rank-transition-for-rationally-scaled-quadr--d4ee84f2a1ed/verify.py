#!/usr/bin/env python3
"""Exact finite checks for rationally scaled quadratic-shift equations.

Run with Python 3's standard library only; finite checks do not prove Faltings'
result or the algebraic smoothness argument.
"""
from fractions import Fraction as Q
from math import comb


def form(k, d, u, lam):
    return sum(Q(comb(k, j) * d ** ((j-1)//2))
               * u ** (k-j) * lam ** (j-1)
               for j in range(1, k+1, 2))


def multiply_by_radical_binomial(k, d, u, lam):
    # Represent (u-lam*sqrt(d))**k by A+B*sqrt(d).
    A, B = Q(1), Q(0)
    for _ in range(k):
        A, B = A*u-B*lam*d, B*u-A*lam
    return A, B


def add(P, R, b=-13500):
    if P is None:
        return R
    if R is None:
        return P
    x, y = P
    z, w = R
    if x == z and y == -w:
        return None
    if P == R:
        if y == 0:
            return None
        slope = (3*x*x)/(2*y)
    else:
        slope = (w-y)/(z-x)
    X = slope*slope-x-z
    Y = slope*(x-X)-y
    assert Y*Y == X**3+b
    return X, Y


conic = set()
for j in range(-20, 21):
    t = Q(j, 100)
    U = (2*t*t-4*t-1)/(2*t*t+1)
    V = (1-2*t-2*t*t)/(2*t*t+1)
    u, lam = U/3, V/3
    assert lam > 0 and form(3, 6, u, lam) == 1
    conic.add((u, lam))
assert len(conic) == 41

P = Q(60), Q(450)
assert P[1]**2 == P[0]**3 - 13500
R = None
multiples = []
for _ in range(7):
    R = add(R, P)
    assert R is not None
    X, Y = R
    assert X > 0 and Y != 0
    u, lam = Q(15)/X, abs(Y)/(Q(30)*X)
    assert lam > 0 and form(4, 15, u, lam) == 1
    multiples.append(R)
assert multiples[1] == (Q(24), Q(-18))
assert multiples[4][0] == Q(167460, 3721)
assert multiples[4][0].denominator != 1

identity_checks = 0
for k in range(2, 19):
    for d, u, lam in [(6, Q(-1, 3), Q(1, 3)),
                       (15, Q(1, 4), Q(1, 4)),
                       (7, Q(2, 5), Q(3, 11))]:
        A, B = multiply_by_radical_binomial(k, d, u, lam)
        assert A.denominator > 0
        assert B == -lam * form(k, d, u, lam)
        identity_checks += 1

print('VERIFY_OK conic_points=%d elliptic_multiples=%d '
      'nonintegral_5P_x=%s binomial_checks=%d rational_arithmetic=yes'
      % (len(conic), len(multiples), multiples[4][0], identity_checks))
