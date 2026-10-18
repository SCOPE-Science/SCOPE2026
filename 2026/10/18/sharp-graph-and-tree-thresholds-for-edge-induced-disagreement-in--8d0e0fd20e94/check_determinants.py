#!/usr/bin/env python3
"""Independent exact Cramer determinant verifier for small leader-follower networks.
Does not use the elimination solver from verify_harmonic.py.
"""
from fractions import Fraction
from itertools import combinations, permutations, product


def determinant(A):
    n=len(A)
    if n==0:return 1
    out=0
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        prod=1
        for i in range(n):prod*=A[i][p[i]]
        out+=(-1 if inv%2 else 1)*prod
    return out


def opinion(n,edges):
    # Boundary vertices are 0, 1 with potentials 0, 1.
    k=n-2
    A=[[0]*k for _ in range(k)]
    b=[0]*k
    for u,v in edges:
        for x,y in ((u,v),(v,u)):
            if x<2: continue
            a=x-2
            A[a][a]+=1
            if y==1:b[a]+=1
            if y>=2:A[a][y-2]-=1
    d=determinant(A)
    assert d>0
    values=[Fraction(0),Fraction(1)]
    for col in range(k):
        B=[list(row) for row in A]
        for i in range(k):B[i][col]=b[i]
        values.append(Fraction(determinant(B),d))
    return values


def p(v):
    m=sum(v)/len(v)
    return sum((x-m)**2 for x in v)


def conn(n,E):
    reach={0}
    while 1:
        new=reach.copy()
        for u,v in E:
            if u in reach:new.add(v)
            if v in reach:new.add(u)
        if new==reach:return len(reach)==n
        reach=new


def trees(n,seq):
    deg=[1]*n
    for v in seq:deg[v]+=1
    E=[]
    for v in seq:
        u=next(i for i in range(n) if deg[i]==1)
        E.append(tuple(sorted((u,v))))
        deg[u]-=1;deg[v]-=1
    u,v=[i for i in range(n) if deg[i]==1]
    E.append(tuple(sorted((u,v))))
    return E


def test_case(n,E):
    initial=p(opinion(n,E)); EE=set(E); c=0; dec=0
    for e in combinations(range(2,n),2):
        if e in EE:continue
        delta=p(opinion(n,E+[e]))-initial
        assert delta<=0,(n,E,e,delta)
        c+=1
        if delta<0:dec+=1
    return c,dec


def run():
    for n in range(2,6):
        pairs=list(combinations(range(n),2));seen=0;count=0;decreases=0
        for mask in range(1<<len(pairs)):
            E=[e for i,e in enumerate(pairs) if mask>>i&1]
            if not conn(n,E):continue
            seen+=1
            c,d=test_case(n,E);count+=c;decreases+=d
        print('determinant graph',n,seen,count,decreases)
    for n in range(2,7):
        seen=0;count=0;decreases=0
        for code in product(range(n),repeat=n-2):
            E=trees(n,code);seen+=1
            c,d=test_case(n,E);count+=c;decreases+=d
        print('determinant tree',n,seen,count,decreases)
    print('INDEPENDENT DETERMINANT CHECK PASSED')

if __name__=='__main__':run()
