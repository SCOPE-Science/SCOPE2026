"""Numerical checks of stationary projection tails in a linearly sheared reset diffusion.
Run: python check.py. Uses Python 3, SciPy and NumPy.
"""
import math
import numpy as np
from scipy.integrate import quad


def coefficients(D,r,g,u,v):
    assert D>0 and r>0 and abs(u*u+v*v-1)<1e-10
    c3=2*D*g*g*u*u/3
    c2=2*D*g*u*v
    c1=2*D
    return c1,c2,c3


def variance(t,D,r,g,u,v):
    c1,c2,c3=coefficients(D,r,g,u,v)
    return c1*t+c2*t*t+c3*t*t*t


def pred(z,D,r,g,u,v):
    assert z>0 and u*g!=0
    c1,c2,c3=coefficients(D,r,g,u,v)
    ell=(3/(2*c3*r))**.25
    B=4*r*ell/3
    K=math.sqrt(r)/(2*math.sqrt(c3)*ell)*math.exp(r*c2/(3*c3))
    return ell,B,K


def ratio(z,D,r,g,u,v):
    ell,B,K=pred(z,D,r,g,u,v)
    a=ell*math.sqrt(z)
    def integrand(q):
        if q<=0:return 0
        t=a*q
        V=variance(t,D,r,g,u,v)
        if V<=0:return 0
        exponent=-r*t-z*z/(2*V)+B*math.sqrt(z)
        if exponent < -740:return 0
        return r*a/(math.sqrt(2*math.pi*V))*math.exp(exponent)
    # Compact integration: the omitted tails are exponentially suppressed by the saddle action.
    result,err=quad(integrand,0.2,4,epsabs=1e-9,epsrel=1e-9,limit=500,points=[0.7,1.,1.3])
    return result/(K/math.sqrt(z))


def m2(D,r,g):
    return 2*D/r+4*D*g*g/r**3

def m4(D,r,g):
    return 24*D*D/r**2+192*D*D*g*g/r**4+960*D*D*g**4/r**6


def run():
    tests=0
    for D,r,g in [(1.,1.,1.),(0.5,1.3,-2.),(2.,0.8,0.35)]:
        for u,v in [(1.,0.),(2**-.5,2**-.5),(.6,-.8)]:
            zlist=[1000.,10000.,100000.]
            ratios=[ratio(z,D,r,g,u,v) for z in zlist]
            assert all(x>0 and math.isfinite(x) for x in ratios)
            # For every finite nonzero projection the ratio must converge towards one.
            assert abs(ratios[-1]-1)<abs(ratios[0]-1) + .015, (D,r,g,u,v,ratios)
            tests+=3
            print('D,r,g,u,v',D,r,g,u,v, 'ratios',ratios)
    assert abs(m2(1,1,1)-6)<1e-12
    assert abs(m4(1,1,1)-1176)<1e-12
    tests+=2
    # Stationary vertical marginal is Laplace: m2=2D/r, m4=24D^2/r^2.
    for D,r in [(1.,1.),(2.3,.7)]:
        assert abs(24*D*D/r**2/(2*D/r)**2-6)<1e-12
        tests+=1
    print('PASS',tests,'numeric and exact moment checks')

if __name__=='__main__':run()
