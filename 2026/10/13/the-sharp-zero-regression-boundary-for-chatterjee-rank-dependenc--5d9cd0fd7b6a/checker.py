"""Exact-rational checks for the symmetric checkerboard witness family.

This checks finite constructions, not the all-copula Jensen theorem.
Run with Python 3.9 or later: python checker.py
"""
from fractions import Fraction as F


def mean_abs_uniform_intervals(a, b, width):
    """Expected absolute difference between uniforms on two equal-width intervals.

    Caller chooses identical or disjoint intervals (up to shared endpoints).
    """
    if a == b:
        return width / 3
    if a < b:
        assert a + width <= b
        return b - a
    assert b + width <= a
    return a - b


def check(m):
    assert isinstance(m, int) and m >= 1
    h = F(1, 2 * m)
    total_abs = F(0)
    row_means = []
    covered = []
    for j in range(m):
        lo = j * h
        hi = 1 - (j + 1) * h
        assert lo + h <= hi or lo + h == hi
        # On this row, the response is a 50:50 mixture of two uniforms.
        row_mean = ((lo + h / 2) + (hi + h / 2)) / 2
        assert row_mean == F(1, 2)
        row_means.append(row_mean)
        # Sum over four equiprobable choices of the two response components.
        conditional_abs = (
            mean_abs_uniform_intervals(lo, lo, h)
            + mean_abs_uniform_intervals(lo, hi, h)
            + mean_abs_uniform_intervals(hi, lo, h)
            + mean_abs_uniform_intervals(hi, hi, h)
        ) / 4
        assert conditional_abs == F(1, 12*m) + F(1, 2) - F(2*j+1, 4*m)
        total_abs += conditional_abs / m
        covered.extend([(lo, lo + h), (hi, hi + h)])
    # All 2*m response intervals form an exact partition of [0,1].
    covered.sort()
    assert covered[0][0] == 0 and covered[-1][1] == 1
    for k in range(2*m - 1):
        assert covered[k][1] == covered[k+1][0]
    assert all(mean == F(1, 2) for mean in row_means)
    assert total_abs == F(1, 4) + F(1, 12*m)
    xi = 1 - 3*total_abs
    assert xi == F(1, 4) - F(1, 4*m)
    eta = 12 * sum((mean - F(1, 2))**2 for mean in row_means) / m
    assert eta == 0
    return xi


if __name__ == '__main__':
    count = 0
    for m in range(1, 129):
        result = check(m)
        count += 1
    assert check(1) == 0
    assert check(2) == F(1, 8)
    assert check(4) == F(3, 16)
    assert check(128) == F(127, 512)
    print('PASS: 128 exact checkerboard instances; 4 endpoint checks; uniform margins, zero regression and xi verified.')
