#!/usr/bin/env python3
"""Independent exhaustive verification of minimal edge domination in crown graphs.

Usage: python verify.py
Only Python's standard library is required. Every edge-subset is examined at orders
3, 4 and 5; no structural theorem is used by the exhaustive test itself.
"""
from itertools import permutations
from math import factorial


def crown_edges(n):
    return tuple((i, j) for i in range(n) for j in range(n) if i != j)


def derangements(indices):
    return (p for p in permutations(indices) if all(i != j for i, j in zip(indices, p)))


def expected_min(n):
    edges = crown_edges(n)
    position = {edge: i for i, edge in enumerate(edges)}
    ans = set()
    for k in range(n):
        rem = tuple(i for i in range(n) if i != k)
        for p in derangements(rem):
            mask = 0
            for i, j in zip(rem, p):
                mask |= 1 << position[(i, j)]
            ans.add(mask)
    return ans


def expected_max(n):
    assert n >= 5
    edges = crown_edges(n)
    position = {edge: i for i, edge in enumerate(edges)}
    ans = set()
    for missing in range(n):
        for center in range(n):
            if center == missing:
                continue
            mask = 0
            for j in range(n):
                if j not in (missing, center):
                    mask |= 1 << position[(center, j)]
                    mask |= 1 << position[(j, center)]
            ans.add(mask)
    return ans


def brute_all_minimal(n):
    """Enumerate all edge-subsets using independently computed domination masks."""
    edges = crown_edges(n)
    ecount = len(edges)
    limit = 1 << ecount
    neighborhood = []
    for i, j in edges:
        neighborhood.append(sum((1 << k) for k, (r, c) in enumerate(edges)
                                if i == r or j == c))
    universe = limit - 1
    dominated = [0] * limit
    minimal = set()
    for mask in range(1, limit):
        low = mask & -mask
        pos = low.bit_length() - 1
        smaller = mask ^ low
        dominated[mask] = dominated[smaller] | neighborhood[pos]
        if dominated[mask] != universe:
            continue
        selected = mask
        is_minimal = True
        while selected:
            bit = selected & -selected
            if dominated[mask ^ bit] == universe:
                is_minimal = False
                break
            selected ^= bit
        if is_minimal:
            minimal.add(mask)
    return minimal


def verify():
    checked = 0
    for n in (3, 4, 5):
        minimal = brute_all_minimal(n)
        checked += 1 << (n * (n - 1))
        sizes = [mask.bit_count() for mask in minimal]
        smallest, largest = min(sizes), max(sizes)
        predicted_min = expected_min(n)
        assert smallest == n - 1, (n, smallest)
        assert {m for m in minimal if m.bit_count() == smallest} == predicted_min
        predicted_count = n * sum(1 for _ in derangements(tuple(range(n - 1))))
        assert len(predicted_min) == predicted_count
        if n >= 5:
            predicted_max = expected_max(n)
            assert largest == 2 * n - 4, (n, largest)
            assert {m for m in minimal if m.bit_count() == largest} == predicted_max
            assert len(predicted_max) == n * (n - 1)
        print('n=%d edges=%d all_edge_subsets=%d minimal_sets=%d min=%d min_count=%d max=%d max_count=%d' % (
            n, n * (n - 1), 1 << (n * (n - 1)), len(minimal), smallest,
            sum(k == smallest for k in sizes), largest, sum(k == largest for k in sizes)))
    # Verify structural constructions independently at larger sizes.
    for n in range(5, 26):
        ed = crown_edges(n)
        all_e = set(ed)
        for missing in range(n):
            for center in range(n):
                if center == missing:
                    continue
                chosen = {(center, j) for j in range(n) if j not in (missing, center)}
                chosen |= {(j, center) for j in range(n) if j not in (missing, center)}
                assert len(chosen) == 2 * n - 4
                def dominates(S):
                    return all(any(a == c or b == d for a, b in S) for c, d in all_e)
                assert dominates(chosen)
                for e in chosen:
                    assert not dominates(chosen - {e})
    print('larger_n_extremal_constructions=5..25, passed')
    print('exhaustively_examined_edge_subsets=%d' % checked)
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    verify()
