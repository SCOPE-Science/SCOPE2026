#!/usr/bin/env python3
"""Exact symbolic and quadrature checks for a real harmonic quadratic norm inequality.

Requires SymPy and NumPy. This is a corroborating checker, not a substitute
for the global proof via phase alignment and the derivative sign argument.
"""
import math
import random
from fractions import Fraction
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

x,y,a,b,c,d,q,s=sp.symbols('x y a b c d q s', real=True)

def disk_even_moment(i,j):
    """Probability-normalized area moment E[x^i y^j] on the unit disk."""
    if i%2 or j%2:
        return sp.Integer(0)
    m,n=i//2,j//2
    return sp.factorial(2*m)*sp.factorial(2*n)/(4**(m+n)*sp.factorial(m)*sp.factorial(n)*sp.factorial(m+n+1))

def integrate_polynomial(expr):
    return sp.expand(sum(coeff*disk_even_moment(*powers)
                         for powers,coeff in sp.Poly(sp.expand(expr),x,y).terms()))

f=a+b*x+c*(x*x-y*y)+2*d*x*y
second=integrate_polynomial(f**2)
fourth=integrate_polynomial(f**4)
expected2=a*a+b*b/sp.Integer(4)+(c*c+d*d)/sp.Integer(6)
expected4=(a**4+sp.Rational(3,2)*a*a*b*b+a*a*(c*c+d*d)
           +a*b*b*c+b**4/sp.Integer(8)+sp.Rational(3,8)*b*b*(c*c+d*d)
           +sp.Rational(3,40)*(c*c+d*d)**2)
assert sp.expand(second-expected2)==0
assert sp.expand(fourth-expected4)==0
print('PASS: exact disk moments and all quartic coefficients')

A=1+q*q/sp.Integer(6)
B=6+4*q+3*q*q/sp.Integer(2)
C=1+q*q+3*q**4/sp.Integer(40)
s_star=sp.factor((B*A-2*C)/(B-4*A))
F=sp.factor((C+B*s_star+2*s_star*s_star)/(A+s_star)**2)
P=12*q**4+67*q**3-180*q*q-680*q-480
assert sp.simplify(sp.diff(F,q)+180*(5*q*q+24*q+12)*P/
     (43*q**4+240*q**3+300*q*q+1440*q+1080)**2)==0
assert sp.simplify(F-9*(33*q**4+240*q**3+520*q*q+960*q+560)/(
             2*(43*q**4+240*q**3+300*q*q+1440*q+1080)))==0
assert sp.simplify(s_star-(3*q**4+20*q**3+15*q*q+120*q+120)/(
             5*(5*q*q+24*q+12)))==0
assert sp.limit(F,q,sp.oo)==sp.Rational(297,86)
assert F.subs(q,0)==sp.Rational(7,3)
assert sp.Poly(P,q).count_roots(0,sp.oo)==1
print('PASS: exact optimizing rational function, derivative, and unique positive root')

# All pairs of homogeneous degrees. Their sharp squared-norm fourth-power ratios:
# 0+1: 7/3; 0+2: 63/23; 1+2: 297/86.
t=sp.symbols('t', nonnegative=True)
for expr, t_opt, sharp in [
    ((1-t)**2+6*t*(1-t)+2*t*t,sp.Rational(2,3),sp.Rational(7,3)),
    ((1-t)**2+6*t*(1-t)+sp.Rational(27,10)*t*t,sp.Rational(20,23),sp.Rational(63,23)),
    (2*t*t+9*t*(1-t)+sp.Rational(27,10)*(1-t)**2,sp.Rational(18,43),sp.Rational(297,86))]:
    assert sp.expand(expr).coeff(t,2)<0
    assert sp.simplify(expr.subs(t,t_opt)-sharp)==0
    assert sp.simplify(sp.diff(expr,t).subs(t,t_opt))==0
print('PASS: exact two-homogeneous-degree gaps')

q_star=float(sp.nroots(P,n=25,maxsteps=300)[1])
s_opt=float(s_star.subs(q,q_star))
K=float(F.subs(q,q_star))
assert 3.64073364<q_star<3.64073365
assert 4.33055335<K<4.33055337
assert s_opt>0
assert K>float(sp.Rational(297,86))

# Independent high-order tensor Gauss quadrature in disk polar coordinates.
# r^2 is uniform on [0,1], theta uniform on [0,2*pi].
nt=64
nodes,weights=leggauss(32)
rad_sq=(nodes+1)/2
rad_w=weights/2
angles=(np.arange(nt)+0.13)*2*np.pi/nt
xx=np.sqrt(rad_sq)[:,None]*np.cos(angles)[None,:]
yy=np.sqrt(rad_sq)[:,None]*np.sin(angles)[None,:]
w=rad_w[:,None]/nt

def quad_moments(a,b,c,d):
    p=a+b*xx+c*(xx*xx-yy*yy)+2*d*xx*yy
    return float(np.sum(w*p*p)),float(np.sum(w*p**4))

random.seed(1741)
for i in range(100):
    coeff=[random.uniform(-2.5,2.5) for _ in range(4)]
    n2,n4=quad_moments(*coeff)
    sub={a:coeff[0],b:coeff[1],c:coeff[2],d:coeff[3]}
    assert abs(n2-float(expected2.subs(sub)))<1e-11
    assert abs(n4-float(expected4.subs(sub)))<1e-9
    assert n4/(n2*n2)<K+1e-10
assert abs(quad_moments(1,2*math.sqrt(s_opt),q_star,0)[1]/
          quad_moments(1,2*math.sqrt(s_opt),q_star,0)[0]**2-K)<2e-12
print('PASS: 100 independent high-order disk quadrature comparisons; sharp equality reproduced')
print('q_star:',format(q_star,'.15g'),'s_star:',format(s_opt,'.15g'),'K:',format(K,'.15g'))
