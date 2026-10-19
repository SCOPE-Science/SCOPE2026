#!/usr/bin/env python3
"""Numerical and exact-algebra checks for a three-rate exponential ambiguity transform."""
import mpmath as mp
import sympy as sp
mp.mp.dps = 60
s,r = sp.symbols('s r')
P = sp.expand((1-r)**2*s**2 + (1-r)*(7-r)*s + 12)
assert sp.expand(P.subs(s,s-3)-((1-r)**2*s**2+(1-r)*(1+5*r)*s+6*r*(1+r))) == 0
assert sp.factor(sp.discriminant(P,s))==(r-1)**2*(r**2-14*r+1)
assert sp.factor(P.subs(s,-3))==6*r*(1+r)
assert sp.factor(P.subs(s,-4))==12*r*r
for j,form in enumerate((12,6*(1+r),2*(r*r+4*r+1),6*r*(1+r),12*r*r)):
    assert sp.simplify(P.subs(s,-j)-form)==0
print('Exact polynomial, shifted Hurwitz form, discriminant, and pole-cancellation identities: PASS')

def f(x,a,d):
    return mp.exp(-a*x)*(-mp.expm1(-d*x))**2/(2*d*d) if x>=0 else mp.mpf(0)

def formula(tau,nu,a,d):
    T=abs(tau); rho=mp.exp(-d*T); z=(2*a+2j*mp.pi*nu)/d
    poly=(1-rho)**2*z*z+(1-rho)*(7-rho)*z+12
    den=mp.fprod(z+k for k in range(5))
    return mp.exp(-a*T-1j*mp.pi*nu*T)*poly/(2*d**5*den)

cases = [(mp.mpf(a),mp.mpf(d),mp.mpf(t),mp.mpf(nu))
    for a,d,t,nu in [('0.7','0.9','0','0'),('1.4','0.6','.1','.3'),('.3','2','.75','1.2'),('2.1','1.3','2','.7'),('.8','1.7','-.5','-.25'),('.25','.8','4','3'),('1','1','1','0')]]
max_err=mp.mpf(0)
for a,d,t,nu in cases:
    T=abs(t)
    # independently integrate the product of the threefold convoluted signal
    direct=mp.exp(-1j*mp.pi*nu*T)*mp.quad(lambda u: f(u+T,a,d)*f(u,a,d)*mp.exp(-2j*mp.pi*nu*u), [0,1,4,12,50,mp.inf])
    closed=formula(t,nu,a,d)
    err=abs(direct-closed)/(1+abs(closed))
    max_err=max(max_err,err)
    assert err<mp.mpf('1e-13'),(a,d,t,nu,err)
print('Independent defining-integral checks: PASS, cases=',len(cases),' max scaled error=',mp.nstr(max_err,8))

rho_star=7-4*mp.sqrt(3); Tstar=mp.log(7+4*mp.sqrt(3))
assert abs(rho_star*mp.exp(Tstar)-1)<mp.mpf('1e-55')
for rho in [mp.mpf('.005'),rho_star,mp.mpf('.15'),mp.mpf('.7')]:
    delta=1-rho
    disc=rho*rho-14*rho+1
    roots=[(-(7-rho)+k*mp.sqrt(disc))/(2*delta) for k in [1,-1]]
    assert max(mp.re(z) for z in roots)<-3
    for z in roots:
        assert abs((1-rho)**2*z*z+(1-rho)*(7-rho)*z+12)<mp.mpf('1e-50')
    print('rho=',mp.nstr(rho,12),' roots=', [mp.nstr(z,14) for z in roots])
print('Exact threshold rho* =',mp.nstr(rho_star,25),' delay*d =',mp.nstr(Tstar,25))
print('ALL CHECKS PASS')
