#!/usr/bin/env python3
"""Standalone finite arithmetic checks for the explicit Cesaro singular-density law.
Requires Python 3.9+ standard library only; these tests do not prove limits.
"""
import cmath
import math


def symbol(w, xi):
    return abs(w) / math.sqrt((xi * xi + 0.25) * ((xi + w) ** 2 + 0.25))


def density(w, t):
    w = abs(w)
    if not w or t >= 2:
        return 0.0
    qp = (w * w - 1) / 4 + w * math.sqrt(1 - t * t / 4) / t
    qm = (w * w - 1) / 4 - w * math.sqrt(1 - t * t / 4) / t
    return (math.sqrt(max(qp, 0)) - math.sqrt(max(qm, 0))) / math.pi


def grid_density(w, t, step=0.0008, bound=50):
    # Positive-level superlevel sets have bounded support; R=50 suffices here.
    count = 0
    count_cells = int(2 * bound / step)
    for i in range(count_cells):
        x = -bound + (i + 0.5) * step
        if symbol(w, x) > t:
            count += 1
    return count * step / (2 * math.pi)


def finite_hs_squared(n, w):
    total = 0.0
    for j in range(1, n + 1):
        for k in range(1, j + 1):
            d = w * math.log(j / k)
            total += (2 - 2 * math.cos(d)) / (j * j)
    return total


def main():
    checks = 0
    for w in (0.35, 0.6, 1.0, 1.2, 2.0, 4.0):
        for t in (0.25, 0.6, 1.2, 1.7, 1.95):
            predicted = density(w, t)
            observed = grid_density(w, t)
            assert abs(predicted - observed) < 0.0015, (w, t, predicted, observed)
            assert abs(predicted - density(-w, t)) < 1e-14
            checks += 2
        if w > 1:
            central = 4 * w / (1 + w * w)
            assert 0 < central < 2
            t = (central + 2) / 2
            qm = (w * w - 1) / 4 - w * math.sqrt(1 - t * t / 4) / t
            assert qm > 0
        else:
            assert 4 * w / (1 + w * w) <= 2
        checks += 1
    for w in (0.6, 1.0, 2.0, 4.0):
        expected = 2 * w * w / (1 + w * w)
        a = finite_hs_squared(128, w) / math.log(128)
        b = finite_hs_squared(512, w) / math.log(512)
        assert 0 < a < b < expected
        checks += 1
    print('PASS', checks, 'checks (finite grids, threshold splitting, HS trends)')


if __name__ == '__main__':
    main()
