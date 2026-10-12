#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import isqrt


def compositions3(N):
    return [(a,b,N-a-b) for a in range(1,N-1) for b in range(1,N-a) if N-a-b>=1]


def discrepancy_vectors(N):
    C=compositions3(N)
    out=set()
    for v in C:
        for s in C:
            out.add(tuple(si-vi for si,vi in zip(s,v)))
    return sorted(out)


def lh_num(d):
    # LH = lh_num(d)/N when d is in count units.
    return Fraction(sum(abs(x) for x in d),2)


def gallagher_sq_num(d):
    # G^2 = gallagher_sq_num(d)/N^2.
    return Fraction(sum(x*x for x in d),2)


def strict_reversal(a,b):
    return (lh_num(a)-lh_num(b))*(gallagher_sq_num(a)-gallagher_sq_num(b)) < 0

# Two-party identity: d=(k,-k), so LH^2=G^2=k^2 in count units.
for k in range(-100,101):
    d=(k,-k)
    assert lh_num(d)**2 == gallagher_sq_num(d)

# Three-party structural identity.  For d=(a,b,-a-b), a,b>=0,
# L=a+b and h=|a-b|, G^2=(3L^2+h^2)/4.
for a in range(0,101):
    for b in range(0,101):
        if a==0 and b==0:
            continue
        d=(a,b,-a-b)
        L=Fraction(a+b)
        h=Fraction(abs(a-b))
        assert lh_num(d)==L
        assert gallagher_sq_num(d)==(3*L*L+h*h)/4
        assert Fraction(3,4)*L*L <= gallagher_sq_num(d) <= L*L

# Positive common-denominator three-party grid census.
EXPECTED_VECTORS={3:1,4:7,5:19,6:37,7:61,8:91,9:127,10:169,11:217}
EXPECTED_REVERSALS={3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:36}
first_layer=[]
for N in range(3,12):
    ds=discrepancy_vectors(N)
    assert len(ds)==EXPECTED_VECTORS[N], (N,len(ds))
    rev=[]
    for a,b in combinations(ds,2):
        if strict_reversal(a,b):
            rev.append((a,b))
    assert len(rev)==EXPECTED_REVERSALS[N], (N,len(rev))
    if N==11:
        first_layer=rev

# Classify the first layer: up to party permutation and global sign, only
# (7,-7,0) versus (8,-4,-4).
def canon_shape(d):
    s1=tuple(sorted(d))
    s2=tuple(sorted(-x for x in d))
    return min(s1,s2)
shapes=set()
for a,b in first_layer:
    shapes.add(tuple(sorted((canon_shape(a),canon_shape(b)))))
assert shapes == {tuple(sorted(((-7,0,7),(-8,4,4))))}

# Explicit positive-count witness at N=11.
VA=(1,8,2); SA=(8,1,2)
VB=(9,1,1); SB=(1,5,5)
dA=tuple(s-v for s,v in zip(SA,VA))
dB=tuple(s-v for s,v in zip(SB,VB))
assert dA==(7,-7,0)
assert dB==(-8,4,4)
assert lh_num(dA)==7 and lh_num(dB)==8
assert gallagher_sq_num(dA)==49 and gallagher_sq_num(dB)==48
assert strict_reversal(dA,dB)

print('VERIFY_OK')
print('two_party_identity_checked_k_-100_to_100')
print('three_party_identity_checked_a_b_0_to_100')
print('positive_grid_vector_counts',EXPECTED_VECTORS)
print('positive_grid_reversal_counts',EXPECTED_REVERSALS)
print('first_layer_reversing_pairs',len(first_layer))
print('first_layer_shape',sorted(shapes))
print('witness_A_votes_seats_d',VA,SA,dA,'LH',lh_num(dA),'G2',gallagher_sq_num(dA))
print('witness_B_votes_seats_d',VB,SB,dB,'LH',lh_num(dB),'G2',gallagher_sq_num(dB))
