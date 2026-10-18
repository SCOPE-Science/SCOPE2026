#!/usr/bin/env python3
"""Exact independent lattice-volume checks for the two-layer clique prism."""
import itertools
import math
from fractions import Fraction


def analytic_integral(m):
    return sum(((-1) ** j) * Fraction(math.comb(m, j), (2 ** j) * (2 * j + 1))
               for j in range(m + 1))


def predicted_volume(n):
    assert n >= 2
    return 2 * n * ((n - 1) * analytic_integral(n - 2)
                    + analytic_integral(n - 1) - 1
                    + Fraction(1, 2 ** (n - 1)))


def ehrhart_count(n, scale):
    """Enumerate scaled vertex potentials; use exact minimum partition for other row."""
    if scale == 0:
        return 1
    total = 0
    for tail in itertools.product(range(-scale, scale + 1), repeat=n - 1):
        first_row = (0,) + tail
        if max(first_row) - min(first_row) > scale:
            continue
        lo = [value - scale for value in first_row]
        hi = [value + scale for value in first_row]
        for min_second in range(min(lo), max(hi) + 1):
            all_above_min = 1
            all_strictly_above_min = 1
            for lower, upper in zip(lo, hi):
                cap = max(0, min(min_second + scale, upper)
                          - max(min_second, lower) + 1)
                strict_cap = max(0, min(min_second + scale, upper)
                                 - max(min_second + 1, lower) + 1)
                all_above_min *= cap
                all_strictly_above_min *= strict_cap
                if not all_above_min and not all_strictly_above_min:
                    break
            total += all_above_min - all_strictly_above_min
    return total


def independent_volume(n):
    degree = 2 * n - 1
    values = [ehrhart_count(n, scale) for scale in range(degree + 1)]
    diff = sum((-1) ** (degree - i) * math.comb(degree, i) * count
               for i, count in enumerate(values))
    return Fraction(diff, math.factorial(degree)), values


def main():
    cases = 0
    for n in range(2, 6):
        got, lattice_counts = independent_volume(n)
        expect = predicted_volume(n)
        assert got == expect, (n, got, expect)
        print('n=', n, 'dimension=', 2 * n - 1,
              'exact volume=', got,
              'Ehrhart scales=', len(lattice_counts), 'PASS')
        cases += 1
    print('PASS: all', cases, 'independent exact volume comparisons.')

if __name__ == '__main__':
    main()
