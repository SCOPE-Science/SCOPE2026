"""Reproduce numerical checks for a single weighted chord in greedy dimer adsorption.

Python 3 standard library only. Numerical tests are not a substitute for the proof.
"""
from functools import lru_cache
from math import exp, isclose

@lru_cache(maxsize=None)
def expected_dimers(edges):
    """Exact first-clock decomposition, evaluated in double precision."""
    if not edges:
        return 0.0
    total_rate = sum(rate for _, _, rate in edges)
    total = 0.0
    for u, v, rate in edges:
        remaining = tuple((a, b, r) for a, b, r in edges
                          if a not in (u, v) and b not in (u, v))
        total += rate / total_rate * (1.0 + expected_dimers(remaining))
    return total


def cycle(n, chord_distance=None, chord_rate=1.0):
    assert n >= 5
    edges = [(u, (u + 1) % n, 1.0) for u in range(n)]
    if chord_distance is not None:
        assert 2 <= chord_distance <= n - 2
        assert chord_rate > 0
        edges.append((0, chord_distance, float(chord_rate)))
    return tuple(edges)


def limit_defect(rate, steps=160000):
    """Midpoint quadrature in uniform beta-quantile coordinates."""
    assert rate > 0
    h = 1.0 / steps
    total = 0.0
    for j in range(steps):
        quantile = (j + 0.5) * h
        u = 1.0 - (1.0 - quantile) ** (1.0 / rate)
        total += exp(-2.0 * u) * (2.0 * u - 1.0)
    return exp(-2.0) * h * total


def run():
    vals = []
    for rate in (0.25, 0.5, 1.0, 2.0):
        theoretical = limit_defect(rate)
        actual = expected_dimers(cycle(20, 10, rate)) - expected_dimers(cycle(20))
        assert abs(actual - theoretical) < 0.0002, (rate, actual, theoretical)
        vals.append(theoretical)
        print(f'rate={rate:g}: limit={theoretical:+.12f} finite C20={actual:+.12f}')
    assert all(a > b for a, b in zip(vals, vals[1:]))
    assert vals[0] > 0 > vals[1]
    assert isclose(vals[2], -exp(-4), abs_tol=3e-10)
    assert isclose(limit_defect(0.0001), exp(-4), abs_tol=5e-5)
    assert isclose(limit_defect(10000), -exp(-2), abs_tol=6e-5)
    assert expected_dimers(cycle(12)) > 0
    print('All finite-chain and limiting-formula checks passed.')

if __name__ == '__main__':
    run()
