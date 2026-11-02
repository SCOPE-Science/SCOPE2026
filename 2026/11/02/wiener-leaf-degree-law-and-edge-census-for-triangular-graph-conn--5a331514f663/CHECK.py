#!/usr/bin/env python3
"""Independent finite checks for the triangular-graph connected-domination exchange formulas.

Run: python3 check_ctree_reconfiguration.py
Requires only Python 3 standard library.
"""
from collections import deque
from itertools import combinations, product
from math import comb


def pair_edges(n):
    return list(combinations(range(n), 2))


def is_connected_dominating(n, edges, mask):
    chosen = [e for i, e in enumerate(edges) if (mask >> i) & 1]
    if not chosen:
        return False
    # All vertices of the line graph must have a chosen incident edge.
    for u, v in edges:
        if not any(u in e or v in e for e in chosen):
            return False
    # A breadth-first search on the line graph induced by chosen edges.
    reached = {0}
    queue = deque([0])
    while queue:
        i = queue.popleft()
        for j, e in enumerate(chosen):
            if j not in reached and any(v in chosen[i] for v in e):
                reached.add(j)
                queue.append(j)
    return len(reached) == len(chosen)


def tree_description(n, edges, mask):
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            adj[u].append(v)
            adj[v].append(u)
    support = [v for v in range(n) if adj[v]]
    return adj, support


def wiener_leaf_degree(n, edges, mask):
    adj, support = tree_description(n, edges, mask)
    assert len(support) == n - 1
    leaves = sum(len(adj[v]) == 1 for v in support)
    distances = 0
    for u in support:
        queue = deque([u]); ds = {u: 0}
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if w not in ds:
                    ds[w] = ds[v] + 1; queue.append(w)
        assert len(ds) == n - 1
        distances += sum(ds.values())
    return distances // 2 + (n - 2) * (leaves - 1)


def predicted_total_edges(n):
    m = n - 1
    total_w = sum(comb(m, s) * s ** s * (m - s) ** (m - s)
                  for s in range(1, m)) // 2
    number_trees = m ** (m - 2)
    total_leaves = m * (m - 1) ** (m - 2)
    full_degree_sum = n * (total_w + (m - 1) * (total_leaves - number_trees))
    assert full_degree_sum % 2 == 0
    return full_degree_sum // 2


def finite_check(n):
    edges = pair_edges(n)
    N = len(edges)
    tested = 0
    for mask in range(1 << N):
        valid = is_connected_dominating(n, edges, mask)
        tested += 1
        if mask.bit_count() < n - 2:
            assert not valid, (n, mask)
    states = []
    for chosen in combinations(range(N), n - 2):
        mask = sum(1 << i for i in chosen)
        if is_connected_dominating(n, edges, mask):
            adj, support = tree_description(n, edges, mask)
            assert len(support) == n - 1
            states.append(mask)
    m = n - 1
    assert len(states) == n * m ** (m - 2)
    id_of = {mask: i for i, mask in enumerate(states)}
    nbr = []
    for mask in states:
        found = set()
        for i in range(N):
            if mask & (1 << i):
                for j in range(N):
                    if not mask & (1 << j):
                        other = mask ^ (1 << i) ^ (1 << j)
                        if is_connected_dominating(n, edges, other):
                            assert other in id_of
                            found.add(id_of[other])
        assert len(found) == wiener_leaf_degree(n, edges, mask)
        nbr.append(found)
    for i, around in enumerate(nbr):
        for j in around:
            assert i in nbr[j]
    edges_count = sum(map(len, nbr)) // 2
    assert edges_count == predicted_total_edges(n)
    # Connectivity is proved in general, and independently checked here.
    reachable = {0}; q = deque([0])
    while q:
        v = q.popleft()
        for w in nbr[v] - reachable:
            reachable.add(w); q.append(w)
    assert len(reachable) == len(states)
    print('n=%d all_subsets=%d optima=%d exchanges=%d connected=yes' %
          (n, tested, len(states), edges_count))
    return tested


def check_closed_form(n):
    m = n - 1
    if m >= 4:
        star = (m - 1) * (2 * m - 3)
        path = m * (m ** 2 - 1) // 6 + m - 1
        assert star - path == -(m - 8) * (m - 3) * (m - 1) // 6
    if m >= 6:
        # A double broom with two pendants at each end of a path on m-4 vertices.
        adj = [[] for _ in range(m)]
        def add(u, v):
            adj[u].append(v); adj[v].append(u)
        for u in range(m - 5):
            add(u, u + 1)
        for u, v in ((0, m-4), (0, m-3), (m-5, m-2), (m-5, m-1)):
            add(u, v)
        dist_sum = 0
        for source in range(m):
            dist = {source: 0}; q = deque([source])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in dist:
                        dist[v] = dist[u] + 1; q.append(v)
            assert len(dist) == m
            dist_sum += sum(dist.values())
        wb = dist_sum // 2
        wp = m * (m ** 2 - 1) // 6
        assert wb == wp - (2 * m - 6)
        assert wb + (m - 1) * (4 - 1) == wp + (m - 1) + 4


if __name__ == '__main__':
    subtotal = sum(finite_check(n) for n in range(3, 7))
    for n in range(3, 18):
        check_closed_form(n)
    print('ALL_CHECKS_PASSED total_graph_subsets=%d' % subtotal)
