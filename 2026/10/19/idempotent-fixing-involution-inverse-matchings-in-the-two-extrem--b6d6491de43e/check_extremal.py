#!/usr/bin/env python3
"""Exact exhaustive tests for the two extremal-rank formulas."""
from itertools import combinations_with_replacement

def compose(a,b):
    return tuple(a[i-1] for i in b)

def rank_two(f):
    n=len(f)
    a,b=sorted(set(f))
    c=sum(z==a for z in f)
    if a<=c<b:
        return f
    if b<=c:
        return (b,)*a+(c+1,)*(n-a)
    d=b-1
    return (c,)*d+(a,)*(n-d)

def top_rank(f):
    n=len(f)
    cuts=[i for i in range(1,n) if f[i-1]==f[i]]
    assert len(cuts)==1
    c=cuts[0]
    z=next(j for j in range(1,n+1) if j not in f)
    if z==c or z==c+1:
        return f
    if z<c:
        d=z;w=c+1
    else:
        d=z-1;w=c
    image=[j for j in range(1,n+1) if j!=w]
    return tuple(image[i if i<d else i-1] for i in range(n))

def main():
    count=0
    for n in range(3,9):
        maps=list(combinations_with_replacement(range(1,n+1),n))
        for rank,fn in [(2,rank_two),(n-1,top_rank)]:
            for f in maps:
                if len(set(f))!=rank:
                    continue
                g=fn(f)
                assert len(set(g))==rank
                assert all(g[i]<=g[i+1] for i in range(n-1))
                assert fn(g)==f
                assert compose(compose(f,g),f)==f
                assert compose(compose(g,f),g)==g
                if compose(f,f)==f:
                    assert g==f
                count+=1
    print('VERIFY_OK: extremal ranks, n=3..8,',count,'map-class tests')

if __name__=='__main__':
    main()
