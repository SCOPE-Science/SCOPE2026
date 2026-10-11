#!/usr/bin/env python3
"""Finite checks for rooted and strong Morse matching complexes of trees.

The enumeration computes matchings from every vertex filtration via subset dynamic
programming. It separately computes rooted gradient facets and tree diameters.
No libraries beyond Python's standard library are required.
"""
from itertools import product
from collections import deque
from heapq import heapify, heappop, heappush


def prufer_tree(code, n):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    leaves = [i for i, deg in enumerate(degree) if deg == 1]
    heapify(leaves)
    edges = []
    for x in code:
        u = heappop(leaves)
        edges.append((min(u, x), max(u, x)))
        degree[u] -= 1
        degree[x] -= 1
        if degree[x] == 1:
            heappush(leaves, x)
    a = heappop(leaves)
    b = heappop(leaves)
    edges.append((min(a, b), max(a, b)))
    return tuple(sorted(edges))


def make_data(edges, n):
    adjacency = [[] for _ in range(n)]
    for j, (u, v) in enumerate(edges):
        adjacency[u].append((v, j, 2*j))
        adjacency[v].append((u, j, 2*j+1))
    return adjacency


def all_strong_matchings(edges, n):
    adjacency = make_data(edges, n)
    states = [set() for _ in range(1 << n)]
    states[0].add(0)
    for seen in range((1 << n) - 1):
        if not states[seen]:
            continue
        for v in range(n):
            if (seen >> v) & 1:
                continue
            predecessors = [bit for w, _, bit in adjacency[v] if (seen >> w) & 1]
            new_bit = 1 << predecessors[0] if len(predecessors) == 1 else 0
            states[seen | (1 << v)].update(s | new_bit for s in states[seen])
    return states[-1]


def rooted_facets(edges, n):
    adjacency = make_data(edges, n)
    facets = []
    for root in range(n):
        parent = [-1] * n
        parent[root] = root
        Q = deque([root])
        F = 0
        while Q:
            u = Q.popleft()
            for v, _, bit_from_v in adjacency[u]:
                if parent[v] != -1:
                    continue
                parent[v] = u
                F |= 1 << (bit_from_v ^ 1)
                Q.append(v)
        # bit_from_v at vertex u points to edge; for v->u the reversed
        # orientation occupies the opposite member of the edge's bit pair.
        assert F.bit_count() == n - 1
        facets.append(F)
    return facets


def diameter(adjacency, n):
    D = 0
    for src in range(n):
        dist = [-1] * n
        dist[src] = 0
        Q = deque([src])
        while Q:
            u = Q.popleft()
            for v, _, _ in adjacency[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    Q.append(v)
        D = max(D, max(dist))
    return D


def verify(edges, n):
    roots = rooted_facets(edges, n)
    R = set(roots)
    assert len(R) == n
    strong = all_strong_matchings(edges, n)
    assert R.issubset(strong)
    for s in strong:
        assert s.bit_count() <= n - 1
    maxima = {s for s in strong if s.bit_count() == n - 1}
    assert maxima == R
    root_cover = all(any(s & f == s for f in R) for s in strong)
    D = diameter(make_data(edges, n), n)
    assert root_cover == (D <= 3), (edges, n, D)
    # Verifies the structural leaf-removal proof on each possible root facet.
    remaining = set(range(n))
    adjacency = make_data(edges, n)
    while len(remaining) > 1:
        leaf = next(v for v in sorted(remaining) if sum(w in remaining for w, _, _ in adjacency[v]) == 1)
        neighbor = next(w for w, _, _ in adjacency[leaf] if w in remaining)
        private = roots[leaf] & ~roots[neighbor]
        assert private.bit_count() == 1
        assert all((roots[r] & private) == 0 for r in remaining if r != leaf)
        assert ((roots[leaf] & ~private) & roots[neighbor]) == roots[leaf] & ~private
        assert roots[leaf].bit_count() >= 2
        remaining.remove(leaf)
    return D, len(strong), len(R)


def main():
    seen = 0
    by_diameter = {}
    for n in range(3, 7):
        for code in product(range(n), repeat=n-2):
            edges = prufer_tree(code, n)
            D, count, rooted = verify(edges, n)
            by_diameter[D] = by_diameter.get(D, 0) + 1
            seen += 1
    for n in (7, 8, 9):
        codes = [tuple([x] * (n - 2)) for x in range(n)]
        codes += [tuple(range(n-2)), tuple([0,1] * ((n-2)//2) + ([0] if (n-2)%2 else []))]
        for code in codes:
            edges = prufer_tree(code, n)
            D, count, rooted = verify(edges, n)
            by_diameter[D] = by_diameter.get(D, 0) + 1
            seen += 1
    # The path with four edges is the minimal non-pure example.
    assert verify(tuple((i,i+1) for i in range(4)), 5)[0] == 4
    print('VERIFY_OK', seen, 'labeled-tree test instances;', 'diameter_counts=', sorted(by_diameter.items()))

if __name__ == '__main__':
    main()
