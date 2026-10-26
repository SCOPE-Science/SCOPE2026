#!/usr/bin/env python3
"""Independent finite examples and direct inequality tests for BPR Wardrop bounds.
Requires Python 3 and scipy. This numerical exercise does not establish the universal theorem.
"""
from math import isclose
from scipy.optimize import brentq

# For parallel arcs c_1(x)=x^p, c_2(x)=1+x^p and total demand t,
# the all-interior Wardrop condition gives c_1(t/2+d)=c_2(t/2-d).
def arc_shift(p,t):
    if t<=1:
        return t/2
    return brentq(lambda d:t**3*d+4*t*d**3-1,0,t/2) if p==4 else brentq(lambda d:(t/2+d)**p-(t/2-d)**p-1,0,t/2)

checks=0
for p in (1,2,3,4,5):
    for t in (0.1,0.5,1,2,5,10,20,100):
        d=arc_shift(p,t)
        x1,x2=t/2+d,t/2-d
        assert x1>=0 and x2>=-1e-9
        assert (2*abs(d)**(p+1))**(1/(p+1))<=1+1e-8
        checks+=1
        if t>1:
            assert isclose(x1**p-x2**p,1,rel_tol=1e-7,abs_tol=1e-6)
            checks+=1
for t in (2,3,10):
    d=arc_shift(4,t)
    assert abs(t**3*d-1)<6/max(t,2)**8
    checks+=1
# Integer convexity inequality used in the global variational proof.
for p in range(1,7):
    for u in (0,0.1,0.4,1,2,7):
        for v in (0,0.1,0.4,1,2,7):
            assert (u**p-v**p)*(u-v)+1e-10>=abs(u-v)**(p+1)
            checks+=1
print('PASS:',checks,'finite checks; universal and semialgebraic arguments are analytical')
