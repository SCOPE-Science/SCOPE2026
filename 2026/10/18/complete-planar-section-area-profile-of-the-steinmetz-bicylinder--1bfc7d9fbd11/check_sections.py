#!/usr/bin/env python3
"""Independent numerical and symbolic checks for central bicylinder sections."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import sympy as sp


def formula(a,b,c):
    a,b,c=sorted((abs(float(a)),abs(float(b))),reverse=True)[0], sorted((abs(float(a)),abs(float(b))),reverse=True)[1],abs(float(c))
    r=math.sqrt(a*a+b*b+c*c)
    if r==0: raise ValueError('nonzero normal required')
    if a==0:return 4.0
    if b==0:
        if c==0:return math.pi
        return (2*r/a)*(math.atan2(a,c)+a*c/(a*a+c*c))
    if c==0:return math.pi*r/a
    return r/(a*b)*((a+b)*math.atan((a+b)/c)-(a-b)*math.atan((a-b)/c))


def polar_area(a,b,c,N=65536):
    u=np.array([a,b,c], dtype=float);u/=np.linalg.norm(u)
    w=np.cross(u,[0.,0.,1.]); nw=np.linalg.norm(w)
    if nw<1e-12:w=np.array([1.,0.,0.])
    else:w/=nw
    v=np.cross(u,w)
    angles=(np.arange(N)+0.5)*2*math.pi/N
    x=w[0]*np.cos(angles)+v[0]*np.sin(angles)
    y=w[1]*np.cos(angles)+v[1]*np.sin(angles)
    z=w[2]*np.cos(angles)+v[2]*np.sin(angles)
    return math.pi*np.mean(1/np.maximum(x*x+z*z,y*y+z*z))


def slice_area(a,b,c):
    a,b=sorted((abs(float(a)),abs(float(b))),reverse=True)
    c=abs(float(c));rho=math.sqrt(a*a+b*b+c*c)
    if not a:return 4.
    if not b:
        lim=a/rho
        return 4*rho/a*quad(lambda z: math.sqrt(max(0,1-z*z)),0,lim,epsabs=1e-11)[0]
    low=(a-b)/math.hypot(c,a-b) if a!=b or c else 0.
    high=(a+b)/math.hypot(c,a+b)
    lowterm=4*rho/a*quad(lambda z: math.sqrt(max(0,1-z*z)),0,low,epsabs=1e-11)[0]
    highterm=2*rho/(a*b)*quad(lambda z:(a+b)*math.sqrt(max(0,1-z*z))-c*z,low,high,epsabs=1e-11)[0]
    return lowterm+highterm


a,b,c,r,t=sp.symbols('a b c r t', positive=True, real=True)
X,Y=sp.symbols('X Y', positive=True, real=True)
left=sp.cancel((c*X/(c**2+t**2*X)-c*Y/(c**2+t**2*Y))/(X-Y))
assert sp.simplify(left-c**3/((c**2+t**2*X)*(c**2+t**2*Y)))==0
print('SYMBOLIC_SECANT_IDENTITY_OK')

rng=np.random.default_rng(20261017)
cases=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),(1,1,1),(1,0,1),(3,2,1),(1,1,5)]
cases+=[(float(x),float(y),float(z)) for x,y,z in rng.normal(size=(150,3))]
worst_polar=worst_slice=0
for aa,bb,cc in cases:
    f=formula(aa,bb,cc)
    pol=polar_area(aa,bb,cc,16384)
    sl=slice_area(aa,bb,cc)
    worst_polar=max(worst_polar,abs(f-pol));worst_slice=max(worst_slice,abs(f-sl))
    assert abs(f-pol)<2e-5, (aa,bb,cc,f,pol)
    assert abs(f-sl)<2e-9, (aa,bb,cc,f,sl)
    assert math.pi-1e-9<=f<=math.pi*math.sqrt(2)+1e-9
print('INDEPENDENT_POLAR_AND_CHORD_QUADRATURE_OK',len(cases),'max_errors',worst_polar,worst_slice)

for cc in [0.01,0.15,0.5,1,2,8,50]:
    p=1.
    grid=np.linspace(0,math.pi/4,300)
    vals=[formula(math.cos(theta),math.sin(theta),cc) for theta in grid]
    assert min(np.diff(vals))>1e-12
print('DIRECTIONAL_BALANCING_MONOTONICITY_OK 7x300')

def T(rr):
    return rr*(rr*rr+4)*math.atan(2/rr)-2*(rr*rr+2)
def Tint(rr):
    return quad(lambda tau:(rr*rr*(2-tau*tau)-2*tau*tau)/(rr*rr+tau*tau),0,2,epsabs=2e-12)[0]
for rr in [0.05,0.25,0.5,1,2,3,5,10,30,100]:
    assert abs(T(rr)-Tint(rr))<1e-9
root=brentq(T,1e-5,100,xtol=1e-12)
F=lambda rr:2*math.hypot(rr,math.sqrt(2))*math.atan(2/rr)
assert 1.32<root<1.321
assert 3.8203<F(root)<3.8205
assert abs(F(1e-10)-math.pi*math.sqrt(2))<1e-9
assert abs(F(1e9)-4)<1e-9
assert abs(formula(1,0,0)-math.pi)<1e-15
assert abs(formula(1,1,0)-math.pi*math.sqrt(2))<1e-15
print('MERIDIAN_ONE_MINIMUM_AND_EXTREME_SECTIONS_OK root=%.12f value=%.12f'% (root,F(root)))
print('ALL_BICYLINDER_SECTION_CHECKS_OK')
