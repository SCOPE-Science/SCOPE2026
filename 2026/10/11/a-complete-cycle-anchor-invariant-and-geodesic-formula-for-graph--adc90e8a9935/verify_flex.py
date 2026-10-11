#!/usr/bin/env python3
"""Finite checks of source/sink flex connectivity and geodesics.

Self-contained Python 3 script (standard library only). Computations illustrate,
but do not replace, the all-graph argument in RESULT.md.
"""
from collections import deque
from itertools import combinations


def verify_graph(n, edges):
    edges = sorted(tuple(sorted(e)) for e in edges)
    m = len(edges)
    adjacency = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adjacency[u].append((i, v))
        adjacency[v].append((i, u))
    assert all(adjacency)

    def arc(orientation, index):
        u, v = edges[index]
        return (v, u) if ((orientation >> index) & 1) else (u, v)

    def flips(orientation):
        for vertex in range(n):
            outs = 0
            for index, _ in adjacency[vertex]:
                outs += arc(orientation, index)[0] == vertex
            if outs == 0 or outs == len(adjacency[vertex]):
                yield orientation ^ sum(1 << index for index, _ in adjacency[vertex])

    def cyc_vertices(orientation):
        oriented = [arc(orientation, i) for i in range(m)]
        reach = [set([v]) for v in range(n)]
        for source, target in oriented:
            reach[source].add(target)
        for k in range(n):
            for i in range(n):
                if k in reach[i]:
                    reach[i].update(reach[k])
        cyclic = set()
        for u, v in oriented:
            if u in reach[v]:
                cyclic.add(u)
                cyclic.add(v)
        return cyclic

    def difference_potential(x, y):
        h = {0: 0}
        todo = [0]
        while todo:
            u = todo.pop()
            for index, v in adjacency[u]:
                a, b = arc(x, index)
                reversed_in_y = arc(y, index) != (a, b)
                # On X-directed edges, h(a)-h(b) is either 1 or 0.
                wanted = h[u] - (1 if a == u else -1) * reversed_in_y
                if v in h:
                    if h[v] != wanted:
                        return None
                else:
                    h[v] = wanted
                    todo.append(v)
        assert len(h) == n
        return [h[v] for v in range(n)]

    def formula(x, y):
        h = difference_potential(x, y)
        if h is None:
            return None
        C = cyc_vertices(x)
        if C:
            levels = {h[v] for v in C}
            if len(levels) > 1:
                return None
            anchor = next(iter(levels))
            return sum(abs(z - anchor) for z in h)
        vals = sorted(h)
        median = vals[n // 2]
        return sum(abs(z - median) for z in h)

    checked = 0
    for x in range(1 << m):
        dist = {x: 0}
        q = deque([x])
        while q:
            a = q.popleft()
            for b in flips(a):
                if b not in dist:
                    dist[b] = dist[a] + 1
                    q.append(b)
        for y in range(1 << m):
            assert formula(x, y) == dist.get(y), (n, edges, x, y, formula(x, y), dist.get(y))
            checked += 1
    return checked


def main():
    base_graphs = [
        (2, [(0, 1)]),
        (3, [(0, 1), (1, 2)]),
        (3, [(0, 1), (1, 2), (0, 2)]),
        (4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
        (4, list(combinations(range(4), 2))),
        (5, [(i, (i + 1) % 5) for i in range(5)]),
        (5, [(i, (i + 1) % 5) for i in range(5)] + [(0, 2), (0, 3)]),
        (5, [(i, j) for i in range(2) for j in range(2, 5)]),
        (6, [(i, (i + 1) % 6) for i in range(6)]),
        (6, [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (2, 3)]),
        (6, [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (4, 5), (5, 0)]),
    ]
    total = 0
    for n, edges in base_graphs:
        checked = verify_graph(n, edges)
        total += checked
        print(f"PASS vertices={n} edges={len(edges)} ordered_orientation_pairs={checked}")
    print(f"VERIFY_OK graphs={len(base_graphs)} ordered_orientation_pairs={total}")


if __name__ == '__main__':
    main()
