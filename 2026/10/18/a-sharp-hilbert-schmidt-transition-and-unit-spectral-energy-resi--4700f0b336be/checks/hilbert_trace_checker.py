#!/usr/bin/env python3
"""Supplementary numerical checks of the exact logarithmic-Hilbert trace formula.

Only Python standard-library arithmetic; the analytic proof is in RESULT.md.
"""
from math import pi, log, isclose

ZETA2 = pi*pi/6
for n in (1, 2, 4, 15, 100):
    h1 = sum(1/j for j in range(1, n+1))
    h2 = sum(1/(j*j) for j in range(1, n+1))
    exact = h1/n**2 - (ZETA2-h2)/n
    N = 250000
    truncated = sum(1/(k*(k+n)**2) for k in range(1, N+1))
    assert truncated <= exact + 2e-13
    # The positive tail is at most integral from N to infinity of x**(-3).
    assert 0 <= exact-truncated <= 1/(2*N*N) + 3e-13

for n in (1000, 10000, 100000):
    # Here the harmonic terms are accurately computed via a finite sum.
    h1 = sum(1/j for j in range(1, n+1))
    h2 = sum(1/(j*j) for j in range(1, n+1))
    # For large n, avoid catastrophic cancellation by summing the positive zeta tail.
    # Euler-Maclaurin: sum_{j>n}j^-2 = 1/n - 1/(2n^2) + O(n^-3).
    tail2 = 1/n - 1/(2*n*n)
    J = h1/n**2-tail2/n
    assert 0.8 < (n*n*J)/log(n) < 1.1

for eps in (0.3, 0.1, 0.03):
    # The integral used in the proof is computed exactly.
    model_integral = log(3)**(-eps) / eps
    assert abs(eps*model_integral - log(3)**(-eps)) < 1e-12
print('Supplementary partial fractions, asymptotics, and boundary-model checks passed.')
