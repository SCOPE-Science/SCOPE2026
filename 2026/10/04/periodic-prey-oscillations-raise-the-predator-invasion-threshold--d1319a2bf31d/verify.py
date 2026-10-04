#!/usr/bin/env python3
import math

def F(u,r):
    return u*math.exp(r*(1-u))-(2-u)

def bisect(a,b,r,n=200):
    fa,fb=F(a,r),F(b,r)
    assert fa*fb<0
    for _ in range(n):
        m=(a+b)/2
        fm=F(m,r)
        if fa*fm<=0:
            b,fb=m,fm
        else:
            a,fa=m,fm
    return (a+b)/2

r=2.2
# bracket the lower member of the nontrivial 2-cycle; u=1 is a separate root
u=bisect(0.3,0.8,r)
v=2-u
assert abs(v-u*math.exp(r*(1-u)))<1e-13
assert abs(u-v*math.exp(r*(1-v)))<1e-13
assert abs((u+v)-2)<1e-13
prod=u*v
threshold=1/math.sqrt(prod)
R0=1.1
pred_mult=(R0**2)*prod
prey_mult=(1-r*u)*(1-r*v)
assert abs(prod-0.747050778074353)<1e-12
assert abs(threshold-1.1569775681472)<1e-12
assert abs(pred_mult-0.903931441469967)<1e-12
assert abs(prey_mult-0.215725765879869)<1e-12
assert 1<R0<threshold
assert abs(pred_mult)<1 and abs(prey_mult)<1
print('VERIFY_OK')
