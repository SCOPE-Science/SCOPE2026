#!/usr/bin/env python3
"""Finite checks for the level-balanced Cesaro-shift power identity.

Uses finite-support sequences and an infinite-tail evaluation, and checks
explicitly the first three levels of an unevenly branching tree.
Neither finite checking nor float arithmetic proves the general theorem.
"""
from math import isclose
import random
from mpmath import mp, zeta

mp.dps = 55

def ces_norm(a, p):
    a = list(map(mp.mpf, a))
    if not a:
        return mp.mpf('0')
    prefix = mp.mpf('0')
    total = mp.mpf('0')
    for k in range(len(a)-1):
        prefix += abs(a[k])
        total += (prefix / (k+1))**p
    prefix += abs(a[-1])
    total += prefix**p * zeta(p, len(a))
    return total**(1/p)

rng = random.Random(22031)
tests=0
for p in [mp.mpf('1.15'),mp.mpf('1.5'),mp.mpf('2'),mp.mpf('3.5'),mp.mpf('6')]:
    for n in range(1,10):
        sharp = (zeta(p)/zeta(p,n+1))**(1/p)
        delta=[mp.mpf('0')]*n+[mp.mpf('1')]
        assert mp.almosteq(ces_norm(delta[n:],p)/ces_norm(delta,p), sharp)
        tests+=1
        for _ in range(32):
            a=[mp.mpf(rng.randrange(0,101))/100 for _ in range(14)]
            source=ces_norm(a,p)
            if source:
                ratio=ces_norm(a[n:],p)/source
                assert ratio<=sharp+mp.mpf('1e-35')
                tests+=1

# Tree: root -> (u,v); u -> (a,b,c), v -> (d).
# Thus (c_0,c_1,c_2)=(1,2,4). For a level-2 input, the second
# weighted iterate is gamma^2 * (sum of level-2 coefficients)/4.
gamma=mp.mpf('1.3')
vals=[mp.mpf('2'),mp.mpf('1'),mp.mpf('0.5'),mp.mpf('4')]
first_u=gamma*mp.mpf(2)/4*sum(vals[:3])
first_v=gamma*mp.mpf(2)/4*vals[3]
second=gamma*mp.mpf(1)/2*(first_u+first_v)
assert mp.almosteq(second,gamma**2*sum(vals)/4)
tests+=1
print('Passed',tests,'finite scalar/tree checks; not a proof.')
