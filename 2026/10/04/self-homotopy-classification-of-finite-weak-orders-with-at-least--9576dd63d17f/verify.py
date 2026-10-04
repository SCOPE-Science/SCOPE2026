#!/usr/bin/env python3
from itertools import product
from collections import deque


def weak_order(level_sizes):
    levels=[]; level_of={}; k=0
    for i,r in enumerate(level_sizes):
        L=list(range(k,k+r)); levels.append(L)
        for x in L: level_of[x]=i
        k += r
    def leq(a,b):
        return a==b or level_of[a] < level_of[b]
    return levels, level_of, leq


def monotone_maps(level_sizes):
    levels, level_of, leq = weak_order(level_sizes)
    n=sum(level_sizes)
    out=[]
    comparable_pairs=[(a,b) for a in range(n) for b in range(n) if leq(a,b)]
    for f in product(range(n), repeat=n):
        if all(leq(f[a],f[b]) for a,b in comparable_pairs):
            out.append(f)
    return out, levels, level_of, leq


def predicted_nonzero(f, levels, level_of):
    for i,L in enumerate(levels):
        vals={f[x] for x in L}
        if len(vals) < 2 or any(level_of[y] != i for y in vals):
            return False
    return True


def image_contractible_weak_order(f, levels, level_of):
    # For an induced subposet of a weak order, connectedness plus a singleton
    # occupied level gives a cone. In these self-map images, the theorem says
    # precisely the predicted-zero cases have such a singleton occupied level.
    image=set(f)
    occupied=[]
    for i in range(len(levels)):
        s={y for y in image if level_of[y]==i}
        if s: occupied.append(s)
    if len(occupied)==1:
        return len(occupied[0])==1
    return any(len(s)==1 for s in occupied)


def components_of_map_poset(maps, leq):
    m=len(maps); adj=[[] for _ in range(m)]
    def map_leq(f,g): return all(leq(f[x],g[x]) for x in range(len(f)))
    for i in range(m):
        for j in range(i):
            if map_leq(maps[i],maps[j]) or map_leq(maps[j],maps[i]):
                adj[i].append(j); adj[j].append(i)
    seen=set(); comps=[]
    for s in range(m):
        if s in seen: continue
        q=[s]; seen.add(s); comp=[]
        while q:
            u=q.pop(); comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); q.append(v)
        comps.append(comp)
    return comps


def check(level_sizes, do_components=False):
    maps, levels, level_of, leq = monotone_maps(level_sizes)
    nonzero=[f for f in maps if predicted_nonzero(f,levels,level_of)]
    expected=1
    for r in level_sizes:
        expected *= r**r-r
    assert len(nonzero)==expected, (level_sizes,len(nonzero),expected)
    for f in maps:
        if not predicted_nonzero(f,levels,level_of):
            assert image_contractible_weak_order(f,levels,level_of), (level_sizes,f)
    result={"sizes":level_sizes,"maps":len(maps),"predicted_nonzero":len(nonzero),"predicted_classes":1+expected}
    if do_components:
        comps=components_of_map_poset(maps,leq)
        sizes=sorted(len(c) for c in comps)
        assert len(comps)==1+expected
        assert sizes.count(1)==expected
        assert sizes[-1]==len(maps)-expected
        result["components"]=len(comps)
        result["component_sizes"]=sizes
    return result


r1=check((2,2,2), True)
r2=check((2,2,3), False)
print(r1)
print(r2)
print("VERIFY_OK")
