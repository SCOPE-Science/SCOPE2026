#!/usr/bin/env python3
import math

def C(theta):
    return abs(math.sin(2.0*theta))

def ratio(theta):
    # Away from cusps: |dC/dtheta| / sqrt(F_Q), sqrt(F_Q)=2.
    return abs(math.cos(2.0*theta))

for t in (0.1, 0.3, 0.7, 1.0):
    assert 0.0 <= ratio(t) < 1.0

# One-sided derivatives at theta=0 are +2 and -2.
for h in (1e-3, 1e-5, 1e-7):
    right=(C(h)-C(0.0))/h
    left=(C(-h)-C(0.0))/(-h)
    assert abs(right-2.0) < 5*h
    assert abs(left+2.0) < 5*h

# Hence the two-sided derivative cannot exist, although |one-sided slope|=sqrt(F_Q)=2.
print('VERIFY_OK')
