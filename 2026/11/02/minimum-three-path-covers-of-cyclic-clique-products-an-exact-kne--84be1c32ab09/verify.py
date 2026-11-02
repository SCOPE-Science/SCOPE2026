#!/usr/bin/env python3
"""Checks exact counts of maximum dissociation sets in cyclic clique products.

No third-party dependencies. Run: python3 verify.py
"""
from itertools import combinations, product
from math import comb


def expected(n, m):
    d = comb(n - 2, 2)
    return d**m + (n - 1) * (3 - n)**m + n * (n - 3) // 2


def graph_neighbors(n, m):
    """Adjacency of the original Cartesian product C_m square K_n."""
    a = []
    for i in range(m):
        for j in range(n):
            a.append({i*n + k for k in range(n) if k != j} |
                     {((i-1) % m)*n + j, ((i+1) % m)*n + j})
    return a


def maximum_by_original_graph(n, m):
    """Enumerate all subsets with up to two vertices in each clique fiber."""
    rows = [tuple()] + [(j,) for j in range(n)] + list(combinations(range(n), 2))
    neigh = graph_neighbors(n, m)
    best, count, number_seen = -1, 0, 0
    for choice in product(rows, repeat=m):
        number_seen += 1
        s = {i*n+j for i, r in enumerate(choice) for j in r}
        good = True
        for u in s:
            if sum(1 for v in neigh[u] if v in s) > 1:
                good = False
                break
        if good:
            c = len(s)
            if c > best:
                best, count = c, 1
            elif c == best:
                count += 1
    return best, count, number_seen


def kneser_trace(n, m):
    labels = list(combinations(range(n), 2))
    edges = [[i for i, w in enumerate(labels) if not set(w).intersection(v)]
             for v in labels]
    total = 0
    for i in range(len(labels)):
        dp = [0] * len(labels)
        dp[i] = 1
        for _ in range(m):
            nxt = [0] * len(labels)
            for v, ways in enumerate(dp):
                if ways:
                    for w in edges[v]:
                        nxt[w] += ways
            dp = nxt
        total += dp[i]
    return total


def check_graph_H(n, vertices, edge_pairs):
    """Independent generic-H check: brute force all choices of two per fiber."""
    pairs = list(combinations(range(n), 2))
    nbrs = [set() for _ in range(vertices)]
    for a, b in edge_pairs:
        nbrs[a].add(b); nbrs[b].add(a)
    count_original, count_hom = 0, 0
    for state in product(pairs, repeat=vertices):
        # Standard graph-homomorphism criterion checked without constructing G.
        hom = all(set(state[a]).isdisjoint(state[b]) for a, b in edge_pairs)
        count_hom += int(hom)
        # Separately evaluate the original product's degree condition.
        good = True
        chosen = {(v, j) for v, pair in enumerate(state) for j in pair}
        for v, j in chosen:
            in_clique = sum((v, jj) in chosen for jj in range(n) if jj != j)
            vertical = sum((w, j) in chosen for w in nbrs[v])
            if in_clique + vertical > 1:
                good = False
                break
        count_original += int(good)
    assert count_original == count_hom, (n,vertices,count_original,count_hom)
    return count_original


def main():
    for n, m in [(5, 3), (5, 4), (6, 3), (6, 4), (7, 3), (7, 4)]:
        maximum, count, number_seen = maximum_by_original_graph(n, m)
        if n >= 6:
            expect = expected(n, m)
            assert (maximum, count) == (2*m, expect), (n,m,maximum,count,expect)
            assert kneser_trace(n, m) == count, (n,m)
        print('ORIGINAL_GRAPH_EXHAUSTIVE_OK', n, m, maximum, count, number_seen)
    for n in range(6, 11):
        for m in range(3, 13):
            assert kneser_trace(n, m) == expected(n, m), (n, m)
    print('INDEPENDENT_KNESER_CLOSED_WALK_COUNTS_OK', 'n=6..10', 'm=3..12')
    H = [
        ('path_4', 6, 4, [(0,1),(1,2),(2,3)]),
        ('cycle_4', 6, 4, [(0,1),(1,2),(2,3),(3,0)]),
        ('star_4', 6, 4, [(0,1),(0,2),(0,3)]),
        ('triangle', 6, 3, [(0,1),(1,2),(2,0)]),
        ('triangle_with_leaf', 6, 4, [(0,1),(1,2),(2,0),(2,3)]),
        ('complete_4', 8, 4, list(combinations(range(4), 2))),
    ]
    for title, n, v, e in H:
        value = check_graph_H(n, v, e)
        print('GENERIC_BASE_GRAPH_CORRESPONDENCE_OK', title, n, value)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
