#!/usr/bin/env python3
import math

def pois(lam,k):
    return math.exp(-lam)*lam**k/math.factorial(k)

def formula(eps):
    return math.exp(-1.0-eps/2.0)*(1.0+1.5*eps+eps**3/6.0)

def direct(eps):
    a=eps
    b=1.0-eps/2.0
    total=0.0
    for n in range(0,8):
        for m in range(0,8):
            x=n+2*m
            if 1 <= x <= 3:
                total += pois(a,n)*pois(b,m)
    return total

maxerr=0.0
for eps in (1e-6,1e-4,0.01,0.1,0.5,1.0,1.9):
    assert 0.0 < eps < 2.0
    mean=eps+2.0*(1.0-eps/2.0)
    var=eps+4.0*(1.0-eps/2.0)
    sd=math.sqrt(var)
    assert abs(mean-2.0) < 1e-15
    assert abs(var-(4.0-eps)) < 1e-15
    assert 1.0 < sd < 2.0
    f=formula(eps)
    d=direct(eps)
    maxerr=max(maxerr,abs(f-d))
    assert abs(f-d) < 1e-14

target=math.exp(-1.0)
assert abs(formula(1e-9)-target) < 2e-9
print(f"VERIFY_OK target={target:.15f} formula_error<1e-14")
