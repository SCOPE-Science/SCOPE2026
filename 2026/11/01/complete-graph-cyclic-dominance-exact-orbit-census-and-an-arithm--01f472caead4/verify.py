"""Reproduce finite checks for the complete-graph three-colour threshold automaton.

No external dependencies. Run with: python verify.py
Finite checks are corroboration, not a proof for every N.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def update_direct(state, threshold):
    n = len(state)
    successor = []
    for i, color in enumerate(state):
        predators = sum(1 for j in range(n)
                        if j != i and state[j] == (color + 1) % 3)
        successor.append((color + 1) % 3 if predators >= threshold else color)
    return tuple(successor)


def orbit_class(state, threshold):
    seen = {}
    current = state
    while current not in seen:
        if len(seen) > 16:
            raise AssertionError('A period or preperiod exceeded the test budget')
        seen[current] = len(seen)
        current = update_direct(current, threshold)
    return seen[current], len(seen) - seen[current]


def predicted_census(n, threshold):
    fixed = 3 + 3 * sum(comb(n, j) for j in range(1, min(threshold - 1, n - 1) + 1))
    one = 3 * sum(comb(n, j) for j in range(threshold, n))
    two = three = 0
    for n0 in range(1, n - 1):
        for n1 in range(1, n - n0):
            n2 = n - n0 - n1
            weight = factorial(n) // (factorial(n0) * factorial(n1) * factorial(n2))
            large = sum(x >= threshold for x in (n0, n1, n2))
            if large == 0:
                fixed += weight
            elif large == 1:
                one += weight
            elif large == 2:
                two += weight
            else:
                three += weight
    return fixed, one, two, three


def main():
    checked = 0
    for n in range(3, 10):
        for threshold in range(1, n + 2):
            counts = Counter(orbit_class(state, threshold)
                             for state in product(range(3), repeat=n))
            assert set(counts) <= {(0, 1), (1, 1), (2, 1), (0, 3)}
            actual = tuple(counts[key] for key in ((0, 1), (1, 1), (2, 1), (0, 3)))
            expected = predicted_census(n, threshold)
            assert actual == expected, (n, threshold, actual, expected)
            assert sum(expected) == 3 ** n
            assert (expected[3] > 0) == (n >= 3 * threshold)
            assert (expected[2] > 0) == (threshold >= 2 and n >= 2 * threshold + 1)
            checked += 3 ** n
    print('PASS:', checked, 'vertex-level states across all threshold tests.')


if __name__ == '__main__':
    main()
