#!/usr/bin/env python3
"""Independent finite checks of the four-run binary string-attractor theorem.

Run: python3 standalone/verify.py
No external packages or data files are required.
"""
from collections import defaultdict
from itertools import combinations, product


def position_occurrence_masks(word):
    """factor -> union of positional intervals of all its occurrences."""
    result = defaultdict(int)
    n = len(word)
    for i in range(n):
        for j in range(i + 1, n + 1):
            result[word[i:j]] |= ((1 << j) - (1 << i))
    return tuple(set(result.values()))


def is_attractor(occ_masks, locations):
    occupied = sum(1 << i for i in locations)
    return all(mask & occupied for mask in occ_masks)


def predicted_size(a, b, c, d):
    return 3 if ((a > c and d > b) or
                 (c >= a + 2 and b >= d + 2)) else 2


def explicit_attractor(a, b, c, d):
    """Return a proved witness in zero-based positions."""
    if a >= c and b >= d:
        return (a - 1, a + b - 1)
    if c >= a and d >= b:
        return (a + b, a + b + c)
    if c > a and b >= d and b <= d + 1:
        return (a + b - 1, a + b + c - 1)
    if c >= a and b > d and c <= a + 1:
        return (a, a + b)
    if a >= c:
        return (a - 1, a + b - 1, a + b + c)
    return (a, a + b, a + b + c)


def brute_optimum(masks, n):
    for positions in combinations(range(n), 2):
        if is_attractor(masks, positions):
            return 2
    return 3


def generating_coefficient(n):
    def term(shift):
        r = n - shift
        return sum((j + 1) * (r - 2*j + 1)
                   for j in range(r//2 + 1)) if r >= 0 else 0
    return term(6) + term(8)


def main():
    checked = 0
    for a, b, c, d in product(range(1, 9), repeat=4):
        w = '0'*a + '1'*b + '0'*c + '1'*d
        occ = position_occurrence_masks(w)
        expected = predicted_size(a, b, c, d)
        actual = brute_optimum(occ, len(w))
        assert expected == actual, (a, b, c, d, expected, actual)
        witness = explicit_attractor(a, b, c, d)
        assert len(witness) == expected and len(set(witness)) == expected
        assert is_attractor(occ, witness), (a, b, c, d, witness)
        checked += 1

    checked_coefficients = 0
    for n in range(4, 23):
        observed = 0
        for a in range(1, n - 2):
            for b in range(1, n - a - 1):
                for c in range(1, n - a - b):
                    d = n - a - b - c
                    observed += (predicted_size(a, b, c, d) == 3)
        assert observed == generating_coefficient(n), (n, observed)
        checked_coefficients += 1

    print(f'VERIFY_OK exhaustive_parameter_quadruples={checked} '
          f'generating_coefficients={checked_coefficients} '
          f'parameters=1..8 lengths=4..22')

if __name__ == '__main__':
    main()
