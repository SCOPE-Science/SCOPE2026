#!/usr/bin/env python3
"""Independent checks for the maximal-independent-set formula on Moebius ladders.

Uses only Python's standard library. Graph predicate and coefficient formula
are implemented independently, then compared exhaustively on small orders.
"""
from collections import Counter
from math import comb


def adjacency(n):
    a = [0] * (2 * n)
    for i in range(n):
        j = (i + 1) % n
        if i + 1 < n:
            edges = ((i, i + 1), (n + i, n + i + 1))
        else:
            edges = ((n - 1, n), (2 * n - 1, 0))
        for u, v in edges:
            a[u] |= 1 << v
            a[v] |= 1 << u
        u, v = i, n + i
        a[u] |= 1 << v
        a[v] |= 1 << u
    return a


def coefficients(n):
    # For j occupied rungs (j selected vertices), every empty rung
    # separates two different occupied rail choices.
    return {j: 2 * n * comb(j, n - j) // j for j in range((n + 1)//2, n + 1)
            if j % 2 == 1 and 0 <= n - j <= j and
            (2 * n * comb(j, n - j)) % j == 0}


def exhaustive(n):
    adj = adjacency(n)
    full = (1 << (2 * n)) - 1
    out = Counter()
    for mask in range(1 << (2 * n)):
        # independent: no selected vertex has a selected neighbor
        bits = mask
        conflict = False
        covered = mask
        while bits:
            low = bits & -bits
            i = low.bit_length() - 1
            if adj[i] & mask:
                conflict = True
                break
            covered |= adj[i]
            bits ^= low
        if not conflict and covered == full:
            out[mask.bit_count()] += 1
    return dict(out)


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def omega(n):
    # trace of roots of x^2+x+1, a 3-periodic sequence 2,-1,-1.
    return (2, -1, -1)[n % 3]


def main():
    subsets = 0
    for n in range(3, 11):
        by_graph = exhaustive(n)
        by_formula = coefficients(n)
        assert by_graph == by_formula, (n, by_graph, by_formula)
        subsets += 1 << (2 * n)
    for n in range(3, 201):
        coef = coefficients(n)
        assert sum(coef.values()) == lucas(n) - omega(n), (n, sum(coef.values()))
        assert all(j % 2 for j in coef)
        assert min(coef) == (next(j for j in range((n + 1)//2, n + 1) if j % 2))
        assert max(coef) == (n if n % 2 else n - 1)
    print('VERIFY_OK exhaustive_n=3..10 masks=%d formula_and_OEIS_n=3..200 parity_extremal=passed' % subsets)


if __name__ == '__main__':
    main()
