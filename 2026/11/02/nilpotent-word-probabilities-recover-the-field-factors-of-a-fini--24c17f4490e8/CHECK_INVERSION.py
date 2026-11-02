#!/usr/bin/env python3
"""Exact exponential-spectrum reconstruction of field factors from nilpotent word laws."""
from itertools import combinations_with_replacement
from fractions import Fraction as F
from collections import defaultdict

def product_profile(qs,k):
    a=F(1)
    for q in qs:a*=1-F(q-1,q)**k
    return a

def formal_survival(qs):
    # Exact representation of 1-P_k as sum c_b b**k, b in (0,1).
    terms={F(1): F(1)}
    for q in qs:
        b=F(q-1,q);tmp=defaultdict(F)
        for v,c in terms.items():
            tmp[v]+=c
            tmp[v*b]-=c
        terms={v:c for v,c in tmp.items() if c}
    terms.pop(F(1),None)
    return {x:-c for x,c in terms.items() if c}

def reconstruct(qs):
    # Simulates rigorous largest-exponential-base removal; no numerical limits.
    remaining=list(qs)
    out=[]
    while remaining:
        spectrum=formal_survival(remaining)
        b=max(spectrum)
        mult=spectrum[b]
        assert isinstance(mult,F) and mult.denominator==1 and mult>0
        q=1/(1-b)
        assert q.denominator==1
        out.extend([int(q)]*int(mult))
        for j in range(int(mult)):remaining.remove(int(q))
    return sorted(out)

qs=(2,3,4,5,7,8,9)
count=0
for r in range(1,5):
    for fields in combinations_with_replacement(qs,r):
        assert reconstruct(fields)==sorted(fields)
        expansion=formal_survival(fields)
        for k in range(1,13):
            assert 1-product_profile(fields,k)==sum(c*(b**k) for b,c in expansion.items())
        count+=1
print(f'Exact dominant-exponential peeling checked on {count} field-factor multisets, 1 to 4 factors.')
# Direct Vandermonde argument applies to at most two nonzero exponential spectra.
# Verify an illustrative P2 collision and its P3 separation exactly.
assert product_profile((8,),2)==product_profile((2,2,2,3),2)==F(15,64)
assert product_profile((8,),3)!=product_profile((2,2,2,3),3)
# Sanity-check finite cutoff L=2**rA+2**rB-2 against sample distinct pairs.
small=list(combinations_with_replacement(qs,2))
for i,A in enumerate(small):
    for B in small[i+1:]:
        if A!=B:
            bound=2**len(A)+2**len(B)-2
            assert any(product_profile(A,k)!=product_profile(B,k) for k in range(1,bound+1))
print(f'Finite prefix separation through length 6 verified for {len(small)} two-factor samples.')
assert product_profile((4,),1)==product_profile((2,2),1)==F(1,4)
assert product_profile((4,),2)==F(7,16)
assert product_profile((2,2),2)==F(9,16)
print('Sharp two-factor threshold: P1(F4)=P1(F2xF2)=1/4, P2=7/16 versus 9/16')
print('VERIFY_OK')
