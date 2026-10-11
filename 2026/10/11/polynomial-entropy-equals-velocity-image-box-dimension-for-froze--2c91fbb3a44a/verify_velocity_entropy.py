"""Finite arithmetic checks supporting the velocity-image entropy theorem.
The infinite covering and separated-set estimates are proved analytically.
"""
from fractions import Fraction
from math import ceil

def circ(t):
    t = t % 1
    return min(t, 1-t)

def hit(delta,n,eps):
    return max(circ(j*delta) for j in range(n)) >= eps

count=0
for n in (10, 20, 40, 80, 160):
    eps=Fraction(1,32)
    for numerator in range(1,200):
        delta=Fraction(numerator,1000)
        if circ(delta) >= 4*eps/n:
            assert hit(delta,n,eps), (delta,n)
            count+=1
for k in range(1,9):
    assert 4**k * Fraction(1,3**k)**2 == Fraction(4,9)**k
print('PASS: %d exact circle separation tests; 8 finite Koch similarity identities' % count)
