#!/usr/bin/env python3
"""Finite checks for a sharp covering-code implication threshold."""
from itertools import product, combinations

def subseq(p,w):
    i=0
    for x in w:
        if i<len(p) and x==p[i]: i+=1
    return i==len(p)

def words(q,n): return product(range(q),repeat=n)

def all_n_subsequences(z,n):
    return [tuple(z[i] for i in ix) for ix in combinations(range(len(z)),n)]

def z_binary(p,R):
    if len(p)==1:return p*(2*R+1)
    if len(p)==2:
        if p[0]==p[1]:return p[:1]*(2*R+2)
        return (p[0],)*(R+1)+(p[1],)*(R+1)
    if p==(0,0,0) or p==(1,1,1):return p[:1]*(2*R+3)
    if p in ((0,0,1),(1,1,0),(1,0,0),(0,1,1)):
        # derive by reversal/complement from base 001
        z=(0,)*(R+2)+(1,)*(R+1)
        transformations=[lambda x:x,lambda x:x[::-1],lambda x:tuple(1-y for y in x),lambda x:tuple(1-y for y in x[::-1])]
        for trans in transformations:
            if trans((0,0,1))==p: return trans(z)
        raise AssertionError
    assert p in ((0,1,0),(1,0,1))
    z=(0,1)*(R+1)+(0,)
    return z if p==(0,1,0) else tuple(1-y for y in z)

witness_cases=0
for R in (1,2,3,4):
    for m in (1,2,3):
        for p in words(2,m):
            z=z_binary(p,R)
            assert len(z)==2*R+m
            for c in all_n_subsequences(z,R+m):
                assert subseq(p,c),('robust',p,R,z,c)
            witness_cases+=1

binary_avoidance_cases=0
for R in (1,2,3):
    n=R+4
    for z in words(2,2*R+4):
        assert any(not subseq((0,1,1,0),c) for c in all_n_subsequences(z,n)),('binary counterexample',R,z)
        binary_avoidance_cases+=1

large_alphabet_cases=0
for q,R in ((3,1),(3,2),(4,1)):
    n=R+3
    for z in words(q,2*R+3):
        for a in (0,1,2):
            if z.count(a)<=R:
                rem=list(i for i,x in enumerate(z) if x!=a)
                c=tuple(z[i] for i in rem[:n])
                assert len(c)==n and not subseq((0,1,2),c)
                break
        else:raise AssertionError((q,R,z))
        large_alphabet_cases+=1
print('VERIFY_OK')
print('binary_robust_witnesses',witness_cases)
print('binary_long_boundary_superwords',binary_avoidance_cases)
print('nonbinary_boundary_superwords',large_alphabet_cases)
