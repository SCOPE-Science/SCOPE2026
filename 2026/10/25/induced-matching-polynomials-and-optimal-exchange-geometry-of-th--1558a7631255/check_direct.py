#!/usr/bin/env python3
"""Direct vertex-subset enumeration of induced matchings and their exchanges.

Independent of the compatibility-graph local counting method. Standard-library only.
"""
from itertools import combinations
from collections import Counter, deque


def calc(kind):
    verts=range(16)
    def edge(u,v):
        a,b=divmod(u,4);c,d=divmod(v,4)
        if kind=='R':return a==c or b==d
        dx=(a-c)%4;dy=(b-d)%4
        return (dx,dy) in ((0,1),(0,3),(1,0),(3,0),(1,1),(3,3))
    g={(u,v) for u,v in combinations(verts,2) if edge(u,v)}
    E=list(sorted(g))
    def induced(selected):
        ends=[]
        for a,b in selected:ends.extend((a,b))
        if len(set(ends))!=len(ends):return False
        return sum(edge(a,b) for a,b in combinations(ends,2))==len(selected)
    bag={r:[tuple(c) for c in combinations(E,r) if induced(c)] for r in (1,2,3,4)}
    counts=[1]+[len(bag[i]) for i in range(1,5)]
    if kind=='R':assert counts==[1,48,216,0,0]
    else:assert counts==[1,48,192,32,0]
    mx=bag[2 if kind=='R' else 3]
    k=len(mx[0]);S=[frozenset(t) for t in mx]
    adj=[set() for _ in S]
    for i,j in combinations(range(len(S)),2):
        if len(S[i]&S[j])==k-1:adj[i].add(j);adj[j].add(i)
    deg=Counter(map(len,adj));components=[]
    unseen=set(range(len(S)))
    while unseen:
        start=unseen.pop();stack=[start];num=1
        while stack:
            for y in adj[stack.pop()]:
                if y in unseen:unseen.remove(y);stack.append(y);num+=1
        components.append(num)
    assert (sum(map(len,adj))//2,dict(deg),sorted(components)) == ((1728,{16:216},[216]) if kind=='R' else (0,{0:32},[1]*32))
    print(kind,'direct_counts',counts,'exchange_edges',sum(map(len,adj))//2,'exchange_degree_dist',sorted(deg.items()),'component_sizes',sorted(components))
for kind in ('R','S'):calc(kind)
