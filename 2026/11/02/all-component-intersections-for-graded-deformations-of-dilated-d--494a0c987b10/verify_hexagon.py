#!/usr/bin/env python3
"""Exact checks for lattice-hexagon decompositions and common coarsenings.

The exhaustive ranges here supplement the all-k proof, and do not certify
an unbounded statement by enumeration.
"""
from functools import lru_cache

S1=(1,0,0,1,0,0)
S2=(0,1,0,0,1,0)
S3=(0,0,1,0,0,1)
T1=(1,0,1,0,1,0)
T2=(0,1,0,1,0,1)
H=(1,1,1,1,1,1)
GENERATORS=(S1,S2,S3,T1,T2)

def add(*vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(6))

def scaled(k, t):
    return tuple(sorted([S1,S2,S3]*(k-t)+[T1,T2]*t))

def edge_sum(c):
    return tuple(sum(c[j]*GENERATORS[j][i] for j in range(5)) for i in range(6))

def partitions(atoms):
    """All unlabeled Minkowski-coarsening multisets of listed atoms."""
    size=len(atoms)
    @lru_cache(None)
    def rec(mask):
        if not mask:
            return frozenset([tuple()])
        first=mask&-mask
        out=set()
        subset=mask
        while subset:
            if subset&first:
                part=tuple(sum(atoms[j][i] for j in range(size) if subset>>j&1)
                           for i in range(6))
                for rest in rec(mask^subset):
                    out.add(tuple(sorted((part,)+rest)))
            subset=(subset-1)&mask
        return frozenset(out)
    return rec((1<<size)-1)

def refines(fine, coarse):
    """Whether finer summands can be grouped to equal the coarser ones."""
    fine=tuple(fine)
    coarse=tuple(coarse)
    @lru_cache(None)
    def rec(index, available):
        if index==len(coarse):
            return available==0
        subset=available
        while subset:
            target=tuple(sum(fine[j][i] for j in range(len(fine))
                              if subset>>j&1) for i in range(6))
            if target==coarse[index] and rec(index+1, available^subset):
                return True
            subset=(subset-1)&available
        return False
    return rec(0,(1<<len(fine))-1)

def common_fine(k, left, right):
    return tuple(sorted([S1,S2,S3]*(k-right)+
                        [T1,T2]*left+[H]*(right-left)))

def check():
    assert add(T1,T2)==add(S1,S2,S3)==H
    cases=0
    for k in range(1,7):
        decompositions=[]
        for a in range(k+1):
            for b in range(k+1):
                for c in range(k+1):
                    for d in range(k+1):
                        for e in range(k+1):
                            if edge_sum((a,b,c,d,e))==(k,)*6:
                                decompositions.append((a,b,c,d,e))
        expected={(k-t,k-t,k-t,t,t) for t in range(k+1)}
        assert set(decompositions)==expected, (k,decompositions)
    for k in range(1,4):
        forms={t:partitions(scaled(k,t)) for t in range(k+1)}
        for t in range(k+1):
            for u in range(t+1,k+1):
                canonical=common_fine(k,t,u)
                assert len(canonical)==3*k-2*u+t
                common=forms[t]&forms[u]
                assert canonical in common
                assert all(refines(canonical,c) for c in common)
                cases+=1
    print('VERIFY_OK: decomposition factorization checked through k=6;'
          f' all {cases} pair intersections exhaustively checked through k=3')

if __name__=='__main__':
    check()
