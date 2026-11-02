#!/usr/bin/env python3
"""Exact independent finite checks for prescribed consecutive-pattern packings.

No external dependencies. Run: python verify.py
Each finite calculation supplements, but does not replace, the infinite proof.
"""
from functools import lru_cache
from math import prod


def shape(m, k):
    assert m >= 3 and k > 2*m
    p = tuple(range(1, m)) + (k-1, k) + tuple(range(m, k-1))
    assert sorted(p) == list(range(1, k+1))
    return p


def predecessors(m, k, copies):
    """One generator for each adjacent rank pair in each local chain."""
    d=k-m; n=k+(copies-1)*d; before=[0]*n; p=shape(m,k)
    order=sorted(range(k),key=lambda x:p[x])
    for t in range(copies):
        off=t*d
        for x,y in zip(order,order[1:]):
            before[off+y] |= (1<<(off+x))
    return before


def count_by_minimal_deletion(m,k,copies):
    before=predecessors(m,k,copies)
    n=len(before); full=(1<<n)-1
    @lru_cache(None)
    def rec(chosen):
        if chosen==full:return 1
        out=0
        for i in range(n):
            bit=1<<i
            if not (chosen&bit) and (before[i]&~chosen)==0:
                out+=rec(chosen|bit)
        return out
    return rec(0)


def count_by_maximal_deletion(m,k,copies):
    """Independently build all within-copy pairwise inequalities, strip maximal vertices."""
    d=k-m; n=k+(copies-1)*d; p=shape(m,k)
    later=[0]*n
    for t in range(copies):
        offset=t*d
        for a in range(k):
            for b in range(k):
                if p[a]<p[b]:
                    later[offset+a] |= 1<<(offset+b)
    @lru_cache(None)
    def rec(rem):
        if not rem:return 1
        ans=0
        x=rem
        while x:
            bit=x&-x; x-=bit; i=bit.bit_length()-1
            if later[i]&rem==0:
                ans+=rec(rem^bit)
        return ans
    return rec((1<<n)-1)


def closure(before):
    n=len(before)
    pred=before[:]
    while True:
        changed=False
        for i in range(n):
            b=pred[i]
            cur=b
            while cur:
                bit=cur&-cur; cur-=bit
                b |= pred[bit.bit_length()-1]
            if b!=pred[i]:pred[i]=b;changed=True
        if not changed:return pred


def check_separator(m,k,copies):
    preds=closure(predecessors(m,k,copies))
    n=len(preds); q=n-1; u=q-1
    assert preds[q]&(1<<u),('u below q',m,k,copies)
    above=[i for i in range(n) if preds[i]&(1<<q)]
    assert len(above)==2*copies,(m,k,copies,len(above))
    assert all(i==q or ((preds[i]&(1<<q))!=0) or ((preds[q]&(1<<i))!=0) for i in range(n)), ('q separator',m,k,copies)
    assert all(not (preds[i]&(1<<u) and preds[q]&(1<<i)) for i in range(n) if i!=u and i!=q),('cover',m,k,copies)


def main():
    instances=0; summed=0
    for m in range(3,7):
        for k in range(2*m+1,2*m+4):
            for j in range(1,6):
                expected=prod(range(1,2*j,2))
                a=count_by_minimal_deletion(m,k,j)
                b=count_by_maximal_deletion(m,k,j)
                assert a==expected==b,(m,k,j,a,b,expected)
                check_separator(m,k,j)
                instances+=1;summed+=a
    print('VERIFY_OK cases=',instances,'overlap m=3..6','length K=2m+1..2m+3',
          'copies j=1..5','two independent exact linear-extension counters and separator/cover checks',
          'sum_counts=',summed)

if __name__=='__main__':main()
