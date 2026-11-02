"""Exact integer-matrix checks for two-particle moves on friendship graphs.

Run: python verify_exact.py
Requires sympy.
"""
from itertools import combinations
from math import comb
from collections import Counter
from sympy import Matrix, symbols, prod


def make_matrix(m):
    base = [(0, 2*i+1) for i in range(m)] + [(0, 2*i+2) for i in range(m)] + [(2*i+1, 2*i+2) for i in range(m)]
    assert len(base) == 3*m
    vertices = list(combinations(range(2*m+1), 2))
    idx = {p: k for k, p in enumerate(vertices)}
    N = len(vertices)
    L = Matrix.zeros(N)
    E = 0
    for j, (a,b) in enumerate(vertices):
        for u,v in base:
            if (a == u and b != v) or (a == v and b != u):
                new = tuple(sorted((v if a == u else u, b)))
            elif (b == u and a != v) or (b == v and a != u):
                new = tuple(sorted((a, v if b == u else u)))
            else:
                continue
            k = idx[new]
            assert j != k
            L[j,k] -= 1
            L[j,j] += 1
            E += 1
    assert L == L.T
    assert L*Matrix.ones(N,1) == Matrix.zeros(N,1)
    assert E % 2 == 0
    return L, E//2


def predicted(m):
    q=comb(m,2)
    out=Counter()
    for value,number in [(0,1),(1,m-1),(2,q),(3,m),(4,m*(m-2)),
                         (6,q),(2*m,m-1),(2*m+1,1),(2*m+2,m)]:
        out[value] += number
    return {e:k for e,k in out.items() if k}

x=symbols('x')
for m in range(2, 9):
    L,E = make_matrix(m)
    assert L.rows==m*(2*m+1)
    assert E==3*m*(2*m-1)
    spec=predicted(m)
    assert sum(spec.values()) == L.rows
    assert sum(e*k for e,k in spec.items())==2*E
    poly=L.charpoly(x).as_expr()
    target=prod((x-e)**k for e,k in spec.items())
    assert poly.expand()==target.expand(),m
    if m <= 4:
        tau=int(L[:-1,:-1].det(method='domain-ge'))
        wanted=2**(3*m*m-3*m-1)*3**(m+comb(m,2))*m**(m-2)*(m+1)**m
        assert tau == wanted, (m,tau,wanted)
    print('EXACT_OK',m,L.rows,E,len(spec),flush=True)
print('EXACT_ALL_PASS')
