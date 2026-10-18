#!/usr/bin/env python3
"""Exact checks for one-contact, one-generation SIR final outbreak size.

Requires only Python 3 standard library. Vertices are 0,...,n-1.
"""
from fractions import Fraction
from functools import lru_cache


def mean_outbreak(adj):
    """Fraction expectation for a uniform single source by Bellman recursion."""
    n = len(adj)
    @lru_cache(None)
    def future(current, seen):
        return 1 + sum((future(j, seen | (1 << j))
                        for j in adj[current] if not (seen >> j) & 1),
                       Fraction(0)) / len(adj[current])
    return sum((future(v, 1 << v) for v in range(n)), Fraction(0)) / n


def mean_outbreak_by_paths(adj):
    """Independent path-weight enumeration, including absorbing contacts."""
    n = len(adj)
    def dist(current, seen, length, weight):
        infected_contacts = sum(bool(seen & (1 << j)) for j in adj[current])
        result = length * weight * Fraction(infected_contacts, len(adj[current]))
        for j in adj[current]:
            if not seen & (1 << j):
                result += dist(j, seen | (1 << j), length + 1,
                               weight / len(adj[current]))
        return result
    return sum((dist(v, 1 << v, 1, Fraction(1)) for v in range(n)),
               Fraction(0)) / n


def graph_from_edges(n, edges):
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    return tuple(tuple(sorted(x)) for x in adj)


def connected(adj):
    seen = {0}; todo = [0]
    while todo:
        i = todo.pop()
        for j in adj[i]:
            if j not in seen:
                seen.add(j)
                todo.append(j)
    return len(seen) == len(adj)


def exhaustive_minimality():
    all_comparisons = 0
    for n in range(2, 6):
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        graphs = comparisons = decreases = 0
        for bits in range(1 << len(pairs)):
            edges = [p for ix, p in enumerate(pairs) if (bits >> ix) & 1]
            adj = graph_from_edges(n, edges)
            if not connected(adj):
                continue
            graphs += 1
            old = mean_outbreak(adj)
            assert old == mean_outbreak_by_paths(adj)
            for ix, e in enumerate(pairs):
                if bits & (1 << ix):
                    continue
                new_adj = graph_from_edges(n, edges + [e])
                new = mean_outbreak(new_adj)
                assert new == mean_outbreak_by_paths(new_adj)
                comparisons += 1
                assert new >= old, (n, bits, e, old, new)
                if new < old:
                    decreases += 1
        all_comparisons += comparisons
        print(f'n={n}: connected labelled graphs={graphs}, '
              f'labelled edge additions={comparisons}, decreases={decreases}')
    print(f'Total eligible labelled edge additions for n=2..5: {all_comparisons}')


def family(m):
    hubs = (0, 1)
    edges = [(i, j) for i in hubs for j in range(2, m + 2)]
    return graph_from_edges(m + 2, edges), graph_from_edges(m + 2, edges + [(0, 1)])


def exact_family(m):
    before = Fraction(4 * m + 3, m + 2)
    after = Fraction(8 * m**3 + 21 * m**2 + 23 * m + 8,
                     2 * (m + 1)**2 * (m + 2))
    delta = Fraction(-(m * m - 3 * m - 2), 2 * (m + 1)**2 * (m + 2))
    return before, after, delta


def check_family():
    for m in range(1, 17):
        G, H = family(m)
        before, after, delta = exact_family(m)
        assert mean_outbreak(G) == before
        assert mean_outbreak(H) == after
        assert mean_outbreak_by_paths(G) == before
        assert mean_outbreak_by_paths(H) == after
        assert after - before == delta
    print('Family m=1..16: both exact algorithms agree with the formulas.')
    print('K_(2,4):', tuple(map(str, exact_family(4))))
    print('K_(2,5):', tuple(map(str, exact_family(5))))


if __name__ == '__main__':
    exhaustive_minimality()
    check_family()
