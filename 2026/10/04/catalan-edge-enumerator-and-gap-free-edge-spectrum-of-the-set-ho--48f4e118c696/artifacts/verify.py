#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial
from collections import Counter

# A full plane binary tree is either a leaf None or a pair (left,right).
@lru_cache(None)
def trees(n):
    if n == 1:
        return (None,)
    out=[]
    for i in range(1,n):
        for L in trees(i):
            for R in trees(n-i):
                out.append((L,R))
    return tuple(out)

def leaf_paths(T, prefix=()):
    if T is None:
        return [prefix]
    L,R=T
    return leaf_paths(L,prefix+(0,))+leaf_paths(R,prefix+(1,))

def lcp(a,b):
    k=0
    while k < min(len(a),len(b)) and a[k]==b[k]:
        k+=1
    return k

def edge_set(T):
    paths=leaf_paths(T)
    n=len(paths)
    E=set()
    # For i<j<k, M_3 has an edge iff C(i;j,k), i.e. j,k coalesce deeper.
    for i,j,k in combinations(range(n),3):
        if lcp(paths[j],paths[k]) > lcp(paths[i],paths[j]):
            E.add((i,j,k))
    return E

def edge_count(T):
    return len(edge_set(T))

def recursive_count(T):
    if T is None:
        return 0
    L,R=T
    i=len(leaf_paths(L)); j=len(leaf_paths(R))
    return recursive_count(L)+recursive_count(R)+i*comb(j,2)

def catalan(m):
    return comb(2*m,m)//(m+1)

def poly_recurrence(N):
    P=[Counter() for _ in range(N+1)]
    P[1][0]=1
    for n in range(2,N+1):
        for i in range(1,n):
            shift=i*comb(n-i,2)
            for a,ca in P[i].items():
                for b,cb in P[n-i].items():
                    P[n][a+b+shift]+=ca*cb
    return P

def canonical_hypergraph(n,E):
    triples=list(combinations(range(n),3))
    pos={t:i for i,t in enumerate(triples)}
    best=None
    for p in permutations(range(n)):
        mask=0
        for t in E:
            u=tuple(sorted(p[x] for x in t))
            mask |= 1 << pos[u]
        if best is None or mask < best:
            best=mask
    return best

N=10
P=poly_recurrence(N)
for n in range(1,N+1):
    direct=Counter(edge_count(T) for T in trees(n))
    assert direct==P[n], (n,direct,P[n])
    assert len(trees(n))==catalan(n-1)
    assert sum(P[n].values())==catalan(n-1)
    for T in trees(n):
        assert edge_count(T)==recursive_count(T)
    total=comb(n,3)
    for e,c in P[n].items():
        assert P[n][total-e]==c

# Direct finite isomorphism check through six vertices: distinct plane-tree
# types really yield distinct unlabelled 3-hypergraphs in this range.
for n in range(1,7):
    can={canonical_hypergraph(n,edge_set(T)) for T in trees(n)}
    assert len(can)==catalan(n-1), (n,len(can),catalan(n-1))

# Edge-count spectra: the five-point midpoint is the unique finite gap,
# and from six vertices onward every possible edge count occurs (checked
# computationally here through n=10; RESULT.md gives the induction proof).
assert set(P[5])==set(range(11))-{5}
for n in range(6,N+1):
    assert set(P[n])==set(range(comb(n,3)+1)), n

# Paper's Figure 3 statement: the five four-vertex types have 0,...,4 edges.
assert P[4]==Counter({0:1,1:1,2:1,3:1,4:1})

# Injective ordered-tuple orbit count corollary.
orb=[]
for n in range(1,9):
    orb.append(factorial(n)*catalan(n-1))
assert orb==[1,2,12,120,1680,30240,665280,17297280]

print('age_counts_n1_to_10', [sum(P[n].values()) for n in range(1,11)])
print('P4', sorted(P[4].items()))
print('P5', sorted(P[5].items()))
print('P6_support', (min(P[6]), max(P[6]), len(P[6])))
print('injective_orbits_n1_to_8', orb)
print('VERIFY_OK')
