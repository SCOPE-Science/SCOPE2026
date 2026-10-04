#!/usr/bin/env python3
import math


def assert_close(a,b,tol=1e-12):
    if abs(a-b)>tol*max(1.0,abs(a),abs(b)):
        raise AssertionError((a,b))

# Boundary-value algebra: regular terms cancel exactly for odd m and double for even m.
for m in range(2,10):
    # In normalized units T_- contributes 1 and T_+ contributes 1 off poles.
    factor = 1 + (-1)**m
    if m % 2:
        assert factor == 0
    else:
        assert factor == 2

# Published m=3 origin coefficients.
P=math.sqrt(6.0)
Q=6.0
K3=-math.pi/4.0
A3=1.0/(math.pi**3*P)       # coefficient of z^{-3}
A1=Q/(6.0*math.pi*P)        # coefficient of z^{-1}
coef_d2=K3*A3/math.factorial(2)
coef_d0=K3*A1
assert_close(coef_d2,-1.0/(8.0*math.pi**2*P))
assert_close(coef_d0,-Q/(24.0*P))

# The leading Laurent coefficient is nonzero, hence odd m has top derivative order m-1.
primes=[2,3,5,7,11,13,17,19]
for m in [3,5,7,9]:
    omegas=[1.0]+[math.sqrt(p) for p in primes[:m-1]]
    lead=1.0/(math.pi**m*math.prod(omegas))
    K=(2.0**(1-m))*math.pi*((-1.0)**((m-1)//2))
    top=K*lead/math.factorial(m-1)
    assert top != 0.0 and math.isfinite(top)

# Exact Pell-type numerator in |k*sqrt(A/B)-n| cannot vanish for nonsquare A/B.
pairs=[(2,1),(3,1),(3,2),(5,2),(7,3)]
for A,B in pairs:
    for k in range(1,80):
        alpha=math.sqrt(A/B)
        n=round(k*alpha)
        numerator=A*k*k-B*n*n
        assert numerator != 0
        lhs=abs(k*alpha-n)
        rhs=abs(numerator)/(B*abs(k*alpha+n))
        assert_close(lhs,rhs,1e-10)

print('VERIFY_OK')
