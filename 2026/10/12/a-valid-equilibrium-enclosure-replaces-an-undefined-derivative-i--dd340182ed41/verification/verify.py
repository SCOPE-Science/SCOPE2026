#!/usr/bin/env python3
import math

def bisect(fn,a,b,it=120):
    fa,fb=fn(a),fn(b)
    assert fa>0 and fb<0
    for _ in range(it):
        m=(a+b)/2
        fm=fn(m)
        if fm>0:a=m
        else:b=m
    return (a+b)/2

# The printed inverse argument is positive for the theorem's parameter range,
# while admissible decreasing convex examples have nonpositive derivatives.
for r in (0.1,0.35,0.8):
    for e in (0.1,0.4,0.9):
        assert (1-r)/e > 0

for k in (1,2,3,4):
    for r in (0.1,0.35,0.8):
        for e in (0.1,0.4,0.9):
            # p_*=1, pi(P)=(1-P)^k.
            def pi(p): return (1-p)**k
            def dp(p): return -k*(1-p)**(k-1)
            def f(p): return -r-e*dp(p)*(1-p)+pi(p)
            p0=bisect(f,0.0,1.0)
            pr=1-r**(1/k)
            def h(p): return 1-p-r-e*dp(p)*(1-p)
            bar=bisect(h,0.0,1.0)
            U=(1-r-e*dp(0.0))/(1-e*dp(0.0))
            assert pr < p0 + 1e-12
            assert p0 <= bar + 1e-12
            assert bar <= min(1.0,U) + 1e-12
            assert dp(p0) <= 1e-14
            if k==1:
                exact=1-r/(1+e)
                assert abs(p0-exact)<1e-12
                assert abs(U-exact)<1e-12
print('VERIFY_OK')
