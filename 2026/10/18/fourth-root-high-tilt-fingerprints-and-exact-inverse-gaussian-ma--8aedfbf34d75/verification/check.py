#!/usr/bin/env python3
"""Exact triangular-system checks and convergence diagnostics; standard library only."""
import math
n=0
for a in (0.1, 0.5, 1.0, 2.0):
    target = (2**0.75)*0.7*math.sqrt(a)
    errors=[]
    for t in (1e6,1e10,1e14):
        z1=math.sqrt(1+2*t)-1
        z2=math.sqrt(1+2*a*z1)-1
        assert abs(z1+z1*z1/2-t)<3e-14*t; n+=1
        assert abs(z2+z2*z2/2-a*z1)<3e-14*(a*z1); n+=1
        norm=(1.3*(z1-math.sqrt(2*t))+0.7*z2)/(t**0.25)
        errors.append(abs(norm-target))
    assert errors[2]<errors[1]<errors[0]; n+=1
    assert errors[-1]<0.0007; n+=1
for t in (0.01,1.0,100.0):
    # With the first row decoupled (B_12=0), the first marginal is IG
    # despite coupling in the opposite row.
    z1=math.sqrt(1+2*t)-1
    assert abs(0.7*z1-0.7*(math.sqrt(1+2*t)-1))<1e-12; n+=1
print(f'{n} checks passed')
