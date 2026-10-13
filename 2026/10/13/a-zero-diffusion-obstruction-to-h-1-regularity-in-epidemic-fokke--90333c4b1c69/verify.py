#!/usr/bin/env python3
"""Exact rational premise checks for a characteristic-transport example."""
from fractions import Fraction as Q

one=Q(1)
zero=Q(0)
ten=Q(10)

def Fs(s,i): return one-s-s*i/ten
def Fi(s,i): return (s/ten-2)*i

def div(s,i): return -3+(s-i)/ten

# Inward/tangent boundary signs for square [0,2]^2.
for i in (zero,one,Q(2)):
    assert Fs(zero,i)==one
    assert Fs(Q(2),i)<=-one
for s in (zero,one,Q(2)):
    assert Fi(s,zero)==zero
    assert Fi(s,Q(2))<=Q(-18,5)
# On S+I=1, total drift = -I, proving simplex invariance.
for i in (zero,Q(1,5),Q(1,2),one):
    s=one-i
    assert Fs(s,i)+Fi(s,i)==-i
# Initial square and physical region, exactly.
lo=Q(1,5);hi=Q(2,5)
assert 25*(hi-lo)**2==1
assert 25**2*(hi-lo)**2==25
assert 2*hi<1
# Divergence of the drift and strict finite-time flow determinant.
for s in (lo,hi):
    for i in (lo,hi):
        assert (-one-i/ten)+(s/ten-2)==div(s,i)
print('VERIFY_OK')
