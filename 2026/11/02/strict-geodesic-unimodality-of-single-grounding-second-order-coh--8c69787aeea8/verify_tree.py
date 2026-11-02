#!/usr/bin/env python3
"""Exact independent checks for the tree single-grounding squared-Green result.

Run with Python 3 standard library: python verify_tree.py
"""
from fractions import Fraction as F
import random
from collections import deque


def exact_inverse(a):
    n = len(a)
    q = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k = next((i for i in range(j, n) if q[i][j]), None)
        if k is None:
            raise ArithmeticError('singular matrix')
        q[j], q[k] = q[k], q[j]
        z = q[j][j]
        q[j] = [x / z for x in q[j]]
        for i in range(n):
            if i != j:
                z = q[i][j]
                if z:
                    q[i] = [x - z * y for x, y in zip(q[i], q[j])]
    return [row[n:] for row in q]


def grounded_trace_square(n, edges, root):
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for u, v, r in edges:
        c = 1 / r
        L[u][u] += c
        L[v][v] += c
        L[u][v] -= c
        L[v][u] -= c
    vertices = [u for u in range(n) if u != root]
    Q = exact_inverse([[L[u][v] for v in vertices] for u in vertices])
    return sum(x * x for row in Q for x in row)


def optimized_values(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, r in edges:
        adj[u].append((v, r))
        adj[v].append((u, r))
    parent = [-1] * n
    parent[0] = 0
    order = [0]
    edge_r = [F(0)] * n
    depth = [F(0)] * n
    for u in order:
        for v, r in adj[u]:
            if parent[v] < 0:
                parent[v] = u
                edge_r[v] = r
                depth[v] = depth[u] + r
                order.append(v)
    assert len(order) == n
    sz = [1] * n
    W = [F(0)] * n
    for v in reversed(order[1:]):
        u = parent[v]
        sz[u] += sz[v]
        W[u] += W[v] + edge_r[v] * sz[v] ** 2
    S = [F(0)] * n
    S[0] = W[0]
    J = [F(0)] * n
    J[0] = sum(edge_r[v] * (2 * depth[parent[v]] + edge_r[v]) * sz[v] ** 2 for v in order[1:])
    brackets = {}
    for v in order[1:]:
        u = parent[v]
        r = edge_r[v]
        p, q = n - sz[v], sz[v]
        SA = S[u] - W[v] - r * q ** 2
        SB = W[v]
        bracket = 2 * (SA - SB) + r * (p ** 2 - q ** 2)
        brackets[(u, v)] = bracket
        J[v] = J[u] + r * bracket
        S[v] = S[u] + r * (p ** 2 - q ** 2)
    return J, brackets, adj


def compare(n, edges):
    J, B, adj = optimized_values(n, edges)
    direct = [grounded_trace_square(n, edges, root) for root in range(n)]
    assert J == direct, (n, edges, J, direct)
    m = min(J)
    minima = [i for i, x in enumerate(J) if x == m]
    assert len(minima) <= 2
    if len(minima) == 2:
        assert any(v == minima[1] for v, r in adj[minima[0]])
    for root in range(n):
        for a, r in adj[root]:
            if J[a] >= J[root]:
                continue
            # A root-descent move only heads toward the global optimizer.
            stack = [a]
            seen = {root, a}
            component = set()
            for v in stack:
                component.add(v)
                for w, rr in adj[v]:
                    if w not in seen:
                        seen.add(w)
                        stack.append(w)
            assert any(v in component for v in minima)
    # Along each simple path, bracket signs switch at most once.
    for start in range(n):
        par = [-1] * n
        par[start] = start
        order = [start]
        for v in order:
            for w, r in adj[v]:
                if par[w] < 0:
                    par[w] = v
                    order.append(w)
        for stop in range(n):
            path = [stop]
            while path[-1] != start:
                path.append(par[path[-1]])
            path.reverse()
            vals = []
            for u, v in zip(path, path[1:]):
                if (u, v) in B:
                    vals.append(B[(u, v)])
                else:
                    vals.append(-B[(v, u)])
            assert all(x < y for x, y in zip(vals, vals[1:])), (edges, path, vals)
    return len(edges), len(minima)


def main():
    rng = random.Random(20261025)
    cases = 0
    matrix_inversions = 0
    ties = 0
    for n in range(2, 11):
        for k in range(70):
            edges = []
            for v in range(1, n):
                p = rng.randrange(v)
                r = F(rng.choice([1, 2, 3, 5, 7, 11, 17]), rng.choice([1, 2, 3, 4, 7]))
                edges.append((p, v, r))
            _, n_minima = compare(n, edges)
            cases += 1
            matrix_inversions += n
            ties += n_minima == 2
    for r in [F(1), F(2), F(3), F(5, 3)]:
        compare(4, [(0, 1, F(1)), (1, 2, r), (2, 3, F(1))])
        cases += 1
        matrix_inversions += 4
        ties += 1
    # Equality at 2 vertices, and strict non-convexity of objective along some paths.
    compare(2, [(0, 1, F(1, 3))])
    cases += 1
    matrix_inversions += 2
    ties += 1
    J, _, _ = optimized_values(4, [(0,1,F(1)), (1,2,F(10)), (2,3,F(20))])
    assert J[0] + J[2] < 2 * J[1]
    print('PASS: exact grounded matrix inverse and O(n) objective identity')
    print('PASS: strict along-path edge-bracket increase, full optimizer set, descent')
    print('PASS: nonconvex illustrative path and two-adjacent-leader ties')
    print(f'TREE_CASES={cases}; INDEPENDENT_MATRIX_INVERSIONS={matrix_inversions}; TIE_CASES={ties}')


if __name__ == '__main__':
    main()
