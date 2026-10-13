from itertools import combinations
from collections import deque

def crown(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj

def all_dist(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj)
        d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v] == 10**9:
                    d[v]=d[u]+1
                    q.append(v)
        D.append(d)
    return D

def is_multiset_resolving(D,S):
    reps=[]
    for v in range(len(D)):
        reps.append(tuple(sorted(D[v][s] for s in S)))
    return len(reps) == len(set(reps))

def predicted(n,S):
    if n >= 4:
        return False
    if n != 3:
        raise ValueError("verification domain starts at n=3")
    S=set(S)
    patterns=[]
    for i in range(3):
        patterns.append((int(i in S), int(3+i in S)))
    if len(S) != 3:
        return False
    return set(patterns) in (
        {(0,0),(1,0),(1,1)},
        {(0,0),(0,1),(1,1)},
    )

graphs=0
subsets=0
resolving_counts={}
for n in range(3,9):
    D=all_dist(crown(n))
    count=0
    by_size={}
    for mask in range(1<<(2*n)):
        S=[v for v in range(2*n) if (mask>>v)&1]
        actual=is_multiset_resolving(D,S)
        expect=predicted(n,S)
        assert actual == expect, (n,S,actual,expect)
        subsets += 1
        if actual:
            count += 1
            by_size[len(S)] = by_size.get(len(S),0)+1
    resolving_counts[n]=(count,by_size)
    graphs += 1

assert resolving_counts[3] == (12,{3:12})
for n in range(4,9):
    assert resolving_counts[n] == (0,{})

print("VERIFY_OK")
print("crown_graphs_checked =",graphs)
print("n_range = 3..8")
print("vertex_subsets_checked =",subsets)
print("Cr_3_resolving_sets = 12, all of size 3")
print("Cr_n_resolving_sets = 0 for n=4..8")
print("all direct distance-multiset tests matched the classification")
