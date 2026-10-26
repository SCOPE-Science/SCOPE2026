#!/usr/bin/env python3
"""Independent finite-path enumeration and integral checks for the single-rate dimer defect.

Only the formulas and dynamics of the mathematical statement are used.
All infinite-volume and asymptotic assertions require the analytic proof.
"""
import math
from fractions import Fraction
from functools import lru_cache
from scipy.integrate import quad

COUNT = 0


def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)


def exact_path(n, center, strength):
    """Exact, rational weighted random-greedy law for n edges of a path."""
    rates = tuple(strength if i == center else Fraction(1) for i in range(n))
    zero = tuple(Fraction(0) for _ in range(n))

    @lru_cache(None)
    def solve(mask):
        if mask == 0:
            return zero
        active = [i for i in range(n) if (mask >> i) & 1]
        total = sum((rates[i] for i in active), Fraction(0))
        out = list(zero)
        for edge in active:
            # An accepted dimer blocks itself and adjacent edges.
            blocked = sum(1 << i for i in (edge - 1, edge, edge + 1) if 0 <= i < n)
            descendant = solve(mask & ~blocked)
            weight = rates[edge] / total
            for i, value in enumerate(descendant):
                out[i] += weight * (value + (i == edge))
        return tuple(out)

    return solve((1 << n) - 1)


def float_path(n, center, strength):
    rates = [strength if i == center else 1.0 for i in range(n)]

    @lru_cache(None)
    def solve(mask):
        if mask == 0:
            return (0.0,) * n
        active = [i for i in range(n) if (mask >> i) & 1]
        total = sum(rates[i] for i in active)
        out = [0.0] * n
        for edge in active:
            blocked = sum(1 << i for i in (edge - 1, edge, edge + 1) if 0 <= i < n)
            descendant = solve(mask & ~blocked)
            weight = rates[edge] / total
            for i, value in enumerate(descendant):
                out[i] += weight * (value + (i == edge))
        return tuple(out)

    return solve((1 << n) - 1)


def triangle_kernel(lam, j):
    """Integral without the alternating sign and factorial prefactor."""
    def integrate_x(x):
        inner = quad(lambda y: math.exp(x + y) * (x - y) ** (j - 1),
                     0, x, epsabs=2e-12, limit=200)[0]
        return (1 - lam * x ** (lam - 1)) * inner
    return quad(integrate_x, 0, 1, epsabs=2e-11, limit=250)[0]


def infinite_edge(lam, j):
    baseline = (1.0 - math.exp(-2.0)) / 2
    if j == 0:
        return math.exp(-2.0) * quad(
            lambda x: lam * x ** (lam - 1) * math.exp(2*x),
            0, 1, epsabs=1e-12, limit=250)[0]
    return baseline + (-1) ** (j - 1) * math.exp(-2) * triangle_kernel(lam, j) / math.factorial(j-1)


def run():
    base = (1 - math.exp(-2))/2
    # Exact first-edge order, symmetry, rate response in actual finite paths.
    for n in (7, 9, 11, 13):
        center = n // 2
        for lam in (Fraction(1, 3), Fraction(1), Fraction(2), Fraction(4)):
            vals = exact_path(n, center, lam)
            check(all(Fraction(0) <= v <= Fraction(1) for v in vals), 'probability interval')
            for j in range(center+1):
                check(vals[center+j] == vals[center-j], 'finite reflection')
            baseline_vals = exact_path(n, center, Fraction(1))
            if lam != 1:
                check((vals[center] - baseline_vals[center]) * (lam - 1) > 0,
                      'defect monotonicity')
                for j in range(1, center+1):
                    check((vals[center+j] - baseline_vals[center+j])
                          * (lam - 1) * (-1)**j > 0,
                          'finite alternating signs')
    # Infinite integral, independently computed finite-path conditioning.
    n = 25
    center = n // 2
    for lam in (0.4, 1.0, 2.0, 4.0):
        vals = float_path(n, center, lam)
        for j in range(0, 5):
            inf = infinite_edge(lam, j)
            check(abs(vals[center+j] - inf) < 7e-5,
                  f'finite/infinite mismatch strength={lam}, j={j}')
            check(abs(vals[center-j] - inf) < 7e-5,
                  f'finite reflection mismatch strength={lam}, j={j}')
            if j >= 1:
                check(abs(inf - base) <= 1 / math.factorial(j) + 1e-12,
                      'uniform factorial estimate')
                if lam != 1:
                    check((inf-base) * (lam-1) * (-1)**j > 0,
                          'infinite alternating sign')
    # Stable normalized factorial coefficient; does not subtract nearly equal quantities.
    for lam in (0.4, 2.0, 4.0):
        ratios = []
        for j in (7, 12, 21):
            # Written as a positivity-sensitive signed integral ratio:
            # ratio = (j(j+1) * integral)/(e*(1-lam)).
            ratio = math.exp(-1) * j * (j+1) * triangle_kernel(lam, j) / (1-lam)
            ratios.append(ratio)
            check(0.35 < ratio < 1.1, 'normalized asymptotic amplitude')
        check(abs(ratios[-1] - 1) < abs(ratios[0] - 1),
              'factorial coefficient convergence trend')
    print(f'PASS {COUNT} finite rational and analytical comparisons')


if __name__ == '__main__':
    run()
