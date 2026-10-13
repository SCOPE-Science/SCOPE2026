#!/usr/bin/env python3
"""Finite and symbolic checks for a proposed moment density.
Run with Python 3 plus SymPy and mpmath. These checks supplement, not replace,
the analytic all-orders proof supplied with the mathematical statement.
"""
from math import comb
import sympy as sp
import mpmath as mp

c,u,v=sp.symbols('c u v',real=True)
t=u+sp.I*v
num=sp.expand(t*(t-2)**2*(3-2*sp.conjugate(t)))
q=-4*u**3+17*u**2-4*u*v**2-24*u+5*v**2+12
assert sp.expand(sp.im(num)-v*q)==0

U=2*c**2-sp.Rational(1,2)
V2=(4*c**2-1)**2*(1-c**2)/(4*c**2)
P=64*c**6-112*c**4+44*c**2+7
X=(4*c**2-1)**3/(4*c**2)
assert sp.factor(q.subs({u:U,v**2:V2})-P/(4*c**2))==0
assert sp.factor((3-2*U)**2+4*V2 - (1-c**2)*(8*c**2+1)/c**2)==0
assert sp.factor(sp.diff(X,c)-(4*c**2-1)**2*(8*c**2+1)/(2*c**3))==0
Y=sp.symbols('Y')
Py=64*Y**3-112*Y**2+44*Y+7
assert sp.factor(sp.diff(Py,Y)-4*(4*Y-1)*(12*Y-11))==0
assert Py.subs(Y,sp.Rational(11,12))==sp.Rational(68,27)
assert Py.subs(Y,sp.Rational(1,4))==12
assert Py.subs(Y,1)==3
print('EXACT_ALGEBRA_OK')

mp.mp.dps=55
pi=mp.pi

def angle_density(a):
    C=mp.cos(a)
    return (64*C**4-112*C**2+44+7/(C*C))/(4*pi)

def angle_X(a):
    C=mp.cos(a)
    return (4*C*C-1)**3/(4*C*C)

for k in range(15):
    expected=comb(3*k,k)-2*(comb(3*k,k-1) if k>0 else 0)+(comb(3*k,k-2) if k>1 else 0)
    actual=mp.quad(lambda a:angle_density(a)*angle_X(a)**k,[0,pi/3])
    err=abs(actual-mp.mpf(expected))
    assert err<mp.mpf('1e-38'),(k,expected,actual,err)
    if k<=8:
        print(f'MOMENT_{k}={expected} ERROR={mp.nstr(err,3)}')
print('MOMENTS_0_TO_14_OK')

B=[comb(3*k,k)-2*(comb(3*k,k-1) if k>0 else 0)+(comb(3*k,k-2) if k>1 else 0) for k in range(25)]
for m in range(1,7):
    H=sp.Matrix([[B[i+j] for j in range(m)] for i in range(m)])
    Hshift=sp.Matrix([[B[i+j+1] for j in range(m)] for i in range(m)])
    assert H.det()>0 and Hshift.det()>0
print('LEADING_HANKEL_AND_SHIFTED_MINORS_1_TO_6_POSITIVE')
print('VERIFY_OK')
