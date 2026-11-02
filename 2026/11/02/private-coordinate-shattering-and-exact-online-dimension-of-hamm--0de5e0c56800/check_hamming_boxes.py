#!/usr/bin/env python3
"""Reproducibility checks for finite Cartesian-box concepts on Hamming graphs.

No external packages; executes independent graph-distance and finite-concept tests.
Finite tests are not proofs for unrestricted alphabet sizes or dimension.
"""
from functools import lru_cache
from itertools import product
from math import prod


def instance(shape):
    pts=list(product(*(range(n) for n in shape)))
    concepts={0}
    for sides in product(*(range(1,1<<n) for n in shape)):
        bits=0
        for index,pt in enumerate(pts):
            if all((sides[i]>>pt[i])&1 for i in range(len(shape))):
                bits|=1<<index
        concepts.add(bits)
    return pts,tuple(sorted(concepts))


def private_support(shape,pts,sm):
    selected=[pt for idx,pt in enumerate(pts) if (sm>>idx)&1]
    for pt in selected:
        if not any(sum(other[i]==pt[i] for other in selected)==1 for i in range(len(shape))):
            return False
    return True


def independent_convexity(shape,pts,S):
    """All-pairs, all-shortest-path criterion, independent of box generation."""
    chosen=[i for i in range(len(pts)) if S>>i&1]
    for a in chosen:
        for b in chosen:
            dist=sum(pts[a][i]!=pts[b][i] for i in range(len(shape)))
            for z,p in enumerate(pts):
                if S>>z&1:continue
                if (sum(pts[a][i]!=p[i] for i in range(len(shape)))
                  + sum(p[i]!=pts[b][i] for i in range(len(shape)))==dist):
                    return False
    return True


def static_check(shape,pts,concepts):
    n=len(pts);support_counts=[0]*(n+1)
    witness={}
    for S in range(1<<n):
        idx=[i for i in range(n) if S>>i&1]
        trace_set=set()
        for c in concepts:
            pattern=0
            for t,i in enumerate(idx):
                if (c>>i)&1:pattern|=1<<t
            trace_set.add(pattern)
        shattered=len(trace_set)==(1<<len(idx))
        expected=private_support(shape,pts,S)
        assert shattered==expected,(shape,S,shattered,expected)
        if shattered:
            support_counts[len(idx)]+=1
            witness.setdefault(len(idx),S)
    r=sum(v>1 for v in shape)
    k=sum(v-1 for v in shape)
    exact_vc=k if r>=2 else k+1
    assert max(i for i,c in enumerate(support_counts) if c)>-1
    assert max(i for i,c in enumerate(support_counts) if c)==exact_vc,(shape,support_counts,exact_vc)
    print('STATIC_SHATTERING_PASS',shape,'VC',exact_vc,'maximum_support_count',support_counts[exact_vc],flush=True)
    if len(shape)==2 and min(shape)>=3:
        assert support_counts[exact_vc]==prod(shape)
    if shape==(2,2):assert support_counts[exact_vc]==6
    if shape==(2,3):assert support_counts[exact_vc]==8


def online_check(shape,pts,concepts):
    query_masks=[]
    for q in range(len(pts)):
        query_masks.append(sum(1<<j for j,c in enumerate(concepts) if c>>q&1))
    @lru_cache(None)
    def ld(version):
        if version.bit_count()<2:return 0
        value=0
        for mask in query_masks:
            yes=version&mask
            no=version^yes
            if not yes or not no:continue
            if min(yes.bit_count(),no.bit_count())<(1<<value):continue
            candidate=1+min(ld(yes),ld(no))
            if candidate>value:value=candidate
        return value
    result=ld((1<<len(concepts))-1)
    target=1+sum(n-1 for n in shape)
    assert result==target,(shape,result,target)
    print('ONLINE_SHATTERING_PASS',shape,'Ldim',result,'concepts',len(concepts),'states',ld.cache_info().currsize,flush=True)


def main():
    independent_shapes=[(1,1),(1,3),(2,2),(2,3),(2,4),(3,3),(2,2,2),(2,2,3)]
    for shape in independent_shapes:
        pts,concepts=instance(shape)
        expected=1+prod((1<<n)-1 for n in shape)
        assert len(concepts)==expected
        all_convex={S for S in range(1<<len(pts)) if independent_convexity(shape,pts,S)}
        assert all_convex==set(concepts),(shape,len(all_convex),len(concepts))
        print('INDEPENDENT_GRAPH_GEODESIC_CHECK_PASS',shape,'vertices',len(pts),'convex_sets',len(concepts),flush=True)
        static_check(shape,pts,concepts)
        online_check(shape,pts,concepts)
    for shape in [(2,2,4),(2,3,3),(2,2,2,2),(3,3,3),(2,2,2,2,2)]:
        pts,concepts=instance(shape)
        online_check(shape,pts,concepts)
    print('ALL_HAMMING_BOX_CHECKS_PASS',flush=True)

if __name__=='__main__':main()
