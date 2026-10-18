#!/usr/bin/env python3
"""Independent enumeration of maximal independent sets and slide graphs of cycles.
No external modules needed; all state transitions are independently tested.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def is_maximal_independent(state, n):
    s=set(state)
    return all((u+1)%n not in s for u in s) and all(
        v in s or (v-1)%n in s or (v+1)%n in s for v in range(n))


def expected(n,k):
    t=n-2*k
    if t==0:
        return (2,0,Counter({0:2}),2)
    total=n*comb(k,t)//k
    edges=n*comb(k-2,t-1)
    degrees=Counter({2*r:n*comb(t-1,r-1)*comb(k-t-1,r-1)//r
                     for r in range(1,min(t,k-t)+1)})
    return (total,edges,degrees,1)


def verify(n,k):
    states=[z for z in combinations(range(n),k) if is_maximal_independent(z,n)]
    lookup={state:i for i,state in enumerate(states)}
    adj=[set() for _ in states]
    for idx,s in enumerate(states):
        occ=set(s)
        for u in s:
            for v in ((u-1)%n,(u+1)%n):
                if v in occ:continue
                nxt=tuple(sorted((occ-{u})|{v}))
                j=lookup.get(nxt)
                if j is not None: adj[idx].add(j)
    assert all(i in adj[j] for i,near in enumerate(adj) for j in near)
    total=len(states)
    edges=sum(len(near) for near in adj)//2
    degree=Counter(map(len,adj))
    seen=set();comp=[];bip=True
    for i in range(total):
        if i in seen:continue
        color={i:0};queue=deque([i]);seen.add(i)
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if v in color:
                    if color[v]==color[u]:bip=False
                else:
                    color[v]=1-color[u];queue.append(v);seen.add(v)
        comp.append(len(color))
    exp=expected(n,k)
    assert (total,edges,degree,len(comp))==exp, (n,k,(total,edges,degree,len(comp)),exp)
    assert bip == (n%2==0 or n==2*k)
    # For odd n, certified direct odd-girth lower bound uses the modular sum invariant.
    # This algorithm computes odd-girth independently via a BFS from every vertex
    # for graphs with at most 100 vertices.
    if n%2 and total <=100:
        oddgirth=10**9
        for root in range(total):
            dist={root:0};q=deque([root])
            while q:
                u=q.popleft()
                for v in adj[u]:
                    if v in dist:
                        if (dist[u]+dist[v]+1)%2:
                            oddgirth=min(oddgirth,dist[u]+dist[v]+1)
                    else:
                        dist[v]=dist[u]+1;q.append(v)
        assert oddgirth==n,(n,k,oddgirth)
    return f'n={n} k={k} t={n-2*k} states={total} edges={edges} degrees={sorted(degree.items())} components={sorted(comp)} bipartite={bip}'

if __name__=='__main__':
    count=0
    for n in range(8,21):
        for k in range((n+2)//3+1,n//2+1):
            print(verify(n,k));count+=1
    print(f'REPLAY_OK brute pairs={count}')
