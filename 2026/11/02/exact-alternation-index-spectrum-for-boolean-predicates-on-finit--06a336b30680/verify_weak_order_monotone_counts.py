#!/usr/bin/env python3
"""Independent finite check for forbidden alternating colored chains in weak orders.

Only Python's standard library is used.  The mathematical proof covers all finite
weak orders; these exhaustively checked finite configurations are corroboration.
"""
from itertools import combinations, product
from math import comb

def elementary_spectrum(level_sizes):
    coefficients = [1]
    for size in level_sizes:
        b = (1 << size) - 1
        next_coefficients = coefficients + [0]
        for j in range(1, len(next_coefficients)):
            next_coefficients[j] += b * coefficients[j - 1]
        coefficients = next_coefficients
    return coefficients

def direct_alternating_spectrum(level_sizes):
    """Enumerate every coloring and each candidate alternating chain."""
    levels = []
    offset = 0
    for size in level_sizes:
        levels.append(tuple(range(offset, offset + size)))
        offset += size
    h = len(levels)
    templates = [[] for _ in range(h + 1)]
    for length in range(1, h + 1):
        for positions in combinations(range(h), length):
            for chain in product(*(levels[i] for i in positions)):
                ones = sum(1 << x for t, x in enumerate(chain) if t % 2 == 0)
                all_bits = sum(1 << x for x in chain)
                templates[length].append((all_bits, ones))
    histogram = [0] * (h + 1)
    for coloring in range(1 << offset):
        longest = 0
        for length in range(h, 0, -1):
            if any(coloring & all_bits == ones for all_bits, ones in templates[length]):
                longest = length
                break
        histogram[longest] += 1
    return histogram

def main():
    tested = 0
    colorings = 0
    cases = set()
    for h in range(0, 5):
        for sizes in product((1, 2, 3), repeat=h):
            if sum(sizes) <= 9:
                cases.add(sizes)
    for sizes in product((1, 2), repeat=5):
        if sum(sizes) <= 10:
            cases.add(sizes)
    cases.update({(3, 3, 3), (2, 2, 2, 2, 2), (4, 1, 2), (1, 4, 2),
                  (1, 1, 1, 1, 1, 1), (2, 1, 2, 1, 2)})
    for sizes in sorted(cases):
        expected = elementary_spectrum(sizes)
        actual = direct_alternating_spectrum(sizes)
        assert actual == expected, (sizes, actual, expected)
        assert sum(actual) == (1 << sum(sizes)), sizes
        for k in range(len(sizes) + 1):
            assert sum(actual[: k + 1]) == sum(expected[: k + 1])
        tested += 1
        colorings += 1 << sum(sizes)
    assert elementary_spectrum((2, 2, 2)) == [1, 9, 27, 27]
    assert elementary_spectrum((2, 1, 3)) == elementary_spectrum((3, 2, 1))
    print('ALL_WEAK_ORDER_ALTERNATION_CHECKS_PASS',tested, colorings)

if __name__ == '__main__':
    main()
