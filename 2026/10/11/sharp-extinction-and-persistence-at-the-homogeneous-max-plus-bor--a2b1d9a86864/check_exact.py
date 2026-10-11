#!/usr/bin/env python3
"""Exact-arithmetic spot checks for a two-dimensional homogeneous max-plus map.

This program checks rational examples and deliberately does not replace the
analytic proof for all real parameters or all initial conditions.
"""
from fractions import Fraction as Q
from itertools import product


def iterate(t, d, x, y, steps):
    for _ in range(steps):
        positive = x if x > 0 else Q(0)
        x, y = y + t * positive, -d * positive
    return x, y


def extinction_time(t, d, x, y, cutoff=2000):
    for k in range(cutoff + 1):
        if x == 0 and y == 0:
            return k
        positive = x if x > 0 else Q(0)
        x, y = y + t * positive, -d * positive
    return None


def check_oscillatory():
    # m=ceil(pi/arccos(t/(2 sqrt(d)))) is certified for these
    # selected exact-angle or explicitly bounded-angle examples.
    cases = [
        (Q(0), Q(1), 2),
        (Q(1), Q(1), 3),
        (Q(1), Q(2), 3),
        (Q(2), Q(2), 4),
        (Q(2), Q(3), 4),
        (Q(3), Q(4), 5),
        (Q(3), Q(3), 6),
    ]
    for t, d, m in cases:
        assert t * t < 4 * d
        N = m + 2
        for x, y in product(range(-5, 6), repeat=2):
            assert iterate(t, d, Q(x), Q(y), N) == (0, 0), (t, d, x, y, N)
        assert extinction_time(t, d, Q(1), Q(100000000), N) == N, (t, d, N)


def check_critical():
    for lam in [Q(1, 2), Q(1), Q(2), Q(3)]:
        t, d = 2 * lam, lam * lam
        x = Q(1)
        assert extinction_time(t, d, x, -lam * x, 200) is None
        assert extinction_time(t, d, x, Q(0), 200) is None
        for k in [1, 2, 3, 5, 10, 20]:
            delta = lam * x / k
            y = -lam * x - delta
            assert extinction_time(t, d, x, y, k + 4) == k + 2
            # A slightly smaller distance to the boundary persists longer.
            assert extinction_time(t, d, x, y + delta / 2, 2 * k + 4) == 2 * k + 2


def check_overdamped():
    for large, small in [(Q(2), Q(1)), (Q(3), Q(2)),
                         (Q(5), Q(2)), (Q(8), Q(2))]:
        t, d = large + small, large * small
        x, gap, quotient = Q(1), large - small, large / small
        assert extinction_time(t, d, x, -large, 150) is None
        assert extinction_time(t, d, x, Q(0), 150) is None
        for k in [1, 2, 3, 5, 10]:
            delta = gap / (quotient ** k - 1)
            y = -large * x - delta
            assert extinction_time(t, d, x, y, 200) == k + 2
            assert extinction_time(t, d, x, -large * x - delta / 2, 200) > k + 2


def check_nonpositive_start():
    for t, d in [(Q(0), Q(1)), (Q(1), Q(1)), (Q(2), Q(1)), (Q(3), Q(2))]:
        for x in [-10, -1, 0]:
            for y in [-10, -1, 0]:
                assert extinction_time(t, d, Q(x), Q(y), 3) is not None
            for y in [1, 7]:
                if t*t >= 4*d:
                    assert extinction_time(t, d, Q(x), Q(y), 100) is None


if __name__ == '__main__':
    check_oscillatory()
    check_critical()
    check_overdamped()
    check_nonpositive_start()
    print('EXACT_RATIONAL_REGRESSION_OK')
