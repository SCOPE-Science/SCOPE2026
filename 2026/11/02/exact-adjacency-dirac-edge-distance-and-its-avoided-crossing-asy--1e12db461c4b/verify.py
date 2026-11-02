#!/usr/bin/env python3
"""Exact rational finite-case checks for the edge Connes distance reduction.

This script tests, but does not replace, the all-dimension representation
calculation and asymptotic argument written in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def build(n, t):
    vertices = tuple(combinations(range(n), 2))
    idx = {v: j for j, v in enumerate(vertices)}
    f = {}
    for v in vertices:
        if v == (0, 1): f[v] = F(1)
        elif v == (0, 2): f[v] = F(-1)
        elif 1 in v and 0 not in v and 2 not in v: f[v] = t
        elif 2 in v and 0 not in v and 1 not in v: f[v] = -t
        else: f[v] = F(0)
    size = len(vertices)
    k = [[F(0) for _ in range(size)] for _ in range(size)]
    for i, a in enumerate(vertices):
        for j in range(i+1, size):
            b=vertices[j]
            if len(set(a) & set(b)) == 1:
                k[i][j] = f[b]-f[a]
                k[j][i] = -k[i][j]
    return vertices, idx, k


def verify(n,t):
    m=n-3
    V, idx, k=build(n,t)
    # Unnormalized odd vectors v_0=e_{01}-e_{02}, v_i=e_{1i}-e_{2i}.
    pairs=[((0,1),(0,2))]+[((1,j),(2,j)) for j in range(3,n)]
    cols=[]
    for vp,vn in pairs:
        i=idx[vp];j=idx[vn]
        cols.append([row[i]-row[j] for row in k])
    G=[[sum(x*y for x,y in zip(p,q))/2 for q in cols] for p in cols]
    A=6+3*m-2*m*t+m*t*t
    B=-2+8*t-2*t*t
    diag=1-2*t+(2*m+7)*t*t
    off=1-2*t+5*t*t
    for i in range(m+1):
        for j in range(m+1):
            expected=A if i==0 and j==0 else (B if min(i,j)==0 else (diag if i==j else off))
            assert G[i][j] == expected, (n,t,i,j,G[i][j],expected)
    # Eigenvalues on odd space: one (m-1)-fold scalar and one 2x2 block.
    c=m-2*m*t+(7*m+2)*t*t
    assert diag+(m-1)*off == c
    assert diag-off == (2*m+2)*t*t
    assert A>0
    assert c-(2*m+2)*t*t == m*(1-2*t+5*t*t)>0
    assert A*c-m*B*B >=0  # the 2-by-2 block is positive semidefinite.
    # K swaps +/- parity: the odd Gram therefore captures all its nonzero singular values.
    # Check swap anticommutation, symmetry and skew-adjointness directly.
    sw=[]
    for v in V:
        swapped=tuple(sorted((2 if a==1 else 1 if a==2 else a) for a in v))
        sw.append(idx[swapped])
    for i in range(len(V)):
        for j in range(len(V)):
            assert k[i][j]==-k[j][i]
            assert k[sw[i]][sw[j]]==-k[i][j]
    return (m+1)**2+2*len(V)**2+4


def main():
    tests=(F(-2),F(-1),F(0),F(1,4),F(1,3),F(1,2),F(2,3),F(1),F(2))
    count=0
    for n in range(5,11):
        for t in tests:
            count+=verify(n,t)
    print('CHECK_OK: exact rational Gram blocks, parity, and norm domination; '
          f'{count} assertions across 54 graph/parameter cases')


if __name__=='__main__':main()
