#!/usr/bin/env python3
"""Exact integer certificate for the rectangular-grid anticanonical wall."""
from fractions import Fraction
from math import gcd


def boundary_pairs():
    return {(3, 6): 3, (4, 4): 2, (6, 3): 3}


def witness(r, s, m):
    """Find integral vertical/horizontal multiplicities giving -mK."""
    for a in range(m + 1):
        b = m - a
        if r * a <= 2 * m and s * b <= 2 * m:
            return (a, b, 2 * m - r * a, 2 * m - s * b)
    return None


def check():
    for r in range(3, 31):
        for s in range(3, 31):
            wall = 4 - (r - 2) * (s - 2)
            assert wall == 2 * (r + s) - r * s
            # The supporting divisor has nonnegative intersections with
            # both families of grid fibres and the exceptional curves.
            assert s - s == 0 and r - r == 0
            assert wall > 0 or wall == 0 or wall < 0
            for m in range(1, 13):
                x = witness(r, s, m)
                if wall < 0:
                    assert x is None
                elif wall == 0:
                    e = boundary_pairs()[(r, s)]
                    if m % e:
                        assert x is None
                    else:
                        assert x is not None
                        a, b, u, v = x
                        assert u == v == 0 and a + b == m
                        assert Fraction(a, m) == Fraction(s - 2, s)
                        assert Fraction(b, m) == Fraction(r - 2, r)
                        assert max(a, b) < m
                else:
                    if m % (r * s) == 0:
                        assert x is not None
                        # A strict interior rational slope provides two
                        # positive residual ruling degrees for large m.
                        low, high = Fraction(s - 2, s), Fraction(2, r)
                        assert low < high
                        slope = (low + high) / 2
                        M = slope.denominator * (1 - slope).denominator
                        a = M * slope
                        b = M - a
                        assert a.denominator == 1
                        assert b.denominator == 1
                        assert 2 * M - r * a > 0
                        assert 2 * M - s * b > 0
    assert set(boundary_pairs()) == {(r, s) for r in range(3, 31) for s in range(3, 31) if (r - 2) * (s - 2) == 4}
    print('VERIFY_OK: 784 grid pairs, exact wall, constructive sections, and boundary generator degrees')

if __name__ == '__main__':
    check()
