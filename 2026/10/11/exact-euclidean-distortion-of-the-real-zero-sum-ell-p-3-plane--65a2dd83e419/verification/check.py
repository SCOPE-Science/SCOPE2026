"""Reproducible finite checks for the exact zero-sum plane distortion law.
The finite tests are corroboration, not a proof of the continuum statements.
"""
import math
from fractions import Fraction

# Exact quartic identity on the integral A_2 hyperplane.
exact = 0
for a in range(-8,9):
    for b in range(-8,9):
        c = -a-b
        lhs = 2*(a**4+b**4+c**4)
        rhs = (a*a+b*b+c*c)**2
        assert lhs == rhs, (a,b,c)
        exact += 1

# Exact vanishing of derivative certificate at p=2,4.
from math import isclose
for k in range(1,1000):
    r = k/1000
    for p in (2,4):
        deriv = (2+r)*r**(p-1)+(1-r)*(1+r)**(p-1)-(1+2*r)
        assert abs(deriv) <= 1e-11

# Compare predicted end-point maximum/minimum with a dense angular grid.
tests = 0
for p in (1,1.05,1.25,1.5,1.75,2,2.1,2.5,3,3.5,3.9,4,4.1,4.5,5,7,12,25,100,math.inf):
    def f(r):
        a = math.sqrt(2*(1+r+r*r))
        if math.isinf(p):
            return (1+r)/a
        return (1+r**p+(1+r)**p)**(1/p)/a
    f0, f1 = f(0), f(1)
    lo, hi = min(f0,f1),max(f0,f1)
    for j in range(0,1001):
        val=f(j/1000)
        assert lo-4e-14<=val<=hi+4e-14, (p,j,val,lo,hi)
        tests += 1
    expected=2/math.sqrt(3) if math.isinf(p) else max((1+2**(p-1))**(1/p)/math.sqrt(3),math.sqrt(3)/(1+2**(p-1))**(1/p))
    found=hi/lo
    assert abs(found-expected)<2e-13, (p,expected,found)

print(f'VERIFY_OK quartic_exact={exact} derivative_special={1998} radial_bounds={tests} parameter_cases=20')
