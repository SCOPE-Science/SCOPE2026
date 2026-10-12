#!/usr/bin/env python3
"""Independent minimum-cost-flow verification on run-limited overlap graphs.

For each n this computes shortest source-to-sink path distances by BFS
and the minimum assignment cost by the Hungarian algorithm (not via
construct.py). This certifies optimum extra-arc cost independently.
"""
from collections import deque


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def valid(w):
    return all(w[i:i+3] not in ('000', '111') for i in range(len(w)-2))


def solve(n):
    m = n-1
    words = [format(i, '0%db' % m) for i in range(1<<m)]
    words = [w for w in words if valid(w)]
    adjacency = {w: [] for w in words}
    pred = {w: [] for w in words}
    for w in words:
        for b in '01':
            if valid(w+b):
                nxt = w[1:]+b
                adjacency[w].append(nxt)
                pred[nxt].append(w)
    src = sorted(w for w in words if len(pred[w])-len(adjacency[w]) == 1)
    dst = sorted(w for w in words if len(adjacency[w])-len(pred[w]) == 1)
    assert len(src)==len(dst)
    if not src:
        return 0,0
    N=len(src)
    costs=[]
    for start in src:
        dist={start:0}
        Q=deque([start])
        while Q:
            v=Q.popleft()
            for u in adjacency[v]:
                if u not in dist:
                    dist[u]=dist[v]+1
                    Q.append(u)
        costs.append([dist[t] for t in dst])
    # Standard independent Hungarian implementation for rectangular assignment.
    u=[0]*(N+1)
    v=[0]*(N+1)
    p=[0]*(N+1)
    way=[0]*(N+1)
    for i in range(1,N+1):
        p[0]=i
        j0=0
        minv=[10**9]*(N+1)
        used=[False]*(N+1)
        while True:
            used[j0]=True
            i0=p[j0]
            delta=10**9
            j1=0
            for j in range(1,N+1):
                if not used[j]:
                    cur=costs[i0-1][j-1]-u[i0]-v[j]
                    if cur<minv[j]:
                        minv[j]=cur
                        way[j]=j0
                    if minv[j]<delta:
                        delta=minv[j]
                        j1=j
            for j in range(N+1):
                if used[j]:
                    u[p[j]]+=delta
                    v[j]-=delta
                else:
                    minv[j]-=delta
            j0=j1
            if p[j0]==0:
                break
        while True:
            j1=way[j0]
            p[j0]=p[j1]
            j0=j1
            if j0==0:
                break
    chosen = [(p[j]-1,j-1) for j in range(1,N+1)]
    actual=sum(costs[i][j] for i,j in chosen)
    structural=sum(next(i for i in range(1,m-1) if s[i]==s[i+1]) for s in src)
    assert actual==structural==2*fib(n-1)-2, (n,actual,structural)
    return actual,N

if __name__=='__main__':
    for n in range(3,14):
        cost,source_count=solve(n)
        print('n=%d independent_extra_cost=%d independent_sources=%d' % (n,cost,source_count))
    print('VERIFY_OK')
