#!/usr/bin/env python3
"""Independent finite-instance enumeration of commuting idempotents in incidence algebras.

No external packages. The general formula in RESULT.md is proved algebraically;
finite exhaustive tests here do not certify the universal quantifiers.
"""
from itertools import product


def plus(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def times(a, b, q):
    if q != 4:
        return (a * b) % q
    # GF(4) = GF(2)[t]/(t*t+t+1), polynomial-bit representation.
    u = 0
    while b:
        if b & 1:
            u ^= a
        a <<= 1
        if a & 4:
            a ^= 7
        b >>= 1
    return u


def check_instance(label, n, strict_pairs, q, k):
    pairs = [(i, i) for i in range(n)] + strict_pairs
    index = {p: h for h, p in enumerate(pairs)}
    terms = []
    for h, (i, j) in enumerate(pairs):
        for z in range(n):
            if (i, z) in index and (z, j) in index:
                terms.append((h, index[i, z], index[z, j]))

    def product_a(a, b):
        ans = [0] * len(pairs)
        for dest, source1, source2 in terms:
            ans[dest] = plus(ans[dest], times(a[source1], b[source2], q), q)
        return tuple(ans)

    idempotents = [a for a in product(range(q), repeat=len(pairs))
                   if product_a(a, a) == a]
    observed = {}
    # All tuples, checking every defining equation, without conjugacy shortcuts.
    def recurse(chosen, tuple_product_ok):
        if len(chosen) == k:
            signature = tuple(tuple(chosen[t][i] for t in range(k))
                              for i in range(n))
            observed[signature] = observed.get(signature, 0) + 1
            return
        for a in idempotents:
            if all(product_a(a, b) == product_a(b, a) for b in chosen):
                recurse(chosen + [a], True)
    recurse([], True)
    all_colors = list(product(range(2), repeat=k))
    expected = {}
    for coloring in product(all_colors, repeat=n):
        different = sum(coloring[i] != coloring[j] for i, j in strict_pairs)
        expected[coloring] = q ** different
    assert expected == observed, (label, q, k,
        [(c, expected[c], observed.get(c)) for c in expected
          if expected[c] != observed.get(c)][:5])
    def norm(v):
        return v % 2 if q == 4 else v % q

    def matrix_rank(rows):
        if not rows: return 0
        rows = [row[:] for row in rows]
        r = 0
        for col in range(len(rows[0])):
            pivot = next((j for j in range(r, len(rows)) if rows[j][col]), None)
            if pivot is None: continue
            rows[r], rows[pivot] = rows[pivot], rows[r]
            a = rows[r][col]
            inv = next(v for v in range(1, q) if times(a, v, q) == 1)
            rows[r] = [times(inv, a, q) for a in rows[r]]
            for j in range(len(rows)):
                if j == r or not rows[j][col]: continue
                a = rows[j][col]
                rows[j] = [plus(rows[j][p], times(norm(-1), times(a, rows[r][p], q), q), q)
                           for p in range(len(rows[0]))]
            r += 1
        return r

    # Independent first-order Jacobian rank test for all canonical diagonal tuples.
    for coloring in expected:
        jac = []
        for ell, (a, b) in enumerate(pairs):
            for t in range(k):
                row = [0] * (k * len(pairs))
                row[t * len(pairs) + ell] = norm(coloring[a][t] + coloring[b][t] - 1)
                jac.append(row)
            for t in range(k):
                for u in range(t + 1, k):
                    row = [0] * (k * len(pairs))
                    row[t * len(pairs) + ell] = norm(coloring[b][u] - coloring[a][u])
                    row[u * len(pairs) + ell] = norm(coloring[a][t] - coloring[b][t])
                    jac.append(row)
        tangent_dimension = k * len(pairs) - matrix_rank(jac)
        mixed = sum(coloring[a] != coloring[b] for a, b in strict_pairs)
        assert tangent_dimension == mixed, (label, coloring, tangent_dimension, mixed)
    print(label, 'q=', q, 'k=', k, 'tuples=', sum(observed.values()),
          'and all tangent dimensions PASS')


def run():
    tests = [
        ('edge', 2, [(0, 1)], 2, 3),
        ('edge', 2, [(0, 1)], 3, 2),
        ('edge', 2, [(0, 1)], 4, 2),
        ('chain3', 3, [(0, 1), (0, 2), (1, 2)], 2, 2),
        ('chain3', 3, [(0, 1), (0, 2), (1, 2)], 3, 2),
        ('chain3', 3, [(0, 1), (0, 2), (1, 2)], 4, 2),
        ('fork3', 3, [(0, 2), (1, 2)], 3, 2),
        ('diamond4', 4, [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3)], 2, 2),
    ]
    for args in tests:
        check_instance(*args)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
