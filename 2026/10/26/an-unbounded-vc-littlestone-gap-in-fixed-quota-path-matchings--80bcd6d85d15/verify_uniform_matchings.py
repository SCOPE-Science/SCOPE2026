#!/usr/bin/env python3
"""Exact finite certificates for three-edge matching incidence on an eight-vertex path."""
from functools import lru_cache
from itertools import combinations, product


def concepts(num_edges, rank):
    return [tuple(q) for q in combinations(range(num_edges),rank)
            if all(q[j+1] > q[j]+1 for j in range(rank-1))]


def vc_dimension(num_edges, family):
    value=0
    for k in range(num_edges+1):
        for indices in combinations(range(num_edges), k):
            traces={tuple(int(i in F) for i in indices) for F in family}
            if len(traces)==2**k:
                value=k
    return value


def littlestone_dimension(num_edges, family):
    signatures=[sum(1<<j for j,F in enumerate(family) if i in F)
                for i in range(num_edges)]
    @lru_cache(None)
    def go(state):
        if state.bit_count()<2:return 0
        result=0
        for signature in signatures:
            one=state & signature
            zero=state & ~signature
            if one and zero:
                result=max(result,1+min(go(one),go(zero)))
        return result
    return go((1<<len(family))-1)

# Query labels for depth 3, indexed by preceding feedback (0/1).
TREE={():0,(0,):3,(1,):2,(0,0):1,(0,1):5,(1,0):3,(1,1):4}
WITNESSES={
    (0,0,0):(2,4,6),(0,0,1):(1,4,6),
    (0,1,0):(1,3,6),(0,1,1):(1,3,5),
    (1,0,0):(0,4,6),(1,0,1):(0,3,5),
    (1,1,0):(0,2,5),(1,1,1):(0,2,4)
}
MISSING={
    (0,2,4):(0,1,0),(0,2,5):(0,1,1),
    (0,2,6):(0,1,0),(0,3,5):(0,0,1),
    (0,3,6):(0,0,0),(0,4,6):(0,1,0),
    (1,3,5):(1,0,1),(1,3,6):(1,0,0),
    (1,4,6):(1,1,0),(2,4,6):(0,1,0)
}
F=concepts(7,3)
assert len(F)==10 and set(F)==set(MISSING)
for bits,matching in WITNESSES.items():
    assert matching in F
    for depth in range(3):
        assert int(TREE[bits[:depth]] in matching)==bits[depth]
for query,missing in MISSING.items():
    traces={tuple(int(i in M) for i in query) for M in F}
    assert missing not in traces and (1,1,1) in traces
assert vc_dimension(7,F)==2
assert littlestone_dimension(7,F)==3
print('P8 base: 10 rank-three matchings, VC=2, Ldim=3')
print('Eight complete adaptive branch certificates: PASS')
print('Ten exhaustive candidate VC-triple obstructions: PASS')
for n in range(1,7):
    for rank in range(0,(n+1)//2+1):
        Fsmall=concepts(n,rank)
        if not Fsmall:continue
        vc=vc_dimension(n,Fsmall)
        ld=littlestone_dimension(n,Fsmall)
        assert ld<3, (n,rank,vc,ld)
print('Minimality: every fixed-cardinality matching class on a path with at most six edges has Ldim<=2: PASS')
# For disjoint query domains, the product class has additive VC and Ldim.
# Here the exact base dimensions are used in the proven additivity lemma.
for s in (1,2,3,4,10):
    print(f'{s} components: VC={2*s}, Ldim={3*s} (by direct-product lemma)')
print('ALL_MATCHING_CHECKS_PASS')
