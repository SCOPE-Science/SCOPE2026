#!/usr/bin/env python3
"""Exact finite checks for length-weighted cyclic simplex sums.

Python 3 standard library only. These tests are not a proof for arbitrary n.
"""
from fractions import Fraction as F
import random


def all_tubes(n, weights):
    tubes = []
    for length in range(2, n):
        for start in range(n):
            mask = sum(1 << ((start + j) % n) for j in range(length))
            tubes.append((mask, weights[length]))
    tubes.append(((1 << n) - 1, weights[n]))
    return tubes


def expected(n, weights):
    numerator = sum((j-1) * weights[j] for j in range(2, n)) + F(n-1, n) * weights[n]
    denominator = sum(weights[2:n]) + F(1, n) * weights[n]
    return numerator / denominator


def verify(n, weights):
    assert n >= 3 and len(weights) == n + 1
    assert all(w >= 0 for w in weights)
    assert any(weights[2:])
    tube_list = all_tubes(n, weights)
    total = sum(w for _, w in tube_list)
    assert total > 0
    mean = total / n
    target = expected(n, weights)
    best = F(0)
    maximizers = []
    total_mask = (1 << n) - 1
    for mask in range(1, total_mask):
        comp = total_mask ^ mask
        z_mask = sum(w for tube, w in tube_list if tube & mask == tube)
        z_comp = sum(w for tube, w in tube_list if tube & comp == tube)
        lo_gap = mean * mask.bit_count() - z_mask
        hi_gap = mean * comp.bit_count() - z_comp
        assert lo_gap > 0 and hi_gap > 0
        ratio = lo_gap / hi_gap
        if ratio > best:
            best = ratio
            maximizers = [mask]
        elif ratio == best:
            maximizers.append(mask)
    assert best == target, (n, weights, best, target)
    for i in range(n):
        assert total_mask ^ (1 << i) in maximizers
    return len(maximizers)


def main():
    rng = random.Random(20261014)
    tests = 0
    strictly_positive = 0
    for n in range(3, 10):
        # Each dimension: sparse, dense, singleton-length, and mixed profiles.
        profiles = []
        for j in range(2, n + 1):
            w = [F(0)] * (n+1)
            w[j] = F(1)
            profiles.append(w)
        for m in range(1, n):
            w = [F(0)] * (n+1)
            for j in range(2, min(n, m+2)):
                w[j] = F(1)
            if m == n-1:
                w[n] = F(1)
            profiles.append(w)
            expected_m = F(m+1, 2) if m < n-1 else F(n-1, 2) + F(1, 2*(n-1))
            assert expected(n,w) == expected_m
        for _ in range(100):
            w = [F(0), F(0)] + [F(rng.randrange(0, 7), rng.randrange(1, 5)) for _ in range(n-1)]
            if not any(w[2:]):
                w[2] = F(1)
            profiles.append(w)
        for w in profiles:
            cnt = verify(n, w)
            tests += 1
            if all(v > 0 for v in w[2:]):
                assert cnt == n, (n, w, cnt)
                strictly_positive += 1
    print(f"PASS: {tests} exact profiles across n=3..9")
    print(f"PASS: {strictly_positive} positive profiles have exactly n maximal subset ratios")
    print("PASS: all discrete filtration values and final-step anomaly")

if __name__ == '__main__':
    main()
