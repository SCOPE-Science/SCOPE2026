#!/usr/bin/env python3
"""Deterministic constructive checks for cyclic length-four palindrome covers."""
from collections import defaultdict, deque


def eulerian_tour(q):
    assert q >= 2
    edges = [(a,b) for a in range(q) for b in range(a+1,q)]
    if q % 2 == 0:
        edges += [(a,a+1) for a in range(0,q,2)]
    adj = [[] for _ in range(q)]
    for i,(a,b) in enumerate(edges):
        adj[a].append((b,i))
        adj[b].append((a,i))
    used = [False] * len(edges)
    stack=[0]; path=[]
    while stack:
        v=stack[-1]
        while adj[v] and used[adj[v][-1][1]]:adj[v].pop()
        if not adj[v]:
            path.append(stack.pop())
        else:
            u,i=adj[v].pop()
            used[i]=True
            stack.append(u)
    path=path[::-1]
    assert len(path)==len(edges)+1 and path[0]==path[-1] and all(used)
    return path


def construction(q):
    path=eulerian_tour(q)
    first=set(); runs=[]
    for u,v in zip(path,path[1:]):
        runs.append([u,False]) # original Euler-tour vertex
        key=tuple(sorted((u,v)))
        if key not in first:
            first.add(key)
            runs.append([v,True])
            runs.append([u,True])
    assert len(first)==q*(q-1)//2
    assert all(runs[i][0] != runs[(i+1)%len(runs)][0] for i in range(len(runs)))
    seenlong=set(); out=[]; runlengths=[]
    for a,inserted in runs:
        if inserted: L=2
        elif a not in seenlong:
            seenlong.add(a);L=4
        else:L=1
        out.extend([a]*L)
        runlengths.append(L)
    assert len(seenlong)==q
    return out,runs,runlengths


def cyclic_factors(w,k):
    n=len(w)
    return {tuple(w[(i+j)%n] for j in range(k)) for i in range(n)}


def verify(q):
    w,runs,lengths=construction(q)
    bound=(5*q*q+q)//2 + (q//2 if q%2==0 else 0)
    assert len(w)==bound,(q,len(w),bound)
    targets={(a,b,b,a) for a in range(q) for b in range(q)}
    assert targets <= cyclic_factors(w,4)
    assert len(runs)==3*q*(q-1)//2+(q//2 if q%2==0 else 0)
    assert lengths.count(4)==q and lengths.count(2)==q*(q-1)
    assert all(length in (1,2,4) for length in lengths)
    return bound


def exact_bfs(q):
    """Independent shortest-cover BFS; feasible for q=2,3."""
    assert q in (2,3)
    goal=(1<<(q*q))-1
    best=None
    initial=[(a*q+b)*q+c for a in range(q) for b in range(q) for c in range(q)]
    for seed in initial:
        qd=deque([(seed,0)])
        dist={(seed,0):0}
        while qd:
            state,mask=qd.popleft()
            d=dist[(state,mask)]
            if best is not None and d>=best:continue
            a=state//(q*q);b=(state//q)%q;c=state%q
            for x in range(q):
                t=(b*q+c)*q+x
                newmask=mask | (1<<(a*q+b) if a==x and b==c else 0)
                if t==seed and newmask==goal:
                    best=d+1 if best is None else min(best,d+1)
                key=t,newmask
                if key not in dist:
                    dist[key]=d+1
                    qd.append(key)
    return best


def main():
    for q in range(2,51):
        verify(q)
    # Full circular-word BFS, separate from Eulerian construction.
    for q in (2,3):
        observed=exact_bfs(q)
        assert observed == verify(q), (q,observed,verify(q))
    print('VERIFY_OK: all constructed q=2..50, exact BFS q=2,3; bounds 12,24,44,65,96')
if __name__=='__main__':main()
