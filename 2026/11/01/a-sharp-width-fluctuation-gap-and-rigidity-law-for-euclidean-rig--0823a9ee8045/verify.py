"""Arithmetic and numerical diagnostic checks for right-prism width fluctuations.

Requires Python 3.10+, scipy, numpy, sympy.  This is a diagnostic, not a
replacement for the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln
import sympy as sp


def constants(d):
    a = math.exp(2*gammaln(d/2)-gammaln((d-1)/2)-gammaln((d+1)/2))
    b = math.exp(gammaln(d/2)-0.5*math.log(math.pi)-gammaln((d+1)/2))
    r = 2*math.exp(gammaln(d/2)-0.5*math.log(math.pi)-gammaln((d-1)/2))/d
    p = (d-1)/d
    q = 1/d
    Q = q*a*a-2*r*a*b+p*b*b
    z = (p*q-r*r)/Q
    tstar = (p*b-r*a)/(q*a-r*b)
    return a,b,p,q,r,Q,z,tstar


def checks():
    pi=sp.pi
    a=pi/4; b=sp.Rational(1,2); p=sp.Rational(2,3); q=sp.Rational(1,3);r=sp.Rational(1,3)
    Q=sp.simplify(q*a*a-2*r*a*b+p*b*b)
    z=sp.simplify((p*q-r*r)/Q)
    t=sp.simplify((p*b-r*a)/(q*a-r*b))
    assert sp.simplify(t-(4-pi)/(pi-2))==0
    assert sp.simplify(z-16/(3*(pi*pi-4*pi+8)))==0
    x,y=sp.symbols('x y',real=True)
    lhs=(p*(1+y)+2*r*x+q*x*x)/(a+b*x)**2-z
    rhs=(p*y+(q*a-r*b)**2/Q*(x-t)**2)/(a+b*x)**2
    assert sp.simplify(lhs-rhs)==0
    print('EXACT_3D_CONSTANT_AND_STABILITY_PASSED')

    for d in range(3,31):
        aa,bb,pp,qq,rr,QQ,zz,tt=constants(d)
        assert tt>0 and zz>1
        c=math.exp(gammaln(d/2)-0.5*math.log(math.pi)-gammaln((d-1)/2))
        def e(fun):return quad(lambda z:2*c*(1-z*z)**((d-3)/2)*fun(z),0,1,epsabs=1e-11)[0]
        for calc,integ in [(aa,e(lambda z:math.sqrt(1-z*z))),
                           (bb,e(lambda z:z)),
                           (pp,e(lambda z:1-z*z)),
                           (qq,e(lambda z:z*z)),
                           (rr,e(lambda z:z*math.sqrt(1-z*z)))]:
            assert abs(calc-integ)<1e-10,(d,calc,integ)
        for t0 in [0.05,tt,tt*1.7,5.5]:
            for eta in [0,0.06,0.45]:
                D=(pp*(1+eta)+2*rr*t0+qq*t0*t0)/(aa+bb*t0)**2-zz
                bound=(pp*eta+(qq*aa-rr*bb)**2/QQ*(t0-tt)**2)/(aa+bb*t0)**2
                assert abs(D-bound)<3e-11,(d,t0,eta,D,bound)
    print('ALL_DIMENSIONS_BETA_INTEGRALS_AND_STABILITY_PASSED')

    for d in (100,300,1000,2000):
        aa,bb,pp,qq,rr,QQ,zz,tt=constants(d)
        assert abs(tt*math.sqrt(d)-math.sqrt(math.pi/2)/(math.pi-2))<0.02
        assert abs((zz-1)*d*d-(math.pi-3)/(2*(math.pi-2)))<0.00015
    print('GAUSSIAN_HIGH_DIMENSION_SCALING_PASSED')

    # Integrate the exact 3D cylinder width law independently for a disk base.
    m=2.0
    h=m*float(t)
    def W(z):return m*math.sqrt(1-z*z)+h*z
    m1=quad(W,0,1,epsabs=1e-13)[0]
    m2=quad(lambda z:W(z)**2,0,1,epsabs=1e-13)[0]
    var_ratio=m2/m1**2-1
    assert abs(var_ratio-float(z-1))<1e-12
    print('INDEPENDENT_DISK_CYLINDER_QUADRATURE_PASSED')

    # Uniform sphere directions with a square base: verify exact nonzero base defect.
    rng=np.random.default_rng(20261027)
    n=1500000
    xyz=rng.normal(size=(n,3))
    xyz/=np.linalg.norm(xyz,axis=1)[:,None]
    u=xyz[:,:2]
    h0=1.3
    w=np.abs(u[:,0])+np.abs(u[:,1])+h0*np.abs(xyz[:,2])
    empirical=w.var()/w.mean()**2
    mbase=4/math.pi
    etabase=(1+2/math.pi)/(mbase**2)-1  # E(|cos|+|sin|)^2=1+2/pi
    aa,bb,pp,qq,rr,QQ,zz,tt=constants(3)
    exact=(pp*(1+etabase)+2*rr*(h0/mbase)+qq*(h0/mbase)**2)/(aa+bb*(h0/mbase))**2-1
    assert abs(empirical-exact)<0.002, (empirical,exact)
    print('INDEPENDENT_SQUARE_PRISM_SAMPLING_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':checks()
