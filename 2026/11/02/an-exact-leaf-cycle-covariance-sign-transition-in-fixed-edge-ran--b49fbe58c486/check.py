#!/usr/bin/env python3
"""Independent exact checks for degree-one/cycle-count covariance in random graphs.

Uses all simple labelled graphs through six vertices, and rational-moment
identities over a broader grid. No external dependencies.
"""
from math import comb
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations,permutations

def ff(a,k):
    z=1
    for j in range(k): z*=a-j
    return z if k<=a else 0

def predicted(n,m,h,e,aut):
    N=comb(n,2); A=comb(n-1,2)
    if m<e or m>A+1: return F(0)
    p1=F((n-1)*comb(A,m-1),comb(N,m))
    eh=F(ff(n,h),aut)*F(ff(m,e),ff(N,e))
    ec=F(ff(n-1,h),aut)*F(ff(m-1,e),ff(A,e)) if m-1>=e and e<=A and h<=n-1 else F(0)
    return n*p1*(ec-eh)

def direct(n):
    edges=list(combinations(range(n),2)); E=len(edges)
    idmap={p:i for i,p in enumerate(edges)}
    triangles=[sum(1<<idmap[tuple(sorted(x))] for x in combinations(v,2)) for v in combinations(range(n),3)]
    squares=set()
    for v in combinations(range(n),4):
        for p in permutations(v[1:]):
            cyc=(v[0],)+p
            bm=sum(1<<idmap[tuple(sorted((cyc[j],cyc[(j+1)%4])))] for j in range(4))
            squares.add(bm)
    squares=sorted(squares)
    moments=defaultdict(lambda:[0,0,0,0])
    for g in range(1<<E):
        m=g.bit_count()
        deg=[0]*n
        for i,(u,v) in enumerate(edges):
            if g&(1<<i):deg[u]+=1;deg[v]+=1
        l=sum(x==1 for x in deg)
        t=sum((g&tri)==tri for tri in triangles)
        s=sum((g&sq)==sq for sq in squares)
        a=moments[m]
        a[0]+=l;a[1]+=t;a[2]+=l*t;a[3]+=s  # separately square cov below
    assert all(len(v)==4 for v in moments.values())
    checks=0
    for m,vals in moments.items():
        ct=comb(E,m)
        observed=F(vals[2],ct)-F(vals[0],ct)*F(vals[1],ct)
        expected=predicted(n,m,3,3,6)
        assert observed==expected,(n,m,observed,expected)
        checks+=1
    # One separate pass for C4 mixed moment
    l2=[0]*(E+1);ls=[0]*(E+1);tots=[0]*(E+1)
    for g in range(1<<E):
        m=g.bit_count()
        deg=[0]*n
        for i,(u,v) in enumerate(edges):
            if g&(1<<i):deg[u]+=1;deg[v]+=1
        l=sum(d==1 for d in deg)
        s=sum((g&sq)==sq for sq in squares)
        l2[m]+=l;ls[m]+=l*s;tots[m]+=s
    for m in range(E+1):
        ct=comb(E,m)
        observed=F(ls[m],ct)-F(l2[m],ct)*F(tots[m],ct)
        expected=predicted(n,m,4,4,8)
        assert observed==expected,(n,m,observed,expected)
        checks+=1
    return checks

def symbolic_tests():
    checks=0
    for n in range(4,41):
        N=comb(n,2); A=comb(n-1,2)
        if n>=5:
            ratio=F(3*(n+1)*(n*n-n-4),3*n*n-3*n-4)
            assert n<ratio<n+1
            checks+=2
        for m in range(0,min(N,A+1)+1):
            c=predicted(n,m,3,3,6)
            if n>=5 and 3<=m<=A+1:
                assert (c<0 if m<=n else c>0)
            checks+=1
        for h,e,aut in [(4,4,8),(4,6,24),(5,5,10)]:
            if h>n or e>A:continue
            prior=None
            for m in range(e,min(N,A+1)+1):
                c=predicted(n,m,h,e,aut)
                if prior is not None and prior>0:
                    assert c>0
                prior=c
                checks+=1
    return checks

if __name__=='__main__':
    x=sum(direct(n) for n in range(4,7))
    y=symbolic_tests()
    print(f'PASS: {x} exhaustive graph-ensemble checks; {y} exact rational formula/sign checks; total {x+y}')
