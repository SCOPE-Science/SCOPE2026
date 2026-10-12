#!/usr/bin/env python3
from collections import deque
from math import comb

def a(n,S):
    return frozenset((x+1)%n for x in S)

def b(n,S):
    return frozenset(0 if x==n-1 else x for x in S)

def rank_formula(n,S):
    S=tuple(sorted(S))
    if len(S)==1:
        return 0
    i,j=S
    g=j-i
    return min(g*n-i,(n-g)*n-j)

def canonical(n,S):
    i,j=sorted(S)
    g=j-i
    if g < n-g:
        return g,i
    return n-g,j

def reverse_bfs_distances(n):
    nodes=[frozenset([i]) for i in range(n)]
    nodes += [frozenset([i,j]) for i in range(n) for j in range(i+1,n)]
    idx={S:k for k,S in enumerate(nodes)}
    rev=[[] for _ in nodes]
    for S in nodes:
        u=idx[S]
        for f in (a,b):
            T=f(n,S)
            rev[idx[T]].append(u)
    dist=[None]*len(nodes)
    q=deque()
    for i in range(n):
        k=idx[frozenset([i])]
        dist[k]=0
        q.append(k)
    while q:
        v=q.popleft()
        for u in rev[v]:
            if dist[u] is None:
                dist[u]=dist[v]+1
                q.append(u)
    return {S:dist[k] for S,k in idx.items()}

checked=0
for n in range(2,81):
    distances=reverse_bfs_distances(n)
    weights=[]
    for i in range(n):
        for j in range(i+1,n):
            S=frozenset([i,j])
            D=rank_formula(n,S)
            r,x=canonical(n,S)
            assert D==(r-1)*n+(n-x)
            assert distances[S]==D, (n,S,distances[S],D)
            # Every letter lowers the rank by at most one.
            assert rank_formula(n,a(n,S)) >= D-1
            assert rank_formula(n,b(n,S)) >= D-1
            # At least one letter realizes the unit drop.
            assert min(rank_formula(n,a(n,S)),rank_formula(n,b(n,S))) == D-1
            weights.append(D)
            checked += 1
    C=comb(n,2)
    assert sorted(weights)==list(range(1,C+1))
    assert max(weights)==C
    assert sum(weights)*2 == C*(C+1)
    # The unique hardest pair in this labeling.
    hard=[S for S,d in distances.items() if len(S)==2 and d==C]
    assert hard==[frozenset([0,n//2])], (n,hard)

print(
    "VERIFY_OK "
    f"n=2..80 pairs={checked} "
    "reverse_BFS_matches_formula "
    "rank_drop_bound "
    "spectrum=1..binom(n,2) "
    "unique_hardest_pair"
)
