#!/usr/bin/env python3
"""Exact rational checks for the finite-income Gini counterexample.

The universal result for one through three incomes is proved analytically
by endpoint monotonicity and Karamata's inequality in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement


def gini_pairwise(a):
    z = tuple(Q(v) for v in a)
    assert z and min(z) > 0
    return sum(abs(v-w) for v,w in combinations(z,2)) / (len(z)*sum(z))


def gini_sorted(a):
    z = sorted(Q(v) for v in a)
    n=len(z)
    return sum((2*j-n-1)*v for j,v in enumerate(z,1))/(n*sum(z))


def majorizes(a,b):
    a,b=sorted(Q(t) for t in a),sorted(Q(t) for t in b)
    return (len(a)==len(b) and sum(a)==sum(b) and
            all(sum(a[:i])<=sum(b[:i]) for i in range(1,len(a))))


x=(1,1,1,3)
y=(1,1,2,2)
assert majorizes(x,y)
assert not majorizes(y,x)
raw=(gini_pairwise(x),gini_pairwise(y))
assert raw==(Q(1,4),Q(1,6))

cap=lambda t: Q(min(t,2))
capped=(gini_pairwise([cap(t) for t in x]), gini_pairwise([cap(t) for t in y]))
assert capped==(Q(3,20),Q(1,6))
assert capped[0]-capped[1]==-Q(1,60)

# This interpolation at integer arguments comes from the smooth, strictly
# increasing, strictly concave function f(t)=1-8**(-t), t>0.
smooth=lambda t: Q(1)-Q(8)**(-t)
assert tuple(map(smooth,(1,2,3)))==(Q(7,8),Q(63,64),Q(511,512))
smoothed=(gini_pairwise([smooth(t) for t in x]),gini_pairwise([smooth(t) for t in y]))
assert smoothed==(Q(27,1060),Q(1,34))
assert smoothed[0]-smoothed[1]==-Q(71,18020)

# Independent formula implementation and exhaustive low-dimensional tests
# over positive integer profiles for selected concave rational maps.
profiles_checked=0
for n in (1,2,3,4):
    for a in combinations_with_replacement(range(1,8),n):
        assert gini_pairwise(a)==gini_sorted(a)
        profiles_checked+=1

small_comparisons=0
maps=[lambda t:Q(t), lambda t:Q(min(t,2)),
      lambda t:Q(min(t,3)), lambda t:Q(1)-Q(8)**(-t),
      lambda t:Q(4)-Q(2)**(-t)]
for n in (1,2,3):
    profiles=list(combinations_with_replacement(range(1,8),n))
    for a in profiles:
        for b in profiles:
            if not majorizes(a,b):
                continue
            for f in maps:
                fa,fb=[f(t) for t in a],[f(t) for t in b]
                assert sum(fa)<=sum(fb)
                assert gini_pairwise(fa)>=gini_pairwise(fb)
                small_comparisons+=1

print('VERIFY_OK majorization=PASS raw=1/4,1/6 capped=3/20,1/6')
print('VERIFY_OK smooth=27/1060,1/34 smooth_gap=-71/18020')
print(f'VERIFY_OK independent_gini_profiles={profiles_checked} low_order_transform_comparisons={small_comparisons}')
