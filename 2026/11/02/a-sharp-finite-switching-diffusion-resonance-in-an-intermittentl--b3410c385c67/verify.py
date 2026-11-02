"""Reproduce the active-diffusivity formula and its sharp switching optimum.

Dependencies: Python 3, numpy, scipy, sympy.
Run: python verify.py
"""
from math import isclose, sqrt
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad
import sympy as sp


def formula(x, r, y, speed=1., rot=1., thermal=0.):
    u = 1. + y*y + (r+1.)*x
    den = u*u + y*y*(r-1.)**2*x*x
    num = (1.+x)*u + y*y*(r-1.)*x
    return thermal + speed*speed/(2.*rot*(r+1.))*num/den


def direct_integral(x,r,y,speed=1.,rot=1.,thermal=0.):
    lam=rot*x
    Q=np.array([[-r*lam,r*lam],[lam,-lam]],dtype=complex)
    A=Q+1j*rot*np.diag([y,-y])-rot*np.eye(2)
    pi=1./(r+1.)
    # The independent Fourier-mode propagator supplies the velocity correlation.
    def corr(t):
        return speed*speed*pi*np.real(expm(A*t)[0,0])
    integral,err=quad(corr,0.,np.inf,epsabs=3e-11,epsrel=3e-11,limit=350)
    assert err<2e-8,(err,x,r,y)
    return thermal+0.5*integral


def derivative_polynomial(x,r,y):
    c0=(y*y-1.)*(1.+y*y)**2
    c1=-2.*(1.+y*y)*((r+1.)+(r-3.)*y*y)
    c2=4.*y*y-((r+1.)+(r-1.)*y*y)**2
    return c0+c1*x+c2*x*x


def threshold(y): return (y*y+2*y-1.)/(1.+y*y)


def optimum(r,y):
    assert y>1. and r>threshold(y)
    a0=(y*y-1.)*(1.+y*y)**2
    a1=-2.*(1.+y*y)*((r+1.)+(r-3.)*y*y)
    a2=4.*y*y-((r+1.)+(r-1.)*y*y)**2
    # Stable positive root, including large r or near-threshold parameters.
    return 2.*a0/(sqrt(a1*a1-4.*a2*a0)-a1)


def symbolic_proof_checks():
    x,r,y=sp.symbols('x r y',real=True,positive=True)
    U=1+y**2+(r+1)*x
    P=(1+x)*U+y**2*(r-1)*x
    Q=U**2+y**2*(r-1)**2*x**2
    target=(r*(1+y**2)**2*(y**2-1)
          -2*r*(1+y**2)*((r+1)+(r-3)*y**2)*x
          +r*(4*y**2-((r+1)+(r-1)*y**2)**2)*x**2)
    assert sp.simplify(sp.diff(P,x)*Q-P*sp.diff(Q,x)-target)==0
    rc=(y**2+2*y-1)/(1+y**2)
    assert sp.simplify(((r+1)+(r-1)*y**2).subs(r,rc)-2*y)==0
    a1=-2*(1+y**2)*((r+1)+(r-3)*y**2)
    assert sp.factor(a1.subs(r,rc)-4*y*(1+y**2)*(y-1))==0
    xstar=sp.Rational(5,3)
    f=sp.factor((sp.Rational(1,2)/(r+1)*P/Q).subs({r:2,y:2}))
    assert sp.simplify(f-(3*x*x+12*x+5)/(6*(13*x*x+30*x+25)))==0
    assert sp.simplify(sp.diff(f,x).subs(x,xstar))==0
    assert sp.simplify(f.subs(x,xstar)-sp.Rational(1,20))==0
    assert sp.simplify(f.subs(x,0)-sp.Rational(1,30))==0
    assert sp.limit(f,x,sp.oo)==sp.Rational(1,26)
    return 8


def main():
    checks=symbolic_proof_checks()
    # Independently integrate matrix-exponential velocity correlations.
    for y in (1.1,1.5,2.,3.5):
        rc=threshold(y)
        for r in (1., (1.+rc)/2., rc, rc+0.25, rc+1.):
            for x in (0.06,0.45,1.5,6.):
                expected=formula(x,r,y,speed=1.2,rot=0.9,thermal=0.07)
                observed=direct_integral(x,r,y,speed=1.2,rot=0.9,thermal=0.07)
                assert abs(observed-expected)<2e-9,(x,r,y,observed,expected)
                checks+=1
    # Check monotonicity or the unique rate optimum and exact divergence.
    for y in (1.1,1.5,2.,3.5,8.):
        rc=threshold(y)
        for r in (1.,(1.+rc)/2.,rc):
            xs=np.geomspace(0.0002,200.,81)
            fs=np.array([formula(x,r,y) for x in xs])
            assert np.all(np.diff(fs)>0),(y,r)
            checks+=80
        for r in (rc+0.02,rc+0.2,rc+2.):
            root=optimum(r,y)
            assert root>0 and abs(derivative_polynomial(root,r,y))<2e-6*max(1,root**2)
            for fac in (0.0001,0.05,0.5,1.1,4.,100.):
                x=root*fac
                if x<root:
                    assert derivative_polynomial(x,r,y)>-1e-8
                else:
                    assert derivative_polynomial(x,r,y)<1e-8
                assert formula(root,r,y)>=formula(x,r,y)-1e-11
                checks+=2
        for eps in (1e-4,1e-5):
            root=optimum(rc+eps,y)
            assert abs(root*eps/(y-1.)-1.)<0.003,(root,y,eps)
            checks+=1
    print('PASS',checks,'independent quadratures, inequalities, symbolic checks')
    print('Example r=2, omega/Dr=2: rate/Dr=5/3, D_active=v^2/(20 Dr)')

if __name__=='__main__': main()
