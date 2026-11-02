#!/usr/bin/env python3
"""Independent exact verification via the bipartite double cover of KG(5,2).
No packages beyond Python's standard library are required.
"""
import itertools
from collections import Counter,deque

PAIRS=list(itertools.combinations(range(5),2))
EDGES=[]
for x,A in enumerate(PAIRS):
    for y,B in enumerate(PAIRS):
        if set(A).isdisjoint(B):EDGES.append((x,10+y))
EDGES=tuple(sorted(EDGES))
assert len(EDGES)==30 and len(set(EDGES))==30
# Concrete isomorphism from the double cover of KG(5,2) to GP(10,3).
MAP=(0,19,13,2,8,17,11,6,15,4,5,14,18,7,3,12,16,1,10,9)
P={(min(MAP[a],MAP[b]),max(MAP[a],MAP[b])) for a,b in EDGES}
Q=set()
for i in range(10):
    for a,b in [(i,(i+1)%10),(i,10+i),(10+i,10+(i+3)%10)]:Q.add((min(a,b),max(a,b)))
assert P==Q

incident=[[] for _ in range(20)]
for j,(u,v) in enumerate(EDGES):incident[u].append(j);incident[v].append(j)
assert all(len(x)==3 for x in incident)
full=(1<<30)-1

def matchings(mask):
    if mask==0:
        yield 0
        return
    v=(mask & -mask).bit_length()-1
    for j in incident[v]:
        a,b=EDGES[j]; w=b if a==v else a
        if mask>>w & 1:
            for smaller in matchings(mask & ~(1<<v) & ~(1<<w)):
                yield smaller | (1<<j)

def alternating_classes(mzero):
    """Enumerate the two complementary perfect matchings by alternating on 2-factor cycles."""
    adj=[[] for _ in range(20)]
    for j,(u,v) in enumerate(EDGES):
        if not (mzero>>j&1):adj[u].append((v,j));adj[v].append((u,j))
    assert all(len(x)==2 for x in adj)
    cycles=[];seen=set()
    for s in range(20):
        if s in seen:continue
        cur=s;prev=-1;edges=[]
        while cur not in seen:
            seen.add(cur)
            nxt=[p for p in adj[cur] if p[0]!=prev][0]
            newv,j=nxt;edges.append(j)
            prev,cur=cur,newv
        assert cur==s and len(edges)%2==0
        cycles.append(edges)
    for pattern in itertools.product((0,1),repeat=len(cycles)):
        one=0
        for cy,bit in zip(cycles,pattern):
            for t in range(bit,len(cy),2):one|=1<<cy[t]
        two=full^mzero^one
        yield (mzero,one,two)

match=list(matchings((1<<20)-1))
assert len(match)==60
states=sorted(set(C for m in match for C in alternating_classes(m)))
assert len(states)==192
ids={c:i for i,c in enumerate(states)}

def moves(masks):
    out=set()
    for x,y,z in ((0,1,2),(0,2,1),(1,2,0)):
        # Traverse the bichromatic 2-factor using the third matching as complement.
        residual=masks[x]|masks[y]
        at=[[] for _ in range(20)]
        for j,(a,b) in enumerate(EDGES):
            if residual>>j & 1:at[a].append((b,j));at[b].append((a,j))
        vis=set()
        for start in range(20):
            if start in vis:continue
            q=[start];vis.add(start);bits=0
            for u in q:
                for v,j in at[u]:
                    bits|=1<<j
                    if v not in vis:vis.add(v);q.append(v)
            nxt=list(masks);nxt[x]^=bits;nxt[y]^=bits
            out.add(ids[tuple(nxt)])
    return out

A=[moves(C) for C in states]
assert all(i in A[j] for j,v in enumerate(A) for i in v)

def connected():
    unseen=set(range(len(A))); groups=[]
    while unseen:
        v=min(unseen);q=[v];unseen.remove(v)
        for x in q:
            for y in A[x]:
                if y in unseen:unseen.remove(y);q.append(y)
        groups.append(q)
    return sorted(groups,key=lambda g:-len(g))

def dists(u):
    ds={u:0};q=deque([u])
    while q:
        v=q.popleft()
        for w in A[v]:
            if w not in ds:ds[w]=ds[v]+1;q.append(w)
    return ds

def squares(G):
    total=0
    for i,u in enumerate(G):
        for v in G[i+1:]:
            t=len(A[u]&A[v]);total+=t*(t-1)//2
    assert total%2==0
    return total//2

def pentagons(G):
    # A 5-step closed walk in a loopless, triangle-free graph is a simple pentagon.
    tot=0
    for u in G:
        counts={u:1}
        for _ in range(5):
            nxt={}
            for v,ways in counts.items():
                for w in A[v]:nxt[w]=nxt.get(w,0)+ways
            counts=nxt
        tot+=counts.get(u,0)
    assert tot%10==0
    return tot//10

def is_bipartite(G):
    parity={G[0]:0};q=[G[0]]
    for v in q:
        for w in A[v]:
            if w not in parity:parity[w]=1-parity[v];q.append(w)
            elif parity[w]==parity[v]:return False
    return True

def three_colorable(G):
    order=sorted(G,key=lambda v:-len(A[v])); col={}
    def rec(i):
        if i==len(order):return True
        v=order[i]
        for c in range(3):
            if all(col.get(w)!=c for w in A[v]):
                col[v]=c
                if rec(i+1):return True
                del col[v]
        return False
    return rec(0)

groups=connected()
assert list(map(len,groups))==[120]+[12]*6
assert sum(len(x) for x in A)==1008
for k,G in enumerate(groups):
    deg=Counter(len(A[x]) for x in G)
    profiles=Counter(tuple(Counter(dists(x).values()).get(j,0) for j in range(6 if k==0 else 3)) for x in G)
    obs=(deg,profiles,squares(G),pentagons(G),is_bipartite(G))
    exp=(Counter({6:120}),Counter({(1,6,27,48,32,6):120}),90,0,True) if k==0 else (Counter({4:12}),Counter({(1,4,7):12}),15,48,False)
    assert obs==exp,(k,obs,exp)
    if k:assert three_colorable(G)
print('DESARGUES_INDEPENDENT_PASS matchings=60 states=192 edges=504 components=1x120+6x12')
print('DESARGUES_INDEPENDENT_SPHERES 120:(1,6,27,48,32,6); 12:(1,4,7)')
print('DESARGUES_INDEPENDENT_PARITY one_bipartite_six_three_chromatic pentagons=288 squares=180')
