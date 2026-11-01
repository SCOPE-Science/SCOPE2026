#!/usr/bin/env python3
"""Exhaustive small-field checks for the rank-one square-zero commuting graph.
Works with Python 3 standard library; no external data.
"""
from itertools import product
from collections import Counter, deque
from math import prod


def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def mul(a,b,q):
    if q!=4: return (a*b)%q
    a0,a1=a&1,(a>>1)&1
    b0,b1=b&1,(b>>1)&1
    return ((a0&b0)^(a1&b1)) | (((a0&b1)^(a1&b0)^(a1&b1))<<1)

def dot(a,b,q):
    s=0
    for x,y in zip(a,b): s=add(s,mul(x,y,q),q)
    return s

def qbin(n,k,q):
    if k<0 or k>n:return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def tuple_count(n,q,k):
    if k==0:return 1
    result=0
    for r in range(1,n):
        inner=0
        for j in range(r+1):
            s=r-j
            mob=(-1)**s*q**(s*(s-1)//2)
            a=(q**j-1)*(q**(n-r)-1)//(q-1)
            inner+=qbin(r,j,q)*mob*a**k
        result+=qbin(n,r,q)*inner
    return result

def list_matrices(n,q):
    vectors=list(product(range(q),repeat=n))
    matrices=set()
    for u in vectors[1:]:
        for phi in vectors[1:]:
            if dot(u,phi,q):continue
            matrices.add(tuple(mul(a,b,q) for a in u for b in phi))
    return sorted(matrices)

def matrix_product(a,b,n,q):
    out=[]
    for i in range(n):
        for j in range(n):
            out.append(dot(a[i*n:(i+1)*n],b[j::n],q))
    return tuple(out)

def maximal_clique_sizes(N):
    # Tomita pivoted Bron-Kerbosch; N excludes each vertex itself.
    found=Counter()
    def rec(R,P,X):
        if not P and not X:
            found[len(R)]+=1
            return
        pivot=max(P|X,key=lambda v:len(P&N[v]),default=None)
        for v in sorted(P-(N[pivot] if pivot is not None else set())):
            rec(R|{v},P&N[v],X&N[v])
            P.remove(v);X.add(v)
    rec(set(),set(range(len(N))),set())
    return found

def diameter_and_components(N):
    d=len(N);remaining=set(range(d));components=[];diameters=[]
    while remaining:
        root=min(remaining);seen={root};queue=deque([root]);remaining.remove(root)
        while queue:
            a=queue.popleft()
            for b in N[a]-seen:
                seen.add(b);remaining.remove(b);queue.append(b)
        components.append(len(seen))
        diam=0
        for a in seen:
            dist={a:0};queue=deque([a])
            while queue:
                u=queue.popleft()
                for v in N[u]-dist.keys():
                    dist[v]=dist[u]+1;queue.append(v)
            assert len(dist)==len(seen)
            diam=max(diam,max(dist.values()))
        diameters.append(diam)
    return sorted(components),sorted(diameters)

def check(n,q):
    mats=list_matrices(n,q);d=len(mats)
    expected_vertices=(q**n-1)*(q**(n-1)-1)//(q-1)
    assert d==expected_vertices,(n,q,d,expected_vertices)
    N=[set() for _ in mats]
    for i,a in enumerate(mats):
        assert matrix_product(a,a,n,q)==(0,)*(n*n)
        for j in range(i+1,d):
            b=mats[j]
            ab=matrix_product(a,b,n,q);ba=matrix_product(b,a,n,q)
            if ab==ba:
                assert ab==(0,)*(n*n)
                N[i].add(j);N[j].add(i)
    expected_degree=(q**(n-1)-1)+(qbin(n-1,1,q)-1)*(q**(n-2)-1)-1
    assert {len(x) for x in N}=={expected_degree}
    inclusive=[a|{i} for i,a in enumerate(N)]
    direct=[1,d,sum(map(len,inclusive)),sum(len(inclusive[i]&inclusive[j]) for i,ng in enumerate(inclusive) for j in ng)]
    expected=[tuple_count(n,q,k) for k in range(4)]
    assert direct==expected,(n,q,direct,expected)
    maximal=maximal_clique_sizes(N)
    expected_max=Counter()
    for r in range(1,n):
        size=(q**r-1)*(q**(n-r)-1)//(q-1)
        expected_max[size]+=qbin(n,r,q)
    assert maximal==expected_max,(n,q,maximal,expected_max)
    comps,diams=diameter_and_components(N)
    if n==2:
        assert comps==[q-1]*(q+1)
        assert diams==([0]*(q+1) if q==2 else [1]*(q+1))
    elif n==3:assert comps==[d] and diams==[3]
    else:assert comps==[d] and diams==[2]
    print('OK',f'n={n}',f'q={q}',f'vertices={d}',f'degree={expected_degree}',f'T0..3={direct}',f'maximal_cliques={dict(sorted(maximal.items()))}',f'components={comps}',f'diameters={diams}')

if __name__=='__main__':
    for n,q in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)]:check(n,q)
    print('VERIFY_OK')
