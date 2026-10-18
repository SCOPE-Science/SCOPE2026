#!/usr/bin/env python3
"""Reproduce exact identities and numerical checks for the cone Wills polynomial.

Requirements: Python 3 with sympy and mpmath. Numerical tests are not an
exhaustive proof; the global monotonicity argument is in RESULT.md.
"""
import sympy as sp
import mpmath as mp

p,t=sp.symbols('p t', positive=True,real=True)
s=1+sp.sqrt(1+t*t)
m=t+p-sp.atan(t)
x=t/sp.sqrt(1+t*t)
Q=m*m-sp.Rational(3,2)*p*s
H=2*m**3-sp.Rational(9,2)*p*m*s+9*p*t
assert sp.simplify(sp.diff(m,t)-x*x)==0
assert sp.simplify(sp.diff(s,t)-x)==0
assert sp.simplify(sp.diff(Q,t)-(2*m*x*x-sp.Rational(3,2)*p*x))==0
assert sp.simplify(sp.diff(H,t)-(3*x*x*(m*m+Q)-sp.Rational(9,2)*p*x*m+9*p))==0
# Treat q as an independent symbol with q^2=Q, differentiating F=H+/-2q^3.
q=sp.symbols('q',positive=True)
for sign in (-1,1):
    derivative=sp.diff(H,t)+sign*3*q*sp.diff(Q,t)
    squared=3*(x*(m+sign*q)-sp.Rational(3,4)*p)**2+sp.Rational(9,16)*p*(16-3*p)
    diff=sp.expand(derivative-squared)
    assert sp.simplify(diff.subs(q*q,Q))==0
# Exact rational inequality in the proof (replace pi by a positive formal p).
a=sp.Rational(9,13)
b=sp.Rational(2,3)*p+sp.Rational(6,13)
E=sp.factor(sp.Rational(3,4)*a*b*b-p)
assert sp.simplify(E-(507*p*p-1495*p+243)/2197)==0
assert E.subs(p,3)==sp.Rational(321,2197)
assert sp.diff(E,p).subs(p,3)>0
assert sp.diff(E,p,2)>0
# Check monic reciprocal cubic discriminant factorization at algebraic level.
M,B,C=sp.symbols('M B C',real=True)
Q0=M*M-3*B
H0=2*M**3-9*M*B+27*C
D=sp.discriminant(sp.Symbol('z')**3+M*sp.Symbol('z')**2+B*sp.Symbol('z')+C,sp.Symbol('z'))
assert sp.expand(27*D-(4*Q0**3-H0**2))==0

mp.mp.dps=60
P=mp.pi
def vals(tt):
    mm=tt+P-mp.atan(tt)
    ss=1+mp.sqrt(1+tt*tt)
    QQ=mm*mm-3*P*ss/2
    HH=2*mm**3-9*P*mm*ss/2+9*P*tt
    return (HH+2*QQ**mp.mpf('1.5'), HH-2*QQ**mp.mpf('1.5'),
            (4*QQ**3-HH**2)/27)
alpha=mp.findroot(lambda tt:vals(tt)[0],(mp.mpf('1.75'),mp.mpf('1.8')))
beta=mp.findroot(lambda tt:vals(tt)[1],(mp.mpf('1.85'),mp.mpf('1.9')))
assert abs(alpha-mp.mpf('1.7602188991659217646070077431926189299945637699684'))<mp.mpf('1e-44')
assert abs(beta-mp.mpf('1.8972451274494761112220056361240909307522375749772'))<mp.mpf('1e-44')
assert vals(mp.mpf('1.75'))[2]<0
assert vals(mp.mpf('1.80'))[2]>0
assert vals(mp.mpf('1.85'))[2]>0
assert vals(mp.mpf('1.90'))[2]<0
print('SYMBOLIC_IDENTITIES_OK')
print('RATIONAL_BOUND_OK')
print('ALPHA =',mp.nstr(alpha,54))
print('BETA  =',mp.nstr(beta,54))
print('NUMERICAL_SIGNATURES_OK')
