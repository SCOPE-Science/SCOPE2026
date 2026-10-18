"""Independent finite diagnostics for the square-root conclave clock theorem.

Requires Python 3, numpy and scipy. Finite tests do not replace the asymptotic proof.
Run: python verify.py
"""
import math
from fractions import Fraction

import numpy as np
from scipy.stats import binom

checks = 0
for n in (3, 4, 5, 8, 12, 20, 32):
    for c in (0.0, 0.5, 1.0, 2.0):
        alpha = c / math.sqrt(n)
        for a in range(1, n):
            theta = alpha * math.log(a / (n - a))
            p = 1 / (1 + math.exp(-theta))
            h = p**n + (1 - p)**n
            identity = math.cosh(n * theta / 2) / math.cosh(theta / 2)**n
            assert math.isclose(h / (2 ** (1-n)), identity, rel_tol=2e-11, abs_tol=2e-11)
            checks += 1

for n in range(2, 70):
    exact = Fraction(1, 2)**n + Fraction(1, 2)**n
    assert exact == Fraction(1, 2**(n-1))
    checks += 1

for c in (0.0, 0.5, 1.0, 2.0):
    estimates = []
    for n in (40, 80, 160, 320, 640):
        a = np.arange(1, n)
        alpha = c / np.sqrt(n)
        p = 1 / (1 + ((n-a)/a)**alpha)
        Q = binom.pmf(a[None, :], n, p[:, None])
        h = p**n + (1 - p)**n
        assert np.max(np.abs(Q.sum(axis=1) + h - 1)) < 2e-12
        checks += 1
        pi = binom.pmf(a, n, 0.5)
        pi /= pi.sum()
        for _ in range(20):
            pi = pi @ Q
            pi /= pi.sum()
        estimate = float(np.dot(pi, h) * (2**(n-1)))
        estimates.append(estimate)
        target = math.exp(c*c/2)
        if n == 640:
            assert abs(estimate / target - 1) < 0.016, (c, estimate, target)
            checks += 1
        if c == 0:
            assert math.isclose(estimate, 1, abs_tol=3e-11)
            checks += 1
    if c > 0:
        assert abs(estimates[-1] - math.exp(c*c/2)) < abs(estimates[0] - math.exp(c*c/2))
        checks += 1
    print(f'c={c:.1f} n=40,80,160,320,640; normalized rates={estimates}; target={math.exp(c*c/2):.12g}')
print(f'PASS: {checks} finite deterministic diagnostics; analytic proof needed for all asymptotic claims.')
