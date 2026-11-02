#!/usr/bin/env python3
"""Independent finite checks for mixed rectangle/functional ladder bounds.

A 1 in halfgraph H_t occurs precisely when row <= column.
No optional packages are required. All computations are exact.
"""
from itertools import combinations
from math import ceil


def minimal_residual(t, r):
    """Exhaustively enumerate canonical cut rectangles, with <= r cuts."""
    best = t
    for k in range(min(r, t) + 1):
        for cuts in combinations(range(t), k):
            rem = [sum(not any(i <= c <= j for c in cuts) for j in range(i, t))
                   for i in range(t)]
            best = min(best, max(rem, default=0))
    return best


def all_rectangles(t):
    """Enumerate all nonempty bipartite rectangles in H_t independently."""
    cells = {(i, j) for i in range(t) for j in range(i, t)}
    candidates = set()
    for amask in range(1, 1 << t):
        A = [i for i in range(t) if (amask >> i) & 1]
        for bmask in range(1, 1 << t):
            B = [j for j in range(t) if (bmask >> j) & 1]
            rect = frozenset((i, j) for i in A for j in B)
            if rect <= cells:
                candidates.add(rect)
    return list(candidates)


def min_over_arbitrary_rectangles(t, r):
    rectangles = all_rectangles(t)
    best = t
    for k in range(r + 1):
        for picked in combinations(rectangles, k):
            covered = set().union(*picked)
            max_row = max((sum((i, j) not in covered for j in range(i, t))
                           for i in range(t)), default=0)
            best = min(best, max_row)
    return best


def test_witness(r, s):
    t = (r + 1) * (s + 1) - 1
    cuts = {k * (s + 1) - 1 for k in range(1, r + 1)}
    assert len(cuts) == r
    for i in range(t):
        for j in range(t):
            graph = any(j == i + h for h in range(s))
            rect = any(i <= c <= j for c in cuts)
            assert (graph or rect) == (i <= j), (r, s, t, i, j)


def main():
    cases = 0
    for t in range(0, 12):
        for r in range(0, 9):
            observed = minimal_residual(t, r)
            expected = max(0, ceil((t - min(t, r)) / (min(t, r) + 1)))
            assert observed == expected, (t, r, observed, expected)
            cases += 1
    strict_cases = 0
    for t in range(1, 5):
        for r in range(0, 3):
            assert min_over_arbitrary_rectangles(t, r) == minimal_residual(t, r)
            strict_cases += 1
    rigidity_cases = 0
    for r in range(1, 5):
        for s in range(0, 4):
            t = (r + 1) * (s + 1) - 1
            if t > 12:
                continue
            expected = tuple(k*(s+1)-1 for k in range(1, r+1))
            winners = []
            for cuts in combinations(range(t), r):
                max_rem = max((sum(not any(i <= c <= j for c in cuts)
                                   for j in range(i, t))
                               for i in range(t)), default=0)
                if max_rem <= s:
                    winners.append(cuts)
            assert winners == [expected], (r,s,winners,expected)
            rigidity_cases += 1
    witness_cells = 0
    for r in range(5):
        for s in range(5):
            test_witness(r, s)
            witness_cells += ((r + 1) * (s + 1) - 1)**2
    print(f'ALL_CHECKS_OK canonical_cases={cases} arbitrary_cases={strict_cases} rigidity_cases={rigidity_cases} witness_cells={witness_cells}')


if __name__ == '__main__':
    main()
