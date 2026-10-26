"""Finite independent checks of conditional Cayley-tree leaf factorial moments.
Run with Python 3 and no third-party dependencies.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product


def decode(code, n):
    deg = [1] * n
    for v in code:
        deg[v] += 1
    adj = [[] for _ in range(n)]
    for v in code:
        u = next(j for j in range(n) if deg[j] == 1)
        adj[u].append(v)
        adj[v].append(u)
        deg[u] -= 1
        deg[v] -= 1
    a, b = (j for j in range(n) if deg[j] == 1)
    adj[a].append(b)
    adj[b].append(a)
    return adj


def marked_path(adj):
    parent = {0: -1}
    queue = [0]
    for v in queue:
        if v == 1:
            break
        for w in adj[v]:
            if w not in parent:
                parent[w] = v
                queue.append(w)
    path = {1}
    t = 1
    while t != 0:
        t = parent[t]
        path.add(t)
    return path


def falling(a, b):
    p = 1
    for k in range(b):
        p *= a - k
    return p


def predicted(n, d, r, s):
    if d == 1 and s == 2:
        return Fraction(0)
    if n == 2:
        return Fraction(2 if s == 2 else 1 if s == 1 else 1)
    m = n - d - 1
    return Fraction(falling(m, r) * falling(2, s) * (d + 1 - s), d + 1) * Fraction(n - r - s, n) ** (n - d - 2)


def main():
    total_trees = 0
    checks = 0
    for n in range(3, 9):
        counts = defaultdict(int)
        totals = defaultdict(int)
        for code in product(range(n), repeat=n - 2):
            adj = decode(code, n)
            path = marked_path(adj)
            d = len(path) - 1
            X = sum(len(adj[v]) == 1 for v in range(n) if v not in path)
            Y = sum(len(adj[v]) == 1 for v in (0, 1))
            counts[d] += 1
            for r in range(min(3, n - d)):
                for s in range(3):
                    totals[d, r, s] += falling(X, r) * falling(Y, s)
            total_trees += 1
        assert sum(counts.values()) == n ** (n - 2)
        for d in range(1, n):
            path_count = Fraction((d + 1) * n ** (n - d - 2) * falling(n - 2, d - 1))
            assert counts[d] == path_count, (n, d, counts[d], path_count)
            checks += 1
            for r in range(min(3, n - d)):
                for s in range(3):
                    assert Fraction(totals[d, r, s], counts[d]) == predicted(n, d, r, s), (n, d, r, s)
                    checks += 1
            ex = predicted(n, d, 1, 0) + predicted(n, d, 0, 1) if n > d + 1 else predicted(n, d, 0, 1)
            exact = (n - d + 1 - Fraction(2, d + 1)) * Fraction(n - 1, n) ** (n - d - 2)
            assert ex == exact, (n, d, ex, exact)
            checks += 1
        for d in range(1, n - 1):
            e1 = (n - d + 1 - Fraction(2, d + 1)) * Fraction(n - 1, n) ** (n - d - 2)
            e2 = (n - d - Fraction(2, d + 2)) * Fraction(n - 1, n) ** (n - d - 3)
            sign = 2 * (n - 1) - d * (d + 1) ** 2
            assert (e2 > e1) - (e2 < e1) == (sign > 0) - (sign < 0)
            checks += 1
    print('PASS:', total_trees, 'labelled trees;', checks, 'exact rational moment/count/phase comparisons')


if __name__ == '__main__':
    main()
