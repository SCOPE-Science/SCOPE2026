#!/usr/bin/env python3
"""Finite-field checks of axis-tree multigraded section ranks.

This is a numerical consistency check, not a proof of the general theorem.
"""
from itertools import product

P = 101


def paths(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    out = {}
    for start in range(n):
        predecessor = {start: None}
        queue = [start]
        for u in queue:
            for v in adj[u]:
                if v not in predecessor:
                    predecessor[v] = u
                    queue.append(v)
        assert len(queue) == n
        for finish in range(n):
            route = [finish]
            while route[-1] != start:
                route.append(predecessor[route[-1]])
            out[start, finish] = list(reversed(route))
    return adj, out


def constants(n, edges):
    adj, routes = paths(n, edges)
    # Each incident edge receives a distinct rational point on P^1.
    point = {(v, w): j for v in range(n) for j, w in enumerate(sorted(adj[v]))}
    c = {}
    for component in range(n):
        for factor in range(n):
            if factor != component:
                c[component, factor] = point[factor, routes[factor, component][1]]
    for i in range(n):
        for j in range(i + 1, n):
            meet = all(c[i, k] == c[j, k] for k in range(n) if k != i and k != j)
            assert meet == ((i, j) in edges or (j, i) in edges), (edges, i, j)
    return c


def rank_mod(rows):
    if not rows:
        return 0
    a = [list(row) for row in rows]
    m, cols = len(a), len(a[0])
    pivot = 0
    for col in range(cols):
        if pivot == m:
            break
        nonzero = next((i for i in range(pivot, m) if a[i][col]), None)
        if nonzero is None:
            continue
        a[pivot], a[nonzero] = a[nonzero], a[pivot]
        inv = pow(a[pivot][col], -1, P)
        a[pivot] = [(x * inv) % P for x in a[pivot]]
        for i in range(pivot + 1, m):
            q = a[i][col]
            if q:
                a[i] = [(x - q*y) % P for x, y in zip(a[i], a[pivot])]
        pivot += 1
    return pivot


def section_rank(n, c, multi):
    mons = list(product(*(range(x + 1) for x in multi)))
    offsets = [sum(multi[j] + 1 for j in range(i)) for i in range(n)]
    matrix = [[0] * len(mons) for _ in range(sum(x + 1 for x in multi))]
    for col, degrees in enumerate(mons):
        for comp in range(n):
            value = 1
            for j in range(n):
                if j != comp:
                    value = (value * pow(c[comp, j], degrees[j], P)) % P
            matrix[offsets[comp] + degrees[comp]][col] = value
    return rank_mod(matrix)


def main():
    examples = [
        (2, [(0, 1)]),
        (3, [(0, 1), (1, 2)]),
        (4, [(0, 1), (1, 2), (2, 3)]),
        (4, [(0, 1), (0, 2), (0, 3)]),
        (5, [(0, 1), (1, 2), (2, 3), (3, 4)]),
        (5, [(0, 1), (0, 2), (0, 3), (0, 4)]),
    ]
    count = 0
    for n, edges in examples:
        c = constants(n, edges)
        for multi in product(range(3), repeat=n):
            actual = section_rank(n, c, multi)
            expected = 1 + sum(multi)
            assert actual == expected, (n, edges, multi, actual, expected)
            count += 1
    print(f'VERIFY_OK {len(examples)} trees, {count} multidegrees, prime {P}')


if __name__ == '__main__':
    main()
