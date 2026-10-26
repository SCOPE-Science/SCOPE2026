#!/usr/bin/env python3
"""Independent reproducibility arithmetic for the biquadratic monotone-data range."""
from fractions import Fraction as Q
from itertools import product

def weights(t):
    return ((1-t)*(1-2*t),4*t*(1-t),t*(2*t-1))

def isotone(bits):
    return all(bits[3*i+j] <= bits[3*(i+1)+j] for i in range(2) for j in range(3)) and all(bits[3*i+j] <= bits[3*i+j+1] for i in range(3) for j in range(2))

def interp(bits,x,y):
    a,b=weights(x),weights(y)
    return sum((a[i]*b[j]*bits[3*i+j] for i in range(3) for j in range(3)),Q(0))

upsets=[b for b in product((0,1),repeat=9) if isotone(b)]
assert len(upsets)==20
for k in range(17):
    for l in range(17):
        x,y=Q(k,16),Q(l,16)
        assert sum(weights(x)) == sum(weights(y)) == 1
        for f in upsets:
            value=interp(f,x,y)
            assert -Q(17,64) <= value <= Q(81,64)

step=tuple(int(i==2 or j==2) for i in range(3) for j in range(3))
assert isotone(step) and interp(step,Q(1,4),Q(1,4)) == -Q(17,64)
reflected=tuple(1-step[3*(2-i)+(2-j)] for i in range(3) for j in range(3))
assert isotone(reflected) and interp(reflected,Q(3,4),Q(3,4)) == Q(81,64)
print("Exact sample-grid and two sharpness-witness checks passed; continuum proof is in RESULT.md")
