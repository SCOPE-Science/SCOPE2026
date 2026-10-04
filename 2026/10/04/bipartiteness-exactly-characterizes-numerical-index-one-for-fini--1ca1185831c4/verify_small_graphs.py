#!/usr/bin/env python3
from itertools import combinations, product
from collections import deque

def connected(n, edges):
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b); adj[b].append(a)
    seen={0}; q=deque([0])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in seen: seen.add(v); q.append(v)
    return len(seen)==n, adj

def bipartite(n, adj):
    c=[None]*n; c[0]=0; q=deque([0])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if c[v] is None: c[v]=1-c[u]; q.append(v)
            elif c[v]==c[u]: return False
    return True

def diameter(n, adj):
    D=0
    for s in range(n):
        d=[-1]*n; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]<0: d[v]=d[u]+1; q.append(v)
        D=max(D,max(d))
    return D

def tight_connected(n, edges, vals):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        if abs(vals[a]-vals[b])==1:
            adj[a].append(b); adj[b].append(a)
    seen={0}; q=deque([0])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in seen: seen.add(v); q.append(v)
    return len(seen)==n

def check_graph(n, edges, adj):
    D=diameter(n, adj)
    is_bip=bipartite(n, adj)
    all_ext_saturate=True
    ext_count=0
    for tail in product(range(-D,D+1), repeat=n-1):
        vals=(0,)+tail
        if any(abs(vals[a]-vals[b])>1 for a,b in edges):
            continue
        if tight_connected(n, edges, vals):
            ext_count += 1
            if any(abs(vals[a]-vals[b])!=1 for a,b in edges):
                all_ext_saturate=False
    return is_bip, all_ext_saturate, ext_count

def main():
    graph_count=0; extreme_count=0
    for n in range(2,6):
        poss=list(combinations(range(n),2))
        for mask in range(1,1<<len(poss)):
            edges=[poss[i] for i in range(len(poss)) if mask>>i & 1]
            ok,adj=connected(n,edges)
            if not ok: continue
            is_bip,prop,k=check_graph(n,edges,adj)
            if is_bip != prop:
                raise SystemExit(f'FAIL n={n} edges={edges} bip={is_bip} prop={prop}')
            graph_count += 1; extreme_count += k
    print(f'VERIFY_OK connected_labeled_graphs={graph_count} extreme_dual_vertices={extreme_count} n=2..5')

if __name__=='__main__': main()
