#!/usr/bin/env python3
"""Exact finite checks for an edge-addition paradox in random-order greedy occupancy.
Python standard library only. Run: python verify.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial


def greedy_size(n, edges, order):
    neighbors = [0] * n
    for u, v in edges:
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
    selected = 0
    for v in order:
        if not (selected & neighbors[v]):
            selected |= 1 << v
    return selected.bit_count()


def mean_recurrence(n, edges):
    closed = [1 << i for i in range(n)]
    for u, v in edges:
        closed[u] |= 1 << v
        closed[v] |= 1 << u

    @lru_cache(None)
    def F(mask):
        if not mask:
            return Fraction(0)
        count = mask.bit_count()
        total = Fraction(1)
        remain = mask
        while remain:
            bit = remain & -remain
            remain -= bit
            vertex = bit.bit_length() - 1
            total += F(mask & ~closed[vertex]) / count
        return total
    return F((1 << n) - 1)


def mean_permutations(n, edges):
    total = sum(greedy_size(n, edges, p) for p in permutations(range(n)))
    return Fraction(total, factorial(n))


def canonical_marked(n, edges, initial_mask, added_index):
    keys = []
    lookup = {edge: index for index, edge in enumerate(edges)}
    for p in permutations(range(n)):
        perm_indices = [lookup[tuple(sorted((p[u], p[v])))] for u, v in edges]
        transferred_mask = sum(1 << perm_indices[i] for i in range(len(edges)) if initial_mask & (1 << i))
        keys.append((transferred_mask, perm_indices[added_index]))
    return min(keys)


def stars_and_cliques(k, m):
    n = 1 + k + m
    base = [(0, i) for i in range(1, k + 1)]
    base += list(combinations(range(k + 1, n), 2))
    return n, base, base + [(0, k + 1)]


def main():
    exact_graphs = 0
    permutation_orders = 0
    classified = {}
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        expectations = []
        for mask in range(1 << len(pairs)):
            graph = [pair for i, pair in enumerate(pairs) if mask & (1 << i)]
            a = mean_recurrence(n, graph)
            b = mean_permutations(n, graph)
            assert a == b, ('independent methods disagree', n, mask, a, b)
            expectations.append(a)
            exact_graphs += 1
            permutation_orders += factorial(n)
        for mask, baseline in enumerate(expectations):
            for i in range(len(pairs)):
                if mask & (1 << i):
                    continue
                improvement = expectations[mask | (1 << i)] - baseline
                if n < 5:
                    assert improvement <= 0, (n, mask, i, improvement)
                elif improvement > 0:
                    key = canonical_marked(n, pairs, mask, i)
                    classified.setdefault(key, []).append(improvement)
        if n == 5:
            assert len(classified) == 3, classified
            counts = sorted((len(group), set(group)) for group in classified.values())
            assert counts == [(60, {Fraction(1, 15)}), (60, {Fraction(1, 15)}),
                              (120, {Fraction(1, 15)})], counts
            explicit = [
                ([(0, 3), (0, 4), (1, 2)], (0, 1), Fraction(8, 3), Fraction(41, 15)),
                ([(0, 2), (0, 4), (1, 2), (1, 3)], (0, 3), Fraction(37, 15), Fraction(38, 15)),
                ([(0, 2), (0, 3), (0, 4), (1, 2), (1, 3)], (1, 4), Fraction(38, 15), Fraction(13, 5)),
            ]
            for original, extra, a, b in explicit:
                assert mean_recurrence(5, original) == a
                assert mean_recurrence(5, original + [extra]) == b

    for k in range(2, 7):
        for m in range(2, 7):
            n, old, new = stars_and_cliques(k, m)
            gap = mean_recurrence(n, new) - mean_recurrence(n, old)
            theory = Fraction(k - 1, (k + 1) * (k + m + 1))
            assert gap == theory, (k, m, gap, theory)
            if k <= 3 and m <= 3:
                gains = {}
                for ordering in permutations(range(n)):
                    a, b = greedy_size(n, old, ordering), greedy_size(n, new, ordering)
                    g = b - a
                    positions = {v: j for j, v in enumerate(ordering)}
                    event = (positions[k + 1] == min(positions[v] for v in range(k + 1, n))
                             and positions[k + 1] < positions[0]
                             and positions[0] < min(positions[v] for v in range(1, k + 1)))
                    assert g == (k - 1 if event else 0), (k, m, ordering, g, event)
                    gains[g] = gains.get(g, 0) + 1
                assert Fraction(gains.get(k - 1, 0), factorial(n)) == Fraction(1, (k + 1) * (k + m + 1))

    print('VERIFY_OK graphs=%d direct_permutations=%d improving_marked_pairs=240 isomorphism_types=3 family_parameter_pairs=25' % (exact_graphs, permutation_orders))


if __name__ == '__main__':
    main()
