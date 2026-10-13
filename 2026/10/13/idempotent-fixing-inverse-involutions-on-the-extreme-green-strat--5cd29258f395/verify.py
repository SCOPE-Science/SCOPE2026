#!/usr/bin/env python3
"""Exhaustive finite checks for the stated low-rank inverse matchings.
All transformations are encoded by their complete image tuples, not only their
kernel/image parameters. Uses no third-party packages.
"""
from itertools import combinations
from math import comb

def compose(f,g):
    """f after g (maps indexed by 1..n)."""
    return tuple(f[y-1] for y in g)

def rank_two(n,a,b,c):
    assert 1<=a<n and 1<=b<c<=n
    return (b,)*a+(c,)*(n-a)

def mate_two(a,b,c):
    if b<=a<c:return a,b,c
    if a<b:return c-1,a,b
    assert c<=a
    return b,c,a+1

def rank_colast(n,d,m):
    assert 1<=d<n and 1<=m<=n
    image=[i for i in range(1,n+1) if i!=m]
    return tuple(image[x-1] if x<d else
                 image[d-1] if x<=d+1 else
                 image[x-2] for x in range(1,n+1))

def mate_colast(d,m):
    if m in (d,d+1):return d,m
    if m<d:return m,d+1
    assert m>d+1
    return m-1,d

def test_rank(n, mode):
    if mode=='two':
        pars=[(a,b,c) for a in range(1,n) for b,c in combinations(range(1,n+1),2)]
        func=lambda p:rank_two(n,*p)
        mate=lambda p:mate_two(*p)
        assert len(pars)==(n-1)*comb(n,2)
        expected_fixed=comb(n+1,3)
        expected_pairs=comb(n,3)
    else:
        pars=[(d,m) for d in range(1,n) for m in range(1,n+1)]
        func=lambda p:rank_colast(n,*p)
        mate=lambda p:mate_colast(*p)
        assert len(pars)==n*(n-1)
        expected_fixed=2*(n-1)
        expected_pairs=comb(n-1,2)
    paramset=set(pars)
    funcs={p:func(p) for p in pars}
    assert len(set(funcs.values()))==len(pars)
    fixed=0; pairs=set(); nonidem=0
    for p in pars:
        f=funcs[p];p1=mate(p)
        assert p1 in paramset, (n,mode,p,p1)
        assert mate(p1)==p, (n,mode,p,p1)
        g=funcs[p1]
        assert compose(f,compose(g,f))==f, (n,mode,p)
        assert compose(g,compose(f,g))==g, (n,mode,p)
        idem=compose(f,f)==f
        fixed+=(p1==p)
        nonidem+=(not idem)
        assert (p1==p)==idem,(n,mode,p,p1)
        if p1!=p:pairs.add(frozenset((p,p1)))
    assert fixed==expected_fixed,(n,mode,fixed,expected_fixed)
    assert len(pairs)==expected_pairs,(n,mode,len(pairs),expected_pairs)
    assert 2*len(pairs)==nonidem
    return (len(pars),fixed,len(pairs))

for n in range(3,13):
    a=test_rank(n,'two')
    b=test_rank(n,'colast')
    print(f'n={n}: rank2 size/fixed/transpositions={a}; corank1={b}')
print('EXHAUSTIVE_INVERSE_IDENTITIES_AND_FIXED_POINT_COUNTS_OK')
print('VERIFY_OK')
