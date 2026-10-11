"""Exact rational tests of finite-dimensional contractive orbit constructions.

The theorem for arbitrary dimensions and scalar fields has an analytic proof;
this script checks selected real rational instances, not the universal claim.
"""
from fractions import Fraction as Q
from itertools import product


def rank(a):
    b = [[Q(z) for z in row] for row in a]
    if not b:
        return 0
    m, n = len(b), len(b[0])
    k = 0
    for j in range(n):
        pivot = next((i for i in range(k, m) if b[i][j]), None)
        if pivot is None:
            continue
        b[k], b[pivot] = b[pivot], b[k]
        p = b[k][j]
        b[k] = [v/p for v in b[k]]
        for i in range(m):
            if i != k:
                v = b[i][j]
                b[i] = [b[i][h]-v*b[k][h] for h in range(n)]
        k += 1
        if k == m:
            break
    return k


def l1_matrix(a, b):
    n = len(a)
    s, t = sum(v != 0 for v in a), sum(v != 0 for v in b)
    assert 1 <= s <= t <= n and sum(a) == sum(b) == 1
    assert all(v > 0 for v in a[:s]) and all(v == 0 for v in a[s:])
    assert all(v > 0 for v in b[:t]) and all(v == 0 for v in b[t:])
    cols = []
    hs = [[Q(0)]*n for _ in range(s)]
    for i in range(s-1):
        hs[i][i] = Q(1)
        hs[i][t-1] = Q(-1)
    for i in range(s-1):
        for j in range(n):
            hs[s-1][j] -= a[i]*hs[i][j]/a[s-1]
    eps = min(b[:t]) * min(a[:s]) / Q(20*n)
    for i in range(s):
        cols.append([b[j]+eps*hs[i][j] for j in range(n)])
    for j in range(n):
        e = [Q(k==j) for k in range(n)]
        if rank([[c[k] for c in cols+[e]] for k in range(n)]) > len(cols):
            cols.append(e)
        if len(cols) == n:
            break
    assert len(cols) == n
    mat = [[cols[j][i] for j in range(n)] for i in range(n)]
    assert rank(mat)==n
    assert all(sum(abs(mat[i][j]) for i in range(n)) == 1 for j in range(n))
    assert all(sum(mat[i][j]*a[j] for j in range(n)) == b[i] for i in range(n))
    return mat


def linfty_matrix(x,y):
    n = len(x)
    t = sum(abs(z) == 1 for z in y)
    r = sum(abs(z) == 1 for z in x)
    assert 1 <= t <= r <= n
    assert all(abs(v)==1 for v in x[:r]) and all(abs(v)<1 for v in x[r:])
    assert all(abs(v)==1 for v in y[:t]) and all(abs(v)<1 for v in y[t:])
    m = [[Q(0)]*n for _ in range(n)]
    for i in range(t):
        m[i][i] = y[i] / x[i]
    eps = min(Q(1)-abs(v) for v in y[t:]) / Q(4) if t<n else Q(1)
    for i in range(t,n):
        m[i][0] = (y[i]-eps*x[i])/x[0]
        m[i][i] = eps
    assert rank(m)==n
    assert all(sum(abs(v) for v in row)<=1 for row in m)
    assert all(sum(m[i][j]*x[j] for j in range(n))==y[i] for i in range(n))
    return m


def main():
    total1=totalinf=0
    for n in range(2,9):
        for s in range(1,n+1):
            for t in range(s,n+1):
                a=[Q(2*i+1, s*s) for i in range(s)]+[Q(0)]*(n-s)
                b=[Q(2*j+1, t*t) for j in range(t)]+[Q(0)]*(n-t)
                l1_matrix(a,b)
                total1+=1
        for r in range(1,n+1):
            for t in range(1,r+1):
                x=[Q(1)]*r+[Q(2*j+1,2*n+2) for j in range(n-r)]
                y=[Q(1)]*t+[Q(-(2*j+1),2*n+2) for j in range(n-t)]
                linfty_matrix(x,y)
                totalinf+=1
    print(f'PASS l1_instances={total1} linfty_instances={totalinf} dimensions=2..8 exact_rational=True analytic_proof_required=True')

if __name__=='__main__':
    main()
