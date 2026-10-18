#!/usr/bin/env python3
"""Exhaustive computational checks of parity-target orientation fibers on finite cacti."""
from collections import defaultdict
from itertools import product
from math import prod


def oriented_data(n, edges, cycles):
    # Edges are stored with ordered endpoints u,v; bit 0 means u->v, bit 1 v->u.
    buckets = defaultdict(list)
    for assignment in product((0,1), repeat=len(edges)):
        incoming = [0]*n
        oriented = set()
        for (u,v),reverse in zip(edges,assignment):
            a,b = (v,u) if reverse else (u,v)
            incoming[b]+=1
            oriented.add((a,b))
        parity = tuple(x%2 for x in incoming)
        directed = 0
        for cycle in cycles:
            forward = all((cycle[j], cycle[(j+1)%len(cycle)]) in oriented for j in range(len(cycle)))
            backward = all((cycle[(j+1)%len(cycle)],cycle[j]) in oriented for j in range(len(cycle)))
            directed += forward or backward
        buckets[parity].append(directed)
    return buckets


def check(n, edges, cycles, title):
    b = len(edges)-sum(len(x) for x in cycles)
    c = len(cycles)
    assert b>=0 and n==len(edges)-c+1
    signatures = oriented_data(n,edges,cycles)
    spectrum = defaultdict(int)
    for parity, ds in signatures.items():
        assert len(ds)==2**c, (title,parity,ds)
        assert len(set(ds))==1, (title,parity,ds)
        assert sum(parity)%2 == len(edges)%2
        spectrum[ds[0]] += 1
    target_poly = [0]*(c+1)
    for flags in product((0,1),repeat=c):
        i=sum(flags)
        weight=2**b
        for f,cycle in zip(flags,cycles):
            if not f: weight*=2**(len(cycle)-1)-1
        target_poly[i]+=weight
    actual=[spectrum.get(j,0) for j in range(c+1)]
    assert actual == target_poly,(title,actual,target_poly)
    assert sum(actual)==2**(n-1)
    print('PASS',title,'n',n,'edges',len(edges),'cycles',c,'parity target spectrum',actual)


def main():
    check(1,[],[],'single vertex')
    check(5,[(0,1),(1,2),(2,3),(3,4)],[],'five-vertex tree')
    for m in range(3,8):
        check(m,[(i,(i+1)%m) for i in range(m)],[list(range(m))],f'cycle {m}')
    check(5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)], [[0,1,2],[0,3,4]],'two triangles sharing hub')
    check(6,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)],[[0,1,2],[3,4,5]],'dumbbell triangles')
    check(7,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,5),(5,6),(6,3)],[[0,1,2],[3,4,5,6]],'triangle-square with bridge')
    check(8,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0),(0,5),(5,6),(6,7)],[[0,1,2],[0,3,4]],'two cycles with bridge tail')
    print('ALL CHECKS PASSED')
if __name__=='__main__':main()

# Exhaustive small-graph characterization cross-check, independent from
# the cycle-list oracle above: tests all connected labeled simple graphs on <=5 vertices.

def all_cycles(n, edges):
    edge_set={tuple(sorted(e)) for e in edges}
    found=set()
    # Generate simple cycles by root and ordered intermediate permutations.
    for k in range(3,n+1):
        for cyc in __import__('itertools').permutations(range(n),k):
            if cyc[0]!=min(cyc) or cyc[1]>cyc[-1]:continue
            if all(tuple(sorted((cyc[j],cyc[(j+1)%k]))) in edge_set for j in range(k)):
                found.add(frozenset(tuple(sorted((cyc[j],cyc[(j+1)%k]))) for j in range(k)))
    return found

def all_connected(n,edges):
    if n==1:return True
    seen={0};stack=[0];adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:seen.add(v);stack.append(v)
    return len(seen)==n

def is_acyclic(n, arcs):
    indeg=[0]*n;adj=[[] for _ in range(n)]
    for u,v in arcs: indeg[v]+=1;adj[u].append(v)
    stack=[v for v in range(n) if indeg[v]==0];cnt=0
    while stack:
        u=stack.pop();cnt+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:stack.append(v)
    return cnt==n

def exhaustive_classification():
    from itertools import combinations
    total=0;cactus=0;noncactus=0
    for n in range(1,6):
        all_edges=list(combinations(range(n),2))
        for mask in range(1<<len(all_edges)):
            edges=[e for i,e in enumerate(all_edges) if mask>>i&1]
            if not all_connected(n,edges):continue
            cs=all_cycles(n,edges)
            uses=defaultdict(int)
            for c in cs:
                for e in c: uses[e]+=1
            cactus_flag=all(v<=1 for v in uses.values())
            buckets=defaultdict(set)
            for omask in range(1<<len(edges)):
                arcs=[(v,u) if omask>>i&1 else (u,v) for i,(u,v) in enumerate(edges)]
                indeg=[0]*n
                for u,v in arcs:indeg[v]^=1
                buckets[tuple(indeg)].add(is_acyclic(n,arcs))
            invariant=all(len(x)==1 for x in buckets.values())
            assert invariant==cactus_flag,(n,edges,invariant,cactus_flag)
            total+=1;cactus+=cactus_flag;noncactus+=not cactus_flag
    print('CHARACTERIZATION ALL PASS',total,'connected graphs',cactus,'cacti',noncactus,'non-cacti (orders <=5)')

if __name__=='__main__': exhaustive_classification()
