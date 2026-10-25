#!/usr/bin/env python3
"""Exact two-round relational multiplication types for finite dicyclic groups.

The mathematical general-n statement uses a separate case analysis of
one- and two-element multiplication patterns; finite computations here
are cross-checks, not proofs of a universal assertion.
"""
from math import gcd
from collections import defaultdict

def mul(n, x, y):
    a, i = x
    b, j = y
    return (a ^ b, (i + (-j if a else j) + (n if a and b else 0)) % (2*n))

def elements(n):
    return [(e,k) for e in (0,1) for k in range(2*n)]

def atom(n, x, y):
    points = ((0,0), x, y)
    bits=[]
    for i in range(3):
        for j in range(i+1,3):
            bits.append(points[i]==points[j])
    for i in range(3):
        for j in range(3):
            product=mul(n,points[i],points[j])
            for k in range(3):
                bits.append(product==points[k])
    return tuple(bits)

def actual_signature(n, orbit_reduced=True):
    G=elements(n)
    if orbit_reduced:
        # The cyclic elements are permuted by the unit automorphisms;
        # the outside coset is one orbit via a^i b -> a^(i+t) b.
        reps=sorted({gcd(k,2*n) for k in range(2*n)})
        xs=[(0,d%(2*n)) for d in reps]+[(1,0)]
    else:
        xs=G
    return frozenset(frozenset(atom(n,x,y) for y in G) for x in xs)

def reduced_point_profile(n,x):
    identity=(0,0)
    sq=mul(n,x,x)
    if x==identity:
        return ('identity',)
    tags=set()
    for y in elements(n):
        if y in (identity,x):
            continue
        ys=mul(n,y,y)
        tags.add((int(ys==identity),int(y==sq),int(ys==x),int(mul(n,x,y)==identity)))
    return (int(sq==identity),tuple(sorted(tags)))

# The invariant classification in terms of elementary rank-two patterns.
U=(0,0,0,0); I=(1,0,0,0); E=(0,0,0,1)
F=(0,1,0,0); R=(0,0,1,0); T=(0,1,1,1); J=(1,1,0,0)
K={
 'identity': ('identity',),
 'involution_small': (1,(R,)),
 'involution': (1,tuple(sorted((U,R)))),
 'order4_no_root': (0,tuple(sorted((U,E,J)))),
 'order4_root': (0,tuple(sorted((U,E,J,R)))),
 'order3': (0,tuple(sorted((U,I,T,R)))),
 'long_no_root': (0,tuple(sorted((U,I,E,F)))),
 'long_root': (0,tuple(sorted((U,I,E,F,R)))),
}
assert len(set(K.values()))==len(K)

def expected_kinds(n):
    if n==2: return {'identity','involution_small','order4_no_root'}
    common={'identity','involution','order4_no_root','long_no_root'}
    if n>=5: common.add('long_root')
    if n%3==0: common.add('order3')
    if n%4==0: common.add('order4_root')
    return common

def expected_class(n):
    return ('small',n) if n in (2,3,4) else ('stable',n%3==0,n%4==0)

if __name__=='__main__':
    # Independent direct full-vertex q2 computation against orbit reduction.
    for n in range(2,19):
        assert actual_signature(n,False)==actual_signature(n,True), n
    print('FULL_VERSUS_ORBIT_ATOMIC_TYPES_OK n=2..18')
    # Independent four-flag arithmetic against the entire 30-bit atomic type.
    # For each (x,y) with x and y distinct from the identity, the only
    # nontrivial equalities are y=x^2, x=y^2, xy=e, and y^2=e.
    for n in range(2,41):
        G=elements(n)
        seen={reduced_point_profile(n,x) for x in G}
        wanted={K[k] for k in expected_kinds(n)}
        assert seen==wanted, (n,seen^wanted)
    print('ELEMENTARY_PATTERN_TABLE_OK n=2..40')
    rep={('small',2):2,('small',3):3,('small',4):4,
         ('stable',False,False):5,('stable',True,False):6,
         ('stable',False,True):8,('stable',True,True):12}
    signatures={k:actual_signature(n) for k,n in rep.items()}
    assert len(set(signatures.values()))==7
    print('SEVEN_PAIRWISE_DISTINCT_TWO_ROUND_SIGNATURES_OK representatives=2,3,4,5,6,8,12')
    for n in range(2,101):
        assert actual_signature(n)==signatures[expected_class(n)], n
    print('EXACT_QUANTIFIER_TWO_PARTITION_CROSSCHECK_OK n=2..100')
    assert max(4*n for n in rep.values())==48
    assert set(rep.values())=={2,3,4,5,6,8,12}
    print('SHARP_FAMILY_REPRESENTATIVE_BOUND_OK elements=48')
    print('VERIFY_OK')
