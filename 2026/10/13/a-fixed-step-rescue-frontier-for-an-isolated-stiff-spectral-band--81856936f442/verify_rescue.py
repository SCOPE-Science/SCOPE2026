#!/usr/bin/env python3
"""Supplementary deterministic checks for a two-Euler-step spectral-band minimax law.

Requires only Python's standard library. Finite checks do not prove the theorem.
"""
from fractions import Fraction
from math import sqrt, isclose
from random import Random

ROOT2 = sqrt(2.0)
C = ROOT2 - 1.0


def exact_formula(x, y):
    """Parameters must satisfy 2 < x < y."""
    threshold = 1.0 + C * (y - 1.0)
    if x <= threshold:
        d = C * (y - 1.0)
        t = 1.0 / (1.0 + 2.0 * d)
        m = d * d / (1.0 + 2.0 * d)
        return t, m, 'interior'
    den = x * (x - 1.0) + y * (y - 1.0)
    t = (x + y - 2.0) / den
    m = (x - 1.0) * (y - 1.0) * (y - x) / den
    return t, m, 'endpoint'


def interval_norm(t, x, y):
    """Exact formula for continuous interval supremum of |quadratic|."""
    def f(z):
        return (z - 1.0) * (1.0 - t * z)
    vals = [abs(f(x)), abs(f(y))]
    z = (1.0 + t) / (2.0 * t)
    if x < z < y:
        vals.append(abs(f(z)))
    return max(vals)


def run():
    rng = Random(310472)
    numeric_cases = 0
    perturbations = 0
    for _ in range(1600):
        x = 2.0 + 10.0 ** rng.uniform(-3.0, 2.0)
        y = x * (1.0 + 10.0 ** rng.uniform(-3.0, 2.0))
        t, m, branch = exact_formula(x, y)
        assert 0.0 < t < 1.0 / x < 0.5
        actual = interval_norm(t, x, y)
        assert isclose(m, actual, rel_tol=5e-12, abs_tol=3e-10)
        for _ in range(12):
            h = t * (0.25 + 1.5 * rng.random())
            assert interval_norm(h, x, y) >= m - 3e-10 * (1.0 + m)
            perturbations += 1
        numeric_cases += 1

    # Check the endpoint branch's algebra in exact rational arithmetic.
    rational_cases = 0
    for _ in range(1200):
        base = rng.randint(3, 30)
        x = Fraction(base * 100 + rng.randrange(1, 100), 100)
        y = x + Fraction(rng.randrange(1, 100), 100)
        assert float(x) > (1.0 + C * (float(y) - 1.0))
        den = x * (x - 1) + y * (y - 1)
        h = (x + y - 2) / den
        m = (x - 1) * (y - 1) * (y - x) / den
        f = lambda z: (z - 1) * (1 - h * z)
        assert f(x) == m and f(y) == -m
        rational_cases += 1

    # At wide-band endpoint, y=4+2sqrt(2), the minimax norm is exactly 1.
    y = 4.0 + 2.0 * ROOT2
    x = 2.25
    t, m, branch = exact_formula(x, y)
    assert branch == 'interior' and isclose(m, 1.0, abs_tol=2e-15)
    for width in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]:
        ylarge = Fraction(10**8)
        xlarge = ylarge - width
        den = xlarge * (xlarge - 1) + ylarge * (ylarge - 1)
        mlarge = (xlarge - 1) * (ylarge - 1) * (ylarge - xlarge) / den
        assert abs(float(mlarge - width / 2)) < 4e-7
    print('VERIFY_OK', numeric_cases, 'bands,', perturbations,
          'alternative steps,', rational_cases,
          'exact endpoint identities, wide-boundary and bandwidth checks')

if __name__ == '__main__':
    run()
