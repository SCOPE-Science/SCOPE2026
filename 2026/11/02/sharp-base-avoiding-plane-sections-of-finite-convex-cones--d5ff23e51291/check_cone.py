#!/usr/bin/env python3
"""Numerical checks of cap-free isotropic plane sections in convex cones."""
import numpy as np
from scipy.integrate import quad
from math import pi, atan, sqrt

def f(h,H):
    return H-h*atan(H/h) if h>0 else H

def support(shape, ang, r):
    a=pi*r/2
    if shape=='disk':return r
    if shape=='segment':return a*abs(np.cos(ang))
    if shape=='ellipse':
        # exact perimeter normalization via elliptic integral quadrature
        from scipy.special import ellipe
        A=1.5; B=0.4; m=1-(B/A)**2
        s=pi*r/(2*A*ellipe(m))
        return s*np.sqrt(A*A*np.cos(ang)**2+B*B*np.sin(ang)**2)
    if shape=='rectangle':
        v=1.24;w=pi*r/2-v
        return v*abs(np.cos(ang))+w*abs(np.sin(ang))
    if shape=='diamond':
        # vertices ±(a,0), ±(0,b); perimeter 4 sqrt(a²+b²)=2πr
        v=.91;w=np.sqrt((pi*r/2)**2-v*v)
        return max(v*abs(np.cos(ang)),w*abs(np.sin(ang)))
    raise ValueError(shape)

def integral(shape,H,r):
    F=quad(lambda x:f(support(shape,x,r),H),0,2*pi,epsabs=3e-11,limit=400,points=[0,pi/2,pi,3*pi/2])[0]/(2*pi)
    return F/(F+pi*r),F

rng=np.random.default_rng(20261029)
for H in [0.05,0.35,1.5,5.0,22.0]:
    r=1.; lo=f(r,H); hi=sqrt(H*H+(pi*r/2)**2)-pi*r/2
    assert 0<lo<hi
    for shape in ['disk','diamond','ellipse','rectangle','segment']:
        p,F=integral(shape,H,r)
        assert lo-1e-9 <= F <=hi+1e-9,(H,shape,F,lo,hi)
        if shape=='disk':assert abs(F-lo)<1e-10
        if shape=='segment':assert abs(F-hi)<1e-10
        print('EXACT_ANGULAR_QUADRATURE',H,shape,round(p,12),round(F,12))
print('EXACT_SHARP_ENDPOINTS_PASSED')
# The circular-cone total plane measure agrees with the classical mean-width formula.
for H in [0.05,0.35,1.5,5.0,22.0]:
    r=1.
    _,N=integral('disk',H,r)
    assert abs(pi*r+N-(H+pi-atan(H)))<1e-10
print('CIRCULAR_CONE_MEAN_WIDTH_NORMALIZATION_PASSED')

# Check independent joint normal-offset sampling via normal direction uniform on upper hemisphere,
# offset uniform in a common global bounding interval. Counts conditioned on hitting cone.
for shape in ['disk','ellipse','rectangle','diamond']:
    H=1.5;r=1.;n=500000
    az=rng.uniform(0,2*pi,n)
    v=rng.uniform(0,1,n); s=np.sqrt(1-v*v)
    hs=np.array([support(shape,a,r) for a in az])
    low=np.minimum(0,H*v-s*hs); high=np.maximum(0,H*v+s*hs)
    top=H*v-s*hs
    # for normals with vertical component positive, apex-only iff top>0, t∈(0,top)
    T=H+2.*max(pi*r/2,H)
    offsets=rng.uniform(-T,T,n)
    hit=(offsets>low)&(offsets<high)
    capfree=hit&(offsets>0)&(offsets<top)
    p_emp=capfree.sum()/hit.sum()
    p_exact,_=integral(shape,H,r)
    sigma=np.sqrt(p_exact*(1-p_exact)/hit.sum())
    print('INDEPENDENT_JOINT_NORMAL_OFFSET',shape,hit.sum(),p_emp,p_exact,'z',abs(p_emp-p_exact)/sigma)
    assert abs(p_emp-p_exact)<6*sigma+0.002
# A thin full-dimensional rectangle has a nontrivial height/width crossover.
# Compare the singular limit with direct finite-height angular integrations.
for kappa in [0., .25, 1., 3.]:
    r=1.; a=pi*r/2
    c=(1+kappa*kappa)*(pi/2 if kappa==0 else atan(1/kappa))-kappa
    prediction=2*c/(pi**3*r*r)
    H=.001
    b=H**2 if kappa==0 else kappa*H
    assert 0<b<a
    aa=a-b
    F=(2/pi)*quad(lambda x:f(aa*np.cos(x)+b*np.sin(x),H),0,pi/2,epsabs=1e-12,limit=700)[0]
    empirical=F/(pi*r+F)/H**2
    assert abs(empirical-prediction)<.008, (kappa,prediction,empirical)
    print('THIN_RECTANGLE_TRANSITION',kappa,round(prediction,10),round(empirical,10))
print('THIN_RECTANGLE_CROSSOVER_PASSED')
print('ALL_CHECKS_PASSED')
