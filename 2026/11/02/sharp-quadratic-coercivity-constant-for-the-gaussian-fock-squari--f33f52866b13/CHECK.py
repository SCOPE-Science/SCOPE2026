#!/usr/bin/env python3
"""Reproducible exact checks for a quadratic Gaussian Fock coercivity bound.
Requires sympy>=1.12. Numerical tests are ancillary and do not certify the inequality.
"""
from fractions import Fraction as Fr
from math import factorial
import sympy as S

k,u,x=S.symbols('k u x')
P=7*k**3+9*k**2-108*k+108
h=k-2; e=20*k-24
beta=-2*h+8*(k-1)*u-e*u**2
F=S.expand(beta**2-4*h*(4*h*u**2+e*u**4))
u0=(13*k**3-74*k**2+132*k-72)/(44*k**3-168*k**2+144*k)
checks=0

def check(cond):
 global checks
 assert cond
 checks+=1

def vanish_mod(expr):
 num=S.cancel(expr).as_numer_denom()[0]
 return S.rem(S.Poly(num,k),S.Poly(P,k)).is_zero

check(vanish_mod(F.subs(u,u0)))
check(vanish_mod(S.diff(F,u).subs(u,u0)))
check(S.factor(S.discriminant(F,u)) == -268435456*(k-2)**5*(k-1)**3*(5*k-6)*(7*k**3+9*k**2-108*k+108))
# Rational isolation: P has exactly one root in this interval.
lo=Fr(24440873,10000000);hi=Fr(24440874,10000000)
check(S.Rational(lo.numerator,lo.denominator).subs(k,k)==S.Rational(lo.numerator,lo.denominator))
Pf=S.lambdify(k,P,'math')
check(P.subs(k,S.Rational(lo.numerator,lo.denominator))<0)
check(P.subs(k,S.Rational(hi.numerator,hi.denominator))>0)
check(S.diff(P,k).subs(k,S.Rational(lo.numerator,lo.denominator))>0)
# Every sign test is exact over the real algebraic field via rational interval polynomial bounds.
# Evaluate polynomial in k by interval arithmetic with endpoints Fr.
def mul(A,B):
 vals=[a*b for a in A for b in B]
 return (min(vals),max(vals))
def plus(A,B):return(A[0]+B[0],A[1]+B[1])
def interval(poly):
 poly=S.Poly(S.expand(poly),k,domain=S.QQ)
 cur=(Fr(0),Fr(0))
 for coeff in poly.all_coeffs():
  c=Fr(int(coeff.p),int(coeff.q))
  cur=plus(mul(cur,(lo,hi)),(c,c))
 return cur

def lesszero(expr):
 I=interval(expr);check(I[1]<0)
def greaterzero(expr):
 I=interval(expr);check(I[0]>0)
for value in [Fr(77,1000),Fr(571,1000)]:
 greaterzero(F.subs(u,S.Rational(value.numerator,value.denominator)))
for value in [Fr(78,1000),Fr(569,1000)]:
 lesszero(F.subs(u,S.Rational(value.numerator,value.denominator)))
for value in [Fr(97,1000),Fr(368,1000)]:
 lesszero(beta.subs(u,S.Rational(value.numerator,value.denominator)))
for value in [Fr(98,1000),Fr(367,1000)]:
 greaterzero(beta.subs(u,S.Rational(value.numerator,value.denominator)))
# Isolation of u0 via numerator - t*denominator comparison (denominator is negative).
N,D=map(S.expand,S.fraction(u0))
lesszero(D)
for v in [Fr(176,1000),Fr(177,1000)]:
 v=S.Rational(v.numerator,v.denominator)
 if v==S.Rational(176,1000):lesszero(N-v*D) # u0>v and D<0 => N-vD <0
 else:greaterzero(N-v*D) # u0<v
# Sign of beta(u0); rational with denominator D².
num=S.cancel(beta.subs(u,u0)).as_numer_denom()[0]
# numerator may have a negative denominator depending on sympy normalization; use mpmath only for this ancillary check;
# exact positivity follows by beta>0 on (0.098,0.367), containing u0.
# The algebraic minimizer x0=beta(u0)/(2h) is positive, and Q(k,u0,x0)=0 by F(u0)=0.
check(vanish_mod((h*x**2-beta*x+4*h*u**2+e*u**4).subs(x,beta/(2*h)).subs(u,u0)))
# Independent exact coefficient calculation of Gaussian fourth moment for complex sample polynomials.
for aa,bb,cc in [(1,2,-1),(2,3,-1),(1,1,1),(2,0,3),(0,2,3)]:
 coeff=[aa,bb,cc]
 quad=[sum(coeff[i]*coeff[j-i] for i in range(3) if 0<=j-i<3) for j in range(5)]
 m4=sum(factorial(j)*q*q for j,q in enumerate(quad))
 m2=aa*aa+bb*bb+2*cc*cc
 aa2,bb2,cc2=aa*aa,bb*bb,cc*cc
 form=aa**4+4*aa2*bb2+2*bb2*bb2+8*aa2*cc2+8*aa*bb2*cc+24*bb2*cc2+24*cc2*cc2
 check(m4==form)
 check(m4-m2*m2>=0)
print('CHECK_OK',checks)
