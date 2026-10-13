#!/usr/bin/env python3
"""Exact generalized-weight census for two 95-coordinate binary codes.

Only Python's standard library is required. All finite loops are exhaustive.
The direct-support and annihilator computations use different reductions.
"""
from collections import Counter
from itertools import combinations, product

DIM = 7
LENGTH = 95
EXPECTED = {
    1: ((18,54,74,84,90,93,95), (1,7,126,168,280,32,1)),
    9: ((22,56,74,84,90,93,95), (1,12,36,144,256,32,1)),
}
SUBSPACE_COUNTS = (1,127,2667,11811,11811,2667,127,1)

def parity(x):
    return x.bit_count() % 2

def columns(a):
    original = []
    extra = []
    for x in range(1,64):
        # Two complementary three-flats, minus their common origin.
        f = int((x & 7)==0 or (x & 56)==0)
        g = x | (f << 6)
        original.append(g)
        if parity(a & x):
            extra.append(g)
    assert len(original)==63 and len(extra)==32
    return original+extra

def rref_bases(d):
    """Enumerate each d-space of F_2^7 in unique reduced-echelon form."""
    if d==0:
        yield ()
        return
    for pivots in combinations(range(DIM),d):
        free = tuple(j for j in range(DIM) if j not in pivots)
        choices = [tuple(j for j in free if j>p) for p in pivots]
        for masks in product(*(range(1<<len(s)) for s in choices)):
            rows=[]
            for p,available,z in zip(pivots,choices,masks):
                v=1<<p
                for j,bitpos in enumerate(available):
                    if (z>>j)&1:
                        v |= 1<<bitpos
                rows.append(v)
            yield tuple(rows)

def span(basis):
    out=[0]
    for v in basis:
        out += [w^v for w in tuple(out)]
    return out

def census_by_direct_support(cols):
    """Optimize unions of supports of an exhaustive RREF basis census."""
    word_support=[]
    for u in range(1<<DIM):
        bits=0
        for j,g in enumerate(cols):
            bits |= parity(u & g)<<j
        word_support.append(bits)
    assert len(set(word_support))==128
    hist=[]
    for r in range(1,DIM+1):
        counts=Counter()
        for rows in rref_bases(r):
            union=0
            for u in rows:
                union |= word_support[u]
            counts[union.bit_count()]+=1
        assert sum(counts.values()) == SUBSPACE_COUNTS[r]
        hist.append(counts)
    return hist

def census_by_annihilator(cols):
    """Optimize retained columns in exhaustively enumerated orthogonal spaces."""
    multiplicity=Counter(cols)
    assert Counter(multiplicity.values())==Counter({1:31,2:32})
    hist=[]
    for r in range(1,DIM+1):
        counts=Counter()
        for rows in rref_bases(DIM-r):
            zeros=sum(multiplicity[v] for v in span(rows))
            counts[LENGTH-zeros]+=1
        assert sum(counts.values())==SUBSPACE_COUNTS[DIM-r]
        hist.append(counts)
    return hist

def check():
    for a in (1,9):
        c=columns(a)
        left=census_by_direct_support(c)
        right=census_by_annihilator(c)
        assert left==right, f"Two methods disagree for normal {a}"
        minimum=tuple(min(h) for h in left)
        multiplicities=tuple(h[min(h)] for h in left)
        assert (minimum,multiplicities)==EXPECTED[a],(a,minimum,multiplicities)
        assert len(set(c))==63
        print('normal',a,'weights',minimum,'minimizer_counts',multiplicities)
    print('VERIFY_OK')

if __name__=='__main__':
    check()
