#!/usr/bin/env python3
"""Exact finite sanity checks for the line-separation rank threshold."""
from itertools import product, combinations

SEED=((1,0,0),(0,1,0),(1,1,0),(0,0,1),(1,0,1),(2,1,1))

def add(*args):
    return tuple(sum(x[i] for x in args)%3 for i in range(len(args[0])))

def subset_sums(seq, nonempty=True):
    r=[]
    for bits in range(1 if nonempty else 0,1<<len(seq)):
        picks=[seq[i] for i in range(len(seq)) if bits>>i&1]
        r.append((bits,add(*picks) if picks else (0,)*len(seq[0])))
    return r

def span(v):
    return {(0,)*len(v),v,tuple(2*z%3 for z in v)}

def good(seq):
    if not seq:return True
    return all(any(t for t in s) for _,s in subset_sums(seq))

def separated(seq):
    if not seq: return True
    for v in seq:
        h=span(v)
        if not any(add(*[seq[i] for i in range(len(seq)) if bits>>i&1]) in h
                   for bits in range(1,1<<len(seq))
                   if all((seq[i] not in h) for i in range(len(seq)) if bits>>i&1)):
            return True
    return False

def check(seq, dimension, rank_ge3):
    assert all(len(v)==dimension for v in seq)
    assert good(seq)
    for i,v in enumerate(seq):
        for j in range(i):
            assert v not in span(seq[j])
        h=span(v)
        outside=tuple(w for w in seq if w not in h)
        witness=next(((mask,s) for mask,s in subset_sums(outside) if s in h),None)
        if rank_ge3:
            assert witness is not None and witness[1]!=(0,)*dimension
        else:
            assert witness is None
    assert separated(seq)==(not rank_ge3)

def extend(seq):
    dim=len(seq[0]);zero=(0,)*dim
    return tuple(tuple(v)+(0,) for v in seq)+(zero+(1,),(1,)+(0,)*(dim-1)+(1,))

for r in (3,4,5):
    seq=SEED
    for _ in range(r-3):seq=extend(seq)
    check(seq,r,True)

# Exhaustive unordered multisequences on nonzero rank-two ternary vectors,
# retaining only zero-sum-free instances; lengths bounded by Davenport 4.
r=2
vectors=list(v for v in product(range(3),repeat=r) if v!=(0,0))
counts=[0]*5
for length in range(1,5):
    for idx in combinations(range(len(vectors)+length-1),length):
        shifted=tuple(idx[j]-j for j in range(length))
        seq=tuple(vectors[i] for i in shifted)
        if not good(seq):continue
        assert separated(seq),seq
        counts[length]+=1
assert counts[1]>0 and counts[4]>0
print('VERIFY_OK rank3,4,5; rank2 exhaustive zero-sum-free multisequences',counts)
