#!/usr/bin/env python3
"""Independent BFS shortest-path verification for edge-general-position enumeration."""
from collections import deque, Counter
from itertools import combinations, product
from math import comb

def pol_mul(a,b):
    c=Counter()
    for (i,j),u in a.items():
        for (r,s),v in b.items():c[(i+r,j+s)]+=u*v
    return c

def expected(b):
    n=len(b); k=n*(n-1)//2;f=Counter(); g=Counter()
    for bits in range(1<<n):
        P=[i for i in range(n) if (bits>>i)&1]; sz=len(P)
        A={(0,0):1}
        for i in P:
            A=pol_mul(A,{(r,0):comb(b[i],r) for r in range(1,b[i]+1)})
        for (i,j),v in pol_mul(A,{(0,r):comb(k-comb(sz,2),r) for r in range(k-comb(sz,2)+1)}).items():f[(i,j)]+=v
        if P:g[(sum(b[i] for i in P),k-comb(sz,2))]+=1
    return +f,+g

def graph(b):
    n=len(b);N=n+sum(b); E=[]
    for i in range(n):
        for j in range(i+1,n):E.append((i,j,'C'))
    ix=n
    for i,x in enumerate(b):
        for j in range(x):E.append((i,ix,'L'));ix+=1
    adj=[[] for _ in range(N)]
    for ei,(u,v,_) in enumerate(E):adj[u].append((v,ei));adj[v].append((u,ei))
    return E,adj

def forbidden_triples(adj):
    N=len(adj); forb=set()
    # Enumerate every shortest path for every ordered pair by BFS and backtracking.
    for root in range(N):
        dist=[-1]*N;dist[root]=0; Q=deque([root]);prev=[[] for _ in range(N)]
        while Q:
            u=Q.popleft()
            for v,ei in adj[u]:
                if dist[v]<0:dist[v]=dist[u]+1;Q.append(v)
                if dist[v]==dist[u]+1:prev[v].append((u,ei))
        def paths(v):
            if v==root:yield ()
            else:
                for u,e in prev[v]:
                    for p in paths(u):yield p+(e,)
        for target in range(root+1,N):
            for p in paths(target):
                for tri in combinations(p,3):
                    forb.add(sum(1<<e for e in tri))
    return tuple(forb)

def run_case(b):
    E,adj=graph(b);n=len(b);m=len(E);triples=forbidden_triples(adj);feas=[False]*(1<<m);p_count=Counter();g_count=Counter()
    for mask in range(1<<m):
        if any(mask&t==t for t in triples):continue
        feas[mask]=True
        X=sum(bool(mask>>i&1) for i,edge in enumerate(E) if edge[2]=='L')
        Y=mask.bit_count()-X
        p_count[(X,Y)]+=1
    for mask,yes in enumerate(feas):
        if yes and all(not feas[mask|(1<<i)] for i in range(m) if not mask>>i&1):
            X=sum(bool(mask>>i&1) for i,edge in enumerate(E) if edge[2]=='L')
            Y=mask.bit_count()-X
            g_count[(X,Y)]+=1
    f,g=expected(b)
    if +p_count!=f or +g_count!=g:
        raise AssertionError((b,'poly mismatch',+p_count,f,+g_count,g))
    best=max(x+y for x,y in g)
    w=sorted(b,reverse=True)
    ex=comb(n,2)+max(sum(w[:s])-comb(s,2) for s in range(1,n+1))
    assert best==ex,(b,best,ex)
    assert sum(g.values())==2**n-1
    return 1<<m,len(triples),sum(p_count.values()),sum(g_count.values())

def main():
    cases=[(1,1,1),(2,3,2),(1,1,1,1),(2,1,2,1),(2,2,2,2),(1,1,1,1,1)]
    total=0
    for b in cases:
        subsets,triples,feasible,facets=run_case(b);total+=subsets
        print('PASS',','.join(map(str,b)),'subsets',subsets,'geodesic_triples',triples,'feasible',feasible,'facets',facets)
    print('VERIFICATION_OK profiles=%d vertex_edge_subsets=%d'%(len(cases),total))
if __name__=='__main__':main()
