#!/usr/bin/env python3
"""Exact finite checks for independent domination of fully subdivided graphs."""
from collections import Counter
from itertools import combinations
from math import comb


def subdivision_adjacency(n, edges):
    """Return adjacency bit masks: original vertices first, edge vertices last."""
    neighbors = [0] * (n + len(edges))
    for k, (u, v) in enumerate(edges, n):
        neighbors[u] |= 1 << k
        neighbors[v] |= 1 << k
        neighbors[k] |= (1 << u) | (1 << v)
    return neighbors


def direct_polynomial(neighbors):
    N = len(neighbors)
    all_ones = (1 << N) - 1
    count = Counter()
    for subset in range(1, 1 << N):
        remaining = subset
        dominated = subset
        independent = True
        while remaining:
            bit = remaining & -remaining
            v = bit.bit_length() - 1
            if neighbors[v] & subset:
                independent = False
                break
            dominated |= neighbors[v]
            remaining ^= bit
        if independent and dominated == all_ones:
            count[subset.bit_count()] += 1
    return count, (1 << N) - 1


def general_formula(n, edges):
    count = Counter()
    for omitted in range(1 << n):
        chosen_omitted = [v for v in range(n) if omitted >> v & 1]
        inside = [(u, v) for u, v in edges
                  if (omitted >> u & 1) and (omitted >> v & 1)]
        if chosen_omitted:
            degrees = {v: 0 for v in chosen_omitted}
            for u, v in inside:
                degrees[u] += 1
                degrees[v] += 1
            if 0 in degrees.values():
                continue
        count[n - len(chosen_omitted) + len(inside)] += 1
    return count


def bipartite_formula(a, b):
    count = Counter({a+b: 1})
    for p in range(1, a + 1):
        for q in range(1, b + 1):
            count[a+b-p-q+p*q] += comb(a, p)*comb(b, q)
    return count


def main():
    cases = [(1, 1), (1, 2), (1, 4), (1, 6),
             (2, 2), (2, 3), (2, 4), (2, 5),
             (3, 3), (3, 4)]
    direct_subsets = 0
    for a, b in cases:
        edges = [(u, a+v) for u in range(a) for v in range(b)]
        actual, tried = direct_polynomial(subdivision_adjacency(a+b, edges))
        expected = bipartite_formula(a, b)
        assert actual == expected, (a, b, actual, expected)
        assert general_formula(a+b, edges) == expected
        assert sum(expected.values()) == 1 + (2**a-1)*(2**b-1)
        direct_subsets += tried

    general_cases = 0
    general_subsets = 0
    # All labeled graphs on 1,2,3 vertices, plus 20 tests at 4 vertices.
    for n in range(1, 5):
        potential_edges = list(combinations(range(n), 2))
        limit = (1 << len(potential_edges)) if n <= 3 else 20
        for pattern in range(limit):
            edges = [e for j, e in enumerate(potential_edges) if pattern >> j & 1]
            actual, tried = direct_polynomial(subdivision_adjacency(n, edges))
            expected = general_formula(n, edges)
            assert actual == expected, (n, pattern, actual, expected)
            general_subsets += tried
            general_cases += 1

    rectangular_cases = 0
    for a in range(2, 18):
        for b in range(a, 18):
            coefficients = bipartite_formula(a, b)
            products = {i*j for i in range(1, a) for j in range(1, b)}
            support = {a+b-1} | {a+b-1+t for t in products}
            assert set(coefficients) == support
            assert min(support) == a+b-1
            assert max(support) == a*b
            min_count = a*(2**b-1) + b*(2**a-1) - a*b
            assert coefficients[a+b-1] == min_count
            if a == b and a >= 3:
                assert max(set(coefficients) - {a*b}) == a*a-a+1
                assert len(support) == len(products) + 1
            rectangular_cases += 1
    print('VERIFY_OK',
          'complete_bipartite_instances=', len(cases),
          'direct_bipartite_subsets=', direct_subsets,
          'general_graph_instances=', general_cases,
          'direct_general_subsets=', general_subsets,
          'support_parameter_pairs=', rectangular_cases)


if __name__ == '__main__':
    main()
