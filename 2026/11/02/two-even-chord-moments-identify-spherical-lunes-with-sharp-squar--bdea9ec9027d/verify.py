#!/usr/bin/env python3
"""Exact positivity certificate and independent quadrature for spherical-lune chord moments.

Requires Python 3 with sympy and numpy; deterministic and without network access.
"""
from fractions import Fraction
from math import comb, factorial, pi, cos, sin
import sympy as S
import numpy as np

x,t,z=S.symbols('x t z')
p0=S.Rational(6168503,10000000)
S15=sum((-1)**j*x**(2*j+1)/S.factorial(2*j+1) for j in range(8))
C14=sum((-1)**j*x**(2*j)/S.factorial(2*j) for j in range(8))
def Hpoly(s,c,p):
    return (s-x*c)*(3*p*x*x-9*p*p*s*s+x*x*c*c+p*c*c*s*s) + x*c*s*s*(x*x-p*s*s)
P_x=S.Poly(Hpoly(S15,C14,p0),x)
terms=P_x.terms()
assert all(n>=5 and n%2==1 for ((n,),co) in terms)
P=S.Poly(sum(co*t**((n-5)//2) for ((n,),co) in terms),t)
q=S.Rational(11,7)
F=S.Poly(P.as_expr().subs(t,q*q*z).expand(),z)
N=F.degree()
coeff=[F.nth(i) for i in range(N+1)]
bern=[sum(coeff[j]*S.Rational(comb(k,j),comb(N,j)) for j in range(k+1)) for k in range(N+1)]
assert min(bern)>S.Rational(1,10), 'Bernstein certificate fails'

# Machin's identity pi=16 arctan(1/5)-4 arctan(1/239),
# with alternating rational-series enclosures for arctan.
def atan_bounds(a,n=12):
    s=sum((-1)**j * a**(2*j+1)/Fraction(2*j+1) for j in range(n))
    nextterm=a**(2*n+1)/Fraction(2*n+1)
    return ((s,s+nextterm) if n%2==0 else (s-nextterm,s))
lo5,hi5=atan_bounds(Fraction(1,5))
lo239,hi239=atan_bounds(Fraction(1,239))
lo_pi=16*lo5-4*hi239
hi_pi=16*hi5-4*lo239
assert lo_pi > Fraction(31415926,10000000) and hi_pi < Fraction(31415927,10000000)
lo_p=lo_pi**2/16
hi_p=hi_pi**2/16
assert abs(lo_p-Fraction(6168503,10000000))<Fraction(1,10000000)
assert abs(hi_p-Fraction(6168503,10000000))<Fraction(1,10000000)
# For x in [0,pi/2] subset [0,11/7], |S15-sin(x)| <=x^17/17!,
# |C14-cos(x)| <=x^16/16!. The polynomial H has partial derivative
# bounds |H_s|<=500 x^2, |H_c|<=200 x^3, |H_p|<=123 x^5
# for |s|<=2x, |c|<=2, 0<=p<=1, |s-x c|<=x^3.
# Hence its normalized approximation error is at most:
err=q**14*(S.Rational(500,factorial(17))+S.Rational(200,factorial(16)))+S.Rational(123,10000000)
assert err < S.Rational(1,10000) # gives positivity > 0.1 - 0.0001

# Verify moment formulas independently by 4D tensor-product Gauss integration.
nd=0
for theta in (pi/5, pi/2, pi):
    half=theta/2
    radius=1.17
    gz,wz=np.polynomial.legendre.leggauss(28)
    polar=(gz+1)*pi/2
    gp,wp=np.polynomial.legendre.leggauss(20)
    ang=half*gp
    points=np.array([[np.sin(q)*np.cos(a),np.sin(q)*np.sin(a),np.cos(q)]
                     for q in polar for a in ang])
    weights=np.array([ww*np.sin(q)*pi/4*vv/2 for q,ww in zip(polar,wz) for vv in wp])
    dots=points@points.T
    d2=2*radius**2*(1-dots)
    m2=np.einsum('i,ij,j->',weights,d2,weights)
    m4=np.einsum('i,ij,j->',weights,d2*d2,weights)
    v=np.sin(half)/half
    h=(pi*pi/16)*v*v
    a2=2*radius**2*(1-h)
    a4=4*radius**4*(4/3-2*h+(2/9)*v*v*np.cos(half)**2)
    assert abs(m2-a2)<1e-11 and abs(m4-a4)<1e-11,(theta,m2-a2,m4-a4)
    nd+=2

# Verify exact symbolic endpoints and small-angle coefficient.
p=S.symbols('p')
v=1-x*x/S.Integer(6)+x**4/S.Integer(120)
c=1-x*x/S.Integer(2)+x**4/S.Integer(24)
kap=(S.Rational(4,3)-2*p*v**2+S.Rational(2,9)*v**2*c**2)/(1-p*v**2)**2
assert S.simplify(kap.subs(x,0)-(S.Rational(14,9)-2*p)/(1-p)**2)==0
assert S.simplify(S.diff(kap,x,2).subs(x,0)/2-2*(9*p*p-p-4)/(27*(1-p)**3))==0

print('VERIFY_OK Bernstein_coefficients=',len(bern),'min_coefficient=',float(min(bern)),
      'rigorous_error_bound=',float(err),'quadratures=',nd)
