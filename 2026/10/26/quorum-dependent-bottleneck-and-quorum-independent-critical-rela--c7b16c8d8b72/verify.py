"""Exact coefficient checks and numerical bottleneck tests for a collective-risk model.

Run: python verify.py
Uses the Python standard library only.
"""
from fractions import Fraction
from math import comb, pi, sqrt

checks = 0
for N in range(3, 31):
    n = N - 1
    for M in range(2, N):
        a, d = M - 1, N - M
        p = Fraction(a, n)
        peak = Fraction(comb(n, a)) * p ** a * (1 - p) ** d
        h = p * (1 - p)
        neg_second = peak * Fraction(n ** 3, a * d)
        assert neg_second > 0 and peak > 0
        assert h * neg_second / 2 == peak * n / 2
        assert Fraction(2, peak * n) > 0
        checks += 4

def simpson(fun, lo, hi, even_steps):
    step = (hi - lo) / even_steps
    total = fun(lo) + fun(hi)
    for k in range(1, even_steps):
        total += (4 if k & 1 else 2) * fun(lo + k * step)
    return total * step / 3

for N, M in ((3, 2), (5, 3), (7, 2), (8, 5), (11, 7)):
    n, a, d = N - 1, M - 1, N - M
    p = a / n
    peak = comb(n, a) * p ** a * (1 - p) ** d
    width = min(p, 1 - p) / 3
    target = pi * sqrt(2 * n / (peak * a * d))
    ratios = []
    for eps in (0.001, 0.0001):
        f = lambda x: 1 / (x * (1 - x) * (eps + peak - comb(n, a) * x ** a * (1 - x) ** d))
        T = simpson(f, p - width, p + width, 120000)
        ratios.append(sqrt(eps) * T / target)
        assert 0.75 < ratios[-1] < 1.10
        checks += 1
    assert abs(ratios[1] - 1) < abs(ratios[0] - 1)
    checks += 1
print('PASS:', checks, 'exact/numerical assertions; numerical limits are corroboration, not proof')
