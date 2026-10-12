"""Reproducible exact check of super domination profiles for heterogeneously leaf-extended graphs.
Uses independent direct definition and the proposed neighborhood-boundary formula.
Python 3 standard library only.
"""
from itertools import combinations,product
from math import comb
from collections import Counter
from random import Random


def bits(k):
    while k:
        b=k&-k
        yield b.bit_length()-1
        k-=b


def direct(n,edges,r):
    starts=[];j=n
    for v in range(n): starts.append(list(range(j,j+r[v])));j+=r[v]
    A=[0]*j
    for v,ls in enumerate(starts):
        for u in ls:
            A[v]|=1<<u;A[u]|=1<<v
    for u,v in edges:A[u]|=1<<v;A[v]|=1<<u
    answer=Counter();tested=0
    for S in range(1<<j):
        O=((1<<j)-1)^S
        ok=True
        for u in bits(O):
            if not any((A[v]&O)==(1<<u) for v in bits(S)):
                ok=False;break
        if ok:answer[S.bit_count()]+=1
        tested+=1
    return answer,tested


def formula(n,edges,r):
    A=[0]*n
    for u,v in edges:A[u]|=1<<v; A[v]|=1<<u
    R=sum(r)
    P=Counter()
    for U in range(1<<n):
        nbr=0
        for u in bits(U):nbr|=A[u]
        boundary=(nbr&~U).bit_count()
        free=((1<<n)-1)&~(U|nbr)
        rows={0:1}
        for v in bits(free):
            new={}
            for k,c in rows.items():
                new[k]=new.get(k,0)+c*r[v]
                new[k+1]=new.get(k+1,0)+c
            rows=new
        for k,c in rows.items():P[R+boundary+k]+=c
    return P


def num_components(n,edges):
    nbr=[0]*n
    for u,v in edges:nbr[u]|=1<<v;nbr[v]|=1<<u
    unvisited=(1<<n)-1
    comps=[]
    while unvisited:
        cur=unvisited&-unvisited
        stack=cur;mask=0
        while stack:
            vb=stack&-stack;stack-=vb
            if mask&vb:continue
            v=vb.bit_length()-1
            mask|=vb;unvisited&=~vb
            stack|=nbr[v]&~mask
        comps.append([u for u in bits(mask)])
    return comps

cases=0
subsets=0
for n in range(1,5):
    poss=list(combinations(range(n),2))
    for E in range(1<<len(poss)):
        edges=[e for i,e in enumerate(poss) if E>>i&1]
        for r in product([1,2],repeat=n):
            a,t=direct(n,edges,r)
            b=formula(n,edges,r)
            assert a==b,(n,edges,r,a,b)
            R=sum(r);N=n+R
            target=1
            for C in num_components(n,edges):
                p=1
                for v in C:p*=r[v]
                target*=1+p
            assert a[R]==target,(n,edges,r,a[R],target)
            prohibited=sum(comb(rv,2)+rv for rv in r)+sum(r[u]+r[v] for u,v in edges)
            if N>=2:assert a[N-2]==comb(N,2)-prohibited
            cases+=1;subsets+=t
rng=Random(271828)
for n in (5,6):
    poss=list(combinations(range(n),2))
    for _ in range(40 if n==5 else 12):
        edges=[e for e in poss if rng.randrange(4)==0]
        r=tuple(rng.choice((1,2)) for i in range(n))
        a,t=direct(n,edges,r)
        b=formula(n,edges,r)
        assert a==b,(n,edges,r,a,b)
        R=sum(r);N=n+R
        target=1
        for C in num_components(n,edges):
            p=1
            for v in C:p*=r[v]
            target*=1+p
        assert a[R]==target
        prohibited=sum(comb(rv,2)+rv for rv in r)+sum(r[u]+r[v] for u,v in edges)
        assert a[N-2]==comb(N,2)-prohibited
        cases+=1;subsets+=t
print('VERIFY_OK',{'instances':cases,'direct_subsets':subsets,'random_seed':271828})
for n,edge,r in [(2,[(0,1)],(1,2)),(3,[(0,1),(1,2)],(1,2,1)),(3,[],(1,2,2))]:
    print('EXAMPLE',n,edge,r,dict(sorted(formula(n,edge,r).items())))
