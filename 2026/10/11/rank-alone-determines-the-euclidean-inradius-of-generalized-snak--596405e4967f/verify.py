#!/usr/bin/env python3
from itertools import product
from collections import defaultdict, deque
import math

def build(word):
    # Cover edges point from lower element to upper element.
    edges={(1,0),(2,0),(3,1),(3,2)}
    nodes={0,1,2,3}
    for n,ch in enumerate(word, start=1):
        a=2*n+2
        b=2*n+3
        nodes.update((a,b))
        edges.add((b,2*n+1))
        edges.add((b,a))
        if n==1:
            target=2*n-1 if ch=="L" else 2*n
        else:
            prev=word[n-2]
            target=2*n-1 if prev!=ch else 2*n
        edges.add((a,target))
    return nodes, edges

def levels(nodes, edges):
    succ=defaultdict(list)
    indeg={v:0 for v in nodes}
    for u,v in edges:
        succ[u].append(v)
        indeg[v]+=1
    mins=[v for v in nodes if indeg[v]==0]
    assert len(mins)==1
    q=deque(mins)
    lev={mins[0]:0}
    while q:
        u=q.popleft()
        for v in succ[u]:
            lev[v]=max(lev.get(v,-10**9),lev[u]+1)
            indeg[v]-=1
            if indeg[v]==0:
                q.append(v)
    assert len(lev)==len(nodes)
    return mins[0], lev, succ

checks=0
for n in range(0,9):
    words=[""] if n==0 else ("".join(w) for w in product("LR", repeat=n))
    for word in words:
        nodes,edges=build(word)
        pmin,lev,succ=levels(nodes,edges)
        outdeg={v:0 for v in nodes}
        for u,v in edges:
            outdeg[u]+=1
        maxs=[v for v in nodes if outdeg[v]==0]
        assert maxs==[0] or set(maxs)=={0}
        pmax=0
        h=n+2
        assert lev[pmax]==h,(word,lev[pmax],h)
        assert max(lev.values())==h

        r=1/(2+h*math.sqrt(2))
        c={v:r*(1+math.sqrt(2)*lev[v]) for v in nodes}

        for v in nodes:
            assert c[v] >= r-1e-12
            assert 1-c[v] >= r-1e-12
        for u,v in edges:
            assert c[v]-c[u] >= r*math.sqrt(2)-1e-12

        # Longest-chain telescoping coefficient.
        assert abs(r*(2+h*math.sqrt(2))-1)<1e-12
        checks+=1

print(f"VERIFY_OK generalized-snake-order-inradius words={checks} max_length=8")
