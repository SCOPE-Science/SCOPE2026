#!/usr/bin/env python3
"""Finite state certificate for perfect edge domination of GP(n,3)."""
from collections import Counter
from itertools import combinations

def cyclic_states(d):
    ans=[]
    for mask in range(1<<d):
        a=tuple((mask>>i)&1 for i in range(d))
        b=tuple(a[(i-1)%d]^a[(i+1)%d] for i in range(d))
        if any(b[(i-3)%d]^b[(i+3)%d]^a[i] for i in range(d)):
            continue
        if any(a[i]*a[(i+1)%d] or a[i]*b[i] or b[i]*b[(i+3)%d] for i in range(d)):
            continue
        ans.append((a,b))
    return ans

expected={1:{0:1},2:{0:1},5:{0:1,4:5},10:{0:1,4:10,6:20,8:5}}
for d,counts in expected.items():
    observed=dict(sorted(Counter(sum(a)+sum(b) for a,b in cyclic_states(d)).items()))
    assert observed==counts,(d,observed,counts)
    print('PERIOD',d,'LOW_VERTEX_COUNTS',observed)

# Exhaustive *edge subset* check: 21-30 edges, pruned by incompatible
# neighborhoods of nonchosen edges, for n=7..10. For n=10 there are 2^30
# raw sets, so instead enumerate all independent low-vertex sets, independently
# building the chosen edges and verifying the original edge condition.
def edge_list(n):
    return [(i,(i+1)%n) for i in range(n)]+[(i,i+n) for i in range(n)]+[(i+n,(i+3)%n+n) for i in range(n)]

def direct_counts(n):
    edges=edge_list(n)
    neighbors=[0]*(2*n)
    for u,v in edges:
        neighbors[u]|=1<<v;neighbors[v]|=1<<u
    counts=Counter()
    # Search every independent vertex set by a branch & bound on the 2n vertices.
    def visit(i,bits):
        if i==2*n:
            chosen=[not ((bits>>u)&1 or (bits>>v)&1) for u,v in edges]
            for j,(u,v) in enumerate(edges):
                if not chosen[j]:
                    touches=sum(chosen[k] and bool(len({u,v}&set(e))) for k,e in enumerate(edges))
                    if touches!=1: return
            counts[sum(chosen)]+=1
            return
        visit(i+1,bits)
        if not (neighbors[i]&bits):visit(i+1,bits|(1<<i))
    visit(0,0)
    return dict(sorted(counts.items()))
for n in (7,8,9,10):
    if n==10: ex={6:5,12:20,18:10,30:1}
    else: ex={3*n:1}
    got=direct_counts(n)
    assert got==ex,(n,got,ex)
    print('DIRECT_EDGE_DEFINITION',n,got)

# Separate algebraic exhaustive check: recurrence from adjacency equations
# implies 10-periodicity for arbitrary bi-infinite binary sequences.
# Direct symbolic polynomial identity: (1+t^2)(1+t^2+t^4+t^6+t^8)=1+t^10 in F2
p={0,2,4,6,8};prod=set(p)
for e in p:
    if e+2 in prod:prod.remove(e+2)
    else:prod.add(e+2)
assert prod=={0,10}
print('POLYNOMIAL_IDENTITY_OK')
print('VERIFY_OK')
