#!/usr/bin/env python3
from collections import deque

def dist_matrix(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    d=[[99]*N for _ in range(N)]
    for s in range(N):
        d[s][s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[s][v]>d[s][u]+1:
                    d[s][v]=d[s][u]+1; q.append(v)
    return d

def ok(parts,d):
    for P in parts:
        if len(P)<2: continue
        for ii,x in enumerate(P):
            for y in P[ii+1:]:
                delta=d[x][y]
                good=False
                for W in parts:
                    if W is P: continue
                    dx=min(d[x][w] for w in W)
                    dy=min(d[y][w] for w in W)
                    if dx==delta+dy or dy==delta+dx:
                        good=True; break
                if not good: return False
    return True

def construction(n):
    # a_i = i-1, b_i=n+i-1
    return [list(range(0,n-1))+[2*n-1], [n-1,n]] + [[n+i-1] for i in range(2,n)]

def partitions_k(N,k):
    a=[0]*N
    def rec(pos,mx):
        if pos==N:
            if mx==k-1:
                parts=[[] for _ in range(k)]
                for v,c in enumerate(a): parts[c].append(v)
                yield parts
            return
        for c in range(min(mx+1,k-1)+1):
            a[pos]=c
            yield from rec(pos+1,max(mx,c))
    yield from rec(1,0)

checks=0
for n in range(3,13):
    d=dist_matrix(n)
    P=construction(n)
    assert len(P)==n and sorted(v for X in P for v in X)==list(range(2*n))
    assert ok(P,d)
    checks += 1

# Exhaustive finite stress test through n=5: no partition with fewer than n parts,
# and at least one n-part strong resolving partition exists.
partitions_tested=0
for n in range(3,6):
    d=dist_matrix(n)
    for k in range(2,n):
        for P in partitions_k(2*n,k):
            partitions_tested += 1
            assert not ok(P,d), (n,k,P)
    found=False
    for P in partitions_k(2*n,n):
        partitions_tested += 1
        if ok(P,d):
            found=True; break
    assert found
print(f'VERIFY_OK construction_n=3..12 exhaustive_n=3..5 partitions_tested={partitions_tested} construction_checks={checks}')
