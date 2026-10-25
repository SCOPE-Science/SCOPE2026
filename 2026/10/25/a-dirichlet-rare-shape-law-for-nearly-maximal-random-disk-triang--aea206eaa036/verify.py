#!/usr/bin/env python3
"""Reproducible numerical checks of a near-maximal disk-triangle shape theorem.
Only scientific formulas and deterministic random seeds are used.
"""
import numpy as np
from math import pi,sqrt,gamma
M=3*sqrt(3)/4
c=sqrt(3)/2
B=(sqrt(3)/8)*np.array([[2.,1.],[1.,2.]])
ev,Q=np.linalg.eigh(B)
Bi=(Q/np.sqrt(ev))@Q.T
detB=sqrt(np.linalg.det(B))
assert abs(detB-3/8)<1e-13
assert abs(c-sqrt(3)/2)<1e-13

def triangle_area(t,x,y):
    r=1-t
    return .5*(r[:,0]*r[:,1]*np.sin(2*pi/3+x)
            +r[:,1]*r[:,2]*np.sin(2*pi/3+y)
            +r[:,2]*r[:,0]*np.sin(2*pi/3-x-y))

def analytic_constant(b,a,lam):
    # p(theta)=[1+lam cos(3theta)]/(2*pi), 0 <= lam < 1
    I=(1+1.5*lam*lam)/(4*pi*pi)
    return (16*pi/3)*I*a**3*c**(-3*b)*gamma(b)**3/gamma(3*b+2)
assert abs(analytic_constant(1,2,0)-32/(27*sqrt(3)*pi))<1e-13
print('EXACT_RADIAL_ANGULAR_CONSTANTS_OK',analytic_constant(1,2,0))
# Check independent angular triple correlation by midpoint quadrature.
for lam in (0,.25,.6):
    phi=2*pi*(np.arange(10000)+0.5)/10000
    p=lambda x:(1+lam*np.cos(3*x))/(2*pi)
    I=np.mean(p(phi)*p(phi+2*pi/3)*p(phi+4*pi/3))*2*pi
    assert abs(I-(1+1.5*lam*lam)/(4*pi*pi))<2e-13
print('EXACT_THREEFOLD_ANGULAR_CORRELATION_OK')
# Normal form independently checked by central finite differences.
h=1e-4
T=np.zeros((3,3));np.fill_diagonal(T,h)
for i in range(3):
    assert abs((M-triangle_area(T[[i]],np.zeros(1),np.zeros(1))[0])/h-c)<1e-9
for x,y in [(h,0),(0,h),(h,h),(h,-h)]:
    v=np.array([x,y]);q=float(v@B@v)
    t=np.zeros((1,3)); A=triangle_area(t,np.array([x]),np.array([y]))[0]
    assert abs((M-A)/q-1)<4e-5
print('NONDEGENERATE_MIXED_NORMAL_FORM_OK')
# Importance sample in neighborhoods of both regular triangles, reconstruct
# the exact triangle area for sampled polar coordinates, compare coefficients.
rng=np.random.default_rng(20261020)
U=1.4; V=1.4
for b,a,lam,eps,N in [(1,2,0,.02,1_600_000),(1,2,0,.005,1_600_000),
                      (2,2,.35,.008,1_600_000),(.5,.5,0,.008,1_600_000)]:
    u=rng.uniform(0,U,(N,3))
    psi=rng.uniform(0,2*pi,N)
    radial=np.sqrt(V*rng.uniform(0,1,N))
    z=np.stack([radial*np.cos(psi),radial*np.sin(psi)])
    xy=np.sqrt(eps)*(Bi@z)
    t=eps*u/c
    valid=np.all(t<=1,axis=1)
    deficit=M-triangle_area(t,xy[0],xy[1])
    ind=valid & (deficit<eps)
    phi=rng.uniform(0,2*pi,N)
    p=lambda theta:(1+lam*np.cos(3*theta))/(2*pi)
    ang=p(phi)*p(phi+2*pi/3+xy[0])*p(phi+4*pi/3+xy[0]+xy[1])
    prod=np.prod(u**(b-1),axis=1)
    # Original angular density p(phi)p(theta2)p(theta3), and exact radial g(t)=b*t^(b-1).
    pref=(4*pi)*((a/c**b)**3)/detB*(U**3*pi*V)
    weight=pref*prod*ang*ind
    actual=weight.mean()
    expected=analytic_constant(b,a,lam)
    se=weight.std()/np.sqrt(N)
    print('WEIGHTED_ASYMPTOTIC',b,lam,eps,actual,expected,actual/expected,'SE',se,'hits',ind.sum())
    assert abs(actual/expected-1) < .075
    if b==2:
        w=weight[ind]
        shares=np.concatenate([u[ind],np.sum(z[:,ind]**2,axis=0)[:,None]],axis=1)
        mean=(shares*w[:,None]).sum(axis=0)/w.sum()
        print('CONDITIONAL_SHARE_MEANS',mean,'expected',(b/(3*b+2),)*3+(1/(3*b+2),))
        assert max(abs(mean[:3]-b/(3*b+2)))<.02
        assert abs(mean[3]-1/(3*b+2))<.02
print('ALL_GEOMETRIC_SHAPE_LAW_CHECKS_OK')
