#!/usr/bin/env python3
"""Exhaustive original-graph simulation of minimum prism power domination."""
from itertools import combinations

def neighbors(n):
    adj=[]
    for rail in range(2):
        for i in range(n):
            adj.append({rail*n+(i-1)%n,rail*n+(i+1)%n,(1-rail)*n+i})
    return adj

def pds(n,S,adj):
    seen=set(S)
    for s in S: seen.update(adj[s])
    while True:
        fresh={next(iter(adj[v]-seen)) for v in seen if len(adj[v]-seen)==1}
        if not fresh: return len(seen)==2*n
        seen.update(fresh)

def predicted(n,S):
    if n==3: return len(S) in (1,2)
    if len(S)!=2: return False
    u,v=sorted(S)
    a,b=u%n,v%n
    delta=min(abs(a-b),n-abs(a-b))
    return delta<=(3 if u//n==v//n else 2)

def count(n):
    return {3:6,4:28,5:45,6:60}.get(n,11*n)

for n in range(3,61):
    adj=neighbors(n)
    good=[]
    for k in (1,2):
        for S in combinations(range(2*n),k):
            actual=pds(n,S,adj)
            expected=predicted(n,S)
            assert actual==expected,(n,S,actual,expected)
            if actual and k==(1 if n==3 else 2):good.append(S)
    assert len(good)==count(n),(n,len(good),count(n))
    print('INDEPENDENT_ORIGINAL_GRAPH_EXHAUSTIVE_OK',n,len(good))
print('VERIFY_OK')
