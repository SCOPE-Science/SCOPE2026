#!/usr/bin/env python3
"""Direct finite-field centralizer checks for height-two incidence algebras.

The centralizer rank is computed from the full multiplication table,
not from edge-color formulas. Requires only the Python standard library.
"""
from collections import Counter
from itertools import product
from math import comb


def polynomial_mult(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def polynomial_pow(a, k):
    out = [1]
    for _ in range(k):
        out = polynomial_mult(out, a)
    return out


def polynomial_add(*polys):
    n = max(len(p) for p in polys)
    return [sum(p[i] if i < len(p) else 0 for p in polys) for i in range(n)]


def matroid_polynomial(n, edges, q):
    """Independent three-state edge expansion of the graphic-matroid formula."""
    m = len(edges)
    rank_cache = {}
    for mask in range(1 << m):
        parent = list(range(n))
        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v
        rank = 0
        for j, (u, v) in enumerate(edges):
            if (mask >> j) & 1:
                a, b = root(u), root(v)
                if a != b:
                    parent[a] = b
                    rank += 1
        rank_cache[mask] = rank
    coeffs = [0] * (m + 1)
    for status in product((0, 1, 2), repeat=m):
        s_mask = sum((1 << j) for j, v in enumerate(status) if v == 1)
        t_mask = sum((1 << j) for j, v in enumerate(status) if v == 2)
        s, t = s_mask.bit_count(), t_mask.bit_count()
        base_degree = rank_cache[s_mask] + m - s - t
        factor = (q-1)**s * q**(n-rank_cache[s_mask | t_mask] + m-s-t)
        for j in range(t+1):
            coeffs[base_degree + j] += factor * comb(t, j) * (-q)**j
    return coeffs


def predicted(n, edges, q):
    m = len(edges)
    # The input graphs are either forests or have one even cycle.
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    cycle_count = 0
    for a, b in edges:
        x, y = root(a), root(b)
        if x == y:
            cycle_count += 1
        else:
            parent[x] = y
    components = len({root(v) for v in range(n)})
    P = [1, q * q - 1]
    if cycle_count == 0:
        return [q**components * x for x in polynomial_pow(P, m)]
    if cycle_count > 1 or components > 1:
        return matroid_polynomial(n, edges, q)
    assert cycle_count == 1 and components == 1
    # Identify cycle length via leaf stripping.
    deg = [0] * n
    nbr = [[] for _ in range(n)]
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
        nbr[u].append(v)
        nbr[v].append(u)
    waiting = [i for i in range(n) if deg[i] == 1]
    while waiting:
        v = waiting.pop()
        if deg[v] == 0:
            continue
        deg[v] = 0
        for w in nbr[v]:
            if deg[w]:
                deg[w] -= 1
                if deg[w] == 1:
                    waiting.append(w)
    ell = sum(x > 0 for x in deg)
    assert ell >= 4 and ell % 2 == 0
    correction = [0] * (ell + 1)
    correction[ell - 1] += q * (q - 1)**ell
    correction[ell] -= q * (q - 1)**ell
    cycle = polynomial_add(polynomial_pow(P, ell),
                           [(q - 1) * x for x in polynomial_pow([1, -1], ell)],
                           correction)
    return polynomial_mult(polynomial_pow(P, m - ell), cycle)


def product_in_algebra(x, y, edges, n, q):
    m = len(edges)
    out = [x[i] * y[i] % q for i in range(n)]
    for j, (u, v) in enumerate(edges):
        out.append((x[u] * y[n+j] + x[n+j] * y[v]) % q)
    assert len(out) == n + m
    return out


def rank_mod(matrix, q):
    if not matrix:
        return 0
    a = [list(row) for row in matrix]
    rows, cols = len(a), len(a[0])
    piv = 0
    for col in range(cols):
        pivot = next((r for r in range(piv, rows) if a[r][col] % q), None)
        if pivot is None:
            continue
        a[piv], a[pivot] = a[pivot], a[piv]
        inv = pow(a[piv][col] % q, -1, q)
        a[piv] = [(val * inv) % q for val in a[piv]]
        for row in range(piv + 1, rows):
            factor = a[row][col]
            if factor:
                a[row] = [(a[row][k] - factor * a[piv][k]) % q for k in range(cols)]
        piv += 1
        if piv == rows:
            break
    return piv


def verify(n, edges, q, label):
    m = len(edges)
    assert all(0 <= u < n and 0 <= v < n and u != v for u, v in edges)
    # Height-two directed graph: no vertex may be both a head and a tail.
    assert not ({u for u, v in edges} & {v for u, v in edges})
    D = n + m
    basis = [tuple(1 if i == j else 0 for i in range(D)) for j in range(D)]
    actual = Counter()
    for a in product(range(q), repeat=D):
        commutator_columns = []
        for b in basis:
            ab = product_in_algebra(a, b, edges, n, q)
            ba = product_in_algebra(b, a, edges, n, q)
            commutator_columns.append([(x-y) % q for x, y in zip(ab, ba)])
        ad = [[commutator_columns[j][i] for j in range(D)]
              for i in range(D)]
        actual[rank_mod(ad, q)] += 1
    expected = predicted(n, edges, q)
    assert matroid_polynomial(n, edges, q) == expected, (label, "matroid formula")
    computed = [actual.get(i, 0) for i in range(len(expected))]
    assert computed == expected, (label, expected, computed)
    assert sum(expected) == q**D
    print('PASS', label, 'q', q, 'algebra_elements', q**D, 'rank_counts', expected)
    return q**D


def main():
    cases = [
        ('isolated pair', 2, [], 3),
        ('single arrow', 2, [(0, 1)], 3),
        ('star 4', 5, [(0, i) for i in range(1, 5)], 2),
        ('fence 4', 5, [(0, 1), (2, 1), (2, 3), (4, 3)], 2),
        ('fence 3', 4, [(0, 1), (2, 1), (2, 3)], 3),
        ('disconnected forest', 5, [(0, 1), (2, 3)], 3),
        ('cycle 4', 4, [(0, 1), (2, 1), (2, 3), (0, 3)], 2),
        ('cycle 4 q3', 4, [(0, 1), (2, 1), (2, 3), (0, 3)], 3),
        ('cycle 6', 6, [(0, 1), (2, 1), (2, 3), (4, 3), (4, 5), (0, 5)], 2),
        ('cycle4-branch-tree', 6, [(0, 1), (2, 1), (2, 3), (0, 3), (0, 4), (4, 5)], 2),
    ]
    # Alternative valid height-two tree attachments (same cycle length).
    cases[-1] = ('cycle4-two-leaves', 6, [(0, 1), (2, 1), (2, 3), (0, 3), (0, 5), (4, 1)], 2)
    # Distinct attachment pattern on six vertices.
    cases.append(('cycle4-two-leaves-same-parent', 6,
                  [(0, 1), (2, 1), (2, 3), (0, 3), (0, 5), (0, 4)], 2))
    cases.append(('complete-bipartite K2,3', 5,
                  [(0,2), (0,3), (0,4), (1,2), (1,3), (1,4)], 2))
    total = 0
    for label, n, edges, q in cases:
        total += verify(n, edges, q, label)
    print('ALL_INCIDENCE_CENTRALIZER_CHECKS_PASSED', len(cases), total)

if __name__ == '__main__':
    main()
