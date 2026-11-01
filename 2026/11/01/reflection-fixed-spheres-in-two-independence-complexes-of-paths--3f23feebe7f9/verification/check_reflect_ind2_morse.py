#!/usr/bin/env python3
"""Exhaustively check an augmented acyclic face matching for E_m, m<=14.
E_m: subsets of 1..m without three consecutive integers and without {1,2}.
"""
from collections import deque

def faces(m):
    return {s for s in range(1<<m) if not(m>=2 and (s&3)==3) and all((s>>i)&7 != 7 for i in range(m-2))}

def pairs(m):
    if m==1:return [(0,1)]
    if m==2:return [(0,1)]
    d=faces(m)
    res=[]
    for x in d:
        if (x&3)==0:
            y=x|1
            assert y in d
            res.append((x,y))
    for x,y in pairs(m-2):
        a=(x<<2)|2
        b=(y<<2)|2
        assert a in d and b in d
        res.append((a,b))
    return res

def run(m):
    d=faces(m);mate=pairs(m)
    used=set()
    for a,b in mate:
        assert a in d and b in d and b.bit_count()==a.bit_count()+1
        assert b^a and (b^a).bit_count()==1
        assert a not in used and b not in used
        used|={a,b}
    critical=d-used
    assert critical==({sum(1<<i for i in range(1,m,2))} if m%2==0 else set()),(m,critical)
    matched=set(mate)
    graph={x:[] for x in d}
    indeg={x:0 for x in d}
    for y in d:
        for i in range(m):
            if y&(1<<i):
                x=y^(1<<i)
                u,v=(x,y) if (x,y) in matched else (y,x)
                graph[u].append(v)
                indeg[v]+=1
    q=deque(x for x in d if indeg[x]==0)
    count=0
    while q:
        x=q.popleft();count+=1
        for y in graph[x]:
            indeg[y]-=1
            if not indeg[y]:q.append(y)
    assert count==len(d),(m,count,len(d))
    print(f'PASS m={m}: faces={len(d):5d} matched_pairs={len(mate):5d} critical={critical} acyclic')
if __name__=='__main__':
    for m in range(1,15):run(m)
