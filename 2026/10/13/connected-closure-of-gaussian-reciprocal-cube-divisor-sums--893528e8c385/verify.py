#!/usr/bin/env python3
"""Exact certificate for the connected Gaussian reciprocal-cube divisor-sum closure.
Only standard-library integer and rational arithmetic is used.
"""
from math import isqrt
from fractions import Fraction

WITNESSES = [37, 53, 73, 97, 137, 181, 241, 317, 421, 557, 733, 953, 1249, 1637, 2129, 2777, 3613, 4721, 6173, 8053, 10477, 13633, 17729, 23053, 29989, 38993, 50741, 65981, 85781, 111521, 145009, 188533, 245129, 318677, 414313, 538621, 700229, 910361, 1183477, 1538569, 2000153, 2600209, 3380281, 4394413, 5712737, 7426589, 9654577, 12550957, 16316249, 21211181, 27574549, 35846917, 46601021, 60581501, 78755953, 102382769, 133097609, 173026913, 224934989, 292415509, 380140169, 494182313, 642437053, 835168177, 1085718661, 1411434313, 1834864609, 2385324001, 3100921217, 4031197589, 5240556973, 6812724097, 8856541433]
INITIAL_NORMS = (2,5,5,9,13,13,17,17,29,29,37,37,41)
SCALE = 10**8

def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def bounds_x(n):
    # x=n^{-3/2} and sqrt(n) is enclosed by exact integer square-root bounds.
    lo=isqrt(n*SCALE*SCALE)
    assert lo*lo <= n*SCALE*SCALE < (lo+1)**2
    return (Fraction(SCALE,n*(lo+1)), Fraction(SCALE,n*lo))

def verify():
    assert WITNESSES[0]==37 and 2*WITNESSES[0]<3*29
    assert WITNESSES[-1]>=8_000_000_000
    for j,q in enumerate(WITNESSES):
        assert q%4==1 and is_prime(q), q
        if j: assert 2*q<3*WITNESSES[j-1], (WITNESSES[j-1],q)
    # We need check only the second copy of repeated norms and the inert norm 9,
    # plus norm 2; the first copy of 5, 13, 17 has a same-norm factor immediately following.
    for i in [0,2,3,5,7]:
        n=INITIAL_NORMS[i]
        lo_product=Fraction(1)
        for v in INITIAL_NORMS[i+1:]:
            lo_product *= (1+bounds_x(v)[0])
        upper_required=1+bounds_x(n)[1]
        assert lo_product>upper_required,(i,n,lo_product,upper_required)
    # Universal bound for two split ideals at a rational prime q <=3N/2:
    # 2/q^{3/2} >= 2/(3N/2)^{3/2} > 1/N^{3/2}, since 4>27/8.
    assert 4*8>27
    print('EXACT_CERTIFICATE_OK witnesses=%d start=%d last=%d small_cases=5 initial_norms=%d'%
          (len(WITNESSES),WITNESSES[0],WITNESSES[-1],len(INITIAL_NORMS)))
if __name__=='__main__': verify()
