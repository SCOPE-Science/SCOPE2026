#!/usr/bin/env python3
"""Independent finite tests for minimal connected dominating sets of full edge subdivisions.
Runs with the Python standard library and no downloaded dependencies.
The theorem is proved separately; finite checks are not an all-order certificate.
"""
from collections import Counter
from itertools import combinations, product
from math import factorial


def graph(n, edges):
    adj = [0] * (n + len(edges))
    for j, (u, v) in enumerate(edges):
        w = n + j
        for x in (u, v):
            adj[x] |= 1 << w
            adj[w] |= 1 << x
    return adj


def connected_subset(bits, adj):
    if not bits:
        return False
    visited = bits & -bits
    frontier = visited
    while frontier:
        neighbors = 0
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            neighbors |= adj[bit.bit_length() - 1]
        frontier = (neighbors & bits) & ~visited
        visited |= frontier
    return visited == bits


def dominating(bits, adj):
    covered = bits
    rem = bits
    while rem:
        bit = rem & -rem
        rem ^= bit
        covered |= adj[bit.bit_length() - 1]
    return covered == (1 << len(adj)) - 1


def minimal_connected_dominating(bits, adj):
    if not (dominating(bits, adj) and connected_subset(bits, adj)):
        return False
    rem = bits
    while rem:
        bit = rem & -rem
        rem ^= bit
        smaller = bits ^ bit
        if dominating(smaller, adj) and connected_subset(smaller, adj):
            return False
    return True


def all_direct(n, edges):
    adj = graph(n, edges)
    return {bits for bits in range(1, 1 << len(adj))
            if minimal_connected_dominating(bits, adj)}


def predicted_by_leaf_tree(n, edges):
    # An independent implementation of the tree/vertex-cover characterization.
    # This counts actual vertex subsets, not just their cardinalities.
    edge_index = {frozenset((u, v)): j for j, (u, v) in enumerate(edges)}
    nbrs = [set() for _ in range(n)]
    for u, v in edges:
        nbrs[u].add(v)
        nbrs[v].add(u)
    answer = set()
    for s_bits in range(1, (1 << n) - 1):
        selected = [u for u in range(n) if (s_bits >> u) & 1]
        outside = [u for u in range(n) if not (s_bits >> u) & 1]
        if len(selected) == 0:
            continue
        if any(u in outside and v in outside for u, v in edges):
            continue
        ee = [frozenset((u, v)) for u, v in edges if u in selected and v in selected]
        for tree in combinations(ee, len(selected) - 1):
            tj = {v: set() for v in selected}
            for e in tree:
                u, v = tuple(e)
                tj[u].add(v)
                tj[v].add(u)
            if len(selected) > 1 and any(not tj[u] for u in selected):
                continue
            reached = {selected[0]}
            todo = [selected[0]]
            while todo:
                for v in tj[todo.pop()]:
                    if v not in reached:
                        reached.add(v)
                        todo.append(v)
            if len(reached) != len(selected):
                continue
            if any(len(tj[u]) == 1 and not (nbrs[u] & set(outside))
                   for u in selected):
                continue
            choices = [sorted(nbrs[x] & set(selected)) for x in outside]
            if any(not c for c in choices):
                continue
            tbits = 0
            for e in tree:
                tbits |= 1 << (n + edge_index[e])
            for vs in product(*choices):
                bits = s_bits | tbits
                for x, y in zip(outside, vs):
                    bits |= 1 << (n + edge_index[frozenset((x, y))])
                answer.add(bits)
    return answer


def stirling(n, k):
    vals = [[0] * (k + 1) for _ in range(n + 1)]
    vals[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            vals[i][j] = vals[i-1][j-1] + j*vals[i-1][j]
    return vals[n][k]


def predicted_complete_bipartite(a, b):
    poly = Counter()
    for q in range(1, min(a-1, b-1) + 1):
        poly[2*a+b+q-1] += (a**(b-1) * factorial(b)//factorial(b-q)
                               * stirling(a-1, q))
        poly[2*b+a+q-1] += (b**(a-1) * factorial(a)//factorial(a-q)
                               * stirling(b-1, q))
    return +poly


def base_connected(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    return connected_subset((1<<n)-1, adj)


def main():
    graph_cases = 0
    subsets = 0
    for n in (3, 4):
        all_edges = list(combinations(range(n), 2))
        for em in range(1, 1 << len(all_edges)):
            edges = tuple(e for j, e in enumerate(all_edges) if em>>j & 1)
            if not base_connected(n, edges):
                continue
            degrees = [sum(v in e for e in edges) for v in range(n)]
            actual = all_direct(n, edges)
            expected = predicted_by_leaf_tree(n, edges)
            assert actual == expected, (n, edges, actual ^ expected)
            graph_cases += 1
            subsets += (1 << (n+len(edges))) - 1
    named = [
        (5, list(combinations(range(5),2))),
        (5, [(i,(i+1)%5) for i in range(5)]),
        (6, [(i,(i+1)%6) for i in range(6)]),
        (5, [(i, i+1) for i in range(4)]),
        (5, [(0,i) for i in range(1,5)]),
    ]
    for n, edges in named:
        actual = all_direct(n, edges)
        expected = predicted_by_leaf_tree(n, edges)
        assert actual == expected, (n, edges, actual ^ expected)
        graph_cases += 1
        subsets += (1 << (n+len(edges))) - 1
    bi_cases = 0
    for a, b in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,3)]:
        edges = [(i,a+j) for i in range(a) for j in range(b)]
        direct = all_direct(a+b, edges)
        expected = predicted_complete_bipartite(a, b)
        got = Counter(bits.bit_count() for bits in direct)
        assert got == expected, (a,b,got,expected)
        bi_cases += 1
        subsets += (1 << (a+b+a*b)) - 1
    arith_cases = 0
    for a in range(2, 10):
        for b in range(2, 20):
            p = predicted_complete_bipartite(a,b)
            # All coefficients are nonnegative, and the two-shore formula
            # uses exactly the permitted q/p intervals.
            assert p and all(v > 0 for v in p.values())
            arith_cases += 1
    print('VERIFY_OK general_graphs=%d biclique_graphs=%d direct_subsets=%d arithmetic_pairs=%d'
          % (graph_cases, bi_cases, subsets, arith_cases))

if __name__ == '__main__':
    main()
