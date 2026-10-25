#!/usr/bin/env python3
"""Independent brute-force checks of near-packed cyclic independent-set exchange graphs."""
from itertools import combinations
from collections import deque

def evaluate(r, m, s):
    L=(r+1)*m+s
    adj=[0]*L
    for i in range(L):
        adj[i]=sum(1<<((i+d)%L) for d in range(-r,r+1) if d)
    independent=[]
    for seq in combinations(range(L),m):
        mask=sum(1<<x for x in seq)
        if all(not(adj[x]&mask) for x in seq): independent.append(mask)
    ix={a:i for i,a in enumerate(independent)}
    g=[set() for _ in independent]
    move_types=[]
    for a_idx,a in enumerate(independent):
        for u in range(L):
            if not(a>>u&1): continue
            for v in range(L):
                if a>>v&1: continue
                b=a^(1<<u)^(1<<v)
                j=ix.get(b)
                if j is not None and a_idx<j:
                    assert (adj[u]>>v)&1, ('non-slide maximum jump',r,m,s,u,v)
                    g[a_idx].add(j);g[j].add(a_idx)
                    d=min((u-v)%L,(v-u)%L)
                    move_types.append(d)
    comps=0;seen=set()
    for i in range(len(g)):
        if i in seen: continue
        comps+=1;todo=[i];seen.add(i)
        while todo:
            v=todo.pop()
            for u in g[v]:
                if u not in seen:seen.add(u);todo.append(u)
    tri=sum(len(g[u]&g[v]) for u in range(len(g)) for v in g[u] if u<v)//3
    if s==0: expect=(r+1,0,r+1,0,0)
    if s==1: expect=(L,L,1,0,2)
    if s==2: expect=(L*(m+1)//2,L*(m+1),1,L,4)
    got=(len(g),sum(map(len,g))//2,comps,tri,min(map(len,g)) if g else 0)
    assert got==expect, (r,m,s,L,got,expect)
    if s in (1,2): assert all(len(z)==expect[-1] for z in g)
    assert max(move_types,default=0)<=2
    return (r,m,s,L,len(g),sum(map(len,g))//2,comps,tri)

if __name__=='__main__':
    cases=[]
    for r in range(2,6):
        for m in range(2,5):
            for s in range(3):
                cases.append(evaluate(r,m,s))
    print('BRUTE_FORCE_OK',len(cases))
    print('columns r m s N vertices edges components triangles')
    for case in cases:print(*case)
