#!/usr/bin/env python3
"""Finite numerical checks for a harmonic annulus concentration spectrum.

Run with: python3 verify.py
The identities for infinitely many Fourier modes require the accompanying proof.
"""
import math


def spectral_pair(n, L):
    if n == 0:
        return ((2.0 - math.sqrt(3.0)) / 4.0,
                (2.0 + math.sqrt(3.0)) / 4.0)
    x = n * L
    q = (math.cosh(x) - 1.0) / math.sqrt(math.sinh(x) ** 2 - x ** 2)
    return ((1.0 - q) / 2.0, (1.0 + q) / 2.0)


def integrate_simpson(f, lo, hi, steps=2000):
    h = (hi - lo) / steps
    total = f(lo) + f(hi)
    for k in range(1, steps):
        total += (4.0 if k % 2 else 2.0) * f(lo + k * h)
    return total * h / 3.0


def matrix_pair(n, L):
    h = L / 2.0
    if n == 0:
        basis = (lambda t: 1.0, lambda t: t)
    else:
        basis = (lambda t: math.exp(n * t), lambda t: math.exp(-n * t))
    gram = [[integrate_simpson(lambda t, i=i, j=j: basis[i](t) * basis[j](t), -h, h)
             for j in range(2)] for i in range(2)]
    inner = [[integrate_simpson(lambda t, i=i, j=j: basis[i](t) * basis[j](t), -h, 0.0)
              for j in range(2)] for i in range(2)]
    g00, g01, g11 = gram[0][0], gram[0][1], gram[1][1]
    h00, h01, h11 = inner[0][0], inner[0][1], inner[1][1]
    detg = g00 * g11 - g01 * g01
    deth = h00 * h11 - h01 * h01
    mixed = h00 * g11 + h11 * g00 - 2.0 * h01 * g01
    disc = max(0.0, mixed * mixed - 4.0 * detg * deth)
    return ((mixed - math.sqrt(disc)) / (2.0 * detg),
            (mixed + math.sqrt(disc)) / (2.0 * detg))


checks = 0
for length in (0.2, 0.5, 0.9, 1.5, 2.0):
    previous_low = 1.0
    for degree in range(9):
        pair = spectral_pair(degree, length)
        numerical = matrix_pair(degree, length)
        for a, b in zip(pair, numerical):
            assert abs(a - b) < 2e-8, (degree, length, a, b)
            checks += 1
        assert abs(sum(pair) - 1.0) < 1e-12
        checks += 1
        assert 0.0 < pair[0] < (2.0 - math.sqrt(3.0)) / 4.0 + 1e-12
        checks += 1
        assert pair[0] * (1.0 - pair[0]) <= 1.0 / 16.0 + 1e-12
        checks += 1
        if degree > 0:
            assert pair[0] < previous_low
            checks += 1
        previous_low = pair[0]
for x in (8.0, 10.0, 12.0):
    low = spectral_pair(1, x)[0]
    assert abs(low / math.exp(-x) - 1.0) < 0.04
    checks += 1
for length in (0.1, 0.5, 3.0):
    low = spectral_pair(0, length)[0]
    assert abs(low * (1.0 - low) - 1.0 / 16.0) < 1e-14
    checks += 1
print('PASS: %d finite checks; analytic proof required for all-mode statements.' % checks)
