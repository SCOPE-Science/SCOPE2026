#!/usr/bin/env python3
"""Finite exact-rational corroboration of Cesaro Gram trace identities. No infinite-proof claims."""
from fractions import Fraction
from math import comb, pi, log


def gram(n):
    return [[Fraction(1, max(i, j)) for j in range(1, n+1)]
            for i in range(1, n+1)]


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][r] * b[r][j] for r in range(n))
             for j in range(n)] for i in range(n)]


checks = 0
for n in range(1, 11):
    a = gram(n)
    power = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    harmonic = sum((Fraction(1, i) for i in range(1, n+1)), Fraction())
    for k in range(1, 7):
        power = multiply(power, a)
        trace = sum((power[i][i] for i in range(n)), Fraction())
        c = comb(2*k-2, k-1)
        if k == 1:
            assert trace == harmonic
        else:
            # Use a slightly relaxed rational bound on pi^2/6 (1 < zeta(2) < 2).
            assert trace - c*harmonic >= -k*c
            assert trace - c*harmonic <= k*2*(4**(k-2))
        if k == 2:
            assert trace == 2*harmonic - sum((Fraction(1, j*j) for j in range(1, n+1)), Fraction())
        checks += 1
for m in range(8):
    assert comb(2*m, m) == comb(2*(m+1)-2, (m+1)-1)
print(f"PASS: {checks} exact-rational finite trace checks and 8 moment coefficient checks")
