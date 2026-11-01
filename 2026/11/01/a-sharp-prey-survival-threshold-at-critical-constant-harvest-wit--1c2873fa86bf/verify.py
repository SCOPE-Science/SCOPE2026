#!/usr/bin/env python3
"""Exact checks for a critical constant-harvest Gause system.
The analytical infinite-time theorem is proved separately, not by this script.
"""
from fractions import Fraction as Q
import sympy as S
x,u,y,z,K,a,b,c=S.symbols('x u y z K a b c', real=True)
P=x*x/(a*x*x+b*x+1)
r=K/2
pr=S.factor(P.subs(x,r))
alpha=S.factor(-K*S.diff(P,x).subs(x,r))
assert S.simplify(alpha + 4*K*K*(b*K+4)/(a*K*K+2*b*K+4)**2)==0
# Generic shifted equation; confirm exact z'= -2p(u)u-(2u/K+p(u)-p(0))z.
p=S.Function('p')
up=-u*u/K-p(u)*y
yp=(p(u)-p(0))*y
zprime=S.factor(2*u*up/y-u*u*yp/(y*y))
assert S.simplify(zprime.subs(y,u*u/z)-(-2*p(u)*u-(2*u/K+p(u)-p(0))*z))==0
# Wedge boundary derivative identity.
phi_prime=S.factor(yp-2*c*u*up)
bound=S.factor(phi_prime.subs(y,c*u*u))
assert S.simplify(bound-c*u**3*((p(u)-p(0))/u+2/K+2*c*p(u)))==0
examples=((Q(1),Q(-5,4),Q(8,5),Q(16,25)),
          (Q(1,2),Q(-5,4),Q(8),Q(16)),
          (Q(9,16),Q(-9,8),Q(4),Q(2)))
for av,bv,pv,al in examples:
    args={K:S.Integer(4),a:S.Rational(av.numerator,av.denominator),b:S.Rational(bv.numerator,bv.denominator)}
    assert S.simplify(pr.subs(args)-S.Rational(pv.numerator,pv.denominator))==0
    assert S.simplify(alpha.subs(args)-S.Rational(al.numerator,al.denominator))==0
    assert bv<0 and bv* bv < 4*av
# At a=1/2,b=-5/4,K=4, take c=1/8; exact wedge boundary
# term remains negative for all u in [0,1/10].
ps=S.factor(P.subs({x:2+u,a:S.Rational(1,2),b:-S.Rational(5,4)}))
bracket=S.factor((ps-ps.subs(u,0))/u+S.Rational(1,2)+S.Rational(1,4)*ps)
num,den=map(S.Poly,S.fraction(S.factor(bracket)))
# Numerator and denominator signs via monotonic Bernstein-polynomial bound
# for rational sample grid is only diagnostic; exact result uses continuity at u=0.
assert S.limit(bracket,u,0)==-S.Rational(3,2)
assert S.simplify(bracket-(4*u**2-13*u-6)/(2*(2*u**2+3*u+2)))==0
# On 0 <= u <= 1/10, 4u^2 - 13u - 6 <= 1/25 - 6 < 0.
assert S.Rational(4,100)-6 < 0
print('PASS: exact derivative, Riccati-ratio, wedge and three rational parameter checks')
print('Example wedge boundary bracket:',bracket)
