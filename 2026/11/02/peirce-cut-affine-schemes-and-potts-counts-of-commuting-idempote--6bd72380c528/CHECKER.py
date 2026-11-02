#!/usr/bin/env python3
"""Independent finite-field checks of commuting-idempotent enumeration.

Only standard Python is used.  Every algebra product is formed by a path
multiplication table rather than by the proposed Peirce-component formula.
"""
from itertools import product, combinations


def fadd(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def fmul(a, b, q):
    if q != 4:
        return (a * b) % q
    out = 0
    for i in range(2):
        for j in range(2):
            if (a >> i & 1) and (b >> j & 1):
                t = i + j
                out ^= 1 << t if t < 2 else 3  # t^2=t+1
    return out


def basis_paths(n, arrows, d):
    """List (vertex sequence, arrow sequence) with length below d.

    Parallel arrows retain separate identities in the arrow sequence.
    """
    paths = [((v,), ()) for v in range(n)]
    layer = paths[:]
    for step in range(1, d):
        extension = []
        for vertices, seq in layer:
            for i, (u, v) in enumerate(arrows):
                if u == vertices[-1]:
                    extension.append((vertices + (v,), seq + (i,)))
        paths += extension
        layer = extension
    return paths


def algebra(n, arrows, d):
    paths = basis_paths(n, arrows, d)
    lookup = {seq: idx for idx, (_, seq) in enumerate(paths)}
    # Need vertex check for length-zero paths; unique indexing by sequence
    # is not valid at length zero, so use the full key instead.
    lookup = {(vs[0], seq): idx for idx, (vs, seq) in enumerate(paths)}
    table = []
    for i, (vi, si) in enumerate(paths):
        row = []
        for j, (vj, sj) in enumerate(paths):
            if vi[-1] == vj[0] and len(si) + len(sj) < d:
                row.append(lookup[(vi[0], si + sj)])
            else:
                row.append(-1)
        table.append(row)
    return paths, table


def mul(x, y, table, q):
    z = [0] * len(x)
    for i, a in enumerate(x):
        if a:
            for j, b in enumerate(y):
                k = table[i][j]
                if b and k >= 0:
                    z[k] = fadd(z[k], fmul(a, b, q), q)
    return tuple(z)


def direct_count(n, arrows, d, q, m):
    paths, table = algebra(n, arrows, d)
    elements = product(range(q), repeat=len(paths))
    idem = []
    for x in elements:
        if mul(x, x, table, q) == x:
            idem.append(x)
    def commute(a, b):
        return mul(a, b, table, q) == mul(b, a, table, q)
    if m == 1:
        return len(idem), len(paths), len(idem)
    if m == 2:
        count = sum(commute(a, b) for a in idem for b in idem)
        return count, len(paths), len(idem)
    if m == 3:
        adj = [[commute(a, b) for b in idem] for a in idem]
        count = sum(adj[i][j] and adj[j][k] and adj[k][i]
                    for i in range(len(idem)) for j in range(len(idem))
                    for k in range(len(idem)))
        return count, len(paths), len(idem)
    raise ValueError('m must be 1, 2 or 3')


def predicted(n, arrows, d, q, m):
    paths = basis_paths(n, arrows, d)
    edges = [(v[0], v[-1]) for v, s in paths if s and v[0] != v[-1]]
    h = 1 << m
    total = 0
    for colors in product(range(h), repeat=n):
        cut = sum(colors[u] != colors[v] for u, v in edges)
        total += q ** cut
    # Fortuin-Kasteleyn spanning-subgraph identity, computed separately.
    fk = 0
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        def root(a):
            while parent[a] != a:
                a = parent[a]
            return a
        count = 0
        for j, (u, v) in enumerate(edges):
            if (mask >> j) & 1:
                count += 1
                ru, rv = root(u), root(v)
                parent[ru] = rv
        k = len({root(v) for v in range(n)})
        fk += q ** (len(edges) - count) * (1 - q) ** count * h ** k
    assert fk == total, (fk, total)
    return total, len(edges)


def run():
    # Both radical-square-zero and higher-nilpotency path algebras.
    cases = [
        ('single-arrow', 2, [(0, 1)], 2, 2, (1, 2, 3)),
        ('single-arrow-ternary', 2, [(0, 1)], 2, 3, (1, 2)),
        ('single-arrow-GF4', 2, [(0, 1)], 2, 4, (1, 2)),
        ('parallel', 2, [(0, 1), (0, 1)], 2, 2, (1, 2)),
        ('opposite', 2, [(0, 1), (1, 0)], 2, 3, (1, 2)),
        ('loop-ignored', 2, [(0, 0), (0, 1)], 2, 2, (1, 2)),
        ('path-square-zero', 3, [(0, 1), (1, 2)], 2, 2, (1, 2)),
        ('path-cube-zero', 3, [(0, 1), (1, 2)], 3, 2, (1, 2)),
        ('K3-square-zero', 3, [(0, 1), (1, 2), (0, 2)], 2, 2, (1, 2, 3)),
        ('UT3', 3, [(0, 1), (1, 2)], 3, 2, (1, 2, 3)),
        ('UT3-ternary', 3, [(0, 1), (1, 2)], 3, 3, (1, 2)),
        ('UT3-GF4', 3, [(0, 1), (1, 2)], 3, 4, (1, 2)),
        ('UT4', 4, [(0, 1), (1, 2), (2, 3)], 4, 2, (1, 2)),
        ('cycle-truncated', 3, [(0, 1), (1, 2), (2, 0)], 3, 2, (1, 2)),
    ]
    nchecks = 0
    for name, n, arr, d, q, ms in cases:
        for m in ms:
            expected, medges = predicted(n, arr, d, q, m)
            actual, dimension, idems = direct_count(n, arr, d, q, m)
            assert actual == expected, (name, q, m, actual, expected)
            print('PASS', name, 'q=', q, 'm=', m, 'dimA=', dimension,
                  'nonloop_paths=', medges, 'idempotents=', idems,
                  'commuting_tuples=', actual)
            nchecks += 1
    print('PEIRCE_POTTS_COMMUTING_IDEMPOTENTS_OK', nchecks)

if __name__ == '__main__':
    run()
