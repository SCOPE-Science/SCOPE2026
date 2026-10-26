#!/usr/bin/env python3
"""Exact linear-time vertex-isolation membership on trees; proof recurrence in RESULT.md.
Run: python3 verify_isolation_reroot.py. Uses only the Python standard library.
"""
from itertools import product
from math import inf as INF
from heapq import heapify, heappop, heappush
from random import Random

def plus(a,b):return a+b

def combine(a,b):
    s1,s0,s00,an,ay=a
    t1,t0,t00,bn,by=b
    return (plus(s1,t1),plus(s0,t0),plus(s00,t00),plus(an,bn),min(plus(ay,min(bn,by)),plus(an,by)))
UNIT=(0,0,0,0,INF)

def leaf_entry(f):
    # F(x_parent, x_self, dominated_self) on the component side of an edge
    a1=min(f[1][0][0],f[1][0][1],f[1][1][0],f[1][1][1])
    a0=min(f[0][0][0],f[0][0][1],f[0][1][0],f[0][1][1])
    b=f[0][0][1]
    c=min(f[0][0]); d=min(f[0][1])
    return (a1,a0,b,c,d)

def table(agg):
    a1,a0,b,n,y=agg
    f=[[[INF]*2 for _ in range(2)] for _ in range(2)]
    for xp in (0,1):f[xp][1][1]=plus(1,a1)
    f[1][0][1]=a0
    f[0][0][0]=b
    f[0][0][1]=y
    return f

def solve(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v); adj[v].append(u)
    parent=[-1]*n; order=[0]; parent[0]=0
    for v in order:
        for w in adj[v]:
            if parent[w]<0:parent[w]=v; order.append(w)
    assert len(order)==n
    msg={}
    for v in reversed(order[1:]):
        incoming=UNIT
        for u in adj[v]:
            if u!=parent[v]:incoming=combine(incoming,leaf_entry(msg[(u,v)]))
        msg[(v,parent[v])]=table(incoming)
    root_agg=UNIT
    for u in adj[0]:root_agg=combine(root_agg,leaf_entry(msg[(u,0)]))
    root_f=table(root_agg)
    optimum=min(root_f[0][x][d] for x in (0,1) for d in (0,1))
    # Every vertex uses a prefix/suffix scan of incoming messages.
    forced=[None]*n
    forbidden=[None]*n
    for v in order:
        inc=[leaf_entry(msg[(u,v)]) for u in adj[v]]
        degree=len(inc)
        prefix=[UNIT]*(degree+1)
        suffix=[UNIT]*(degree+1)
        for i in range(degree):prefix[i+1]=combine(prefix[i],inc[i])
        for i in range(degree-1,-1,-1):suffix[i]=combine(inc[i],suffix[i+1])
        forced[v]=plus(1,prefix[-1][0])
        forbidden[v]=min(prefix[-1][2],prefix[-1][4])
        for i,u in enumerate(adj[v]):
            if u==parent[v] and v!=0:continue
            # sends v->u, excludes exactly u
            agg=combine(prefix[i],suffix[i+1]);msg[(v,u)]=table(agg)
    return optimum,forced,forbidden

def brute(n,edges):
    adj=[0]*n
    for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    best=INF;forced=[INF]*n;forbidden=[INF]*n
    for mask in range(1<<n):
        weight=mask.bit_count()
        dominated=mask
        for v in range(n):
            if mask>>v&1:dominated|=adj[v]
        if any(not(dominated>>u&1 or dominated>>v&1) for u,v in edges):continue
        if weight<best:best=weight
        for v in range(n):
            if mask>>v&1:forced[v]=min(forced[v],weight)
            else:forbidden[v]=min(forbidden[v],weight)
    return best,forced,forbidden

def prufer_edges(code):
    n=len(code)+2
    degrees=[1]*n
    for v in code:degrees[v]+=1
    heap=[i for i,d in enumerate(degrees) if d==1];heapify(heap)
    edges=[]
    for v in code:
        u=heappop(heap);edges.append((u,v));degrees[v]-=1
        if degrees[v]==1:heappush(heap,v)
    a=heappop(heap);b=heappop(heap);edges.append((a,b))
    return edges

def check():
    checks=0
    for n in range(1,8):
        if n==1:
            cases=[[]]
        else:
            cases=map(prufer_edges,product(range(n),repeat=n-2))
        for e in cases:
            a=solve(n,e); c=brute(n,e)
            if a!=c:raise AssertionError((n,e,a,c))
            checks+=1
    rng=Random(20261023)
    for n in range(8,14):
        for _ in range(80):
            e=[(i,rng.randrange(i)) for i in range(1,n)]
            a=solve(n,e); c=brute(n,e)
            if a!=c:raise AssertionError((n,e,a,c))
            checks+=1
    # Subdividing an edge by a new vertex, direct recognition on all trees up to 6.
    subdiv_checks=0
    for n in range(2,7):
        for code in product(range(n),repeat=n-2):
            e=prufer_edges(code)
            opt,f,z=solve(n,e)
            excluded={v for v in range(n) if f[v]>opt}
            predicted=any(v in excluded and all((x==v or x in excluded) for a,b in e for x in ([b] if a==v else ([a] if b==v else []))) for v in range(n))
            # Equivalent: some closed neighborhood consists of nonessential vertices.
            actual=False
            for idx,(u,v) in enumerate(e):
                ee=e[:idx]+e[idx+1:]+[(u,n),(n,v)]
                new_opt,_,_=brute(n+1,ee)
                actual|=new_opt>opt
            if predicted!=actual:raise AssertionError(('subdivision',n,e,predicted,actual,excluded))
            subdiv_checks+=1
    print('VERIFY_OK', 'independent_bf_tree_cases=',checks,'subdivision_trees=',subdiv_checks)

if __name__=='__main__':check()
