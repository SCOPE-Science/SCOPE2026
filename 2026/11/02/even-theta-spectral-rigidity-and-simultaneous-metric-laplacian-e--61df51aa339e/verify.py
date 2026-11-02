#!/usr/bin/env python3
"""Exact arithmetic and distance checks for even-branch theta spectra.
Requires Python 3.10+ and SymPy (tested with SymPy 1.13+).
Run: python verify.py
"""
from collections import deque
from itertools import combinations
import sympy as sp


def theta(r):
    # 0=u, 1=v, 2=a, 3=b, 4..r+2=w_1..w_(r-1).
    n = r + 3
    edges = [(0, 2), (2, 1), (0, 3), (3, 1)]
    path = [0] + list(range(4, n)) + [1]
    edges += list(zip(path, path[1:]))
    assert len(set(map(frozenset, edges))) == r + 4
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def laplacian(adj):
    n = len(adj)
    return sp.Matrix(n, n, lambda i, j: len(adj[i]) if i == j else (-1 if j in adj[i] else 0))


def distance_rows(adj):
    ds = []
    for src in range(len(adj)):
        d = [-1] * len(adj)
        d[src] = 0
        q = deque([src])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1
                    q.append(v)
        assert -1 not in d
        ds.append(d)
    return ds


def resolving(ds, landmarks):
    return len({tuple(ds[a][v] for a in landmarks) for v in range(len(ds))}) == len(ds)


def ppolys(s, t):
    p = [sp.Integer(1), t]
    while len(p) <= s:
        p.append(sp.expand(t*p[-1] - p[-2]))
    return p


def check():
    z, t = sp.symbols('z t')
    for r in range(2, 25, 2):
        s = r // 2
        adj = theta(r)
        ds = distance_rows(adj)
        expect_beta = 3 if r in (2, 4) else 2
        # One landmark cannot resolve the twins or both terminals.
        assert not any(resolving(ds, (v,)) for v in range(len(adj)))
        if r in (2, 4):
            assert not any(resolving(ds, pair) for pair in combinations(range(len(adj)), 2))
            witness = (0, 2, 3) if r == 2 else (0, 1, 2)
            assert resolving(ds, witness)
        else:
            assert resolving(ds, (2, 4))
        p = ppolys(s, t)
        minus = sp.expand(p[s] + p[s-1])
        plus = sp.expand((t*t + 2*t - 8)*p[s] + (2*t - t*t)*p[s-1])
        assert sp.gcd(minus, plus) == 1
        assert sp.gcd(minus, sp.diff(minus, t)) == 1
        assert sp.gcd(plus, sp.diff(plus, t)) == 1
        assert (plus.subs(t, 0) == 0) == (s % 2 == 1)
        assert minus.subs(t, 0) != 0
        L = laplacian(adj)
        full = sp.Poly(L.charpoly(z).as_expr(), z)
        expected = sp.Poly(((-1)**len(adj))*t*minus*plus, t).as_expr().subs(t, 2-z)
        assert full == sp.Poly(expected, z), (r, 'full spectral factorization')
        multiplicities = [power for _, power in sp.factor_list(full.as_expr())[1]]
        assert max(multiplicities) == (2 if r % 4 == 2 else 1)
        # Every edge crosses parity classes; Q is diagonally similar to L.
        assert all(ds[0][u] % 2 != ds[0][v] % 2 for u in range(len(adj)) for v in adj[u])
        print(f'r={r:2d} vertices={len(adj):2d} metric_dim={expect_beta} max_L=max_Q={max(multiplicities)}')
    print('VERIFY_OK EVEN_THETA r=2,4,...,24 exact_spectral_factorizations, multiplicities, metric_bases')


if __name__ == '__main__':
    check()
