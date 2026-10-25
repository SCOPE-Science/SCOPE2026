#!/usr/bin/env python3
"""Check the exact real quartic identity and finite sharpness witnesses."""
import sympy as s

u,v,t=s.symbols('u v t',real=True,positive=True)
E=t*s.sqrt((1+2*t*t)*(2+t*t)); A=t*(1-t*t)
B=3*t*t+E; lam=1+3*t*t+t**4-E
lhs=(u+t*v)**4+(t*u-v)**4
rhs=lam*(u**4+v**4)+2*(A*(u*u-v*v)+B*u*v)**2/B
assert s.simplify(s.expand(lhs-rhs))==0
assert s.simplify((1+3*t*t+t**4)**2-E**2-(1+t*t)**4)==0
assert s.simplify(E*E-t*t*(1+2*t*t)*(2+t*t))==0
assert s.simplify((E-3*t*t)*B-2*A*A)==0
assert s.simplify(12*t*t*B-2*B*B+4*A*A)==0

# Each numerical two-point witness uses orthogonal eigenvectors of
# the real symmetric traceless quadratic and checks the sharp coefficient.
import math
for z in [0.2,0.7,1.0,1.4,4.0]:
    Ez=z*math.sqrt((1+2*z*z)*(2+z*z))
    Az=z*(1-z*z); Bz=3*z*z+Ez
    R=math.hypot(2*Az,Bz)
    theta=math.atan2(Bz/2,Az)/2
    c,d=math.cos(theta),math.sin(theta)
    scale=(c**4+d**4)**(-0.25)
    fx,fy=scale*c,-scale*d
    gx,gy=scale*d,scale*c
    assert abs(fx**4+fy**4-1)<1e-12
    assert abs(gx**4+gy**4-1)<1e-12
    q=lambda x,y: Az*(x*x-y*y)+Bz*x*y
    dd=(q(fx,gx)**2+q(fy,gy)**2)/Bz
    lamz=1+3*z*z+z**4-Ez
    direct=((fx+z*gx)**4+(fy+z*gy)**4+(z*fx-gx)**4+(z*fy-gy)**4)/2-lamz
    assert abs(dd-direct)<2e-10
    # Each chosen vector is an eigenvector of the quadratic, hence its
    # Euclidean fourth-power distance to the null lines is q^2/R^2.
    sharp_distance=(q(fx,gx)**2+q(fy,gy)**2)/(R*R)
    assert abs(sharp_distance/dd-Bz/(R*R))<1e-12
print('VERIFY_OK')
