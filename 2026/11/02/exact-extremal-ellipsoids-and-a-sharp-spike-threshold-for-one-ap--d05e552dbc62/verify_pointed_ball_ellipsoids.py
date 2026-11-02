"""Numerical cross-checks for the exact ellipsoids of a ball with one axial apex.

Usage: python verify_pointed_ball_ellipsoids.py
The proof is analytic; sampling here is only a consistency check.
"""
import math
import numpy as np


def parameters(d, a):
    assert isinstance(d, int) and d >= 2 and a > 1
    if a <= d:
        j = (0.0, 1.0, 1.0)
    else:
        bj = (a + 1) / (d + 1)
        j = (bj - 1, bj, bj * math.sqrt((d*d - 1)/(a*a - 1)))
    z = 2.0 / (math.sqrt((d-1)**2*a*a+4*d) + (d-1)*a)
    z = -z  # negative root; rationalized for numerical stability
    bl = d*(a-z)/(d+1)
    l = (a-bl, bl, math.sqrt(-d*bl*z))
    return j, l, z


def radial_ellipse(z, e):
    c,b,r=e
    t=(z-c)/b
    return r*math.sqrt(max(0,1-t*t)) if -1<=t<=1 else 0


def radial_body(z, a):
    if z < -1 or z > a: return 0
    if z <= 1/a: return math.sqrt(max(0,1-z*z))
    return (a-z)/math.sqrt(a*a-1)


def check(d,a):
    j,l,zt=parameters(d,a)
    cj,bj,rj=j
    cl,bl,rl=l
    assert abs(cl+bl-a) < 1e-11*max(1,a)
    assert abs((zt-cl)/bl+1/d) < 1e-11
    assert abs((zt-cl)**2/bl**2+(1-zt**2)/rl**2-1)<1e-10
    # Löwner ellipse contains all of the original Euclidean sphere;
    # convexity then gives inclusion of its hull with the extra apex.
    zs=np.linspace(-1,1,3001)
    ell=((zs-cl)/bl)**2+(1-zs*zs)/rl**2
    assert ell.max()<=1+2e-11,(d,a,'outer',ell.max())
    if a<=d:
        assert j==(0.0,1.0,1.0)
    else:
        assert abs(cj-bj+1)<1e-11
        assert abs(cj+math.sqrt(bj*bj+(a*a-1)*rj*rj)-a)<1e-10
        assert abs(rj/bj-math.sqrt((d*d-1)/(a*a-1)))<1e-11
    z_grid=np.linspace(cj-bj,cj+bj,3001)
    gap=min(radial_body(float(z),a)-radial_ellipse(float(z),j) for z in z_grid)
    assert gap>-3e-8,(d,a,'inner',gap)
    # Contact moment system, one pole and a regular simplex of d ring vectors.
    mu=d*d/(d+1)
    lam=d/(d+1)
    t=1/d
    assert abs(mu*t-lam)<1e-12
    assert abs(mu*t*t+lam-1)<1e-12
    assert abs(mu*(1-t*t)/(d-1)-1)<1e-12
    return min(float(1-ell.max()),0),gap


if __name__=='__main__':
    cases=0
    max_outer=0.0
    min_gap=math.inf
    for d in (2,3,4,5,6,10,20,50):
        for ratio in (1.000001,1.01,1.1,1.5,2,3,5,10):
            for a in (ratio, d*(1-1e-8), float(d),d*(1+1e-8),d*ratio):
                if a<=1: continue
                outer,gap=check(d,a)
                max_outer=max(max_outer,abs(outer))
                min_gap=min(min_gap,gap)
                cases+=1
    print(f'PASS: {cases} dimension/spike configurations')
    print(f'Smallest sampled inscribed radial clearance: {min_gap:.3g}')
    print(f'Maximum sampled outer-constraint excess: {max_outer:.3g}')
    print('All numerical checks passed; the analytic proof establishes exactness.')
