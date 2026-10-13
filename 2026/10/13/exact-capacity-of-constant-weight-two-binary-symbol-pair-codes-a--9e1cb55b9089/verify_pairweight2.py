#!/usr/bin/env python3
"""Reproduce the weight-two cyclic symbol-pair distance-four theorem, using the Python standard library."""
from functools import lru_cache
from itertools import combinations
from math import gcd


def optimal_edges(n):
    """Construct an optimal family of two-element supports in Z/nZ for n>=3."""
    assert n >= 3
    k = n // 2
    if n % 2 == 0:
        return {tuple(sorted((i, j))) for i in range(0, n, 2) for j in range(1, n, 2)}
    distances = range(1, k if k % 2 == 0 else k - 1, 2)
    edges = set()
    for i in range(n):
        for s in distances:
            a, b = i, (i + s) % n
            edges.add(tuple(sorted((a, b))))
    if k % 2 == 1:
        # The step-k edges form one n-cycle; select a maximum matching.
        order = [(t * k) % n for t in range(n)]
        assert len(set(order)) == n and gcd(k, n) == 1
        for t in range(0, n - 1, 2):
            edges.add(tuple(sorted((order[t], order[t + 1]))))
    return edges


def pair_read(word):
    n = len(word)
    return [(word[i], word[(i + 1) % n]) for i in range(n)]


def pair_distance(n, edge1, edge2):
    a = [int(j in edge1) for j in range(n)]
    b = [int(j in edge2) for j in range(n)]
    return sum(x != y for x, y in zip(pair_read(a), pair_read(b)))


def verify_family(n, edges):
    assert len(edges) == n * (n // 2) // 2, (n, len(edges))
    neighbors = [set() for _ in range(n)]
    for a, b in edges:
        assert 0 <= a < b < n
        neighbors[a].add(b)
        neighbors[b].add(a)
    for i in range(n):
        assert len(neighbors[i]) <= n // 2
        for j in neighbors[i]:
            assert (j + 1) % n not in neighbors[i], (n, i, j)
    if n <= 15:
        for u, v in combinations(sorted(edges), 2):
            assert pair_distance(n, u, v) >= 4, (n, u, v)


def exact_clique_free_search(n):
    """Independent branching search on the full conflict graph, not using the construction."""
    candidates = list(combinations(range(n), 2))
    conflicts = [0] * len(candidates)
    for u, (a, b) in enumerate(candidates):
        for v in range(u):
            c, d = candidates[v]
            shared = set((a, b)) & set((c, d))
            if len(shared) == 1:
                j, k = tuple(set((a, b)) ^ set((c, d)))
                if (j - k) % n in (1, n-1):
                    conflicts[u] |= (1 << v)
                    conflicts[v] |= (1 << u)
    @lru_cache(None)
    def mis(mask):
        if mask == 0:
            return 0
        v = max((j for j in range(len(candidates)) if (mask >> j) & 1),
                key=lambda j: (mask & conflicts[j]).bit_count())
        without_v = mask & ~(1 << v)
        return max(mis(without_v), 1 + mis(without_v & ~conflicts[v]))
    return mis((1 << len(candidates)) - 1)


def main():
    for n in range(3, 121):
        verify_family(n, optimal_edges(n))
    values = []
    for n in range(3, 12):
        exact = exact_clique_free_search(n)
        formula = n * (n // 2) // 2
        assert exact == formula, (n, exact, formula)
        values.append((n, exact))
    print('VERIFY_OK family construction n=3..120; independent exact search n=3..11')
    print('Values:', values)

if __name__ == '__main__':
    main()
