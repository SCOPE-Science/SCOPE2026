#!/usr/bin/env python3
"""Direct finite-algebra checks for a universal commuting-idempotent formula.

Two associative six-dimensional algebras share the Peirce dimensions
but have different radical multiplication. The first is a path algebra
for 1 -> 2 -> 3; the second has the same three arrows with radical square
zero. No third-party packages are required.
"""
from itertools import product
from collections import Counter


def product_algebra(x, y, p, path):
    out = [0] * 6
    # Basis: vertex idempotents 0,1,2; arrows 0->1,1->2,0->2.
    arrows = ((0, 1), (1, 2), (0, 2))
    for i in range(3):
        out[i] = x[i] * y[i]
    for t, (source, target) in enumerate(arrows):
        out[t + 3] = x[source] * y[t + 3] + x[t + 3] * y[target]
    if path:
        out[5] += x[3] * y[4]
    return tuple(t % p for t in out)


def dot(x, y, p, path):
    return product_algebra(x, y, p, path)


def finite_profile(p, path):
    elems = list(product(range(p), repeat=6))
    idempotents = [x for x in elems if dot(x, x, p, path) == x]
    n = len(idempotents)
    adj = [[dot(x, y, p, path) == dot(y, x, p, path)
            for y in idempotents] for x in idempotents]
    t = [1, n, sum(int(v) for row in adj for v in row)]
    # Ordered pairwise-commuting triples, including repeated vertices.
    t.append(sum(sum(adj[i][h] and adj[j][h] for h in range(n))
                 for i in range(n) for j in range(n) if adj[i][j]))
    # Backtracking maximal cliques using unique pivot recursion.
    neighbors = [set(j for j in range(n) if j != i and adj[i][j]) for i in range(n)]
    max_cliques = []
    def bk(R, P, X):
        if not P and not X:
            max_cliques.append(frozenset(R))
            return
        union = P | X
        pivot = max(union, key=lambda u: len(P & neighbors[u])) if union else None
        for v in list(P - (neighbors[pivot] if pivot is not None else set())):
            bk(R | {v}, P & neighbors[v], X & neighbors[v])
            P.remove(v)
            X.add(v)
    bk(set(), set(range(n)), set())
    return t, Counter(map(len, max_cliques))


def prediction(p, k):
    return sum(p ** sum(c[i] != c[j] for i in range(3)
                        for j in range(i + 1, 3))
               for c in product(range(2 ** k), repeat=3))


def run():
    for p in (2, 3):
        expected = [prediction(p, k) for k in range(4)]
        for path in (False, True):
            observed, maximal = finite_profile(p, path)
            assert observed == expected, (p, path, observed, expected)
            assert maximal == Counter({8: p**3}), (p, path, maximal)
            label = 'path_algebra' if path else 'square_zero'
            print(f'CHECK_OK field={p} algebra={label} tuples={observed} maximal={dict(maximal)}')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
