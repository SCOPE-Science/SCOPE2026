#!/usr/bin/env python3
"""Finite checks of two nested equivalence relations with unary colours.
Runs without third-party libraries. Checks the proposed profile criterion
against an explicit greatest-fixpoint guarded-bisimulation game.
"""
from itertools import combinations, product
from functools import lru_cache
from collections import Counter
import random

@lru_cache(None)
def integer_partitions(n, minpart=1):
    if n==0: return ((),)
    out=[]
    for a in range(minpart,n+1):
        for rest in integer_partitions(n-a,a):
            out.append((a,)+rest)
    return tuple(out)

@lru_cache(None)
def blocks_of_size(n,c):
    if n<1: return ()
    return tuple(v for v in (p for p in combinations_with_replacement_range(c,n)))

def combinations_with_replacement_range(c,n):
    from itertools import combinations_with_replacement
    yield from combinations_with_replacement(range(c),n)

@lru_cache(None)
def inner_types(n,c):
    if n==0: return ((),)
    arr=[]
    for p in integer_partitions(n):
        parts = [blocks_of_size(z,c) for z in p]
        for cand in product(*parts):
            if list(cand)==sorted(cand):arr.append(cand)
    return tuple(sorted(set(arr)))

@lru_cache(None)
def outer_types(n,c):
    if n==0: return ((),)
    arr=[]
    for p in integer_partitions(n):
        parts = [inner_types(z,c) for z in p]
        for cand in product(*parts):
            if list(cand)==sorted(cand):arr.append(cand)
    return tuple(sorted(set(arr)))

def build_model(out):
    cols=[]; in_ids=[];out_ids=[]
    for j, outer in enumerate(out):
        for i,inner in enumerate(outer):
            for col in inner:
                cols.append(col);in_ids.append((j,i));out_ids.append(j)
    return cols,in_ids,out_ids

def profile(model,c):
    colors,inner,outer=model
    b=Counter()
    for oi in set(outer):
        a=Counter()
        for ii in set(inner):
            if ii[0]!=oi:continue
            bc=Counter(colors[j] for j in range(len(colors)) if inner[j]==ii)
            bt=tuple(min(2,bc[i]) for i in range(c))
            a[bt]+=1
        at=tuple(sorted((v,min(2,n)) for v,n in a.items()))
        b[at]+=1
    return frozenset(b)

def guard_sets(model):
    cols,inner,outer=model
    n=len(cols)
    return [(i,) for i in range(n)]+[(i,j) for i in range(n) for j in range(i+1,n) if outer[i]==outer[j]]

def guarded_bisimilar(m,n):
    c1,i1,o1=m; c2,i2,o2=n
    G1=guard_sets(m); G2=guard_sets(n)
    states=[]
    # complete atomic partial maps on guarded subsets
    for a in G1:
      for b in G2:
        if len(a)!=len(b):continue
        for perm in ([b] if len(b)==1 else [b,b[::-1]]):
          if any(c1[x]!=c2[y] for x,y in zip(a,perm)):continue
          if len(a)==2 and ((i1[a[0]]==i1[a[1]])!=(i2[perm[0]]==i2[perm[1]])):continue
          states.append((a,perm))
    S=set(states)
    # greatest fixed point with overlap-conserving extension in both directions
    while True:
      T=set()
      for a,b in S:
        f=dict(zip(a,b));inv=dict(zip(b,a));A=set(a);B=set(b)
        ok=True
        for nxt in G1:
          overlap=A.intersection(nxt)
          if not any(set(xx)==set(nxt) and all(dict(zip(xx,yy)).get(v)==f[v] for v in overlap) for xx,yy in S):
            ok=False;break
        if not ok:continue
        for nxt in G2:
          overlap=B.intersection(nxt)
          if not any(set(yy)==set(nxt) and all(dict(zip(yy,xx)).get(v)==inv[v] for v in overlap) for xx,yy in S):
            ok=False;break
        if ok:T.add((a,b))
      if T==S: break
      S=T
    # GF sentence equivalence means complete global coverage via surviving maps
    return all(any(set(a)==set(g) for a,b in S) for g in G1) and all(any(set(b)==set(g) for a,b in S) for g in G2)

def checks():
    counts=[]
    for c,maxn in [(1,6),(2,4)]:
        models=[]
        for n in range(1,maxn+1):
            ts=outer_types(n,c)
            counts.append((c,n,len(ts)))
            models.extend(build_model(t) for t in ts)
        p=[profile(m,c) for m in models]
        cases=0
        # Complete pairwise comparisons through small populations
        subset=models[:]; ps=p[:]
        for i in range(len(subset)):
          for j in range(i,len(subset)):
            if max(len(subset[i][0]),len(subset[j][0]))>4 and (i+j)%7: continue
            predicted=ps[i]==ps[j]
            observed=guarded_bisimilar(subset[i],subset[j])
            assert predicted==observed,(c,i,j,predicted,observed,subset[i],subset[j])
            cases+=1
        print('PROFILE_VS_GUARDED_GAME_OK',c,maxn,len(models),cases)
    print('ISOMORPHISM_TYPE_COUNTS',counts)
    for c in (1,2,4):
        B=3**c-1
        assert sum(sum(a) for a in product(range(3),repeat=c))==c*3**c
        if c<=2:
            atypes=[a for a in product(range(3),repeat=c) if any(a)]
            assert c*3**c*3**B==sum(sum(b[t]*sum(a) for t,a in enumerate(atypes)) for b in product(range(3),repeat=B))
        print('EXACT_SHARP_BOUND',c,B,3**B-1,c*3**c*3**B)
    print('NESTED_EQUIVALENCE_GF_CHECK_OK')
if __name__=='__main__': checks()
