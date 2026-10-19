#!/usr/bin/env python3
"""Exact arithmetic checks for the one-dissenter Pólya-urn fixed-point phase diagram.

This finite suite supplements, but does not replace, the all-parameter proof.
It uses Python's standard-library Fraction and has no external dependencies.
"""
from fractions import Fraction as Q


def f(z, bias):
    return bias * z / (1 + (bias - 1) * z)


def critical(n, g):
    low = Q(n - 1, 1) / (g + n - 2)
    high = (g * (n - 2) + 1) / (g * (n - 1))
    flip = (g * (n - 2) + n) / (g * n + n - 2)
    return low, flip, high


def interior(n, g, h):
    A = h * (g + n - 2) - (n - 1)
    y = A / ((g - 1) * (1 - h) * (n - 2))
    x = f(y, g)
    return x, y


def direct_map(v, g, h):
    n = len(v)
    return tuple(f((sum(v) - v[i]) / (n - 1), g if i == 0 else h)
                 for i in range(n))


def run():
    checked = 0
    polynomial_checks = 0
    for n in range(3, 19):
        for g in (Q(3, 2), Q(2), Q(5, 2), Q(4), Q(8), Q(13)):
            low, flip, high = critical(n, g)
            assert Q(0) < low < flip < high < 1
            assert high - low == (g - 1)**2 * (n - 2) / (g * (n - 1) * (g + n - 2))
            hs = (low / 2, low, (low + flip) / 2, flip,
                  (flip + high) / 2, high, (high + 1) / 2)
            for h in hs:
                assert 0 < h < 1
                # Exact Perron sign tests at the two boundary equilibria.
                pzero = 1 - h * (g + n - 2) / (n - 1)
                pone = 1 - (g * (n - 2) + 1) / (g * h * (n - 1))
                assert (pzero < 0) == (h > low)
                assert (pone < 0) == (h < high)
                if low < h < high:
                    x, y = interior(n, g, h)
                    assert 0 < y < x < 1
                    v = (x,) + (y,) * (n - 1)
                    assert direct_map(v, g, h) == v
                    fg = g / (1 + (g - 1) * y)**2
                    fh = (h - (h - 1) * y)**2 / h
                    # One-factor sign test for local stability on the quotient.
                    assert 1 - fh * (n - 2 + fg) / (n - 1) > 0
                    # Transverse Jacobian eigenvalue is -fh/(n-1).
                    assert 1 + fh / (n - 1) > 0
                    checked += 1
                    if h == flip:
                        assert y == Q(1, 2)
                # Independently clear denominators in reduced fixed-point equation.
                for y in (Q(0), Q(1), Q(1, 7), Q(2, 7), Q(1, 2), Q(5, 7)):
                    x = f(y, g)
                    m = (x + (n - 2) * y) / (n - 1)
                    denominator = ((n - 1) * (1 + (g - 1) * y)
                                   + (h - 1) * y * (g + (n - 2) * (1 + (g - 1) * y)))
                    factor = ((g - 1) * (h - 1) * (n - 2) * y
                              + h * (g + n - 2) - (n - 1))
                    assert (y - f(m, h)) * denominator == y * (y - 1) * factor
                    polynomial_checks += 1
    x, y = interior(5, Q(4), Q(3, 4))
    assert (x, y) == (Q(5, 6), Q(5, 9))
    assert critical(5, Q(4)) == (Q(4, 7), Q(17, 23), Q(13, 16))
    print(f"PASS: {checked} exact interior Jacobian/fixed-point cases; "
          f"{polynomial_checks} polynomial identity cases; "
          "example (n,g,h,x,y)=(5,4,3/4,5/6,5/9)")

if __name__ == '__main__':
    run()
