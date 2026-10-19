"""Reproducibility checks for first-Hermite spectrogram disk and annulus formulas.

Usage: python3 check.py  (Python 3 standard library only).
The proof for all modes and all radii is analytic; these are finite diagnostics.
"""
import math


def density(m, t):
    return math.exp(-t) * (t if m == 0 else t**(m - 1) * (m-t)**2 / math.factorial(m))


def lambda_closed(m, t):
    if m == 0:
        return 1 - (1 + t) * math.exp(-t)
    p = 1 - math.exp(-t) * sum(t**j / math.factorial(j) for j in range(m))
    return p + (m-1-t) * math.exp(-t) * t**m / math.factorial(m)


def integral_simpson(func, lo, hi, N=12000):
    assert N > 0 and N % 2 == 0
    step = (hi - lo) / N
    acc = func(lo) + func(hi)
    for k in range(1, N):
        acc += (4 if k % 2 else 2) * func(lo + k * step)
    return acc * step / 3


for T in (0.42, 1.0, 1.8, 3.5):
    for m in range(16):
        numerical = integral_simpson(lambda s: density(m, s), 0.0, T)
        closed = lambda_closed(m, T)
        assert abs(numerical - closed) < 2e-10, (m, T, numerical, closed)
        if m < 15:
            predicted = (math.exp(-T) * T**m / math.factorial(m)
                         * (m-T) * (m+1-T) / (m+1))
            assert abs(closed - lambda_closed(m+1, T) - predicted) < 2e-12

energy = 1 - 2 / math.e
vals = [lambda_closed(m, 1.0) for m in range(40)]
assert all(abs(vals[m] - energy) < 1e-12 for m in range(3))
assert all(vals[m] > vals[m+1] for m in range(2, 36))

a = 1 / (math.e - 1)
annular = integral_simpson(lambda t: density(0, t), a, a+1)
formula = (1 - math.exp(-1)) * math.exp(-a)
assert abs(annular - formula) < 2e-11
assert formula > energy
assert abs((1/math.e) * (a+1) - a) < 1e-14
assert abs(math.pi*((math.sqrt((a+1)/math.pi))**2-(math.sqrt(a/math.pi))**2)-1) < 1e-12
print("verified disk", energy, "annular lower bound", formula, "gain", formula - energy)
print("checks: independent quadrature, formulas, signs and area normalization")
