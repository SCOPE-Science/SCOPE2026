#!/usr/bin/env python3
"""Exact finite certificate for a coextinction-variance comparison theorem.

Python 3.10+ standard library only. Pollinators are the four bit positions,
plants are nonempty neighborhood masks. No empirical input is required.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement


def degree_signature(rows, n):
    return (tuple(sorted(r.bit_count() for r in rows)),
            tuple(sorted(sum((r >> j) & 1 for r in rows) for j in range(n))))


def union_histogram(rows, n):
    hist = [0] * (n + 1)
    for a, b in combinations(rows, 2):
        hist[(a | b).bit_count()] += 1
    return tuple(hist)


def coefficient_check():
    counts = []
    total_comparisons = 0
    for m in range(1, 5):
        groups = defaultdict(set)
        mats = 0
        for rows in combinations_with_replacement(range(1, 16), m):
            if rows[0] == 0:
                raise AssertionError('empty row')
            covered = 0
            for r in rows:
                covered |= r
            if covered != 15:
                continue
            key = degree_signature(rows, 4)
            hist = union_histogram(rows, 4)
            groups[key].add((hist[1], hist[4]))
            mats += 1
        distinct_pairs = 0
        for feats in groups.values():
            for x, y in combinations(sorted(feats), 2):
                a = x[0] - y[0]
                b = x[1] - y[1]
                # Same degree margins force P(q)=q(1-q)^2(a+b*q).
                # An interior sign change requires a*(a+b)<0.
                assert a * (a + b) >= 0, (m, x, y)
                distinct_pairs += 1
        counts.append((m, mats, len(groups), distinct_pairs))
        total_comparisons += distinct_pairs
    return counts, total_comparisons


def direct_moments(rows, n, q):
    out = Fraction(0)
    out2 = Fraction(0)
    for removed in range(1 << n):
        k = removed.bit_count()
        p = q**k * (1-q)**(n-k)
        x = sum((r & removed) == r for r in rows)
        out += p*x
        out2 += p*x*x
    return out, out2-out*out


def witness_check():
    A = (1, 1, 3, 6, 10)
    B = (1, 2, 3, 3, 12)
    assert degree_signature(A, 4) == degree_signature(B, 4)
    assert degree_signature(A, 4) == ((1, 1, 2, 2, 2), (1, 1, 3, 3))
    hA, hB = union_histogram(A, 4), union_histogram(B, 4)
    assert hA == (0, 1, 2, 7, 0)
    assert hB == (0, 0, 6, 2, 2)
    for num in range(1, 20):
        q = Fraction(num, 20)
        Ea, Va = direct_moments(A, 4, q)
        Eb, Vb = direct_moments(B, 4, q)
        assert Ea == Eb == 2*q + 3*q*q
        assert Va == q*(1-q)*(9*q*q + 7*q + 4)
        assert Vb == q*(1-q)*(5*q*q + 13*q + 2)
        assert Va-Vb == 2*q*(1-q)**2*(1-2*q)
    return (hA, hB)


if __name__ == '__main__':
    counts, compared = coefficient_check()
    assert [x[1] for x in counts] == [1, 40, 400, 2306]
    assert [x[2] for x in counts] == [1, 8, 33, 103]
    assert [x[3] for x in counts] == [0, 0, 5, 48]
    h = witness_check()
    print('VERIFY_OK counts=', counts, 'feature_comparisons=', compared, 'witness_union_histograms=', h)
