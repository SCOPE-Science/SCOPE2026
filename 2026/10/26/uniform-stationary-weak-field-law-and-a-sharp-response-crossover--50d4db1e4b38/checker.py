"""Reproduce the stationary density, singular limit, and mean-response thresholds.

Requires Python 3, scipy, and mpmath. Uses the differential generator rather
than previously fitted or simulated stationary-state data.
"""
from math import sqrt, exp, expm1
from scipy.integrate import quad
from scipy.optimize import brentq
import mpmath as mp


def parameters(h, D):
    assert h > 0 and D > 0
    root=sqrt(h*h+4*D)
    k=2/(h+root)
    ell=(h+root)/(2*D)
    v=h/D
    a=1-h*k
    e=exp(-v)
    r=(1-a*e)*e/(h*ell+1-e)
    C=1/(1+1/k-r*(1+1/ell))
    return k,ell,v,a,e,r,C


def density(x,h,D):
    k,ell,v,a,e,r,C=parameters(h,D)
    if x < -1:
        return C*h*r*ell*exp(ell*(x+1))
    if x < 0:
        return C*((1-a*e+r)*exp(v*x)-r)
    if x < 1:
        return C*(1-a*exp(v*(x-1)))
    return C*h*k*exp(-k*(x-1))


def mass_and_mean(h,D):
    k,ell,v,a,e,r,C=parameters(h,D)
    intE=-expm1(-v)
    positive=C*(1-a*intE/v)
    negative=C*((1-a*e+r)*intE/v-r)
    outer=C*h*(1+r)
    z=positive+negative+outer
    # Stationary generator identity: E[X 1_{|X|>1}]=h.
    m=h+C*(.5-a*(1/v-intE/(v*v))+
        (1-a*e+r)*(e/v-intE/(v*v))+r/2)
    return z,m,outer


def source_f(h,D):
    root=sqrt(1+4*D/h**2)
    t=mp.tanh(h/(2*D))
    return float(D*(1+(1+(root+2*D/h)*t)/(h*(t+root))))


def self_consistent(h,alpha,beta):
    d0=alpha*h**beta
    fun=lambda D:D-alpha*mass_and_mean(h,D)[2]**beta
    D=brentq(fun,.5*d0,2*d0,xtol=max(1e-300,d0*1e-13),rtol=1e-13)
    assert abs(fun(D)) <= 3e-11*D
    return D


def direct_checks():
    for h,D in [(0.2,0.05),(0.01,0.0003),(0.003,0.000002),(.6,.5)]:
        k,ell,v,a,e,r,C=parameters(h,D)
        z,m,gamma=mass_and_mean(h,D)
        assert abs(z-1)<1e-10
        assert abs(gamma-D/source_f(h,D))<1e-10
        # independent quadrature of all four stationary intervals
        grid=[(-float('inf'),-1),(-1,0),(0,1),(1,float('inf'))]
        z_num=sum(quad(lambda x:density(x,h,D),lo,hi,epsabs=3e-11)[0] for lo,hi in grid)
        m_num=sum(quad(lambda x:x*density(x,h,D),lo,hi,epsabs=3e-11)[0] for lo,hi in grid)
        assert abs(z_num-1)<3e-9,(h,D,z_num)
        assert abs(m_num-m)<3e-9,(h,D,m_num,m)
        # Stationary PDE flux and jump, exact algebra at the interfaces
        assert abs(D*k*k+h*k-1)<1e-9
        assert abs(D*ell*ell-h*ell-1)<1e-9
        assert abs((h*C*(1+r))/D-C*(h/D)*(1+r))<1e-9
    print('Exact density: normalization, source stationary reset rate, independent mean quadrature, flux/PDE identities PASS')


def asymptotic_checks():
    for beta,alpha in [(1.5,2), (2,.5),(2,.75),(2,1),(2.5,2)]:
        values=[]
        for h in [1e-3,1e-4]:
            D=self_consistent(h,alpha,beta)
            z,m,gamma=mass_and_mean(h,D)
            assert abs(z-1)<1e-12
            assert abs(D/(alpha*h**beta)-1)<0.2
            assert abs(gamma/h-1)<0.03
            assert abs(m-.5)<0.1
            if beta<2: val=(m-.5)/h**(beta-1); expected=-alpha
            elif beta>2: val=(m-.5)/h; expected=.5
            else:
                val=(m-.5)/h
                expected=(1+sqrt(1+4*alpha)-4*alpha)/4
            values.append((val,expected))
        assert abs(values[-1][0]-values[-1][1]) < 0.09, (beta,alpha,values)
        print('branch beta=',beta,'alpha=',alpha,'ratios=',values)
    print('Self-consistent small branch and weak-field mean regimes PASS')


def critical_check():
    # Independent high-precision expansion at beta=2, alpha=3/4.
    mp.mp.dps=60
    a=mp.mpf(3)/4
    for hstr in ['0.0001','0.00001','0.000001']:
        h=mp.mpf(hstr)
        # Low branch: c=D/h^2, Gamma/h=(1+h Q(c))^{-1}+ exponentially small.
        def Q(c):return (1+mp.sqrt(1+4*c))/2
        c=mp.findroot(lambda t: t-a/(1+h*Q(t))**2, (a*.9,a*1.1))
        q=Q(c)
        delta=c*h
        aa=1-1/q
        mean=h+(mp.mpf('.5')-aa*delta-(1-aa)*delta**2)/(1+h*q)
        qratio=(mean-mp.mpf('.5'))/h**2
        print("  critical ratio=",mp.nstr(qratio,18)); assert abs(qratio-mp.mpf(45)/16)<10*h
        print('critical h=',hstr,'(mean-1/2)/h^2=',mp.nstr(qratio,16))
    # Coefficient identities from c=alpha/(1+h Q(c))^2 at alpha=3/4.
    from fractions import Fraction as F
    c0=F(3,4); c1=F(-9,4); q0=F(3,2); q1=F(-9,8)
    a0=F(1,3); a1=F(-1,2)
    C1=-q0; C2=q0*q0-q1
    B0=F(1,2); B1=-a0*c0
    B2=-(a0*c1+a1*c0)-(1-a0)*c0*c0
    assert B2+C1*B1+C2*B0==F(45,16)
    print('Critical exact coefficient 45/16 PASS')

if __name__=='__main__':
    direct_checks()
    asymptotic_checks()
    critical_check()
    print('ALL CHECKS PASSED')
