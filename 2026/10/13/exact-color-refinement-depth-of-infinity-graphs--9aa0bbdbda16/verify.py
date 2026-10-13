#!/usr/bin/env python3
from collections import defaultdict

def infinity_graph(p,q):
    # F_{p,q}: C_p and C_q sharing exactly one vertex, numbered 0.
    n=p+q-1
    adj=[set() for _ in range(n)]
    cycles=([0]+list(range(1,p)),
            [0]+list(range(p,p+q-1)))
    for cyc in cycles:
        for i,u in enumerate(cyc):
            v=cyc[(i+1)%len(cyc)]
            adj[u].add(v); adj[v].add(u)
    return adj

def partition(colors):
    cells=defaultdict(set)
    for v,c in enumerate(colors):
        cells[c].add(v)
    return frozenset(frozenset(s) for s in cells.values())

def stable_partition_and_depth(adj):
    colors=[0]*len(adj)
    old=partition(colors)
    for r in range(len(adj)+5):
        sig=[(colors[v],tuple(sorted(colors[w] for w in adj[v])))
             for v in range(len(adj))]
        names={}
        new=[names.setdefault(s,len(names)) for s in sig]
        newpart=partition(new)
        if newpart==old:
            return r,old
        colors,old=new,newpart
    raise RuntimeError("no stabilization")

def formula(p,q):
    if p==q:
        return p//2
    return max(p//2,q//2,min(p,q))

def orbit_partition(p,q):
    cells=[{0}]
    if p==q:
        for d in range(1,p//2+1):
            s={i for i in range(1,p) if min(i,p-i)==d}
            s|={p+i-1 for i in range(1,q) if min(i,q-i)==d}
            if s: cells.append(s)
    else:
        for d in range(1,p//2+1):
            s={i for i in range(1,p) if min(i,p-i)==d}
            if s: cells.append(s)
        for d in range(1,q//2+1):
            s={p+i-1 for i in range(1,q) if min(i,q-i)==d}
            if s: cells.append(s)
    return frozenset(frozenset(s) for s in cells)

depth_checks=orbit_checks=0
for p in range(3,51):
    for q in range(3,51):
        depth,stable=stable_partition_and_depth(infinity_graph(p,q))
        assert depth==formula(p,q),(p,q,depth,formula(p,q))
        depth_checks+=1
        assert stable==orbit_partition(p,q),(p,q)
        orbit_checks+=1

print(f"VERIFY_OK depth_checks={depth_checks} orbit_checks={orbit_checks} p,q=3..50")
