#!/usr/bin/env python3
"""Independent small-instance checks for one-point extension counts of finite series-parallel posets.

Run: python3 verify_series_parallel.py
Only Python standard library is required. Intended for finite corroboration, not as an infinite proof.
"""
from itertools import product
from functools import lru_cache
from random import Random

# A poset is represented by strict comparability pairs i<j.
def combine(P, Q, typ):
    n = P[0]
    m = Q[0]
    edges = set(P[1]) | {(i+n,j+n) for (i,j) in Q[1]}
    if typ == 'series':
        edges.update((i,j+n) for i in range(n) for j in range(m))
    assert typ in ('series','parallel')
    return (n+m,frozenset(edges))

def composed_stats(S, T, typ):
    i1, c1 = S
    i2, c2 = T
    if typ == 'series':
        return (i1+i2-1, c1+c2-i1-i2+i1*i2)
    return (i1*i2, c1+c2+2*i1*i2-2*i1-2*i2+1)

def direct(P):
    n, edges = P
    ideals = 0
    one_types = 0
    e = tuple(edges)
    for states in product((0,1,2),repeat=n):
        # states: 0 is below new x, 1 incomparable, 2 above new x
        good = True
        for a,b in e:
            # a < b, so state(a) <= state(b) for consistency
            if states[a] > states[b]:
                good = False; break
        if not good:
            continue
        lower = [i for i,s in enumerate(states) if s==0]
        upper = [i for i,s in enumerate(states) if s==2]
        # every p<x<q must have p<q (not just a<=b)
        if all((i,j) in edges for i in lower for j in upper):
            one_types += 1
    for mask in range(1<<n):
        if all(not (mask>>j &1) or (mask>>i &1) for i,j in e):
            ideals +=1
    return ideals,one_types

leaf=(1,frozenset())
leaf_stats=(2,3)
@lru_cache(None)
def expressions(n):
    if n == 1:
        return {(leaf,leaf_stats)}
    out=set()
    for s in range(1,n):
        for L,LS in expressions(s):
            for R,RS in expressions(n-s):
                for typ in ('series','parallel'):
                    out.add((combine(L,R,typ),composed_stats(LS,RS,typ)))
    return out

counts=[]
for n in range(1,7):
    exprs=expressions(n)
    unique={}
    for P,stat in exprs:
        if P in unique:
            assert unique[P]==stat,'composition-tree inconsistency'
        unique[P]=stat
    for P,stat in unique.items():
        assert direct(P)==stat, (n,P,stat,direct(P))
        i,c=stat
        assert 1<=i<=2**n and 1<=c<=3**n
    counts.append((n,len(exprs),len(unique)))

# Additional reproducible mixed binary decompositions with up to ten vertices.
rng=Random(20261018)
random_checks=0
for n in range(7,11):
    for trial in range(65):
        stack=[(leaf,leaf_stats) for _ in range(n)]
        while len(stack)>1:
            k=rng.randrange(len(stack)-1)
            L,LS=stack.pop(k)
            R,RS=stack.pop(k)
            typ=rng.choice(('series','parallel'))
            stack.insert(k,(combine(L,R,typ),composed_stats(LS,RS,typ)))
        P,stat=stack[0]
        assert direct(P)==stat,(n,trial,stat,direct(P))
        random_checks+=1

# Explicit non-ancestor forest: diamond, 1 < (2 || 3) < 4.
mid=combine(leaf,leaf,'parallel')
P=combine(combine(leaf,mid,'series'),leaf,'series')
s=composed_stats(composed_stats(leaf_stats,composed_stats(leaf_stats,leaf_stats,'parallel'),'series'),leaf_stats,'series')
assert direct(P)==s==(6,18), (direct(P),s)
# Exact decomposition value on empty poset, counted separately.
assert direct((0,frozenset()))==(1,1)
print('EXHAUSTIVE_SIZES='+str(counts))
print('RANDOM_CHECKS='+str(random_checks))
print('DIAMOND_IDEALS_TYPES='+str(s))
print('EMPTY_IDEALS_TYPES=(1, 1)')
print('ALL_TESTS_PASS')
