#!/usr/bin/env python3
"""Independent substring-enumeration checks for a family of five-run binary words.

Run with Python 3, no dependencies: python3 verify.py
All word positions in this program are zero-based.
"""
from collections import defaultdict
from itertools import combinations
from math import comb
from random import Random


def word(b, c, e):
    return "0" + "1" * b + "0" * c + "1" + "0" * e


def factor_cover_masks(w):
    """For each distinct factor, union the position masks of ALL its occurrences."""
    masks = defaultdict(int)
    for i in range(len(w)):
        for j in range(i + 1, len(w) + 1):
            masks[w[i:j]] |= ((1 << j) - 1) ^ ((1 << i) - 1)
    return dict(masks)


def is_attractor(masks, positions):
    mask = sum(1 << p for p in positions)
    return all(factor_positions & mask for factor_positions in masks.values())


def proposed_markers(b, c, e):
    if e <= c:
        return (0, b, b + c)
    if b <= 3:
        return (min(b, 2), b + c, b + c + 2)
    if c <= 2:
        return (c - 1, b + c - 1, b + c + 2)
    return (0, b, b + c, b + c + 2)


def gamma4_condition(b, c, e):
    return b >= 4 and c >= 3 and e > c


def independent_exact_minimum(masks, n):
    for k in range(1, 5):
        for positions in combinations(range(n), k):
            if is_attractor(masks, positions):
                return k
    raise AssertionError("No attractor of size at most four")


def check_witness(b, c, e, exhaustive=False):
    w = word(b, c, e)
    masks = factor_cover_masks(w)
    marks = proposed_markers(b, c, e)
    assert is_attractor(masks, marks), (b, c, e, marks)
    assert len(marks) == (4 if gamma4_condition(b, c, e) else 3)
    if gamma4_condition(b, c, e):
        # Four different factors having exactly one occurrence in disjoint intervals.
        intervals = [(0, 2), (b - 1, b + 1), (b + c - 1, b + c + 1),
                     (b + c + 2, b + c + e + 1)]
        assert all(intervals[i][1] < intervals[i+1][0] for i in range(3))
        for i, j in intervals:
            f = w[i:j+1]
            assert sum(w[k:k+len(f)] == f for k in range(len(w)-len(f)+1)) == 1, (b, c, e, f)
        assert [w[i:j+1] for i, j in intervals] == ["011", "110", "001", "0"*e]
    if exhaustive:
        g = independent_exact_minimum(masks, len(w))
        assert (g == 4) == gamma4_condition(b, c, e), (b, c, e, g)
    return len(masks)


def check_counts():
    for n in range(5, 101):
        direct = sum(gamma4_condition(b, c, n - 2 - b - c)
                     for b in range(1, n - 3)
                     for c in range(1, n - 2 - b)
                     if n - 2 - b - c >= 1)
        expected = 0 if n < 13 else (n - 11) ** 2 // 4
        assert direct == expected, (n, direct, expected)
        assert comb(n - 3, 2) >= direct


def main():
    exhaustive = 0
    for b in range(1, 7):
        for c in range(1, 7):
            for e in range(1, 7):
                check_witness(b, c, e, exhaustive=True)
                exhaustive += 1
    broad = 0
    for b in range(1, 13):
        for c in range(1, 13):
            for e in range(1, 13):
                check_witness(b, c, e)
                broad += 1
    rng = Random(3819)
    random_sample = 0
    for _ in range(160):
        b, c, e = (rng.randint(1, 60) for __ in range(3))
        check_witness(b, c, e)
        random_sample += 1
    check_counts()
    print("VERIFY_OK exact_minima=%d complete_factor_witnesses=%d random_large=%d fixed_length_counts=5..100" %
          (exhaustive, broad, random_sample))

if __name__ == '__main__':
    main()
