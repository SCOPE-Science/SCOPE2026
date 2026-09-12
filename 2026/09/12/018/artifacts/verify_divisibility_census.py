"""Exhaustive Seifert-divisibility census (stdlib only) supporting the lane-1122 disproof.

Checks div_T(Phi x) == div_S(x) for EVERY nonzero x in [-2,2]^6 (15,624 vectors),
where Phi is the coordinate inclusion for sigma=(0,1,2,3,4,6) and LS, LT are the
canonical unimodular Seifert data (L+L^T=-G) from verify_target.py.
Prints CENSUS_OK on success.
"""
from itertools import product
from math import gcd
from functools import reduce


def zeros(r, c):
    return [[0] * c for _ in range(r)]


def cartan(n, edges):
    G = zeros(n, n)
    for i in range(n):
        G[i][i] = 2
    for (u, v) in edges:
        G[u][v] = G[v][u] = -1
    return G


def seifert(G):
    n = len(G)
    L = zeros(n, n)
    for i in range(n):
        for j in range(n):
            if i == j:
                L[i][j] = -1
            elif j > i:
                L[i][j] = -G[i][j]
    return L


def div_of(L, x):
    n = len(L)
    row = [sum(x[i] * L[i][j] for i in range(n)) for j in range(n)]
    if all(c == 0 for c in row):
        return 0
    return reduce(gcd, [abs(c) for c in row if c != 0])


def content(x):
    nz = [abs(c) for c in x if c != 0]
    return 0 if not nz else reduce(gcd, nz)


G6 = cartan(6, [(0, 1), (1, 2), (2, 3), (3, 4), (2, 5)])
G7 = cartan(7, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (2, 6)])
LS, LT = seifert(G6), seifert(G7)
sigma = [0, 1, 2, 3, 4, 6]


def emb(x):
    y = [0] * 7
    for j, s in enumerate(sigma):
        y[s] = x[j]
    return y


n_prim = n_imp = 0
checked = 0
for x in product(range(-2, 3), repeat=6):
    if all(c == 0 for c in x):
        continue
    x = list(x)
    checked += 1
    ds, dt = div_of(LS, x), div_of(LT, emb(x))
    assert ds == dt, (x, ds, dt)
    if content(x) == 1:
        n_prim += 1
        assert ds == 1, x  # unimodularity forces divisibility 1 on primitives
    else:
        n_imp += 1
print("checked=%d primitive=%d imprimitive=%d, all divisibility equalities hold"
      % (checked, n_prim, n_imp))
print("CENSUS_OK")
