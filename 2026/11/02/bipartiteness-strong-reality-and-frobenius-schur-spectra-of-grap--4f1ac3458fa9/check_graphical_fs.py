#!/usr/bin/env python3
"""Exhaustive small-graph checks of graphical 2-group Frobenius--Schur formulas."""
from itertools import combinations, product


def mul(a, b, q):
    if q == 2:
        return a & b
    assert q == 4
    out = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & (b >> j) & 1:
                out ^= 1 << (i + j)
    if out & 8:
        out ^= 0b1110
    if out & 4:
        out ^= 0b111
    return out


def trace(a, q):
    return a if q == 2 else (a ^ mul(a, a, q))


def rank(mat, q):
    a = [row[:] for row in mat]
    n = len(a)
    j = 0
    for col in range(n):
        pivot = next((i for i in range(j, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[j], a[pivot] = a[pivot], a[j]
        inv = next(k for k in range(1, q) if mul(a[j][col], k, q) == 1)
        a[j] = [mul(c, inv, q) for c in a[j]]
        for i in range(n):
            if i != j and a[i][col]:
                f = a[i][col]
                a[i] = [u ^ mul(f, v, q) for u, v in zip(a[i], a[j])]
        j += 1
    return j


def bipartite(n, edges):
    return any(all((mask >> i & 1) != (mask >> j & 1) for i,j in edges) for mask in range(1 << n))


def test_graph(n, edges, q):
    by_sign = {-1:0, 0:0, 1:0}
    total_fs_degree = 0
    zero_square_vertices = 0
    for x in product(range(q), repeat=n):
        if all(mul(x[i], x[j], q) == 0 for i,j in edges):
            zero_square_vertices += 1
    for t in product(range(q), repeat=len(edges)):
        mat = [[0] * n for _ in range(n)]
        for (i,j),v in zip(edges,t):
            mat[i][j] = mat[j][i] = v
        r = rank(mat,q)
        assert r % 2 == 0
        s = r//2
        gauss = 0
        for x in product(range(q),repeat=n):
            Q = 0
            for (i,j),v in zip(edges,t):
                Q ^= mul(v,mul(x[i], x[j],q),q)
            gauss += (-1 if trace(Q,q) else 1)
        assert gauss * q**s % q**n == 0
        fs = gauss * q**s // q**n
        assert fs in {-1,0,1}
        by_sign[fs] += q**(n-r)
        total_fs_degree += q**(n-r) * q**s * fs
    assert total_fs_degree == (q**len(edges))*zero_square_vertices
    if bipartite(n,edges):
        assert by_sign[0] == by_sign[-1] == 0
    else:
        assert by_sign[0] > 0
    return by_sign


def main():
    checks = 0
    nonbip = 0
    negative = 0
    for n in range(1,5):
        poss = list(combinations(range(n),2))
        for bits in range(1<<len(poss)):
            edges = [e for j,e in enumerate(poss) if bits>>j&1]
            signs=test_graph(n,edges,2)
            checks += 1
            nonbip += not bipartite(n,edges)
            negative += signs[-1] > 0
    assert checks == 1+2+8+64
    assert test_graph(4,list(combinations(range(4),2)),2)[-1] > 0
    q4_checks = 0
    for n,edges in [(3,[(0,1),(1,2),(0,2)]),(4,[(0,1),(1,2),(2,3),(3,0)]),(4,list(combinations(range(4),2)))]:
        test_graph(n,edges,4)
        q4_checks += 1
    print('GRAPHICAL_FS_INDICATORS_OK',checks,q4_checks,'nonbipartite',nonbip,'negative',negative)

if __name__ == '__main__':
    main()
