#!/usr/bin/env python3
"""Exact finite checks of matching-multicut enumerators.

Only standard-library Python is required. A partition is generated once as a
restricted-growth string, so blocks are unlabelled. The acceptance predicate
is computed directly from graph edges; formulas are a separate computation.
"""
from collections import Counter
from itertools import product
from math import comb, factorial


def path(n):
    return n, [(i, i + 1) for i in range(n - 1)]


def cycle(n):
    return n, [(i, (i + 1) % n) for i in range(n)]


def complete(n):
    return n, [(i, j) for i in range(n) for j in range(i + 1, n)]


def cartesian(*graphs):
    lengths = [g[0] for g in graphs]
    tuples = list(product(*(range(n) for n in lengths)))
    lookup = {t: i for i, t in enumerate(tuples)}
    edges = set()
    for ix, coords in enumerate(tuples):
        for k, (_, ge) in enumerate(graphs):
            for a, b in ge:
                if coords[k] == a:
                    dest = list(coords)
                    dest[k] = b
                    edges.add(tuple(sorted((ix, lookup[tuple(dest)]))))
                elif coords[k] == b:
                    dest = list(coords)
                    dest[k] = a
                    edges.add(tuple(sorted((ix, lookup[tuple(dest)]))))
    return len(tuples), sorted(edges)


def direct_counts(graph):
    n, edges = graph
    deg = [0] * n
    label = [0] * n
    counts = Counter()

    def rec(i, biggest):
        if i == n:
            if biggest == 0:
                return
            for j in range(n):
                deg[j] = 0
            cross = 0
            for a, b in edges:
                if label[a] != label[b]:
                    deg[a] += 1
                    deg[b] += 1
                    cross += 1
                    if deg[a] > 1 or deg[b] > 1:
                        return
            counts[(biggest + 1, cross)] += 1
            return
        for value in range(biggest + 2):
            label[i] = value
            rec(i + 1, max(biggest, value))

    # The first label is 0. Only partitions with at least two blocks count.
    rec(1, 0)
    return counts


def stirling(n, k):
    if (n, k) == (0, 0):
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return stirling(n - 1, k - 1) + k * stirling(n - 1, k)


def path_formula(n):
    out = Counter()
    for t in range(1, n // 2 + 1):
        for k in range(2, t + 2):
            out[(k, t)] += comb(n - t, t) * stirling(t, k - 1)
    return +out


def cyclic_partition_count(t, k):
    # Inclusion-exclusion for surjective proper colorings of a t-cycle.
    def chromatic(q):
        return (q - 1)**t + (-1)**t * (q - 1)
    num = sum((-1)**j * comb(k, j) * chromatic(k-j)
              for j in range(k+1))
    assert num % factorial(k) == 0
    return num // factorial(k)


def cycle_formula(n):
    out = Counter()
    for t in range(2, n // 2 + 1):
        matchings = n * comb(n-t, t) // (n-t)
        assert matchings * (n-t) == n * comb(n-t, t)
        for k in range(2, t+1):
            out[(k,t)] += matchings * cyclic_partition_count(t,k)
    return +out


def product_formula(*factors):
    sizes = [g[0] for g in factors]
    out = Counter()
    for j, factor in enumerate(factors):
        mult = 1
        for i, sz in enumerate(sizes):
            if i != j:
                mult *= sz
        for (k, crossings), count in direct_counts(factor).items():
            out[(k, crossings * mult)] += count
    return +out


def connected_graphs(n):
    pairs = [(a,b) for a in range(n) for b in range(a+1,n)]
    for mask in range(1, 1 << len(pairs)):
        edges = [e for i,e in enumerate(pairs) if (mask >> i)&1]
        seen = {0}
        while True:
            more = {v for a,b in edges for u,v in ((a,b),(b,a)) if u in seen}
            if more <= seen:
                break
            seen |= more
        if len(seen) == n:
            yield (n,edges)


def verify():
    for n in range(2, 10):
        observed = direct_counts(path(n))
        target = path_formula(n)
        assert observed == target, ('path', n, observed, target)

    for n in range(3, 10):
        observed = direct_counts(cycle(n))
        target = cycle_formula(n)
        assert observed == target, ('cycle', n, observed, target)

    examples = [
        ('grid2x2', (path(2), path(2))),
        ('grid2x3', (path(2), path(3))),
        ('grid2x4', (path(2), path(4))),
        ('grid2x5', (path(2), path(5))),
        ('grid3x3', (path(3), path(3))),
        ('cylinder3x2', (cycle(3), path(2))),
        ('cylinder4x2', (cycle(4), path(2))),
        ('cylinder5x2', (cycle(5), path(2))),
        ('torus3x3', (cycle(3), cycle(3))),
        ('triangular_prism', (complete(3), path(2))),
        ('cube3', (path(2), path(2), path(2))),
    ]
    for name, factors in examples:
        observed = direct_counts(cartesian(*factors))
        target = product_formula(*factors)
        assert observed == target, (name, observed, target)
        print(name, 'partition classes', sum(observed.values()),
              'nonzero (k,cut-edge) bins', len(observed))
    structural = 0
    for n in (2, 3, 4):
        for g in connected_graphs(n):
            product_graph = cartesian(g, path(2))
            observed = direct_counts(product_graph)
            target = product_formula(g, path(2))
            assert observed == target, ('all_connected', n, g)
            structural += 1
    for sizes in ((2, 2), (2, 4), (3, 3), (3, 5), (4, 6), (2, 2, 5), (3, 4, 7)):
        formula = Counter()
        for i, n in enumerate(sizes):
            mult = 1
            for j, m in enumerate(sizes):
                if i != j:
                    mult *= m
            for (k, t), a in path_formula(n).items():
                formula[(k, t * mult)] += a
        predicted = product_formula(*(path(n) for n in sizes))
        assert formula == predicted, (sizes, formula, predicted)
    print('VERIFY_OK paths n=2..9; cycles n=3..9; eleven named Cartesian products;', structural, 'connected-factor products; seven grid identities')


if __name__ == '__main__':
    verify()
