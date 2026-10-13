#!/usr/bin/env python3
"""Verify an exact general-position polynomial recursion on finite trees.

Uses Python 3 standard library only. This is a finite test suite; the
infinite-family claim rests on the combinatorial proof, not these tests.
"""
from collections import deque
from itertools import combinations, permutations, product
from math import comb
from random import Random


def plus(p, q):
    a = [0] * max(len(p), len(q))
    for i, x in enumerate(p):
        a[i] += x
    for i, x in enumerate(q):
        a[i] += x
    return trim(a)


def minus(p, q):
    return plus(p, [-x for x in q])


def times(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, u in enumerate(p):
        for j, v in enumerate(q):
            out[i + j] += u * v
    return trim(out)


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def graph(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def recurrence(adj, root=0, weights=None):
    """Multivariate formula specialized either to common x or numeric weights."""
    n = len(adj)
    def visit(v, parent):
        children = [visit(w, v) for w in adj[v] if w != parent]
        acc = [1]
        for antichain, gp in children:
            acc = times(acc, antichain)
        vertex = [0, 1] if weights is None else [weights[v]]
        A = plus(acc, vertex)
        G = A[:]
        for antichain, gp in children:
            G = plus(G, minus(gp, antichain))
            G = plus(G, times(vertex, minus(antichain, [1])))
        return A, G
    return visit(root, -1)[1]



def closed_formula(adj, root=0, weights=None):
    """Direct edge-sum formula, implemented separately from the G recursion."""
    n = len(adj)
    parent = [-2] * n
    parent[root] = -1
    stack = [root]
    order = []
    while stack:
        v = stack.pop()
        order.append(v)
        for u in adj[v]:
            if u != parent[v]:
                assert parent[u] == -2
                parent[u] = v
                stack.append(u)
    anti = [None] * n
    for v in reversed(order):
        product_poly = [1]
        for u in adj[v]:
            if parent[u] == v:
                product_poly = times(product_poly, anti[u])
        vertex = [0, 1] if weights is None else [weights[v]]
        anti[v] = plus(product_poly, vertex)
    answer = anti[root]
    for v in order:
        if v != root:
            upper = [0, 1] if weights is None else [weights[parent[v]]]
            answer = plus(answer, times(upper, minus(anti[v], [1])))
    return answer


def all_distances(adj):
    n = len(adj)
    dist = [[-1] * n for _ in range(n)]
    for start in range(n):
        dist[start][start] = 0
        Q = deque([start])
        while Q:
            u = Q.popleft()
            for v in adj[u]:
                if dist[start][v] == -1:
                    dist[start][v] = dist[start][u] + 1
                    Q.append(v)
    return dist


def direct(adj, weights=None):
    n = len(adj)
    d = all_distances(adj)
    ans = [0] * (n + 1) if weights is None else 0
    inspected = 0
    for mask in range(1 << n):
        selected = [v for v in range(n) if mask >> v & 1]
        valid = True
        for u, v, w in combinations(selected, 3):
            if (d[u][v] + d[v][w] == d[u][w]
                or d[u][v] + d[u][w] == d[v][w]
                or d[u][w] + d[w][v] == d[u][v]):
                valid = False
                break
        inspected += 1
        if valid:
            if weights is None:
                ans[len(selected)] += 1
            else:
                p = 1
                for v in selected:
                    p *= weights[v]
                ans += p
    return (trim(ans) if weights is None else ans), inspected


def prufer(n, code):
    if n <= 1:
        return []
    if n == 2:
        return [(0, 1)]
    deg = [1] * n
    for c in code:
        deg[c] += 1
    edges = []
    for c in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, c))
        deg[leaf] -= 1
        deg[c] -= 1
    leaves = [i for i in range(n) if deg[i] == 1]
    edges.append(tuple(leaves))
    return edges


def tripod(a, b, c):
    edges = []
    idx = 1
    for length in (a, b, c):
        parent = 0
        for _ in range(length):
            edges.append((parent, idx))
            parent = idx
            idx += 1
    return graph(idx, edges)


def broom(s, r):
    edges = [(i, i + 1) for i in range(s)]
    edges += [(0, s + j) for j in range(1, r + 1)]
    return graph(s + r + 1, edges)


def run():
    rng = Random(20261008)
    trees = 0
    subsets = 0
    weighted_cases = 0
    roots = 0
    for n in range(1, 11):
        if n <= 6:
            codes = product(range(n), repeat=max(n - 2, 0)) if n >= 3 else [()]
        else:
            samples = {7: 100, 8: 80, 9: 50, 10: 20}[n]
            codes = [tuple(rng.randrange(n) for _ in range(n - 2))
                     for _ in range(samples)]
        for index, code in enumerate(codes):
            adj = graph(n, prufer(n, code))
            coeff, count = direct(adj)
            observed = recurrence(adj)
            assert observed == coeff, (n, code, observed, coeff)
            assert closed_formula(adj) == coeff, (n, code, "closed")
            trees += 1
            subsets += count
            for root in (n - 1, n // 2):
                assert recurrence(adj, root) == coeff, (n, code, root)
                assert closed_formula(adj, root) == coeff, (n, code, root, "closed")
                roots += 1
            if n <= 8 and index < 10:
                for _ in range(2):
                    weights = [rng.randint(1, 4) for _ in range(n)]
                    exact, _ = direct(adj, weights)
                    assert recurrence(adj, 0, weights) == [exact]
                    assert recurrence(adj, n - 1, weights) == [exact]
                    assert closed_formula(adj, 0, weights) == [exact]
                    assert closed_formula(adj, n - 1, weights) == [exact]
                    weighted_cases += 1
            if n >= 3:
                collinear = 0
                for v in range(n):
                    remaining = set(range(n)) - {v}
                    sizes = []
                    while remaining:
                        st = remaining.pop()
                        todo = [st]
                        num = 0
                        while todo:
                            w = todo.pop()
                            num += 1
                            for z in adj[w]:
                                if z != v and z in remaining:
                                    remaining.remove(z)
                                    todo.append(z)
                        sizes.append(num)
                    collinear += sum(a*b for a, b in combinations(sizes, 2))
                expected = comb(n, 3) - collinear
                assert (coeff[3] if len(coeff) > 3 else 0) == expected
        print('ORDER', n, 'checked')

    assert recurrence(tripod(1, 1, 4)) == [1, 7, 21, 4]
    assert recurrence(tripod(1, 2, 3)) == [1, 7, 21, 6]
    for s in range(1, 8):
        for r in range(2, 9):
            got = recurrence(broom(s, r))
            N = s + r + 1
            expected = [1, N, comb(N, 2)] + [
                (s * comb(r, k - 1) if k - 1 <= r else 0)
                + (comb(r, k) if k <= r else 0)
                for k in range(3, r + 2)]
            assert got == trim(expected), (s, r, got, trim(expected))
    print('VERIFIED: trees', trees, 'unweighted_subsets', subsets,
          'root_rechecks', roots, 'weighted_evaluations', weighted_cases,
          'broom_formulas', 7 * 7)


if __name__ == '__main__':
    run()
