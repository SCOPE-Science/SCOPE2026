#!/usr/bin/env python3
"""Independent enumeration of 4-cycles in derangement-position-transposition graph."""
from itertools import permutations, combinations
from collections import Counter
from math import factorial,comb

def count(n):
    perms=[p for p in permutations(range(n)) if all(p[i]!=i for i in range(n))]
    index={p:i for i,p in enumerate(perms)}
    links=[{} for _ in perms]
    for u,p in enumerate(perms):
        for i,j in combinations(range(n),2):
            q=list(p);q[i],q[j]=q[j],q[i];v=index.get(tuple(q))
            if v is not None:links[u][v]=(i,j)
    # Each 4-cycle has two diagonal pairs. Enumerate all unordered pairs of
    # opposite vertices, then pairs of common neighbours, deduplicate cycles.
    cycles=set()
    for u in range(len(perms)):
        paths=Counter(w for v in links[u] for w in links[v] if w>u)
        for w,mult in paths.items():
            if mult<2:continue
            shared=sorted(set(links[u]).intersection(links[w]))
            for v,z in combinations(shared,2):
                cycles.add(tuple(sorted((u,v,w,z))))
    types=Counter()
    for sq in cycles:
        swaps={links[u][v] for u,v in combinations(sq,2) if v in links[u]}
        support=set().union(*(set(ab) for ab in swaps))
        assert len(support) in (3,4)
        types[len(support)]+=1
    assert sum(map(len,links))%2==0
    # Exact tr(A^4) as a sum of squared two-step walk counts,
    # computed from the full adjacency list rather than the 4-cycle formula.
    trace4=0
    for u in range(len(perms)):
        two_walks=Counter(z for v in links[u] for z in links[v])
        trace4+=sum(v*v for v in two_walks.values())
    b=comb(n,2)-n
    def D(k):return sum((-1)**i*comb(k,i)*factorial(k-i) for i in range(k+1))
    m=(b*D(n)+comb(n,2)*D(n-2))//2
    wedge=D(n)*comb(b,2)+b*comb(n,2)*D(n-2)+3*comb(n,4)*D(n-4)
    assert trace4==2*m+4*wedge+8*len(cycles)
    # sign partition imbalance = (-1)^(n-1)(n-1)
    def parity(p):return sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2
    parity_counts=Counter(parity(p) for p in perms)
    assert parity_counts[0]-parity_counts[1]==(-1)**(n-1)*(n-1)
    return len(perms),sum(map(len,links))//2,types[3],types[4],trace4

for n in range(4,8):
    print(n,*count(n),flush=True)
