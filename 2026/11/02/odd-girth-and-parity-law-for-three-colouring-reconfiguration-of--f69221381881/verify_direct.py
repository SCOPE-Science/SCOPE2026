#!/usr/bin/env python3
"""Enumerate proper 3-colourings of cycles directly, including reconfiguration edges.
All graphs and colourings are built afresh here from the stated definitions.
"""
from collections import Counter, deque, defaultdict
from itertools import product
from math import comb

def verify(n):
    S=[v for v in product(range(3), repeat=n) if all(v[i]!=v[(i+1)%n] for i in range(n))]
    assert len(S)==2**n+2*(-1)**n
    indices={v:i for i,v in enumerate(S)}
    groups=defaultdict(list)
    for i,v in enumerate(S):
        p=sum((v[(j+1)%n]-v[j])%3==1 for j in range(n))
        assert (2*p-n)%3==0
        groups[p].append(i)
    adj=[set() for v in S]
    for i,v in enumerate(S):
        for j in range(n):
            if v[(j-1)%n]!=v[(j+1)%n]:continue
            v2=list(v)
            v2[j]=3-v[j]-v[(j-1)%n]
            k=indices[tuple(v2)]
            adj[i].add(k)
    assert all(i in adj[j] for j,a in enumerate(adj) for i in a)
    for p,vs in groups.items():
        wanted=3*comb(n,p)
        assert len(vs)==wanted,(n,p,'count',len(vs),wanted)
        deg=sum(len(adj[u]) for u in vs)
        edges=deg//2
        exp_edges=3*n*comb(n-2,p-1) if 0<p<n else 0
        assert deg%2==0 and edges==exp_edges,(n,p,'edges',edges,exp_edges)
        unseen=set(vs); component_sizes=[]
        while unseen:
            u=unseen.pop();q=[u];sz=0
            while q:
                a=q.pop();sz+=1
                for b in adj[a]:
                    assert b in vs
                    if b in unseen:unseen.remove(b);q.append(b)
            component_sizes.append(sz)
        if p==0 or p==n:
            assert component_sizes==[1,1,1]
            continue
        assert component_sizes==[len(vs)],(n,p,'components',component_sizes)
        if min(p,n-p)==1:
            assert len(vs)==3*n and all(len(adj[u])==2 for u in vs)
        else:
            assert any(len(adj[u])>=3 for u in vs)
        source=vs[0]
        q=deque([(source,0)]);seen={(source,0):0}
        while q:
            a,par=q.popleft()
            if a==source and par==1:break
            for b in adj[a]:
                key=(b,par^1)
                if key not in seen:
                    seen[key]=seen[(a,par)]+1
                    q.append(key)
        odd=seen.get((source,1),None)
        if n%2:
            assert odd==3*n,(n,p,'odd-girth-from-root',odd)
        else:
            assert odd is None,(n,p,'expected-bipartite',odd)
        # Explicitly check a four-cycle exists exactly when both signs occur twice.
        four=False
        for u in vs:
            for v in adj[u]:
                for x in adj[v]:
                    if x==u:continue
                    if any(w!=v for w in adj[x].intersection(adj[u])):four=True;break
                if four:break
            if four:break
        assert four==(2<=p<=n-2),(n,p,'4-cycle',four)
    return n,len(S),sum(len(a) for a in adj)//2,len(groups)

if __name__=='__main__':
    for n in range(3,12):
        print('DIRECT_PASS',*verify(n))
