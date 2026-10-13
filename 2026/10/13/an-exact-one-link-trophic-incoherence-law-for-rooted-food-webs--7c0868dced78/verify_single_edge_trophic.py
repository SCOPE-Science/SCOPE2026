#!/usr/bin/env python3
"""Exact independent verification of the one-edge trophic-incoherence formulas.

Run with Python 3; only the standard library is required.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import heapq
import random


def undirected_tree_from_prufer(code, n):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    leaves = [v for v in range(n) if degree[v] == 1]
    heapq.heapify(leaves)
    edges = []
    for v in code:
        u = heapq.heappop(leaves)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
        if degree[v] == 1:
            heapq.heappush(leaves, v)
    a, b = leaves
    edges.append((a, b))
    return edges


def rooted_parent(edges, n, root=0):
    neigh = [[] for _ in range(n)]
    for a, b in edges:
        neigh[a].append(b)
        neigh[b].append(a)
    par = [-1] * n
    depth = [-1] * n
    depth[root] = 0
    work = [root]
    for u in work:
        for v in neigh[u]:
            if depth[v] == -1:
                par[v] = u
                depth[v] = depth[u] + 1
                work.append(v)
    assert all(d >= 0 for d in depth)
    return par, depth


def gauss_exact(matrix, rhs):
    n = len(rhs)
    a = [list(map(F, row)) + [F(value)] for row, value in zip(matrix, rhs)]
    for j in range(n):
        p = next((i for i in range(j, n) if a[i][j]), None)
        assert p is not None, 'unexpected singular trophic-level system'
        a[j], a[p] = a[p], a[j]
        pivot = a[j][j]
        a[j] = [v / pivot for v in a[j]]
        for i in range(n):
            if i == j:
                continue
            t = a[i][j]
            if t:
                a[i] = [z - t * x for z, x in zip(a[i], a[j])]
    return [a[i][-1] for i in range(n)]


def trophic_sq_direct(arcs, n):
    incoming = [[] for _ in range(n)]
    for u, v in arcs:
        incoming[v].append(u)
    mat = [[0] * n for _ in range(n)]
    rhs = [1] * n
    for v, sources in enumerate(incoming):
        mat[v][v] = 1
        if sources:
            for u in sources:
                mat[v][u] -= F(1, len(sources))
    levels = gauss_exact(mat, rhs)
    diffs = [levels[v] - levels[u] for u, v in arcs]
    assert sum(diffs) == len(arcs)
    sq = sum(x*x for x in diffs) / len(arcs) - 1
    assert sq >= 0
    return sq, levels, diffs


def is_strict_ancestor(v, u, parent):
    w = parent[u]
    while w >= 0:
        if w == v:
            return True
        w = parent[w]
    return False


def verify_one_tree(edges, n, tally):
    parent, depth = rooted_parent(edges, n)
    arcs = [(parent[v], v) for v in range(1, n)]
    arcset = set(arcs)
    zero_count = 0
    zeros = sum((sum(d == k-1 for d in depth) - 1)
                for k in range(1, max(depth)+1)
                for v in range(n) if depth[v] == k)
    assert zeros >= 0
    for v in range(1, n):
        for u in range(n):
            if u == v or (u, v) in arcset:
                continue
            sq, levels, diffs = trophic_sq_direct(arcs + [(u, v)], n)
            cyc = is_strict_ancestor(v, u, parent)
            if cyc:
                ell = depth[u] - depth[v]
                expected = F(2 * (ell+1)**2, n)
                assert sq >= F(8, n)
                tally['feedback'] += 1
            else:
                gap = depth[v] - depth[u]
                expected = F((gap-1)**2, 2*n)
                tally['acyclic'] += 1
            assert sq == expected, (n, edges, u, v, expected, sq, levels, diffs)
            if sq == 0:
                assert not cyc and depth[v] == depth[u] + 1
                zero_count += 1
            tally['checks'] += 1
    assert zero_count == zeros, (n, edges, zero_count, zeros)
    tally['trees'] += 1
    tally['zero_arcs'] += zero_count


def main():
    tally = Counter()
    for n in range(3, 7):
        for code in product(range(n), repeat=n-2):
            verify_one_tree(undirected_tree_from_prufer(code, n), n, tally)
        print('exhaustive_n', n, 'trees', n**(n-2))
    rng = random.Random(246813579)
    for n in (7, 8, 9):
        for _ in range(100):
            code = tuple(rng.randrange(n) for _ in range(n-2))
            verify_one_tree(undirected_tree_from_prufer(code, n), n, tally)
    assert tally['feedback'] > 0 and tally['acyclic'] > 0
    print('VERIFY_OK')
    print('rooted_tree_cases', tally['trees'])
    print('additional_arc_cases', tally['checks'])
    print('acyclic_arc_cases', tally['acyclic'])
    print('feedback_arc_cases', tally['feedback'])
    print('coherence_preserving_new_arcs', tally['zero_arcs'])

if __name__ == '__main__':
    main()
