#!/usr/bin/env python3
"""Exact algebra and independent numerical diagnostics for homothetic-frustum John ellipsoids.

This script is a finite diagnostic, not a substitute for the all-dimensional proof.
"""
from fractions import Fraction as F
from math import sqrt, pi, gamma
from scipy.optimize import minimize


def predicted(d,q):
    m=1-float(q)
    if m==0: return .5,1.,.5
    b=min(.5,1/((d+1)*m))
    a=sqrt(1-2*m*b) if b<.5-1e-13 else sqrt(float(q))
    return b,a,b


def contact_test(d,q):
    q=F(q); m=1-q; qcrit=F(d-1,d+1)
    if q<=qcrit:
        b=F(1,1)/(m*(d+1)); a2=F(d-1,d+1)
    else:
        b=F(1,2);a2=q
    c=b
    assert m*c+F(0,1) <= 1
    assert c+b <= 1
    # Norm-square side containment (1-mc)^2 >= a^2 + (mb)^2.
    assert (1-m*c)**2==a2+(m*b)**2
    y=m*b/(1-m*b)
    ring=F(d-1,d)/(1-y*y)
    top=(1-d*y)/(2*d*(1-y))
    bottom=(1+d*y)/(2*d*(1+y))
    assert all(v>=0 for v in (ring,top,bottom))
    assert ring+top+bottom==1
    assert ring*y+top-bottom==0
    assert ring*y*y+top+bottom==F(1,d)
    assert ring*(1-y*y)/F(d-1,1)==F(1,d)
    if q<qcrit: assert top==0
    if q>qcrit: assert top>0
    return b,a2,y,ring,top,bottom


def volume_ratio(d,q):
    b,a,c=predicted(d,q)
    # frustum body volume = kappa_{d-1} * sum(q**j)/d.
    kappa=lambda n:pi**(n/2)/gamma(n/2+1)
    return kappa(d)/kappa(d-1) * d*a**(d-1)*b/sum(q**j for j in range(d))


def independent_opt(d,q):
    m=1-q
    def fun(z):
        a,b,c=z
        if a<=0 or b<=0:return 1e8
        return -((d-1)*__import__('math').log(a)+__import__('math').log(b))
    constraints=[{'type':'ineq','fun':lambda z:z[2]-z[1]},
                 {'type':'ineq','fun':lambda z:1-z[2]-z[1]},
                 {'type':'ineq','fun':lambda z:(1-m*z[2])**2-z[0]**2-(m*z[1])**2}]
    best=None
    for a,b,c in [(.4,.15,.2),(.7,.3,.4),(.8,.48,.5),(.2,.1,.5)]:
        o=minimize(fun,[a,b,c],method='SLSQP',bounds=[(1e-7,1.2),(1e-7,.5),(0,1)], constraints=constraints,options={'maxiter':200,'ftol':1e-12})
        if o.success and (best is None or o.fun<best.fun):best=o
    assert best is not None,(d,q)
    return best.x

for d in range(3,11):
    qcrit=F(d-1,d+1)
    qs=[F(0),F(1,20),F(1,4),qcrit,F(2,3),F(4,5),F(19,20),F(1)]
    for q in qs:
        b,a2,y,ring,top,bottom=contact_test(d,q)
        bnum,anum,cnum=predicted(d,float(q))
        assert abs(float(b)-bnum)<1e-10
        assert abs(float(a2)-anum*anum)<1e-9
        assert abs(float(b)-cnum)<1e-10
    # Independent constrained optimization tests on both sides of the threshold.
    for q in [0,.2,float(qcrit),.75,.95,1]:
        a,b,c=independent_opt(d,q)
        bp,ap,cp=predicted(d,q)
        assert abs(a-ap)<2e-4 and abs(b-bp)<2e-4 and abs(c-cp)<2e-4,(d,q,(a,b,c),(ap,bp,cp))
    grid=[i/100 for i in range(101)]
    vals=[volume_ratio(d,q) for q in grid]
    assert all(y>=x-1e-14 for x,y in zip(vals,vals[1:]))
    assert vals[-1]>vals[0],(d,vals)
print('EXACT_JOHN_CONTACT_MEASURE_IDENTITIES_PASSED')
print('INDEPENDENT_CONSTRAINED_OPTIMIZATION_PASSED')
print('STRICT_VOLUME_FRACTION_GRID_CHECK_PASSED')
print('ALL_CHECKS_PASSED')

# A genuinely nonspherical cross-section check.  In two transverse dimensions,
# the unit inscribed disk is John's ellipsoid of each regular tangential polygon.
# Lift its finite John contact measure into the three-dimensional frustum.
import numpy as np
for nverts in [3,4,7]:
    theta=np.array([2*pi*j/nverts for j in range(nverts)])
    normals=np.column_stack([np.cos(theta),np.sin(theta)])
    assert np.linalg.norm(np.mean(normals,axis=0))<1e-13
    assert np.linalg.norm((normals.T@normals)*2/nverts-np.eye(2))<1e-13
    for q in [F(0),F(1,5),F(1,2),F(4,5),F(1)]:
        d=3
        b,a2,y,ring,top,bottom=contact_test(d,q)
        yf=float(y);rf=float(ring);tf=float(top);bf=float(bottom)
        points=np.vstack([np.column_stack([np.sqrt(1-yf*yf)*normals,np.full(nverts,yf)]),[0.,0.,1.],[0.,0.,-1.]])
        masses=np.array([rf/nverts]*nverts+[tf,bf])
        assert abs(sum(masses)-1)<1e-12
        assert np.linalg.norm(masses@points)<1e-12
        assert np.linalg.norm((points.T*masses)@points-np.eye(3)/3)<1e-12
print('NONCIRCULAR_BASE_LIFTED_JOHN_CERTIFICATES_PASSED')
