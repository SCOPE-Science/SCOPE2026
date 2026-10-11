#!/usr/bin/env python3
"""Reproduce algebraic identities and illustrative high-energy quadratures.

Only the analytical argument proves the infinite-energy theorem.
"""
import math

# Differentiating g^2*y^2/2 + V gives g^2*y*(yprime+(k*x-a)*y^2+x).
# Substitute yprime = -x+(a-k*x)*y^2 by exact integer coefficient arithmetic.
for a in (-7, -1, 0, 2, 11):
    for k in (1, 2, 5):
        for x in (-4, -1, 0, 3):
            for y in (-2, -1, 0, 4):
                yp = -x + (a-k*x)*y*y
                assert yp+(k*x-a)*y*y+x == 0
                # d^2 W/dq^2 = 1+x*(k*x-a), from W'(q)=x*g(x).
                assert 1+x*(k*x-a) == 1+k*x*x-a*x

def simpson(fun, left, right, n=16000):
    assert n % 2 == 0
    h=(right-left)/n
    val=fun(left)+fun(right)
    for i in range(1,n):
        val+=(4 if i%2 else 2)*fun(left+i*h)
    return val*h/3

# For a=0,k=1, right turn A has E=(exp(A*A)-1)/2.
# Exactly T=4 integral_0^(pi/2) [A*cos(theta)/sqrt(expm1(A*A*cos(theta)^2))] dtheta.
# The removable right-end value of the bracket is 1.
def period(A):
    def integrand(theta):
        u=A*math.cos(theta)
        return 4*u/math.sqrt(math.expm1(u*u)) if abs(u)>1e-9 else 4.0
    return simpson(integrand,0,math.pi/2)

ratios=[]
for A in (3,5,8):
    e_log=math.log(math.expm1(A*A)/2)
    ratio=period(A)*math.sqrt(e_log)/(2*math.pi)
    ratios.append(ratio)
assert ratios[0]>ratios[1]>ratios[2]>1
assert abs(ratios[2]-1)<0.007
print('CHECK_OK; illustrative scaled period ratios:',*[round(v,8) for v in ratios])
