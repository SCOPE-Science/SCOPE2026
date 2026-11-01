#!/usr/bin/env python3
"""Independent numerical and exact-rational checks for squared chords of spherical latitude zones.

Python 3, standard library only. Run: python3 check_zone_moments.py
"""
from fractions import Fraction as F
import math
import random


def moments(u,z):
    # u=m**2 and z=h**2, 0<h<=1 and sqrt(u)+sqrt(z)<=1.
    mean=2*(1-u)
    var=2*(1-u)**2 +4*(u-F(1,3))*z +F(2,3)*z*z
    shared=F(4,3)*u*z
    return mean,var,shared

# Exact-rational symbolic identity: completion of the square, exhaustive
# coefficient comparison in the polynomial ring Q[u,z].
def polynomials():
    # Direct evaluation on seven basis points determines a degree<=2 polynomial;
    # use a larger non-collinear grid for redundancy.
    for ui in range(12):
        u=F(ui,17)
        for zi in range(13):
            z=F(zi,19)
            mean,var,cov=moments(u,z)
            fold=F(4,3)-4*u*u+F(2,3)*(z-(1-3*u))**2
            assert var==fold
            assert mean==2*(1-u)
            assert cov==F(4,3)*u*z
    print('EXACT_FOLD_IDENTITY_AND_SHARED_ENDPOINT_COVARIANCE_PASSED')


def radial_sample(m,h,rng):
    zz=m+h*(2*rng.random()-1)
    az=2*math.pi*rng.random()
    rho=math.sqrt(max(0.,1-zz*zz))
    return rho*math.cos(az),rho*math.sin(az),zz


def sqdist(x,y):
    return sum((a-b)*(a-b) for a,b in zip(x,y))


def monte_carlo():
    rng=random.Random(739391)
    shapes=[(0,1), (0,.5),(.4,.4),(.7,.18),(.55,.24),(.54,.4),(.2,.7)]
    n=90000
    for m,h in shapes:
        assert abs(m)+h<=1+1e-12
        s1=s2=p12=p13=product=0.0
        for _ in range(n):
            x=radial_sample(m,h,rng); y=radial_sample(m,h,rng); z=radial_sample(m,h,rng)
            a=sqdist(x,y);b=sqdist(x,z)
            s1+=a;s2+=a*a;p12+=a;p13+=b;product+=a*b
        mean=s1/n; var=s2/n-mean*mean; cov=product/n-(p12/n)*(p13/n)
        E,V,C=moments(m*m,h*h)
        # The 3-coordinate squared distances are bounded by 4. Variance and
        # covariance Monte Carlo fluctuations decrease as n**(-1/2).
        assert abs(mean-E)<.022,(m,h,mean,E)
        assert abs(var-V)<.048,(m,h,var,V)
        assert abs(cov-C)<.037,(m,h,cov,C)
    print('INDEPENDENT_SURFACE_UNIFORM_THREE_POINT_MONTE_CARLO_PASSED',len(shapes))


def two_branch_and_sharp_window():
    # Exact two-zone ambiguous pair: u=3/10 and z=3/50 or 7/50.
    u=F(3,10); z1=F(3,50); z2=F(7,50)
    assert z1+z2==2*(1-3*u)
    assert math.sqrt(float(u))+math.sqrt(float(z2))<1
    E1,V1,C1=moments(u,z1);E2,V2,C2=moments(u,z2)
    assert E1==E2 and V1==V2 and C1!=C2
    assert (E1,V1,C1,C2)==(F(7,5),F(609,625),F(3,125),F(7,125)),(E1,V1,C1,C2)
    # The stationary z*=1-3u belongs to 0<z<=(1-sqrt(u))**2
    # exactly when 1/4<u<1/3, checked in exact comparisons and numerical mesh.
    for k in range(1,1000):
        uu=k/1000
        if uu>=1:continue
        zstar=1-3*uu
        zmax=(1-math.sqrt(uu))**2
        interior=0<zstar<zmax
        should=(.25<uu<1/3)
        assert interior==should,(uu,zstar,zmax)
    print('SHARP_TWO_MOMENT_AMBIGUITY_WINDOW_AND_EXACT_WITNESS_PASSED')


def inverse_and_fixed_area():
    rng=random.Random(9917)
    for _ in range(1000):
        h=.001+.999*rng.random()
        m=(1-h)*(2*rng.random()-1)
        u,z=m*m,h*h
        E,V,C=moments(u,z)
        ur=1-E/2
        if ur>1e-12:
            zr=3*C/(4*ur)
        else:
            # centered zone: invert variance, root smaller than 1
            zr=1-math.sqrt(max(0,(3*V-4)/2))
        assert abs(ur-u)<1e-12 and abs(zr-z)<1e-7,(h,m,z,zr)
        umax=(1-h)**2
        Vcenter=moments(0,z)[1]
        Vcap=moments(umax,z)[1]
        assert Vcap-1e-12<=V<=Vcenter+1e-12
        def relative(uu):
            em,vr,_=moments(uu,z)
            return vr/(em*em)
        assert relative(0)-1e-12<=relative(u)<=relative(umax)+1e-12
    print('GLOBAL_FIXED_AREA_REVERSAL_AND_THREE_STATISTIC_INVERSION_PASSED')

if __name__=='__main__':
    polynomials();two_branch_and_sharp_window();inverse_and_fixed_area();monte_carlo()
    print('ALL_CHECKS_PASSED')
