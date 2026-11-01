#!/usr/bin/env python3
"""Reproducible exact and numerical checks for volume-uniform solid spherical caps."""
import sympy as sp
import numpy as np
from scipy.integrate import quad

z,t,u=sp.symbols('z t u',real=True)
vol=sp.integrate(1-z*z,(z,1-t,1))
Z=lambda k:sp.factor(sp.integrate((1-z*z)*z**k,(z,1-t,1))/vol)
z0,z1,z2,z3,z4=[Z(k) for k in range(5)]
mu=z1
rad2=(1-z2)/2
m2=(1+z2)/2
m4=(1+z2+z4)/3
mxx=(1-z2)/4
v=(z1+z3)/2
F=sp.factor(2*(m2-mu**2))
G=sp.factor(2*m4+2*m2**2+4*(2*mxx**2+z2**2)-8*mu*v)
F_ref=-3*t*(7*t**3-56*t**2+160*t-160)/(40*(t-3)**2)
G_ref=t**2*(41*t**4-410*t**3+1575*t**2-2800*t+1960)/(70*(t-3)**2)
assert sp.cancel(F-F_ref)==0 and sp.cancel(G-G_ref)==0
Q=sp.factor(G/F**2)
P=7*u**3+14*u**2+20*u+8
B=41*u**4+82*u**3+99*u**2+108*u+36
C=66*u**3+117*u**2+56*u+12
q_ref=160*(1+u)**2*B/(63*P**2)
assert sp.cancel(Q.subs(t,2-u)-q_ref)==0
assert sp.cancel(sp.diff(q_ref,u)-3200*(1+u)*u**2*C/(63*P**3))==0
assert sp.limit(q_ref,u,0)==sp.Rational(10,7)
assert sp.limit(q_ref,u,2)==sp.Rational(7,4)
assert sp.limit((q_ref-sp.Rational(10,7))/u**3,u,0)==sp.Rational(25,63)
print('EXACT_AXIAL_MOMENT_AND_INVERSE_MONOTONICITY_IDENTITIES_PASSED')

# Independently perform numerical quadrature over the physical axial coordinate.
for height in (0.08,0.4,1.0,1.6,2.0):
    a=1-height
    norm=quad(lambda w:1-w*w,a,1,epsabs=1e-12)[0]
    EZ=lambda k:quad(lambda w:w**k*(1-w*w),a,1,epsabs=1e-12)[0]/norm
    A,B2,C3,D4=EZ(1),EZ(2),EZ(3),EZ(4)
    p2=(1+B2)/2
    p4=(1+B2+D4)/3
    transverse=(1-B2)/4
    quad2=2*(p2-A*A)
    quad4=2*p4+2*p2**2+4*(2*transverse**2+B2**2)-8*A*(A+C3)/2
    assert np.isclose(quad2,float(F_ref.subs(t,height)),rtol=1e-11)
    assert np.isclose(quad4,float(G_ref.subs(t,height)),rtol=1e-11)
print('INDEPENDENT_AXIAL_QUADRATURE_PASSED')

# Generate points directly from the three-dimensional volume law via
# rejection in the bounding cylinder; the sampling model is independent
# of the pair-distance and moment identities above.
rng=np.random.default_rng(476803)
def sample_cap(height,n):
    points=np.empty((n,3)); filled=0
    threshold=1 if height>=1 else 1-(1-height)**2
    while filled<n:
        k=int((n-filled)*2.3)+500
        zz=1-height*rng.random(k)
        ok=rng.random(k)*threshold <= (1-zz*zz)
        zz=zz[ok][:n-filled]
        radius=np.sqrt(np.maximum(0,1-zz**2))*np.sqrt(rng.random(len(zz)))
        theta=2*np.pi*rng.random(len(zz))
        nnew=len(zz)
        points[filled:filled+nnew,:]=np.stack((radius*np.cos(theta),radius*np.sin(theta),zz),axis=1)
        filled+=nnew
    return points
for height in (0.2,1.,1.8,2.):
    x,y=sample_cap(height,180_000),sample_cap(height,180_000)
    dd=np.sum((x-y)**2,axis=1)
    empirical2=dd.mean();empirical4=(dd**2).mean()
    theoretical2=float(F_ref.subs(t,height));theoretical4=float(G_ref.subs(t,height))
    assert abs(empirical2/theoretical2-1)<0.025,(height,empirical2,theoretical2)
    assert abs(empirical4/theoretical4-1)<0.04,(height,empirical4,theoretical4)
print('INDEPENDENT_VOLUME_POINT_PAIR_SIMULATION_PASSED')
print('ALL_CHECKS_PASSED')
