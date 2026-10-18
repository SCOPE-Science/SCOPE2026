"""Exact rational corroboration of cubic spherical-harmonic sampling on simplex edge midpoints.

Run with Python 3 standard library: python check_cubic_simplex.py
The general proof is symbolic; these finite exact tests are independent checks, not a proof for all orders.
"""
from fractions import Fraction as F
from itertools import combinations


def gegenbauer3(m, t):
    return ((m + 1) * t**3 - 3 * t) / (m - 2)


def spectrum(m):
    return (
        F(m * (m - 4)**2 * (m + 1), 4 * (m - 2)**3),
        F(m*m * (m-8)**2 * (m-3), 8 * (m-2)**4),
        F(3*m*m * (m-4) * (m+1), 4 * (m-2)**4),
    )


def work(m):
    edges = list(combinations(range(m), 2))
    n = len(edges)
    alpha = F(m-4, 2*(m-2))
    beta = F(-2, m-2)
    qa, qb = gegenbauer3(m, alpha), gegenbauer3(m, beta)
    assert gegenbauer3(m, F(1)) == 1
    K = [[F(1) if e == f else qa if len(set(e)&set(f)) == 1 else qb
          for f in edges] for e in edges]
    e0 = [F(1)] * n
    e1 = [F(int(0 in e)) - F(2, m) for e in edges]
    signs = {(0,1): 1,(2,3):1,(0,2):-1,(1,3):-1}
    e2 = [F(signs.get(e,0)) for e in edges]
    expected = spectrum(m)
    for v, lam in zip((e0,e1,e2),expected):
        assert any(v)
        assert [sum(x*y for x,y in zip(row,v)) for row in K] == [lam*x for x in v], (m,lam)
    assert sum(expected[j]*[1,m-1,m*(m-3)//2][j] for j in range(3)) == n
    assert all(x>0 for x in expected[::2])
    assert (expected[1] == 0) == (m == 8)
    if m == 8:
        assert expected == (F(4,3), F(0), F(4,3))
        for i in range(n):
            for j in range(n):
                assert sum(K[i][k]*K[k][j] for k in range(n)) == F(4,3)*K[i][j]
        # Seven incidence contrasts span the complete 7-dimensional zero eigenspace.
        assert all(sum(K[i][j]*e1[j] for j in range(n)) == 0 for i in range(n))
    return n,expected

if __name__ == '__main__':
    total = 0
    for m in list(range(5,20)) + [24,28,32,40]:
        n, vals = work(m)
        print('m=%d edges=%d eigen=%s'% (m,n,', '.join(map(str, vals))))
        total += 1
    print('PASS',total,'exact-rational cases')
