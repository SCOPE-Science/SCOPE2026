#!/usr/bin/env python3
import math
from math import gcd

def count_layer(E, d, B):
    if E <= B:
        return 0
    mmax = int(math.floor(d * math.sqrt(E - B) / math.pi))
    total = 0
    for m in range(1, mmax + 1):
        transverse = (math.pi * m / d) ** 2
        total += max(0, int(math.floor((E - transverse + B) / (2.0 * B))))
    return total

def count_flat(E, s, B):
    return count_layer(E, s, B)

cases = [(1,1,1.0,1.3), (1,2,0.8,0.7), (2,3,1.1,2.0), (3,5,0.6,1.0)]
for p,q,s,B in cases:
    assert gcd(p,q) == 1
    d1, d2 = p*s, q*s
    for r in range(1,5):
        m1, m2 = p*r, q*r
        k1 = math.pi*m1/d1
        k2 = math.pi*m2/d2
        assert abs(k1-k2) < 1e-12
        assert abs(math.sin(math.pi*r*(-q))) < 1e-10
        assert abs(math.sin(0.0)) < 1e-15
        assert abs(math.sin(math.pi*r*p)) < 1e-10
        printed_sum = k1*k1 + k2*k2
        common_square = (math.pi*r/s)**2
        assert abs(printed_sum - 2.0*common_square) < 1e-10*max(1.0, common_square)
    E = 2_000_000.0
    nf = count_flat(E,s,B)
    nd = count_layer(E,d1,B) + count_layer(E,d2,B)
    cf = s/(3.0*math.pi*B)
    cd = s*(p+q)/(3.0*math.pi*B)
    normf = nf/(E**1.5)
    normd = nd/(E**1.5)
    assert abs(normf/cf - 1.0) < 0.02
    assert abs(normd/cd - 1.0) < 0.02
    assert abs(nf/nd - 1.0/(p+q)) < 0.01

print("VERIFY_OK cases=4")
