#!/usr/bin/env python3
"""Standalone finite/rational diagnostics for a folded-nine-cube distance-power classification.
The universal inequalities require the written analytic proof; this file validates
normalization, Krawtchouk coefficients, and exact rational endpoint certificates.
"""
from fractions import Fraction as Q
from math import comb, log

def kval(n, k):
    arr=[1,n-2*k]
    for j in range(1,n//2):
        num=(n-2*k)*arr[j]-(n-j+1)*arr[j-1]
        assert num % (j+1)==0
        arr.append(num//(j+1))
    return arr

expected={2:[5,8,0,-14], 4:[1,-4,-4,6],
          6:[-3,0,8,-6], 8:[-7,20,-28,14]}
for k,values in expected.items():
    assert kval(9,k)[1:]==values
assert sum(comb(9,k) for k in expected)==255

lower_a=Q(12599,10000); upper_b=Q(14423,10000)
lower_c=Q(15874,10000)
assert lower_a**3<2 and upper_b**3>3 and lower_c**3<4
assert -7+20*lower_a-28*upper_b+14*lower_c == Q(93,2500)>0
A=Q(63,50)
assert A**3>2
assert Q(28,25)**2 < A
P_upper=1-4*A-4*A*Q(28,25)+6*A*A
assert P_upper<0
L6_upper=-Q(11,5)+Q(6,5)*A*A
assert L6_upper<0
assert 3**5<2**8 and 3**10<4**9 and 3**2>2**3

# Directly diagonalize by all 256 quotient characters, by grouping the
# 9-cube into complement pairs.  A character is defined by even-weight mask.
reps=[x for x in range(512) if not (x&256)]
assert len(reps)==256
for p in [0.0, 0.1, 0.25, 1/3, 1.0]:
    expected_spectra={k:sum(j**p*kval(9,k)[j] for j in range(1,5)) for k in expected}
    for k in expected:
        mask=(1<<k)-1
        direct=sum((min(x.bit_count(),9-x.bit_count())**p if x else 0)*
                   (-1 if (x&mask).bit_count()%2 else 1) for x in reps)
        assert abs(direct-expected_spectra[k])<1e-8,(p,k,direct,expected_spectra[k])

def F(p): return -7+20*2**p-28*3**p+14*4**p
lo,hi=0.0,1/3
for _ in range(100):
    mid=(lo+hi)/2
    if F(mid)>0:hi=mid
    else:lo=mid
pstar=(lo+hi)/2
assert .3232<pstar<.3234 and F(pstar)>-1e-11
for k in [2,4,6]:
    assert sum(j**pstar*kval(9,k)[j] for j in range(1,5))<0
print('CHECK_PASS', 'pstar=',format(pstar,'.15f'),
      'endpoint_rank=',255-comb(9,8),'checked_rational_bounds_and_256_characters')
