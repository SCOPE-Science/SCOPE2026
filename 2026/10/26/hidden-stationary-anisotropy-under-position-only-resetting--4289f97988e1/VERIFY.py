#!/usr/bin/env python3
"""Supplementary exact checks for hidden stationary anisotropy with position resetting.

Requires Python 3.10+, sympy and mpmath; optional scipy for transient ODE checks.
This file verifies algebraic claims, not publication priority.
"""
from fractions import Fraction
import math
import sympy as sp
import mpmath as mp

checks = 0

def eq(a, b):
    global checks
    assert sp.simplify(a-b)==0, (a,b,sp.simplify(a-b))
    checks+=1

m, d, r, q=sp.symbols('m d r q', positive=True)
lam=4*q
second=2*m/r
mixed=d/(r+lam)
fourth=24*m**2/r**2+12*d**2/(r*(r+lam))
excess=3+3*d**2*r/(m**2*(r+lam))

# The generator identities for f=z^2, z^2 cos(2theta), z^4.
eq(r*second, 2*m)
eq((r+lam)*mixed, d)
eq(r*fourth, 12*(m*second+d*mixed))
eq(fourth/second**2-3, excess)

# Independent last-reset-age Gaussian mixture and angular covariance.
# For T~Exp(r), E[T^2]=2/r^2 and E[(int_0^T cos(2theta_s)ds)^2]
# = 1/(r*(r+4q)).
mixture=12*(m**2*2/r**2+d**2/(r*(r+lam)))
eq(fourth, mixture)

# All projections have identical fourth moments by the spatial rotation symmetry.
# The planar isotropic fourth tensor yields E[X^2Y^2]=E[X^4]/3.
radial_fourth=sp.Rational(8,3)*fourth
eq(radial_fourth,64*m**2/r**2+32*d**2/(r*(r+lam)))

# Check normalizations and the anisotropic-minus-isotropic fourth-moment excess.
eq(fourth-24*m**2/r**2, 12*d**2/(r*(r+lam)))
eq(excess-3,3*d**2*r/(m**2*(r+lam)))

# Specific physically admissible rational parameter sets.
for dp in [Fraction(1,3),Fraction(1,1),Fraction(2),Fraction(3),Fraction(7)]:
    for dt in [Fraction(1,4),Fraction(1),Fraction(2),Fraction(5)]:
        for rr in [Fraction(1,3),Fraction(1),Fraction(2),Fraction(7)]:
            for qq in [Fraction(1,4),Fraction(1),Fraction(3)]:
                mm=sp.Rational(dp.numerator,dp.denominator)/2+sp.Rational(dt.numerator,dt.denominator)/2
                dd=sp.Rational(dp.numerator,dp.denominator)/2-sp.Rational(dt.numerator,dt.denominator)/2
                subs={m:mm,d:dd,r:sp.Rational(rr.numerator,rr.denominator),q:sp.Rational(qq.numerator,qq.denominator)}
                s=second.subs(subs); h=mixed.subs(subs); f=fourth.subs(subs)
                eq(s*subs[r],2*mm)
                eq(h*(subs[r]+4*subs[q]),dd)
                eq(f*subs[r],12*(mm*s+dd*h))
                if dd:
                    assert 3 < sp.Rational(f,s**2)-3 < 6
                else:
                    assert sp.Rational(f,s**2)-3 == 3
                checks+=1

mp.mp.dps=50
for rr,qq in [(mp.mpf('0.2'),mp.mpf('0.7')),(mp.mpf('1'),mp.mpf('0.3')),(mp.mpf('3'),mp.mpf('2')),(mp.mpf('0.1'),mp.mpf('2'))]:
    l=4*qq
    def integrated_cos_cov(t):
        return t/l+mp.expm1(-l*t)/(l*l)
    ans=mp.quad(lambda t:rr*mp.exp(-rr*t)*integrated_cos_cov(t), [0,1,5,20,mp.inf])
    exact=1/(rr*(rr+l))
    assert abs(ans/exact-1) < mp.mpf('1e-33'), (ans,exact)
    checks+=1

# Transient generator closure converges to the above stationary expectations
# from distinct deterministic initial orientations and zero initial position.
try:
    from scipy.integrate import solve_ivp
    for dp,dt,rr,qq in [(3.,1.,2.,.5),(1.,4.,.7,1.1),(5.,.6,3.,2.),(.1,3.,.3,.2)]:
        mm=(dp+dt)/2;dd=(dp-dt)/2;L=4*qq
        for th0 in [0., .37, 1.21]:
            c2=math.cos(2*th0);c4=math.cos(4*th0)
            def ode(t,y):
                x2,m2c,x4=y
                return [2*mm+2*dd*c2*math.exp(-L*t)-rr*x2,
                        dd+2*mm*c2*math.exp(-L*t)+dd*c4*math.exp(-4*L*t)-(rr+L)*m2c,
                        12*(mm*x2+dd*m2c)-rr*x4]
            time=200./min(rr,qq)
            sol=solve_ivp(ode,(0,time),[0,0,0],rtol=1e-11,atol=1e-12)
            assert sol.success
            expected=[2*mm/rr,dd/(rr+L),24*mm**2/rr**2+12*dd**2/(rr*(rr+L))]
            assert all(abs(a-b)<1e-8*(1+abs(b)) for a,b in zip(sol.y[:,-1],expected)),(sol.y[:,-1],expected)
            checks+=1
except ImportError:
    print('scipy absent: transient checks skipped')

print('PASS',checks,'mathematical checks')
print('Example Dparallel=3, Dperp=1, r=2, q=1/2: variance 2; fourth moment 25.5; excess kurtosis 3.375')
