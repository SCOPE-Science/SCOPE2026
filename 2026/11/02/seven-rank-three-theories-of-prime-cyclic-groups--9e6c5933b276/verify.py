#!/usr/bin/env python3
"""Exact rank-three checks for prime cyclic groups in relational addition.

Requires only Python 3 standard library. All calculations are integer/rational exact.
This file does not substitute finite tests for the infinite symbolic proof.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache

# Solutions of the twelve distinct atomic equations involving z, for odd prime
# characteristic: z = alpha*x + beta*y. Their rational coefficients are:
AFFINE = (
    (F(-1), F(0)),  # z+x=0
    (F(-1), F(1)),  # z+x=y
    (F(0), F(-1)),  # z+y=0
    (F(0), F(0)),   # z=0
    (F(0), F(1,2)), # 2z=y
    (F(0), F(1)),   # z=y
    (F(0), F(2)),   # z=2y
    (F(1,2), F(0)), # 2z=x
    (F(1), F(-1)),  # z+y=x
    (F(1), F(0)),   # z=x
    (F(1), F(1)),   # z=x+y
    (F(2), F(0)),   # z=2x
)
assert len(AFFINE) == len(set(AFFINE)) == 12

slope_pairs={}
for (i,(a,b)),(j,(c,d)) in combinations(enumerate(AFFINE),2):
    if b != d:
        t=(c-a)/(b-d)
        slope_pairs.setdefault(t,[]).append((i,j))
S=tuple(sorted(slope_pairs))
EXPECT_S=tuple(F(x) for x in ['-2','-1','-1/2','0','1/4','1/3','1/2','2/3','1','3/2','2','3','4'])
assert S == EXPECT_S, S
assert len(S)==13
print('THIRTEEN_EXCEPTIONAL_RATIOS_OK',','.join(str(z) for z in S))

# None of the rational exceptional slopes collide for p >= 17. In fact,
# all cross-difference numerators and denominators have prime factors <= 11.
cross_diffs={abs(u.numerator*v.denominator-v.numerator*u.denominator) for u,v in combinations(S,2)}
assert max(cross_diffs) == 15
assert all(d not in (0,17) and d <17 for d in cross_diffs)
assert all(s.denominator <=4 for s in S)
print('EXCEPTIONAL_SLOPES_DISTINCT_ABOVE_THIRTEEN_OK max_cross_difference=15')

# Check coverage for every smaller prime, using the single-variable equations
# represented by the E_i directly; characteristic 2 is included.
def eq_sets(p,x,y):
    return [
        {z for z in range(p) if (z+x)%p==0},
        {z for z in range(p) if (z+x-y)%p==0},
        {z for z in range(p) if (z+y)%p==0},
        {0},
        {z for z in range(p) if (2*z-y)%p==0},
        {y},
        {2*y%p},
        {z for z in range(p) if (2*z-x)%p==0},
        {z for z in range(p) if (z+y-x)%p==0},
        {x},
        {(x+y)%p},
        {2*x%p},
    ]

def generic_exists(p):
    for x in range(1,p):
        for y in range(p):
            sets=eq_sets(p,x,y)
            if all(sets[i].isdisjoint(sets[j]) for i in range(12) for j in range(i+1,12)):
                return True
    return False
for p in (2,3,5,7,11,13,17,19,23,29,31):
    assert generic_exists(p) == (p >= 17),p
print('GENERIC_PAIR_THRESHOLD_CHECK_OK up_to=31')

# The next five properties are exactly the five explicit rank<=3
# prime-isolating sentences given in the proof.
for p in (2,3,5,7,11,13,17,19,23):
    predicates = [
        any(x!=0 and (2*x)%p==0 for x in range(p)),
        any(x!=0 and (3*x)%p==0 for x in range(p)),
        any(x!=0 and (5*x)%p==0 for x in range(p)),
        any(x!=0 and (7*x)%p==0 for x in range(p)),
        any(x!=0 and (11*x)%p==0 for x in range(p)),
    ]
    assert predicates == [p==t for t in (2,3,5,7,11)],(p,predicates)
print('FIVE_CHARACTERISTIC_SENTENCE_CHECKS_OK')

# Independent full Hintikka-signature calculation for finite calibration.
# Includes the identity constant and EVERY ternary addition atom on selected
# variables, including repetitions.
registry={}
def intern(o):
    if o not in registry:registry[o]=len(registry)
    return registry[o]
def sig(p,k=3):
    @lru_cache(None)
    def T(t,r):
        v=(0,)+t
        a=intern(('atoms',tuple((v[i]+v[j]-v[z])%p==0
                                for i in range(len(v)) for j in range(len(v))
                                for z in range(len(v)))))
        if r==0:return a
        return intern(('type',r,a,frozenset(T(t+(u,),r-1) for u in range(p))))
    return T((),k)
primes=(2,3,5,7,11,13,17,19,23)
ids=[sig(p) for p in primes]
assert len(set(ids[:7]))==7
assert ids[6]==ids[7]==ids[8]
print('EXACT_THREE_ROUND_CALIBRATION_OK classes=7 primes='+','.join(map(str,primes)))
print('VERIFY_OK')
