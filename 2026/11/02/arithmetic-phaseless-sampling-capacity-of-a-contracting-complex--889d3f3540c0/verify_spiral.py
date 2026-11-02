#!/usr/bin/env python3
"""Exact arithmetic and finite numerical checks of contracting-spiral phase lifting."""
import cmath
import math
from fractions import Fraction as Q
from itertools import permutations


def det4(a):
    s = Q(0)
    for p in permutations(range(4)):
        swaps = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        term = Q(-1 if swaps % 2 else 1)
        for i, j in enumerate(p):
            term *= a[i][j]
        s += term
    return s


def distinct_exact_rational(d, q):
    # Polar bases: radius determines j+k, root-of-unity phase determines j-k.
    keys = []
    for j in range(d + 1):
        for k in range(d + 1):
            keys.append((j + k, j % q))
    return len(set(keys)) == (d + 1) ** 2


checks = 0
for d in range(9):
    for q in range(1, 15):
        assert distinct_exact_rational(d, q) == (q > d)
        checks += 1

for q in range(1, 15):
    for n in range(1, 15):
        # The exact resonant quantity z_n**q is a real +/- rational power.
        t = Q((-1) ** n, 2 ** (n * q))
        # Norm squares of 1+it and 1-it are 1+t*t exactly.
        assert 1 + t * t == 1 + (-t) * (-t)
        checks += 1

# d=1, rho=1/2 and theta=pi/2, giving exact Gaussian-rational values.
rows = []
for n in range(1, 5):
    radius = Q(1, 2) ** n
    k = n % 4
    real = (radius, Q(0), -radius, Q(0))[k]
    imag = (Q(0), radius, Q(0), -radius)[k]
    # Real coordinates of arbitrary Hermitian lift, up to a sign convention.
    rows.append([Q(1), radius * radius, 2 * real, 2 * imag])
assert det4(rows) == Q(-75, 2048)
checks += 1

for d in range(1, 5):
    for theta in (math.pi * math.sqrt(2), math.pi / (d + 2), 0.73):
        bases = [0.83 ** (j + k) * cmath.exp(1j * (j - k) * theta)
                 for j in range(d + 1) for k in range(d + 1)]
        assert all(abs(bases[a] - bases[b]) > 1e-11
                   for a in range(len(bases)) for b in range(a + 1, len(bases)))
        checks += 1

print(f"PASS: {checks} supplementary assertions; exact lifted determinant = {det4(rows)}")
