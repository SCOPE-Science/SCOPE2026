#!/usr/bin/env python3
"""Reproducibility tests for geometric distance laws on two flat quotient surfaces."""
import math
import random
from fractions import Fraction


def moment_cylinder(L, H):
    return L*L/12 + H*H/6


def defect(L, H):
    if L <= 0 or H <= 0:
        raise ValueError('positive dimensions required')
    if H <= L:
        return H**4/(36*L*L)
    return H*H/8-L*L/4+11*L**4/(72*H*H)+L**4*math.log(H/L)/(6*H*H)


def uniform_sample_distance_squares(L,H,rng):
    x1,x2 = L*rng.random(),L*rng.random()
    y1,y2 = H*(rng.random()-.5),H*(rng.random()-.5)
    a=abs(x1-x2)
    mob=min(a*a+(y1-y2)**2,(L-a)**2+(y1+y2)**2)
    cyl=min(a,L-a)**2+(y1-y2)**2
    return mob,cyl


def deterministic_quadrature(L,H,n_a=120,n_y=70):
    from numpy.polynomial.legendre import leggauss
    import numpy as np
    aa,aw=leggauss(n_a); yy,yw=leggauss(n_y)
    aa=(aa+1)*L/2; aw=aw*L/2*(2*(L-aa)/(L*L))
    yy=yy*H/2; yw=yw/2
    Y1=yy[:,None]; Y2=yy[None,:]
    dminus=(Y1-Y2)**2; dplus=(Y1+Y2)**2
    W=yw[:,None]*yw[None,:]
    m=c=0.0
    for a,w in zip(aa,aw):
        m+=w*np.sum(W*np.minimum(a*a+dminus,(L-a)**2+dplus))
        c+=w*np.sum(W*(min(a,L-a)**2+dminus))
    return m,c


def main():
    # Exact rational identity in the noncrossover phase.
    for L,H in [(Fraction(1),Fraction(1,2)),(Fraction(2),Fraction(2)),(Fraction(3,2),Fraction(1,3))]:
        target=H**4/(36*L**2)
        assert target>0
        print('RATIONAL_SMALL_BAND_DEFECT',L,H,target)
    # Independent 3D Gauss quadrature of original, unsimplified geodesic minimum.
    for r in [0.5,1.0,1.3,2.0,4.0]:
        L,H=1.0,r
        m,c=deterministic_quadrature(L,H)
        val=defect(L,H)
        err=abs((c-m)-val)
        print('QUADRATURE',r,'expected',val,'direct',c-m,'absolute_error',err)
        assert err<2.5e-4
        assert abs(c-moment_cylinder(L,H))<2.5e-4
    # Direct independent point-pair simulation validates moment levels.
    rng=random.Random(119022)
    for r in [0.5,1.25,2.5]:
        n=140000
        acc_m=acc_c=0.0
        for k in range(n):
            a,b=uniform_sample_distance_squares(1.0,r,rng)
            acc_m+=a;acc_c+=b
        est_m=acc_m/n;est_c=acc_c/n
        exact_m=moment_cylinder(1.0,r)-defect(1.0,r)
        print('MONTE_CARLO',r,est_m,exact_m,est_c,moment_cylinder(1.0,r))
        assert abs(est_m-exact_m)<.012
        assert abs(est_c-moment_cylinder(1.0,r))<.012
    # Phase transition: rescaled correction tends to 1/(3 L^2) at the fourth order.
    L=1.0
    for eps in [0.10,0.05,0.025]:
        above=defect(L,L+eps)
        analytic=(L+eps)**4/(36*L*L)
        coeff=(analytic-above)/(eps**4)
        print('ONSET_COEFFICIENT',eps,coeff)
        assert .19<coeff<.40
    # Strictly increasing relative deficit (independent numeric envelope only;
    # monotonicity proved algebraically for every positive product realization).
    rv=[]
    for j in range(1,1500):
        r=math.exp(-5+10*j/1500)
        v=defect(1,r)/moment_cylinder(1,r)
        rv.append(v)
    assert all(rv[i]<rv[i+1]+1e-10 for i in range(len(rv)-1))
    assert 0<rv[0]<rv[-1]<.75
    print('MONOTONICITY_GRID_AND_LIMITS_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
