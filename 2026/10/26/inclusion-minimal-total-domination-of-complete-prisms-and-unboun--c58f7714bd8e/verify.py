#!/usr/bin/env python3
"""Reproduce the complete-prism minimal total domination classification.

Uses only the elementary graph definition and Python's standard library.
"""
from collections import Counter
from itertools import combinations
from math import comb


def run(n):
    N = 2 * n
    adjacency = [0] * N
    for i in range(N):
        layer, position = divmod(i, n)
        for j in range(N):
            other_layer, other_position = divmod(j, n)
            if i != j and (layer == other_layer or position == other_position):
                adjacency[i] |= 1 << j

    def total_dominating(bits):
        return all(bits & neighborhood for neighborhood in adjacency)

    actual = set()
    for bits in range(1, 1 << N):
        if not total_dominating(bits):
            continue
        if all(
            not total_dominating(bits ^ (1 << selected))
            for selected in range(N)
            if bits & (1 << selected)
        ):
            actual.add(bits)

    predicted = {((1 << n) - 1), ((1 << n) - 1) << n}
    for i in range(n):
        predicted.add((1 << i) | (1 << (n + i)))
    for upper in combinations(range(n), 2):
        for lower in combinations((i for i in range(n) if i not in upper), 2):
            predicted.add(sum(1 << i for i in upper) | sum(1 << (n + i) for i in lower))
    assert actual == predicted, f"family mismatch for n={n}"
    counts = Counter(bits.bit_count() for bits in actual)
    expected = Counter()
    expected[2] += n
    expected[n] += 2
    expected[4] += 6 * comb(n, 4) if n >= 4 else 0
    assert counts == +expected, f"coefficient mismatch for n={n}: {counts} / {expected}"
    if n >= 6:
        assert set(counts) == {2, 4, n}
    return dict(sorted(counts.items()))


def main():
    candidates = 0
    for n in range(2, 11):
        counts = run(n)
        candidates += (1 << (2 * n)) - 1
        print(f"n={n} coefficient_distribution={counts}")
    print(f"total_nonempty_subsets_examined={candidates}")
    print("PASS: original-neighborhood exhaustive family comparison and coefficient checks")


if __name__ == "__main__":
    main()
