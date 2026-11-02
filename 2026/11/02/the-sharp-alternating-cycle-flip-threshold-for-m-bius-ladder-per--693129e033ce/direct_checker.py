#!/usr/bin/env python3
"""Finite independent enumeration of perfect matchings and cycle-flip thresholds.
All checks are on labelled undirected graphs; no results are inferred from timeouts.
"""
from collections import Counter, deque


def construct(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for v in range(N):
        for u in ((v+1)%N, (v+n)%N):
            adj[v].add(u);adj[u].add(v)
    return adj

def perfect_matchings(adj):
    N=len(adj)
    results=[]
    def go(mask,chosen):
        if not mask:
            results.append(frozenset(chosen));return
        a=(mask&-mask).bit_length()-1
        for b in sorted(adj[a]):
            if mask&(1<<b):
                e=(min(a,b),max(a,b))
                go(mask ^ (1<<a) ^ (1<<b), chosen+[e])
    go((1<<N)-1,[])
    return results

def one_cycle_difference(A,B):
    sym=A^B
    if not sym:return 0
    neigh={}
    for a,b in sym:
        neigh.setdefault(a,[]).append(b)
        neigh.setdefault(b,[]).append(a)
    if any(len(v)!=2 for v in neigh.values()):return 0
    seen=set();todo=[next(iter(neigh))]
    while todo:
        v=todo.pop()
        if v in seen:continue
        seen.add(v);todo.extend(neigh[v])
    if len(seen)!=len(neigh):return 0
    return len(sym)

def components(adj):
    seen=set();out=[]
    for a in range(len(adj)):
        if a in seen:continue
        q=[a];seen.add(a)
        for v in q:
            for w in adj[v]:
                if w not in seen:seen.add(w);q.append(w)
        out.append(q)
    return sorted(map(len,out))

def lucas(n):
    return sum(1 for x in range(1<<n) if all(not((x>>i&1) and (x>>((i+1)%n)&1)) for i in range(n)))

def run():
    for n in range(4,14):
        A=perfect_matchings(construct(n)); total=len(A)
        assert total==lucas(n)+(2 if n%2 else 0),(n,total)
        ex=[i for i,M in enumerate(A) if all(b-a!=n for a,b in M)]
        assert len(ex)==2
        edg4=[set() for _ in A];edgcut=[set() for _ in A]
        edges_at_threshold=0
        for a in range(total):
            for b in range(a+1,total):
                size=one_cycle_difference(A[a],A[b])
                if size==4:edg4[a].add(b);edg4[b].add(a)
                threshold=(n+1 if n%2 else 4)
                if size and size<=threshold:
                    edgcut[a].add(b);edgcut[b].add(a)
                    if n%2 and size==n+1 and (a in ex or b in ex): edges_at_threshold+=1
        expected=sorted([1,1,lucas(n)]) if n%2 else [lucas(n)]
        assert components(edg4)==expected,(n,components(edg4),expected)
        assert components(edgcut)==[total]
        if n%2:
            assert all(len(edg4[i])==0 for i in ex)
            assert all(len(edgcut[i])==n for i in ex)
            assert edges_at_threshold==2*n
            # These extreme configurations have no alternating cycle of odd rung
            # count below n+1 by checking all one-cycle differences.
            for i in ex:
                assert all(one_cycle_difference(A[i],A[j])==0 or one_cycle_difference(A[i],A[j])>=n+1 for j in range(total) if i!=j)
        print('n=',n,'matchings=',total,'square_components=',expected,'full_threshold=',(n+1 if n%2 else 4),'exception_bridges=',edges_at_threshold)
    print('MOBIUS_DIRECT_EXHAUSTIVE_PASS')
if __name__=='__main__':run()
