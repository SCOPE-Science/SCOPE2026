#!/usr/bin/env python3
"""Exact-rational checks for endpoint cut/cycle norms on halved cubes.

Use: python3 check_halved_cube.py
Standard library only. This finite checker supplements, rather than replaces,
the proof for every integer dimension in the accompanying result.
"""
from fractions import Fraction as F
from math import comb


def poly_product(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def a_value(n, r):
    """Exact potential at a vertex with first two bits 00, last bits weight r."""
    N = n - 2
    p = [1]
    for _ in range(r):
        p = poly_product(p, [1, -1])
    for _ in range(N-r):
        p = poly_product(p, [1, 1])
    integral = sum((F(c, j+1) for j, c in enumerate(p)), F(0))
    return integral/F((1<<N)*(N+2))


def gauss_solve(M, b):
    """Independent exact grounded-Laplacian solve via Gauss-Jordan elimination."""
    N = len(b)
    aug = [[F(x) for x in row] + [F(b[i])] for i, row in enumerate(M)]
    for col in range(N):
        p = next(i for i in range(col, N) if aug[i][col])
        aug[col], aug[p] = aug[p], aug[col]
        v = aug[col][col]
        for j in range(col, N+1):
            aug[col][j] /= v
        for i in range(N):
            if i == col: continue
            factor = aug[i][col]
            if factor:
                for j in range(col, N+1):
                    aug[i][j] -= factor*aug[col][j]
    return [aug[i][-1] for i in range(N)]


def one_dimension(n):
    V = [i for i in range(1 << n) if i.bit_count() % 2 == 0]
    vertices = set(V)
    flips = [(1 << i) | (1 << j) for i in range(n) for j in range(i+1, n)]
    E = [(x, x ^ h) for x in V for h in flips if x < (x ^ h)]
    assert len(E) == (1 << (n-2)) * comb(n,2)
    a = {r: a_value(n, r) for r in range(0,n-1,2)}
    assert all(a[r] > 0 for r in a)
    assert all(a[r] > a[r+2] for r in a if r+2 in a)
    def vpot(x):
        head = x & 3
        if head in (1,2):
            return F(0)
        value = a[(x >> 2).bit_count()]
        return value if head == 0 else -value
    f = {v: vpot(v) for v in V}
    for x in V:
        lap = len(flips)*f[x] - sum((f[x^h] for h in flips),F(0))
        assert lap == (1 if x == 0 else (-1 if x == 3 else 0)), (n,x,lap)
    q_norm = sum((abs(f[x]-f[y]) for x,y in E),F(0))
    eff = f[0]-f[3]
    q_expected = F(n+5,4)-F(1,n-1)
    diag_expected = F((1<<(n-1))-1, len(E))
    p_norm = q_norm + 1 - 2*eff
    p_expected = q_expected + 1 - 2*diag_expected
    assert q_norm == q_expected and eff == diag_expected and p_norm == p_expected
    if n <= 6:
        kept = V[:-1]
        M = [[len(flips)*(x==y)-int((x^y).bit_count()==2) for y in kept]
             for x in kept]
        b = [(1 if x==0 else (-1 if x==3 else 0)) for x in kept]
        g = dict(zip(kept,gauss_solve(M,b)))
        g[V[-1]] = F(0)
        # Grounding changes only the additive constant.
        assert all(g[x]-g[0] == f[x]-f[0] for x in V)
        independent = sum((abs(g[x]-g[y]) for x,y in E), F(0))
        assert independent == q_expected
    return len(V),len(E)


def main():
    edge_count = 0
    for n in range(3,12):
        _, e = one_dimension(n)
        edge_count += e
    print('HALVED_CUBE_ENDPOINT_EXACT_OK dimensions=9'
          ' grounded_dimensions=4 full_graph_edges=' + str(edge_count))

if __name__ == '__main__':
    main()
