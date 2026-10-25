"""Exact tests of outbreak-size distributions for correlated offspring on finite trees.

No external dependencies. Run with: python verify.py
"""
from fractions import Fraction as Q
from itertools import product
from collections import deque


def rooted_edges_from_prufer(code):
    n = len(code) + 2
    degrees = [1] * n
    for x in code:
        degrees[x] += 1
    edges = []
    for x in code:
        leaf = next(v for v in range(n) if degrees[v] == 1)
        edges.append((leaf, x))
        degrees[leaf] -= 1
        degrees[x] -= 1
    last = [v for v in range(n) if degrees[v] == 1]
    edges.append(tuple(last))
    return n, edges


def orient(n, edges, root=0):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    parent = [-1] * n
    depth = [-1] * n
    depth[root] = 0
    todo = deque([root])
    while todo:
        u = todo.popleft()
        for v in adj[u]:
            if depth[v] < 0:
                depth[v] = depth[u] + 1
                parent[v] = u
                todo.append(v)
    assert all(x >= 0 for x in depth)
    children = [[] for _ in range(n)]
    for v in range(n):
        if v != root:
            children[parent[v]].append(v)
    return children, parent, depth


def multiply(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def poly_for_subtree(children, v, p_distribution):
    sub = [poly_for_subtree(children, u, p_distribution) for u in children[v]]
    ans = [Q(0)] * (1 + sum(len(t) - 1 for t in sub) + 1)
    for p, weight in p_distribution:
        current = [Q(1)]
        for dist in sub:
            temp = [(Q(1) - p) + p * dist[0]] + [p * x for x in dist[1:]]
            current = multiply(current, temp)
        current = [Q(0)] + current
        for i, x in enumerate(current):
            ans[i] += weight * x
    return ans


def get_moments(poly):
    mean = sum((i * x for i, x in enumerate(poly)), Q(0))
    second = sum((i * i * x for i, x in enumerate(poly)), Q(0))
    return mean, second - mean * mean


def lca(u, v, parent, depth):
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u


def coefficient(parent, depth, q):
    n = len(parent)
    total = Q(0)
    for u in range(n):
        for v in range(u + 1, n):
            w = lca(u, v, parent, depth)
            if w != u and w != v:
                total += 2 * q ** (depth[u] + depth[v] - depth[w] - 2)
    return total


def check(n, edges, q, variable_dist):
    ch, parent, dep = orient(n, edges)
    baseline = poly_for_subtree(ch, 0, [(q, Q(1))])
    variable = poly_for_subtree(ch, 0, variable_dist)
    assert sum(baseline) == sum(variable) == 1
    m0, v0 = get_moments(baseline)
    m1, v1 = get_moments(variable)
    assert m0 == m1 == sum((q ** dep[v] for v in range(n)), Q(0))
    var_p = sum((w * (p - q) ** 2 for p, w in variable_dist), Q(0))
    B = coefficient(parent, dep, q)
    assert v1 - v0 == B * var_p
    assert Q(0) <= B <= (n - 1) * (n - 2)
    for threshold in range(n + 1):
        stop0 = sum((max(0, i - threshold) * p for i, p in enumerate(baseline)), Q(0))
        stop1 = sum((max(0, i - threshold) * p for i, p in enumerate(variable)), Q(0))
        assert stop1 >= stop0
    return n + 5


def main():
    q = Q(1, 2)
    varying = [(Q(1, 4), Q(1, 2)), (Q(3, 4), Q(1, 2))]
    assert sum(p * w for p, w in varying) == q
    tested, checks = 0, 0
    for n in range(2, 7):
        for code in product(range(n), repeat=n - 2):
            N, edges = rooted_edges_from_prufer(code)
            checks += check(N, edges, q, varying)
            tested += 1
    n, edges = 4, [(0, 1), (0, 2), (0, 3)]
    ch, par, dep = orient(n, edges)
    base = poly_for_subtree(ch, 0, [(q, Q(1))])
    mix = poly_for_subtree(ch, 0, varying)
    assert get_moments(base)[1] == Q(3, 4)
    assert get_moments(mix)[1] == Q(9, 8)
    assert coefficient(par, dep, q) == 6
    checks += 3
    print(f"PASS: {tested} rooted labeled trees, {checks} exact rational checks")

if __name__ == '__main__':
    main()
