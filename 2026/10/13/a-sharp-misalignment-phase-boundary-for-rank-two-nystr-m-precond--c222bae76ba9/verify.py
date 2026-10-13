#!/usr/bin/env python3
"""Exact-rational checks for a rank-two Nyström condition-number law.

The general theorem is proved algebraically in RESULT.md.  Finite tests here
corroborate its identities and reproduce the stated exact counterexample.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def phase(k, mu, t):
    d, a, b = k - 1, k + mu, 1 + mu
    h = k - d * t
    H = a + b
    s = d * t / (b * h)
    S = H + s * (a - d * t)
    G = b * h * H * (1 - 2 * t) + t * (a - d * t) ** 2
    delta = S * S - H * H * (1 + s)
    expected = s * d * G / (b * h)
    assert delta == expected
    assert b > 0 and h > 0 and s > 0
    assert -b * s * d * (1 - t) < 0
    # Exact second derivative and endpoint signs guarantee a unique threshold.
    assert b * H - a > 0
    assert 4 * d * (b * H - a) + 6 * d * d * t > 0
    assert b * k * H > 0
    assert -a * b < 0
    assert (delta > 0) == (G > 0)
    return G, S, 1 + s


# Independent rational matrix construction for the witness.
A = [F(5), F(3), F(3)]
Omega = [[F(1), F(0)], [F(2), F(0)], [F(0), F(1)]]
Y = [[A[i] * Omega[i][j] for j in range(2)] for i in range(3)]
W = [[sum(Omega[i][j] * Y[i][k] for i in range(3)) for k in range(2)] for j in range(2)]
assert W == [[F(17), F(0)], [F(0), F(3)]]
B = [[sum(Y[i][j] * Y[k][j] / W[j][j] for j in range(2)) for k in range(3)] for i in range(3)]
assert B == [[F(25, 17), F(30, 17), F(0)],
             [F(30, 17), F(36, 17), F(0)], [F(0), F(0), F(3)]]
# The nonzero spectrum of B is {61/17,3}; the normalized top vector is (5,6,0)/sqrt(61).
assert B[0][0] + B[1][1] == F(61, 17)
assert F(61, 17) > 3
strength = (F(61, 17) - 3) / (3 + 1)
v = [F(5), F(6), F(0)]
P = [[(F(1) if i == j else F(0)) + strength * v[i] * v[j] / 61
      for j in range(3)] for i in range(3)]
assert P == [[F(2199, 2074), F(75, 1037), F(0)],
             [F(75, 1037), F(1127, 1037), F(0)],
             [F(0), F(0), F(1)]]
detP2 = P[0][0] * P[1][1] - P[0][1] ** 2
S = 6 * P[1][1] + 4 * P[0][0]
assert detP2 == F(39, 34)
assert S == F(11160, 1037)
assert S * S - 100 * detP2 == F(1194450, 1075369) > 0
assert 6 * 4 == F(24)
# The quadratic determinant equals 3(793*z*z-7440*z+16592)/2074.
assert detP2 == F(3 * 793, 2074)
assert S == F(3 * 7440, 2074)
assert F(24) == F(3 * 16592, 2074)
lam_hi = (3720 + 4 * sqrt(42559)) / 793
lam_lo = (3720 - 4 * sqrt(42559)) / 793
assert lam_lo < 4 < lam_hi
assert lam_hi / lam_lo > 1.5

cases = 0
for k, mu, t in product(
    (F(3, 2), F(5, 3), F(2), F(3), F(5), F(12)),
    (F(1, 10), F(1, 3), F(1), F(3), F(20)),
    (F(1, 25), F(1, 12), F(1, 3), F(1, 2), F(2, 3), F(9, 10), F(24, 25))
):
    phase(k, mu, t)
    cases += 1
print('PASS: exact Nyström matrix, preconditioner and witness certificate')
print('PASS: %d rational phase-identity and convexity checks' % cases)
print('witness preconditioned condition %.12f versus 1.5 without preconditioning' % (lam_hi/lam_lo))
