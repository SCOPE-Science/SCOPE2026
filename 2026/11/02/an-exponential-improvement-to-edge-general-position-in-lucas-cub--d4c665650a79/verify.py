#!/usr/bin/env python3
"""Independent finite verification of an edge-geodesic construction on Lucas cubes."""
from collections import deque


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def instance(n):
    vertices = tuple(x for x in range(1 << n)
                     if (x & (x << 1)) == 0
                     and not ((x & 1) and (x & (1 << (n - 1)))))
    vset = set(vertices)
    edges = {tuple(sorted((x, x ^ (1 << i))))
             for x in vertices for i in range(n)
             if x ^ (1 << i) in vset}
    adj = {x: [] for x in vertices}
    for a, b in sorted(edges):
        adj[a].append(b)
        adj[b].append(a)
    selected = set()
    for a, b in edges:
        coord = (a ^ b).bit_length() - 1
        if coord == 0 or (coord == 1 and (a & (1 << (n - 1))) == 0) or (coord == n - 1 and (a & 2) == 0):
            selected.add((a, b))
    return vertices, edges, adj, selected


def bfs(adj, source):
    dist = {source: 0}
    q = deque([source])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                q.append(w)
    return dist


def verify(n):
    vs, edges, adj, selected = instance(n)
    expected = fibonacci(n - 1) + 2 * fibonacci(n - 2)
    assert len(selected) == expected, (n, len(selected), expected)
    dists = {v: bfs(adj, v) for v in vs}
    assert all(dists[a][b] == (a ^ b).bit_count() for a in vs for b in vs)
    geodesics = [0]
    selected_on_paths = [0]
    for k, s in enumerate(vs):
        for t in vs[k + 1:]:
            def visit(v, hits):
                if v == t:
                    geodesics[0] += 1
                    if hits > selected_on_paths[0]:
                        selected_on_paths[0] = hits
                    assert hits <= 2, (n, s, t, hits)
                    return
                for w in adj[v]:
                    if dists[w][t] == dists[v][t] - 1:
                        e = tuple(sorted((v, w)))
                        visit(w, hits + int(e in selected))
            visit(s, 0)
    assert selected_on_paths[0] == 2
    print('n=%d vertices=%d edges=%d selected=%d expected=%d geodesics=%d max_selected_on_geodesic=%d OK' %
          (n, len(vs), len(edges), len(selected), expected, geodesics[0], selected_on_paths[0]))


if __name__ == '__main__':
    for n in range(5, 10):
        verify(n)
    print('ALL_CHECKS_PASSED')
