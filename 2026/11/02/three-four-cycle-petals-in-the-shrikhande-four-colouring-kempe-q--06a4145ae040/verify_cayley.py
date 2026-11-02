#!/usr/bin/env python3
"""Exact standard-library verification of Shrikhande 4-colouring Kempe geometry."""
from itertools import combinations, permutations, product
from collections import Counter, deque

V = list(product(range(4), repeat=2))
D = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
N = [set() for _ in range(16)]
for a,b in combinations(range(16),2):
    u,v=V[a],V[b]
    if ((u[0]-v[0])%4,(u[1]-v[1])%4) in D:
        N[a].add(b);N[b].add(a)
assert all(len(z)==6 for z in N) and sum(map(len,N))==96

# Enumerate all independent four-sets, then exact covers by four such sets.
I4 = [sum(1<<v for v in t) for t in combinations(range(16),4)
      if all(v not in N[u] for u,v in combinations(t,2))]
assert len(I4)==16
assert not any(all(v not in N[u] for u,v in combinations(t,2)) for t in combinations(range(16),5))
I4.sort()
partitions=set()
def cover(rem, chosen):
    if not rem:
        assert len(chosen)==4
        partitions.add(tuple(sorted(chosen)))
        return
    v=(rem&-rem).bit_length()-1
    for c in I4:
        if c&(1<<v) and c&rem==c:
            cover(rem^c,chosen+[c])
cover((1<<16)-1,[])
assert len(partitions)==10

# All proper named 4-colourings. Minimality follows from independence bound 4.
colourings=set()
for p in partitions:
    for ordered in permutations(p):
        colourings.add(tuple(next(c for c,m in enumerate(ordered) if m>>v&1)
                             for v in range(16)))
C=sorted(colourings);assert len(C)==240
index={x:i for i,x in enumerate(C)}

# Full Kempe graph: switch one connected component of the two-colour subgraph.
A=[set() for _ in C]
for i,c in enumerate(C):
    for a,b in combinations(range(4),2):
        left={v for v in range(16) if c[v] in (a,b)}
        while left:
            root=min(left);q=[root];component={root};left.remove(root)
            for x in q:
                for y in N[x]&left:
                    left.remove(y);component.add(y);q.append(y)
            d=list(c)
            for x in component:d[x]=a+b-d[x]
            j=index[tuple(d)]
            if i!=j:A[i].add(j)
assert all(i in A[j] for j in range(240) for i in A[j])
assert sum(map(len,A))//2==1008
assert Counter(map(len,A))=={8:216,12:24}

# Exact pair-distance profile and eccentricity classes.
ecc=[];hist=Counter()
for i in range(240):
    dist={i:0};q=deque([i])
    while q:
        x=q.popleft()
        for y in A[x]:
            if y not in dist:dist[y]=dist[x]+1;q.append(y)
    assert len(dist)==240
    ecc.append(max(dist.values()))
    for j,d in dist.items():
        if i<j:hist[d]+=1
assert Counter(ecc)=={4:168,5:72}
assert hist=={1:1008,2:5400,3:13416,4:8280,5:576}

# Quotient modulo all permutations of colour names.
partition_of=lambda c:tuple(sorted(sum(1<<v for v,x in enumerate(c) if x==k) for k in range(4)))
P=sorted(partitions);qi={p:i for i,p in enumerate(P)}
Q=[set() for _ in P]
for i,c in enumerate(C):
    a=qi[partition_of(c)]
    for j in A[i]:
        b=qi[partition_of(C[j])]
        if a!=b:Q[a].add(b)
assert all(a in Q[b] for b in range(10) for a in Q[b])
assert Counter(map(len,Q))=={2:9,6:1}
assert sum(map(len,Q))//2==12
center=next(i for i in range(10) if len(Q[i])==6)
# Every connected component after deleting center is a three-vertex path.
remaining=set(range(10))-{center}
while remaining:
    root=min(remaining);seen={root};stack=[root]
    for x in stack:
        for y in Q[x]&remaining:
            if y not in seen:seen.add(y);stack.append(y)
    assert len(seen)==3
    assert Counter(len(Q[v]&seen) for v in seen)=={1:2,2:1}
    assert len(Q[center]&seen)==2
    remaining-=seen
print('CAYLEY_KEMPE_PASS')
print('independent4=16 partitions=10 named4=240')
print('named_edges=1008 radius=4 diameter=5 eccentricities=168x4+72x5')
print('distance_histogram=1008,5400,13416,8280,576')
print('quotient=three_C4_sharing_one_vertex')
