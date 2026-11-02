#!/usr/bin/env python3
"""Finite direct graph-level test for maximal mutual visibility of clique-tree expansions."""
from collections import deque, Counter
from itertools import product
import random

def build(tree, widths):
    n=len(widths); blocks=[]; first=0
    for m in widths:
        blocks.append(tuple(range(first,first+m))); first+=m
    adj=[set() for _ in range(first)]
    def connect(a,b): adj[a].add(b);adj[b].add(a)
    for block in blocks:
        for i,a in enumerate(block):
            for b in block[i+1:]: connect(a,b)
    for a,b in tree:
        for u in blocks[a]:
            for v in blocks[b]: connect(u,v)
    return [tuple(sorted(v)) for v in adj],blocks

def all_shortest_interior_masks(adj):
    n=len(adj); masks={}
    for s in range(n):
        dist=[-1]*n;dist[s]=0;qu=deque([s]); parents=[[] for _ in range(n)]
        while qu:
            u=qu.popleft()
            for v in adj[u]:
                if dist[v]<0: dist[v]=dist[u]+1;qu.append(v)
                if dist[v]==dist[u]+1: parents[v].append(u)
        def paths(v):
            if v==s: return [0]
            acc=[]
            for u in parents[v]:
                for mask in paths(u): acc.append(mask | ((1<<u) if u!=s else 0))
            return acc
        for t in range(s+1,n): masks[(s,t)]=tuple(set(paths(t)))
    return masks

def mv(mask,pmasks):
    selected=[i for i in range(mask.bit_length()) if mask>>i&1]
    for ix,a in enumerate(selected):
        for b in selected[ix+1:]:
            if not any(not (mask & p) for p in pmasks[(a,b)]): return False
    return True

def brute_poly(adj):
    n=len(adj);p=all_shortest_interior_masks(adj); vals=[mv(mask,p) for mask in range(1<<n)]; out=Counter()
    for mask in range(1<<n):
        if vals[mask] and all(not vals[mask|(1<<j)] for j in range(n) if not(mask>>j&1)):
            out[mask.bit_count()]+=1
    return out,1<<n

def predicted_poly(tree,widths):
    n=len(widths);out=Counter()
    if n==1: return Counter({widths[0]:1})
    neighbors=[set() for _ in range(n)]
    for a,b in tree: neighbors[a].add(b);neighbors[b].add(a)
    for mask in range(1,1<<n):
        if mask.bit_count()<2: continue
        verts=[i for i in range(n) if mask>>i&1]
        seen={verts[0]}; stack=[verts[0]]
        while stack:
            u=stack.pop()
            for v in neighbors[u]:
                if mask>>v&1 and v not in seen: seen.add(v);stack.append(v)
        if len(seen)!=len(verts): continue
        internal=[v for v in verts if sum(mask>>w&1 for w in neighbors[v])>=2]
        if any(any(w not in seen for w in neighbors[v]) for v in internal):continue
        leaf=[v for v in verts if v not in internal]
        k=sum(widths[v] for v in leaf)+sum(widths[v]-1 for v in internal)
        c=1
        for v in internal:c*=widths[v]
        out[k]+=c
    return out

def trees(n):
    if n==1: return [[]]
    if n==2:return [[(0,1)]]
    result=[]
    for seq in product(range(n),repeat=n-2):
        deg=[1]*n
        for x in seq:deg[x]+=1
        edges=[]
        for x in seq:
            leaf=next(j for j,d in enumerate(deg) if d==1)
            edges.append((leaf,x));deg[leaf]-=1;deg[x]-=1
        a,b=[i for i,d in enumerate(deg) if d==1];edges.append((a,b));result.append(edges)
    return result

def check():
    trials=0;sets=0;maxorder=0
    random.seed(20261030)
    for n in range(1,6):
        seqs=trees(n)
        for ii in range(min(len(seqs),20 if n<=4 else 35)):
            tree=seqs[ii]
            for k in range(5 if n<=4 else 3):
                widths=[random.randrange(1,4) for _ in range(n)]
                if sum(widths)>12: continue
                adj,blocks=build(tree,widths)
                got,subsets=brute_poly(adj)
                exp=predicted_poly(tree,widths)
                if got!=exp:raise AssertionError((tree,widths,got,exp))
                sets+=subsets;trials+=1;maxorder=max(maxorder,len(adj))
    for m in range(1,5):
        for n in range(2,6):
            if m*n>12:continue
            adj,_=build([(i,i+1) for i in range(n-1)],[m]*n)
            got,subsets=brute_poly(adj)
            want=Counter({2*m+j*(m-1):(n-j-1)*m**j for j in range(n-1)})
            if m==1:want=Counter({2:n*(n-1)//2})
            if got!=want:raise AssertionError(('uniform',m,n,got,want))
            trials+=1;sets+=subsets;maxorder=max(maxorder,len(adj))
    print(f'VERIFY_OK graph_instances={trials} candidate_subsets={sets} maximum_order={maxorder}')
if __name__=='__main__':check()
