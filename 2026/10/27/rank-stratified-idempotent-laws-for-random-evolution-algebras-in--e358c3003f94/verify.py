#!/usr/bin/env python3
"""Exhaustive rank-conditioned idempotent counts for small finite fields.

The calculation independently enumerates matrices of all ranks, their fixed
vectors under x -> A*x^[2], and compares with the Gaussian-binomial formula.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import prod


def gf_mult(a,b,q,poly):
    out=0
    while b:
        if b&1: out^=a
        b>>=1
        a<<=1
        if a&q: a^=poly
    return out


def gauss(n,k,q):
    if k<0 or k>n:return 0
    numerator=prod(q**n-q**i for i in range(k))
    denominator=prod(q**k-q**i for i in range(k))
    return numerator//denominator


def order_gl(r,q):
    return prod(q**r-q**i for i in range(r))


def theory(n,s,q):
    # For r independent fixed vectors, expectation is kernel avoidance.
    moments={r:Fraction(q**(r*(n-s))*gauss(n-r,s-r,q),gauss(n,s,q))
             for r in range(s+1)}
    # Convert frame moments into Gaussian-binomial subspace moments.
    subs={r:moments[r]/order_gl(r,2) for r in moments}
    out={}
    for d in range(s+1):
        out[d]=sum(((-1)**(r-d))*2**((r-d)*(r-d-1)//2)*gauss(r,d,2)*subs[r]
                   for r in range(d,s+1))
    assert sum(out.values())==1
    assert all(v>=0 for v in out.values())
    return out


def exhaustive(e,n,poly):
    q=2**e
    vectors=list(product(range(q),repeat=n))
    zero=tuple(0 for _ in range(n))
    mult=[[gf_mult(a,b,q,poly) for b in range(q)] for a in range(q)]
    scalar=lambda a,v:tuple(mult[a][x] for x in v)
    codes={v:i for i,v in enumerate(vectors)}
    qn=q**n
    mask=[[0]*n for _ in vectors]
    for ridx,row in enumerate(vectors):
        for k,v in enumerate(vectors[1:]):
            sq=[mult[x][x] for x in v]
            val=0
            for a,b in zip(row,sq): val^=mult[a][b]
            for j in range(n):
                if val==v[j]:mask[ridx][j]|=(1<<k)
    full=(1<<(qn-1))-1
    @lru_cache(None)
    def augmented(span,idx):
        a=vectors[idx]
        if a in span:return span
        return tuple(sorted({tuple(x^y for x,y in zip(v,scalar(t,a)))
                             for v in span for t in range(q)}))
    initial=(zero,)
    hist=Counter()
    rank_counts=Counter()
    def recur(depth,span,fixmask):
        if depth==n:
            s=0; L=len(span)
            while L>1: L//=q; s+=1
            d=0; K=fixmask.bit_count()+1
            while K>1: K//=2; d+=1
            assert 1<<d == fixmask.bit_count()+1
            hist[(s,d)]+=1
            rank_counts[s]+=1
            return
        for idx in range(qn):
            recur(depth+1,augmented(span,idx),fixmask&mask[idx][depth])
    recur(0,initial,full)
    for s in range(n+1):
        predicted_rank=gauss(n,s,q)*prod(q**n-q**i for i in range(s))
        assert rank_counts[s]==predicted_rank,(e,n,s,rank_counts[s],predicted_rank)
        pred=theory(n,s,q)
        for d in range(s+1):
            assert Fraction(hist[(s,d)],rank_counts[s])==pred[d],(e,n,s,d)
    return rank_counts, hist


def main():
    for e,n,poly in [(1,2,0b11),(1,3,0b11),(1,4,0b11),
                     (2,2,0b111),(2,3,0b111),(3,2,0b1011)]:
        counts,hist=exhaustive(e,n,poly)
        details={s:{2**d-1:hist[s,d] for d in range(s+1) if hist[s,d]}
                 for s in range(n+1)}
        print('GF(%d) n=%d %s'%(2**e,n,details))
    print('RANK_VERIFICATION_OK')

if __name__=='__main__':main()
