#!/usr/bin/env python3
"""Direct exhaustive checks for minimum zero-forcing sets of graph powers.

This verifier builds graph adjacency and runs the simultaneous color-change rule.
The candidate formulas are compared with enumeration of *all* subsets of
minimum size, not with an enumerator that assumes the classification.
"""
from collections import Counter
from itertools import combinations
from math import comb


def adjacency(n, k, cyclic):
    return [set(j for j in range(n)
                if j != i and (
                    min(abs(i - j), n - abs(i - j)) <= k if cyclic
                    else abs(i - j) <= k)) for i in range(n)]


def parallel_rounds(adj, initial):
    blue = set(initial)
    rounds = 0
    while len(blue) != len(adj):
        new = set()
        for vertex in blue:
            white = adj[vertex] - blue
            if len(white) == 1:
                new.update(white)
        if not new:
            return None
        blue.update(new)
        rounds += 1
    return rounds


def candidate_sets(adj, k, cyclic):
    n = len(adj)
    if cyclic:
        if n <= 2 * k + 1:
            return {frozenset(range(n)) - {j} for j in range(n)}
        return {frozenset(adj[v] | {v}) - {w}
                for v in range(n) for w in adj[v]}
    if n <= k + 1:
        return {frozenset(range(n)) - {j} for j in range(n)}
    return {frozenset(adj[v] | {v}) - {w}
            for v in (0, n - 1) for w in adj[v]}


def expected_hist(n, k, cyclic):
    if cyclic:
        if n <= 2 * k + 1:
            return n - 1, Counter({1: n})
        if n == 2 * k + 2:
            return 2 * k, Counter({1: n * k})
        q = n - 2 * k
        a, b = (q + 1) // 2, 1 + (q // 2)
        return 2 * k, Counter({a: n}) + Counter({b: 2 * n * (k - 1)})
    if n <= k + 1:
        return n - 1, Counter({1: n})
    return k, Counter({n - k: 2 * k})


def verify_case(n, k, cyclic):
    adj = adjacency(n, k, cyclic)
    size, wanted = expected_hist(n, k, cyclic)
    found = {}
    tested = 0
    for initial in combinations(range(n), size):
        tested += 1
        rounds = parallel_rounds(adj, initial)
        if rounds is not None:
            found[frozenset(initial)] = rounds
    hist = Counter(found.values())
    if hist != wanted:
        raise AssertionError(('hist', cyclic, n, k, hist, wanted))
    if set(found) != candidate_sets(adj, k, cyclic):
        missing = set(found) - candidate_sets(adj, k, cyclic)
        extra = candidate_sets(adj, k, cyclic) - set(found)
        raise AssertionError(('structure', cyclic, n, k, missing, extra))
    # The cardinality is the stated minimum: degree lower bound, except
    # a complete graph where n-1 is forced by its degree.
    mindeg = min(map(len, adj))
    if mindeg != size:
        raise AssertionError(('degree', cyclic, n, k, mindeg, size))
    return tested, len(found)


def main():
    profiles = subsets = optimal = 0
    for k in range(1, 6):
        for n in range(max(2, k), k + 10):
            tested, valid = verify_case(n, k, False)
            profiles += 1; subsets += tested; optimal += valid
        for n in range(max(3, 2 * k - 1), 2 * k + 9):
            tested, valid = verify_case(n, k, True)
            profiles += 1; subsets += tested; optimal += valid
    # Separately inspect the structural counting of circular intervals,
    # including representative multiplicities at large parameters.
    structural_profiles = 0
    for k in range(1, 11):
        for n in range(2*k+2, 2*k+20):
            adj = adjacency(n, k, True)
            reps = {}
            for v in range(n):
                for w in adj[v]:
                    B = frozenset(adj[v] | {v}) - {w}
                    reps.setdefault(B, []).append((v, w))
            if n == 2*k+2:
                assert len(reps) == n*k
                assert set(len(z) for z in reps.values()) == {2}
            else:
                assert len(reps) == n*(2*k-1)
                assert Counter(map(len, reps.values())) == Counter({1:2*n*(k-1),2:n})
            structural_profiles += 1
    print('ALL CHECKS PASSED')
    print('exhaustive_graph_profiles=', profiles, sep='')
    print('initial_sets_independently_tested=', subsets, sep='')
    print('minimum_zero_forcing_sets_found=', optimal, sep='')
    print('interval_representation_profiles=', structural_profiles, sep='')
    print('tested_path_orders=2..14; cycle_orders=3..18; powers=1..5')


if __name__ == '__main__':
    main()
