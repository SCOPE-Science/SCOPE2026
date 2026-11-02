#!/usr/bin/env python3
"""Exact direct enumeration checks for signed-line-graph frustration on unicyclic graphs.

Run: python verify_unicyclic.py
Pure Python 3 standard library; no external datasets.
"""
from itertools import combinations
from collections import deque
from random import Random


def connected_cycle(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    visited = {0}; q = deque([0])
    while q:
        for v in adj[q.popleft()]:
            if v not in visited: visited.add(v); q.append(v)
    if len(visited) != n or len(edges) != n: return None
    degree = [len(adj[i]) for i in range(n)]
    q = deque(i for i in range(n) if degree[i] == 1)
    while q:
        i = q.popleft(); degree[i] = 0
        for j in adj[i]:
            if degree[j] > 0:
                degree[j] -= 1
                if degree[j] == 1: q.append(j)
    cyc = [i for i in range(n) if degree[i] == 2]
    assert len(cyc) >= 3
    return cyc, [len(a) for a in adj]


def predicted(n, edges):
    cyc, deg = connected_cycle(n,edges)
    if len(cyc) % 2 == 0: return 0, 2
    d = min(deg[i] for i in cyc)
    t = sum(deg[i] == d for i in cyc)
    return d-1, (2 if d == 2 else 4)*t


def direct_orientations(n, edges):
    best = 10**9; count = 0
    for mask in range(1 << len(edges)):
        inc = [0]*n; out = [0]*n
        for j, (u,v) in enumerate(edges):
            if (mask>>j)&1: inc[u]+=1; out[v]+=1
            else: inc[v]+=1; out[u]+=1
        cost = sum(a*b for a,b in zip(inc,out))
        if cost < best: best = cost; count=1
        elif cost == best: count+=1
    return best,count


def direct_signed_switches(n, edges):
    # Enumerate sign switchings in a signed line graph.  Fix the first
    # edge-vertex switch sign to +1 to divide out global sign reversal.
    m = len(edges); incidences = []
    for i,(u,v) in enumerate(edges):
        incidences.extend(((u,i,-1),(v,i,+1)))
    contacts = []
    for u in range(n):
        loc = [(e,s) for w,e,s in incidences if w==u]
        for (a,sa),(b,sb) in combinations(loc,2):
            contacts.append((a,b,sa*sb))
    best=10**9; count=0
    for mask in range(1 << (m-1)):
        cost=0
        for a,b,s in contacts:
            xa = 1 if a==0 or not ((mask>>(a-1))&1) else -1
            xb = 1 if b==0 or not ((mask>>(b-1))&1) else -1
            if s*xa*xb<0: cost+=1
        if cost < best:best=cost;count=1
        elif cost==best:count+=1
    return best,count


def run():
    exhaustive=0; signed=0
    for n in range(3,7):
        for ed in combinations(combinations(range(n),2),n):
            if connected_cycle(n,ed) is None: continue
            want=predicted(n,ed); got=direct_orientations(n,ed)
            assert want==got, ('all graphs',n,ed,want,got)
            exhaustive+=1
            if n <=5:
                signed_got=direct_signed_switches(n,ed)
                assert signed_got == (want[0], want[1]//2),(ed,want,signed_got)
                signed+=1
    rng=Random(1002)
    sampled=0
    for n in range(7,13):
        for rep in range(45):
            k=rng.randrange(3,n+1)
            edges=[(i,(i+1)%k) for i in range(k)]
            for u in range(k,n):
                edges.append((u,rng.randrange(u)))
            got=direct_orientations(n,edges);want=predicted(n,edges)
            assert got==want, ('sample',n,edges,got,want)
            sampled+=1
            if n<=8 and rep<12:
                assert direct_signed_switches(n,edges)==(want[0],want[1]//2)
                signed+=1
    print(f'VERIFY_OK exhaustive_unicyclic_graphs_n3_to6={exhaustive} '
          f'signed_switching_checks={signed} sampled_n7_to12={sampled}')

if __name__=='__main__': run()
