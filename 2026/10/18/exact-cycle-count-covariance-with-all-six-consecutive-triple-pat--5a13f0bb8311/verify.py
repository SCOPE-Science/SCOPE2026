#!/usr/bin/env python3
"""Exact standalone verification of cycle-count/consecutive-triple covariance."""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
import sys

PATTERNS = [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]
LINEAR_NUMERATORS = [lambda n:3*n-2,lambda n:3*n-8,lambda n:3*n-8,lambda n:4-3*n,lambda n:4-3*n,lambda n:10-3*n]


def signature(xs):
    vals=sorted(xs)
    return tuple(vals.index(x)+1 for x in xs)


def cycles(pi):
    n=len(pi)
    visited=[False]*n
    k=0
    for i in range(n):
        if not visited[i]:
            k+=1
            j=i
            while not visited[j]:
                visited[j]=True
                j=pi[j]-1
    return k


def fixed_cycles(rows,vals):
    d=dict(zip(rows,vals))
    c=0
    for start in rows:
        u=start
        seen=[]
        while u in d and u not in seen:
            seen.append(u)
            u=d[u]
        if u==start:
            c+=Q(1,len(seen))
    assert c.denominator==1
    return int(c)


def symbolic_table(n):
    f=[0]*6;b=[0]*6;t=[0]*6
    ids={p:i for i,p in enumerate(PATTERNS)}
    for i in range(1,n-1):
        rows=(i,i+1,i+2)
        for vals in permutations(range(1,n+1),3):
            p=ids[signature(vals)]
            d=dict(zip(rows,vals))
            f[p]+=sum(d[x]==x for x in rows)
            b[p]+=sum(d.get(x)==y and d.get(y)==x for x in rows for y in rows if x<y)
            t[p]+= int(all(d.get(x) in rows for x in rows) and fixed_cycles(rows,vals)==1 and all(d[x]!=x for x in rows))
    return f,b,t


def closed_formula(n):
    f=[n*(n-1)*(n-2)//2,(n-2)*(n*n-2*n-1)//2,(n-2)*(n*n-2*n-1)//2,(n-3)*(n-2)*(n-1)//2,(n-3)*(n-2)*(n-1)//2,(n-2)*(n*n-5*n+8)//2]
    b=[0,(n-2)*(n-1)//2,(n-2)*(n-1)//2,(n-3)*(n-2)//2,(n-3)*(n-2)//2,(n-2)*(n-2)]
    t=[0,0,0,n-2,n-2,0]
    return f,b,t


def verify(nmax=9):
    checks=0
    for n in range(3,nmax+1):
        sums=[0]*6
        ids={p:i for i,p in enumerate(PATTERNS)}
        for pi in permutations(range(1,n+1)):
            c=cycles(pi)
            for i in range(n-2):
                sums[ids[signature(pi[i:i+3])]]+=c
        avgc=sum(Q(1,i) for i in range(1,n+1))
        count=factorial(n)
        for j in range(6):
            cv=Q(sums[j],count)-Q(n-2,6)*avgc
            assert cv==Q(LINEAR_NUMERATORS[j](n),6*n*(n-1)),(n,PATTERNS[j],cv)
            checks+=1
        f,b,t=symbolic_table(n)
        assert (f,b,t)==closed_formula(n),(n,(f,b,t),closed_formula(n))
        checks+=18
    for n in range(10,31):
        # Identity verifying the table polynomials from elementary sums for all n checked;
        # the general proof in RESULT.md uses exact quadratic summation.
        ff,bb,tt=closed_formula(n)
        for j in range(6):
            s=ff[j]+bb[j]+tt[j]
            hc=Q(1,n)+Q(1,n-1)+Q(1,n-2)
            cv=Q(s,n*(n-1)*(n-2))-Q(n-2,6)*hc
            assert cv==Q(LINEAR_NUMERATORS[j](n),6*n*(n-1))
            checks+=1
    print(f'PASS: {checks} exact rational assertions; exhaustive {sum(factorial(n) for n in range(3,nmax+1)):,} permutations (orders 3..{nmax}); independent cycle enumeration plus closed-component counts.')

if __name__=='__main__':
    verify(int(sys.argv[1]) if len(sys.argv)>1 else 9)
