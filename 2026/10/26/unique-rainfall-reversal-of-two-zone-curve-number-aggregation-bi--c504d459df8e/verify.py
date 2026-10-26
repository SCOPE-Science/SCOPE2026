"""Reproducible checks for the two-zone SCS curve-number aggregation theorem.

Run with Python 3: python verify.py
The checks are finite diagnostics, not a replacement for the analytic proof.
"""
from fractions import Fraction
from math import isfinite
import random


def runoff(p, c, lam):
    s = (1.0 - c) / c
    if p <= lam * s:
        return 0.0
    return (p - lam * s) ** 2 / (p + (1.0 - lam) * s)


def gap(p, x, y, w, lam):
    z = w * x + (1.0 - w) * y
    return w * runoff(p, x, lam) + (1.0 - w) * runoff(p, y, lam) - runoff(p, z, lam)


def polynomial(p, x, y, w, lam):
    z = w * x + (1.0 - w) * y
    gamma = 1.0 - lam
    dx = x * p + gamma * (1.0 - x)
    dy = y * p + gamma * (1.0 - y)
    dz = z * p + gamma * (1.0 - z)
    return lam * lam * dx * dy * dz - p * p * (p - gamma) * x * y * z


def gap_formula(p, x, y, w, lam):
    z = w * x + (1.0 - w) * y
    gamma = 1.0 - lam
    dx = x * p + gamma * (1.0 - x)
    dy = y * p + gamma * (1.0 - y)
    dz = z * p + gamma * (1.0 - z)
    return (w * (1 - w) * (y - x) ** 2 * polynomial(p, x, y, w, lam)
            / (gamma * x * y * z * dx * dy * dz))


def crossing(x, y, w, lam):
    onset = lam * (1.0 / y - 1.0)
    lo = max(onset + 1e-10, 1e-10)
    hi = max(1.0, lam * (1.0 / x - 1.0) + 1.0)
    while gap(hi, x, y, w, lam) >= 0:
        hi *= 2.0
        assert hi < 1e9
    assert gap(lo, x, y, w, lam) > 0
    for _ in range(105):
        mid = 0.5 * (lo + hi)
        if gap(mid, x, y, w, lam) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def fraction_runoff(p, c, lam):
    s = (1 - c) / c
    return Fraction(0) if p <= lam * s else (p - lam * s) ** 2 / (p + (1 - lam) * s)


def checks():
    lam = Fraction(1, 5)
    x, y, w = Fraction(2, 5), Fraction(1, 2), Fraction(1, 2)
    z = w * x + (1 - w) * y
    def e(p):
        return w * fraction_runoff(p, x, lam) + (1-w) * fraction_runoff(p, y, lam) - fraction_runoff(p, z, lam)
    assert e(Fraction(1)) == Fraction(59, 117480)
    assert e(Fraction(2)) == Fraction(-13123, 2701440)
    root = crossing(float(x), float(y), float(w), float(lam))
    assert abs(root - 1.1001452368129525) < 1e-10

    rng = random.Random(20261024)
    n_finite = n_root = 0
    for _ in range(2400):
        x = rng.uniform(.04, .84)
        y = rng.uniform(x + .001, 1.0)
        w = rng.uniform(.02, .98)
        lam = rng.uniform(.03, .92)
        p_x = lam * (1.0 / x - 1.0)
        p_y = lam * (1.0 / y - 1.0)
        p = p_x + rng.uniform(.02, 8.0)
        measured = gap(p, x, y, w, lam)
        predicted = gap_formula(p, x, y, w, lam)
        assert abs(measured - predicted) < 1e-9 * (1 + abs(measured))
        n_finite += 1
        root = crossing(x, y, w, lam)
        assert root > max(p_y, 1.0 / (1.0 + lam)) - 5e-7
        assert isfinite(root)
        for t in range(1, 21):
            pp = p_y + (root - p_y) * t / 21.0
            assert gap(pp, x, y, w, lam) > -1e-9
            qq = root + (max(root, 1.0) * 4.0) * t / 21.0
            assert gap(qq, x, y, w, lam) < 1e-9
        n_root += 1
    print('Exact CN 40/50 benchmark, positive and negative rational gaps: passed')
    print('Two-zone exact rational identity comparisons:', n_finite)
    print('Numerical crossover brackets and sign tests:', n_root, 'configurations,', 40*n_root, 'sign evaluations')
    print('Analytical global uniqueness and coefficient signs: proved in RESULT.md, not inferred from these tests')


if __name__ == '__main__':
    checks()
