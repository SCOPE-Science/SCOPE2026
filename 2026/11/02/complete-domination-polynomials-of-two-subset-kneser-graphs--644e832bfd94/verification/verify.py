#!/usr/bin/env python3
"""Reproduce exact domination-polynomial coefficients from graph adjacency.

Usage: python3 verification/verify.py
Uses only Python's standard library. Exhaustive for n=4,...,7 and
independent restricted-cardinality checks for n=8,...,10.
"""
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def coefficients(n):
    if n == 4:
        return [0, 0, 0, 8, 12, 6, 1]
    assert n >= 5
    N = choose(n, 2)
    result = [0] * (N + 1)
    for k in range(3, N + 1):
        if k == 3:
            result[k] = choose(n, 3) + 15 * choose(n, 6)
        else:
            overlap = (choose(N, 1) * choose(2 * n - 4, k)
                       + n * (choose(n - 1, k)
                              - choose(n, 2) * choose(n - 2, k)
                              + choose(n - 1, 2) * choose(n - 3, k)
                              - int(k == n - 1)))
            result[k] = choose(N, k) - overlap + 3 * choose(n, 4) * int(k == 4)
    return result


def closed_neighborhood_masks(n):
    pairs = list(combinations(range(n), 2))
    masks = []
    for i, e in enumerate(pairs):
        mask = 0
        for j, f in enumerate(pairs):
            if i == j or all(a not in f for a in e):
                mask |= 1 << j
        masks.append(mask)
    return masks


def exhaustive_counts(n):
    cover = closed_neighborhood_masks(n)
    N = len(cover)
    full = (1 << N) - 1
    coverage = [0] * (1 << N)
    counts = [0] * (N + 1)
    for mask in range(1, 1 << N):
        low = mask & -mask
        coverage[mask] = coverage[mask ^ low] | cover[low.bit_length() - 1]
        if coverage[mask] == full:
            counts[mask.bit_count()] += 1
    return counts


def restricted_count(n, k):
    cover = closed_neighborhood_masks(n)
    full = (1 << len(cover)) - 1
    count = 0
    for positions in combinations(range(len(cover)), k):
        covered = 0
        for i in positions:
            covered |= cover[i]
        count += covered == full
    return count


def main():
    checked = 0
    for n in range(4, 8):
        actual = exhaustive_counts(n)
        predicted = coefficients(n)
        assert actual == predicted, (n, actual, predicted)
        checked += 1 << choose(n, 2)
        assert predicted[-1] == 1
        print('FULL', n, 'vertices', choose(n, 2), 'domination coefficients', actual[3:7])
    sparse_checked = 0
    for n in range(8, 11):
        predicted = coefficients(n)
        for k in range(3, 6):
            actual = restricted_count(n, k)
            assert actual == predicted[k], (n, k, actual, predicted[k])
            sparse_checked += choose(choose(n, 2), k)
            print('SPARSE', n, k, actual)
    for n in range(5, 50):
        pred = coefficients(n)
        N = choose(n, 2)
        assert all(pred[k] == choose(N, k) for k in range(2 * n - 3, N + 1))
        assert pred[2 * n - 4] == choose(N, 2 * n - 4) - N
    print('VERIFY_OK: %s fully enumerated masks, %s sparse candidates, 45 threshold checks'
          % (checked, sparse_checked))


if __name__ == '__main__':
    main()
