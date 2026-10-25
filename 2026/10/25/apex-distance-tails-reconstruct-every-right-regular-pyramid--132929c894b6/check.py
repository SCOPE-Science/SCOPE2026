#!/usr/bin/env python3
"""Independent numerical checks for apex-to-surface geodesic laws of regular pyramids.
No external dependencies beyond numpy; only forward numerical checks, not proof.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

def parameters(n, a, h):
    alpha=np.pi/n
    b=a*np.tan(alpha)
    L=np.hypot(a,h)
    C=L+a
    return alpha,b,L,C

def square_moment_quadrature(n, a, h, degree=256):
    alpha,b,L,C=parameters(n,a,h)
    z,w=leggauss(degree)
    theta=alpha*z
    wi=alpha*w
    # Area mean over one base sector: integrate dr exactly.
    rm=a/np.cos(theta)
    base_integral=np.sum(wi*(C*C*rm*rm/2 + rm**4/4 -2*C*np.cos(theta)*rm**3/3))
    phi=np.arctan(b/L)
    t=phi*z
    wt=phi*w
    side_integral=np.sum(wt*(L**4/4)*np.cos(t)**(-4))
    actual=n*(base_integral+side_integral)/(n*b*C)
    target=L*C/2+(a*a+b*b)/6
    return actual,target

def tail_area_quadrature(n,a,h,eps,degree=300):
    alpha,b,L,C=parameters(n,a,h)
    x,w=leggauss(degree)
    theta=alpha*x
    disc=C*C*np.cos(theta)**2-2*C*eps+eps*eps
    assert np.min(disc)>0
    root=C*np.cos(theta)-np.sqrt(disc)
    assert np.max(root)<a
    tail_area=n*alpha*np.sum(w*root**2)/2
    total=n*b*C
    return tail_area/total

def main():
    errs=[]
    for n in (3,4,5,7,11,29):
        for h in (.1,.5,1.5,4.0):
            a=1.25
            q,e=square_moment_quadrature(n,a,h)
            assert abs(q-e)<2e-12,(n,h,q,e)
            alpha,b,L,C=parameters(n,a,h)
            eps=1e-3
            z=tail_area_quadrature(n,a,h,eps)
            e2=eps**2/(a*C)+np.tan(alpha)**2*eps**3/(3*a*C*C)
            errs.append(abs(z-e2)/z)
            assert abs(z-e2)/z<0.003,(n,h,z,e2)
    print('PASS: 24 independent Gaussian moment integrals, largest absolute error <2e-12.')
    print('PASS: 24 small-tail integrals, maximum relative two-term error:',max(errs))
    # Verify exact piecewise distance formula agrees with explicit unfolded paths.
    rng=np.random.default_rng(8274)
    for n in (3,4,5,7,11):
      a=1.; h=.7
      alpha,b,L,C=parameters(n,a,h)
      for j in range(10000):
        theta=rng.uniform(-alpha,alpha)
        rr=rng.uniform(0,a/np.cos(theta))**.5 # not area sampling; domain test only
        rr=min(rr,a/np.cos(theta))
        x=rr*np.cos(theta);y=rr*np.sin(theta)
        rho=np.hypot(C-x,y)
        pts=np.stack((C*np.cos(2*np.pi*np.arange(n)/n),C*np.sin(2*np.pi*np.arange(n)/n)),axis=1)
        d=np.linalg.norm(pts-np.array([x,y]),axis=1)
        assert abs(np.min(d)-rho)<1e-11
        ycross=y*L/(C-x)
        assert abs(ycross)<=b+1e-10
    print('PASS: 50,000 Voronoi sector and edge-crossing tests.')
if __name__=='__main__': main()
