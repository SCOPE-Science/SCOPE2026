#!/usr/bin/env python3
"""Reproduce fourth-cumulant asymptotics for preferential-memory telegraph relocation.
Public reproducibility script; dependencies: sympy, scipy, mpmath.
"""
import math
import sympy as sp
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

def verify_formal():
    x,p=sp.symbols('x p',positive=True)
    d=1-sp.sqrt(1+x)
    a=d/(p+d)
    c=(1+1/sp.sqrt(1+x))/2
    # This is the log prefactor from the dominant Kummer solution.
    C=sp.log(c)-a*sp.log(1+d/p)-sp.loggamma(1-a)
    a2=sp.simplify(sp.series(-a,x,0,3).removeO().coeff(x,2))
    expected_a2=(2-p)/(8*p*p)
    assert sp.simplify(a2-expected_a2)==0
    Cser=sp.series(C,x,0,3).removeO().expand()
    C1=sp.simplify(Cser.coeff(x))
    C2=sp.simplify(Cser.coeff(x,2))
    assert sp.simplify(C1 - (sp.EulerGamma/(2*p)-sp.Rational(1,4)))==0
    assert sp.simplify(C2 - (15*p*p -12*sp.EulerGamma*p-24-2*sp.pi**2+24*sp.EulerGamma)/(96*p*p))==0
    assert sp.simplify((24*C2).subs(p,2)-(18-sp.pi**2)/8)==0
    print('Symbolic series: 4/4 exact identities passed')

def full_mgf(z,t,p):
    h=mp.sqrt(1+z*z)
    low=1-h
    high=1+h
    def f(l):
        return mp.hyp1f1(l/(p+l),1,-(p+l)*t)
    return (1+1/h)*f(low)/2 +(1-1/h)*f(high)/2

def moment_direct(t,p,n):
    return mp.diff(lambda z: full_mgf(z,t,p), 0,n)

def moment_ode(t,p):
    def rhs(s,Y):
        B1,A2,B3,A4,J1,J2,J3,J4=Y
        mem=lambda J: J/s if s>0 else 0.
        return [1-(p+2)*B1+p*mem(J1),
                2*B1-p*A2+p*mem(J2),
                3*A2-(p+2)*B3+p*mem(J3),
                4*B3-p*A4+p*mem(J4),
                B1,A2,B3,A4]
    sol=solve_ivp(rhs,(0,t),np.zeros(8),method='DOP853',rtol=2e-11,atol=1e-12)
    assert sol.success
    return sol.y[1,-1],sol.y[3,-1]

def verify_finite():
    mp.mp.dps=44
    N=0
    for p in (0.7,2.0,3.1):
        for t in (0.1,1.0,4.0,10.0):
            a2,a4=moment_ode(t,p)
            b2=float(moment_direct(t,p,2))
            b4=float(moment_direct(t,p,4))
            assert abs(a2-b2)<4e-8*(1+abs(b2)), (p,t,a2,b2)
            assert abs(a4-b4)<4e-8*(1+abs(b4)), (p,t,a4,b4)
            N+=2
    print('Independent moment evolution vs Kummer moments:',N,'comparisons passed')

def verify_asymptotic():
    mp.mp.dps=45
    E=float(mp.euler)
    N=0
    for p in (1.0,2.0,3.0):
        for t in (1e4,1e5):
            m2=moment_direct(t,p,2)
            m4=moment_direct(t,p,4)
            k4=float(m4-3*m2*m2)
            predicted=3*(2-p)/(p*p)*math.log(p*t) + (15*p*p-12*E*p-24-2*math.pi**2+24*E)/(4*p*p)
            assert abs(k4-predicted)<0.25, (p,t,k4,predicted)
            N+=1
    p=2.0
    limit=(18-math.pi**2)/8
    assert limit>0
    m2=moment_direct(1e5,p,2)
    m4=moment_direct(1e5,p,4)
    k4=float(m4-3*m2*m2)
    assert 0.9*limit<k4<1.1*limit,(limit,k4)
    print('Long-time fourth-cumulant comparisons:',N,'passed; critical observed:',round(k4,9),'limit:',round(limit,9))

if __name__=='__main__':
    verify_formal()
    verify_finite()
    verify_asymptotic()
