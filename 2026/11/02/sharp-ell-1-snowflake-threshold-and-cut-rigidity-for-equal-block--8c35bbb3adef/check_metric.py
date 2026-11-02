#!/usr/bin/env python3
"""Exact finite checks for the balanced-cluster real L1 distortion law.

Uses only Python's standard library. Analytical proof is required for arbitrary sizes.
"""
from fractions import Fraction as F
from itertools import combinations, product


def pair_means_for_cut(part_sizes, selected):
    r = len(part_sizes)
    n = part_sizes[0]
    assert all(q == n for q in part_sizes) and r >= 2 and n >= 2
    a = [sum((selected >> (i * n + j)) & 1 for j in range(n)) for i in range(r)]
    u = F(sum(q * (n - q) for q in a), r * (n * (n - 1) // 2))
    w_num = sum(a[i] * (n - a[j]) + (n - a[i]) * a[j]
                for i, j in combinations(range(r), 2))
    w = F(w_num, (r * (r - 1) // 2) * n * n)
    variance = F(2 * sum((a[i] - a[j]) ** 2 for i, j in combinations(range(r), 2)),
                 r * (r - 1) * n * n)
    return u, w, variance, a


def balanced_embedding(r, n, s):
    """Return weighted nontrivial cuts, in exact rational arithmetic."""
    s = F(s)
    assert r >= 2 and n >= 2 and 0 < s <= 2
    N = r * n
    total = n ** r
    cuts = []
    for chosen in product(range(n), repeat=r):
        mask = sum(1 << (i * n + chosen[i]) for i in range(r))
        cuts.append((mask, s * n / (2 * total)))
    remaining = 1 - s * F(n - 1, n)
    if remaining > 0:
        for i in range(r):
            mask = ((1 << n) - 1) << (i * n)
            cuts.append((mask, remaining / 2))
    assert all(weight >= 0 for _, weight in cuts)
    return cuts


def check_one(r, n, s):
    s = F(s)
    cuts = balanced_embedding(r, n, s)
    target = max(F(1), s * F(n - 1, n))
    within = across = 0
    for p, q in combinations(range(r * n), 2):
        distance = sum(weight for mask, weight in cuts if ((mask >> p) ^ (mask >> q)) & 1)
        predicted = s if p // n == q // n else target
        assert distance == predicted, (r, n, s, p, q, distance, predicted)
        assert (distance >= (s if p // n == q // n else 1))
        assert distance <= target * (s if p // n == q // n else 1)
        if p // n == q // n:
            within += 1
        else:
            across += 1
    assert within == r * n * (n - 1) // 2
    assert across == r * (r - 1) * n * n // 2
    return within + across


def main():
    count = 0
    eq_support = 0
    for r, n in [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (4, 2), (4, 3)]:
        for mask in range(1 << (r * n)):
            U, W, V, a = pair_means_for_cut([n] * r, mask)
            assert W == F(n - 1, n) * U + V
            assert V >= 0
            assert (V == 0) == (len(set(a)) == 1)
            count += 3
            if V == 0:
                eq_support += 1
    pairs = 0
    for r, n in [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (4, 2), (4, 3)]:
        for s in [F(1, 2), F(1), F(6, 5), F(n, n - 1), F(3, 2), F(2)]:
            if s > 2:
                continue
            pairs += check_one(r, n, s)
    print('CHECK_OK', {'cut_identity_assertions': count,
                       'balanced_cut_equalities': eq_support,
                       'exact_embedding_pairs': pairs})


if __name__ == '__main__':
    main()
