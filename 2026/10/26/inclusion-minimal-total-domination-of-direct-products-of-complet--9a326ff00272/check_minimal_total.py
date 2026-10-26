#!/usr/bin/env python3
"""Standalone exhaustive check of minimal total domination on complete-graph direct products."""
from collections import Counter
from itertools import combinations
from math import comb


def prediction(p, q):
    if min(p, q) == 2:
        return {4: comb(max(p, q), 2) ** 2}
    c3 = 6 * comb(p, 3) * comb(q, 3)
    c4 = (comb(p, 2) * comb(q, 2) ** 2
          + comb(q, 2) * comb(p, 2) ** 2
          - comb(p, 2) * comb(q, 2))
    return {3: c3, 4: c4}


def exhaustive(p, q):
    vertices = [(i, j) for i in range(p) for j in range(q)]
    number = len(vertices)
    adjacency = []
    for i, j in vertices:
        adjacency.append(sum(1 << t for t, (a, b) in enumerate(vertices)
                             if a != i and b != j))
    outcome = Counter()
    for mask in range(1 << number):
        if not all(mask & neighborhood for neighborhood in adjacency):
            continue
        if all(not all((mask ^ (1 << v)) & neighborhood
                       for neighborhood in adjacency)
               for v in range(number) if mask & (1 << v)):
            outcome[mask.bit_count()] += 1
    return dict(outcome)


def main():
    tests = [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
             (3, 3), (3, 4), (3, 5), (3, 6), (4, 4)]
    for p, q in tests:
        actual = exhaustive(p, q)
        expected = prediction(p, q)
        assert actual == expected, (p, q, actual, expected)
        print(f"K_{p} x K_{q}: PASS, {actual}")
    print(f"All {len(tests)} exhaustive tests passed.")


if __name__ == '__main__':
    main()
