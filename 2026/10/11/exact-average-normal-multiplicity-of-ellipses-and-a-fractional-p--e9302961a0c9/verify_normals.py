#!/usr/bin/env python3
"""Independent numerical checks for the ellipse normal-count law.
Requires numpy and scipy. Finite checks do not establish novelty or a proof.
"""
import math
import random
import numpy as np
from scipy.integrate import quad

PI=math.pi

def formula(r):
    assert r>=1.
    if r==1.:return 2.
    d=r*r-1.
    if r*r<=2.:
        return 2.+3*d*d/(4*r*r)
    A=d/r; B=d
    v=(2*r*r-1)/(r**4-1)
    t=math.asin(math.sqrt(v))
    x=A*(1-v)**1.5
    y=B*v**1.5
    primitive=t/16.-math.sin(2*t)/64.-math.sin(4*t)/64.+math.sin(6*t)/192.
    J=(x*y+r*math.asin(x/r))/2.+3*A*B*primitive
    return 2.+8*J/(PI*r)

def independent_normal_jacobian(r):
    def density(t):
        c=math.cos(t);s=math.sin(t)
        g=math.hypot(c/r,s)
        h=(c/r**2)**2+s*s
        chord=2*g**3/h
        curvature=1/(r*r*g**3)
        if curvature*chord<=1:
            ray=chord-curvature*chord*chord/2
        else:
            ray=curvature*chord*chord/2-chord+1/curvature
        return r*g*ray
    return 4*quad(density,0,PI/2,epsabs=1e-10,epsrel=1e-10,limit=300)[0]/(PI*r)

def independent_normal_count(r,x,y):
    d=r*r-1
    coefficients=[-y,-2*(r*x+d),0.,2*(d-r*x),y]
    roots=np.roots(coefficients)
    return int(np.count_nonzero(np.abs(roots.imag)<1e-7))

def run():
    checks=0
    ratios=(1.,1.05,1.2,1.4,math.sqrt(2),1.42,1.5,2.,3.,5.,10.,20.)
    for r in ratios:
        val=formula(r)
        alt=independent_normal_jacobian(r)
        assert abs(val-alt)<2e-9,(r,val,alt)
        assert 2<=val<4 or r==1
        checks+=2
    rng=random.Random(405172)
    for r in (1.1,1.4,2.,3.,8.):
        A=(r*r-1)/r;B=r*r-1
        tested=0
        for _ in range(900):
            rr=math.sqrt(rng.random()); angle=2*PI*rng.random()
            x=r*rr*math.cos(angle);y=rr*math.sin(angle)
            Q=(abs(x/A)**(2/3)+abs(y/B)**(2/3))
            if abs(Q-1)<0.012:continue
            expected=4 if Q<1 else 2
            observed=independent_normal_count(r,x,y)
            assert observed==expected,(r,x,y,Q,expected,observed)
            tested+=1
        assert tested>=800
        checks+=tested
    coeff=352*math.sqrt(2)/(15*PI)
    for r in (20.,40.,80.,160.):
        scaled=(4-formula(r))*r**3
        assert abs(scaled/coeff-1)<0.02,(r,scaled,coeff)
        checks+=1
    crit=(8/(5*PI))*(2/3)**1.5
    for eps in (0.02,0.01,0.005):
        r=math.sqrt(2+eps)
        raw=2+3*(r*r-1)**2/(4*r*r)
        scaled=(raw-formula(r))/eps**2.5
        assert abs(scaled/crit-1)<0.025,(eps,scaled,crit)
        checks+=1
    assert all(formula(b)>formula(a) for a,b in zip(ratios,ratios[1:]))
    print(f'VERIFY_OK {checks} independent finite checks; direct Jacobian quadrature and normal-polynomial roots agree')

if __name__=='__main__':run()
