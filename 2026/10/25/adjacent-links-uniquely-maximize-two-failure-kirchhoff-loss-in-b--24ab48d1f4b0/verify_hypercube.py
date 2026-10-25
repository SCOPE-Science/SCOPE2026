#!/usr/bin/env python3
"""Exact rational certificates for two-link effective-resistance interdiction in Boolean cubes."""
from fractions import Fraction as F
from math import comb
from itertools import combinations


def kernel(d, h, order):
    """Fourier-Walsh entry of the order-th inverse power of the Laplacian."""
    assert 0 <= h <= d and order in (1,2)
    return sum((F(sum((-1)**j * comb(h,j) * comb(d-h, s-j)
                       for j in range(max(0,s-d+h), min(h,s)+1)),
                  (1 << d) * (2*s)**order)
               for s in range(1,d+1)), F(0))


def certificate(d):
    N=1<<d
    u=[kernel(d,h,1) for h in range(d+1)]
    v=[kernel(d,h,2) for h in range(d+1)]
    a=[u[h]-u[h+1] for h in range(d)]
    b=[v[h]-v[h+1] for h in range(d)]
    assert all(a[h]>a[h+1]>0 and b[h]>b[h+1]>0 for h in range(d-1))
    R,S=2*a[0],2*b[0]
    z=1-R
    assert z>0
    def delta(x,y):
        assert x>=0 and y>=0 and z*z>x*x
        return 2*N*(z*S+x*y)/(z*z-x*x)
    pair_orbits={}
    for k in range(1,d):pair_orbits['parallel',k]=delta(2*a[k],2*b[k])
    for k in range(d-1):pair_orbits['perpendicular',k]=delta(a[k]-a[k+1],b[k]-b[k+1])
    leader=pair_orbits['perpendicular',0]
    assert all(leader>v for k,v in pair_orbits.items() if k!=('perpendicular',0)),(d,pair_orbits)
    assert delta(2*a[1],2*b[1])==max(v for k,v in pair_orbits.items() if k[0]=='parallel')
    return a,b,pair_orbits


def graph_edges(d):
    return [(x,x^(1<<j)) for x in range(1<<d) for j in range(d) if (x & (1<<j))==0]


def inv(A):
    n=len(A)
    aug=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if aug[i][col])
        aug[col],aug[pivot]=aug[pivot],aug[col]
        den=aug[col][col]
        aug[col]=[x/den for x in aug[col]]
        for i in range(n):
            if i==col: continue
            coeff=aug[i][col]
            if coeff: aug[i]=[a-coeff*b for a,b in zip(aug[i],aug[col])]
    return [row[n:] for row in aug]


def direct_kf(d, removed):
    N=1<<d
    A=[[0]*N for _ in range(N)]
    for u,v in graph_edges(d):
        if (u,v) in removed: continue
        A[u][u]+=1;A[v][v]+=1
        A[u][v]-=1;A[v][u]-=1
    G=inv([row[:N-1] for row in A[:N-1]])
    return N*sum((G[i][i] for i in range(N-1)),F(0))-sum((x for row in G for x in row),F(0))


def test_orbits():
    print('Exact 3..12 dimensional family checks')
    for d in range(3,13):
        a,b,orbits=certificate(d)
        p=orbits['parallel',1]
        t=orbits['perpendicular',0]
        assert t>p
        if d<=8:
            print(f'd={d} worst={t} nearest_parallel={p} gap={t-p} b0_minus_3b1={b[0]-3*b[1]}')
    a,b,_=certificate(8)
    assert b[0]-3*b[1]==F(1007,1204224)
    # Independent exact inverse of grounded Laplacians for a nearby pair and a parallel pair.
    for d in [3,4,5]:
        N=1<<d
        uncut=direct_kf(d,set())
        adj={(0,1),(0,2)}
        parallel={(0,1),(2,3)}
        _,_,orbits=certificate(d)
        assert direct_kf(d,adj)-uncut==orbits['perpendicular',0]
        assert direct_kf(d,parallel)-uncut==orbits['parallel',1]
        print(f'grounded_exact: d={d} baseline_Kf={uncut} adjacent and parallel match')
    # Each pair in Q3/Q4 reduces to one of the two predicted graph automorphism orbits.
    for d in (3,4,5):
        _,_,orbits=certificate(d)
        N=1<<d; es=graph_edges(d)
        count=0
        for (u,v),(x,y) in combinations(es,2):
            i=(u^v).bit_length()-1; j=(x^y).bit_length()-1
            if i==j:
                k=(u^x).bit_count()
                val=orbits['parallel',k]
            else:
                k=((u^x)&~((1<<i)|(1<<j))).bit_count()
                val=orbits['perpendicular',k]
            assert val<=orbits['perpendicular',0]
            count+=1
        print(f'exhaustive pair orbit check: d={d}, {count} pairs')
    print('VERIFY_OK: all d=3..12 rational orbit inequalities; exact small dimension grounded inverses; all edge pairs of Q3,Q4,Q5; dimension-eight positive separation certificate.')

if __name__=='__main__':test_orbits()
