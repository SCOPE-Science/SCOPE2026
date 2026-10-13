#!/usr/bin/env python3
"""Exact arithmetic verification of triangle/open-triad covariance identities.
Run: python3 verify.py. Uses only the Python standard library.
This verifies finite cases, not the universal analytic proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def falling(x, k):
    v = 1
    for j in range(k):
        v *= x-j
    return v


def covariance_formula(n, m):
    N=comb(n,2)
    if n < 4:
        raise ValueError('n must be >= 4')
    t=comb(n,3)
    q=lambda k: Q(falling(m,k), falling(N,k))
    es=3*t*q(2)
    et=t*q(3)
    ets=t*(3*q(3)+6*(n-3)*q(4)+(3*t-3-6*(n-3))*q(5))
    ett=t*(q(3)+3*(n-3)*q(5)+(t-1-3*(n-3))*q(6))
    return ets-3*ett-et*es+3*et*et


def covariance_factored(n,m):
    N=comb(n,2)
    t=comb(n,3)
    q3=Q(falling(m,3), falling(N,3))
    return Q(-6*t*q3*(N-m)*(N-m-1)*((n*n-3*n-8)*m+(n-1)*(n*n-n-4)),
             (n+1)*(n+2)*(N-5)*(N-4)*(N-2))


def covariance_binomial(n,p):
    t=comb(n,3)
    return 3*t*p**4*(1-p)*(2*(n-3)-(3*n-8)*p)


def enumerate_graph_moments(n):
    edges=list(combinations(range(n),2))
    triples=list(combinations(range(n),3))
    emap={e:i for i,e in enumerate(edges)}
    tests=[]
    for i,j,k in triples:
        tests.append((sum(1<<emap[e] for e in ((i,j),(i,k),(j,k))),
                      [(1<<emap[(i,j)]),(1<<emap[(i,k)]),(1<<emap[(j,k)])]))
    # For each m, accumulate integer sums of T,W,TW. No probability formulas used.
    acc=[[0,0,0,0] for _ in range(len(edges)+1)]
    for mask in range(1<<len(edges)):
        t=w=0
        for full,es in tests:
            bits=(mask & full).bit_count()
            t += bits==3
            w += bits==2
        z=acc[mask.bit_count()]
        z[0]+=1;z[1]+=t;z[2]+=w;z[3]+=t*w
    return acc


def run():
    tests=0
    for n in range(4,37):
        N=comb(n,2)
        for m in range(N+1):
            a=covariance_formula(n,m)
            b=covariance_factored(n,m)
            assert a==b, (n,m,a,b)
            assert (a<0)==(3<=m<=N-2), (n,m,a)
            assert (a==0)==(m<3 or m>N-2), (n,m,a)
            tests+=1
    for n in (4,5,6):
        by_m=enumerate_graph_moments(n)
        for m,(num,st,sw,stw) in enumerate(by_m):
            assert num==comb(comb(n,2),m)
            direct=Q(stw,num)-Q(st*sw,num*num)
            assert direct==covariance_formula(n,m), (n,m,direct,covariance_formula(n,m))
            tests+=1
        for p in (Q(1,5),Q(2,5),Q(3,5),Q(4,5)):
            N=comb(n,2)
            et=ew=etw=Q(0)
            for m,(num,st,sw,stw) in enumerate(by_m):
                weight=p**m*(1-p)**(N-m)
                et+=st*weight
                ew+=sw*weight
                etw+=stw*weight
            direct=etw-et*ew
            assert direct==covariance_binomial(n,p), (n,p,direct,covariance_binomial(n,p))
            tests+=1
    print('EXACT_CHECK_OK',tests,'formula/sign/binomial cases; full G(n,m) enumeration through n=6')

if __name__=='__main__':
    run()
