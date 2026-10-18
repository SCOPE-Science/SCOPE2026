#!/usr/bin/env python3
"""Exact combinatorial checks for a Euclidean signed-root Rips stage.

This program checks finite instances. A separately stated geometric argument
proves the assertion for all parameters; the finite tests are not that proof.
"""
from itertools import combinations, product
from collections import defaultdict
from math import comb

def build_roots(n):
    roots = []
    for i in range(n):
        for sign in (-1, 1):
            t = [0]*n; t[i]=sign; roots.append(tuple(t))
    for i,j in combinations(range(n),2):
        for si,sj in product((-1,1),repeat=2):
            t=[0]*n;t[i]=si;t[j]=sj;roots.append(tuple(t))
    return roots

def max_cliques(adjs):
    out=[]
    def rec(R,P,X):
        if not P and not X:
            out.append(frozenset(R));return
        pivot=max(P|X,key=lambda v:len(P&adjs[v])) if P|X else None
        for v in sorted(P-(adjs[pivot] if pivot is not None else set())):
            rec(R|{v},P&adjs[v],X&adjs[v]);P.remove(v);X.add(v)
    rec(set(),set(range(len(adjs))),set())
    return set(out)

def expected_facets(n,idx):
    def v(i,s):
        a=[0]*n;a[i]=s;return tuple(a)
    def add(a,b):return tuple(x+y for x,y in zip(a,b))
    short=[v(i,s) for i in range(n) for s in (-1,1)]
    facets=set()
    for i in range(n):
        for sign in (-1,1):
            s=v(i,sign)
            for other_signs in product((-1,1),repeat=n-1):
                roots=[s]+[add(s,v(j,sj)) for j,sj in zip((j for j in range(n) if j!=i),other_signs)]
                facets.add(frozenset(idx[r] for r in roots))
    for signs in product((-1,1),repeat=n):
        facets.add(frozenset(idx[v(i,s)] for i,s in enumerate(signs)))
    for i,j,k in combinations(range(n),3):
        for signs in product((-1,1),repeat=3):
            a,b,c=(v(i,signs[0]),v(j,signs[1]),v(k,signs[2]))
            facets.add(frozenset(idx[r] for r in (add(a,b),add(a,c),add(b,c))))
    for a,b in combinations(short,2):
        if sum(x*y for x,y in zip(a,b))==0:
            facets.add(frozenset(idx[r] for r in (a,b,add(a,b))))
    return facets

def face_layers(facets):
    faces=defaultdict(set)
    for f in facets:
        ff=sorted(f)
        for k in range(1,len(ff)+1):
            for g in combinations(ff,k):faces[k].add(g)
    return faces

def betti_f2(faces):
    ranks={}
    for k in sorted(faces):
        if k==1:continue
        row={f:i for i,f in enumerate(sorted(faces[k-1]))}
        piv={}
        for f in sorted(faces[k]):
            col=0
            for g in combinations(f,k-1):col ^= 1<<row[g]
            while col:
                highest=col.bit_length()-1
                if highest in piv:col^=piv[highest]
                else:piv[highest]=col;break
        ranks[k-1]=len(piv)
    return [len(faces[k])-ranks.get(k-1,0)-ranks.get(k,0) for k in sorted(faces)]

def verify(n):
    roots=build_roots(n); idx={v:i for i,v in enumerate(roots)}
    assert len(roots)==2*n*n==len(idx)
    adjs=[set() for _ in roots]
    initial=[set() for _ in roots]
    for i,j in combinations(range(len(roots)),2):
        d2=sum((a-b)**2 for a,b in zip(roots[i],roots[j]))
        if d2==1:
            initial[i].add(j);initial[j].add(i)
        if d2<=2:
            adjs[i].add(j);adjs[j].add(i)
    assert sum(map(len,initial))//2==4*n*(n-1)
    assert all(len(initial[i])==2*(n-1) for i in range(2*n))
    assert all(len(initial[i])==2 for i in range(2*n,len(roots)))
    visited={0};queue=[0]
    for v in queue:
        for w in initial[v]-visited:
            visited.add(w);queue.append(w)
    assert len(visited)==len(roots)
    assert sum(map(len,initial))//2-len(roots)+1==2*n*(n-2)+1
    observed=max_cliques(adjs)
    expected=expected_facets(n,idx)
    assert observed==expected,(n,len(observed),len(expected),len(observed-expected),len(expected-observed))
    faces=face_layers(expected)
    bettis=betti_f2(faces)
    predicted=[0]*len(bettis); predicted[0]=1
    predicted[2]=8*comb(n,3)+(n==3)
    if n>=4:predicted[n-1]=1
    assert bettis==predicted,(n,bettis,predicted)
    t=8*comb(n,3)
    print('n=%d vertices=%d maximal_facets=%d f_vector=%s predicted_reduced_H2=%d predicted_additional_sphere_dimension=%d F2_betti=%s' %
          (n,len(roots),len(observed),[len(faces[i]) for i in sorted(faces)],t+(n==3),n-1,bettis),flush=True)

if __name__=='__main__':
    for n in (3,4,5,6):verify(n)
    print('VERIFY_OK')
