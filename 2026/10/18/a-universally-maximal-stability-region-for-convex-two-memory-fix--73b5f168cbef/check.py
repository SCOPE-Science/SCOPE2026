#!/usr/bin/env python3
"""Numerical and rational checks for two-memory convex-weight stability."""
import cmath
import math
import random
from fractions import Fraction


def roots(a, q):
    b = -a * (1-q)
    c = -a * q
    d = cmath.sqrt(b*b-4*c)
    return ((-b+d)/2, (-b-d)/2)


def stable_roots(a, q):
    return max(abs(z) for z in roots(a, q)) < 1 - 2e-10


def schur(a, q):
    r=abs(a)**2
    if q*q*r >= 1-1e-12:
        return False
    return (1-q)**2 * abs(a+q*r)**2 < (1-q*q*r)**2 - 1e-11


def quartic(a):
    r=abs(a)**2
    return r*r + (18+8*a.real)*r < 27-1e-10


def exact_F(q, x, y):
    R=x*x+y*y
    return 1-(1-2*q+3*q*q)*R-2*q*(1-q)*(1-q)*R*x+q*q*(2*q-1)*R*R

rng=random.Random(521905)
tests=0
# Grid sweep and off-grid random frequencies.
for a in [x/18+1j*y/18 for x in range(-76,30) for y in range(-55,56,4)]:
    for q in (0.0, 0.02, 0.09, 1/6, 0.24, 1/3, 0.40, 0.5, 0.62, 0.75, 0.95, 1.0):
        s=schur(a,q)
        z=max(abs(z) for z in roots(a,q))
        if abs(z-1)>3e-8:
            assert s==(z<1), ('criterion',a,q,s,z)
        if s:
            assert schur(a,1/3) and quartic(a),('inclusion',a,q)
        tests+=1
for _ in range(60000):
    a=complex(rng.uniform(-4.0,1.6),rng.uniform(-3.1,3.1))
    q=rng.random()
    s=schur(a,q)
    z=max(abs(z) for z in roots(a,q))
    if abs(z-1)>3e-8:
        assert s==(z<1),('criterion random',a,q,s,z)
    if s:
        assert schur(a,1/3) and quartic(a), ('random inclusion',a,q)
    tests+=1
# A critical-point identity for rational complex inputs, checked exactly.
for i in range(-9,10):
 for j in range(-5,6):
    x=Fraction(i,4)
    y=Fraction(j,5)
    R=x*x+y*y
    if R<=1:continue
    q0=(1-x)/(R-x)
    lhs=exact_F(q0,x,y)
    rhs=-y*y*(R-1)**2/(R-x)**2
    assert lhs==rhs,(x,y,lhs,rhs)
    tests+=1
# Exact derivative factorization at rational inputs using difference quotient polynomial.
for i in range(-7,8):
 for j in range(-4,5):
  x=Fraction(i,4)
  y=Fraction(j,5)
  R=x*x+y*y
  for n in range(11):
   q=Fraction(n,10)
   df=(2-6*q)*R-2*R*x*(1-4*q+3*q*q)+(6*q*q-2*q)*R*R
   expected=2*R*(3*q-1)*(x-1+q*(R-x))
   assert df==expected,(x,y,q,df,expected)
   tests+=1
# Strict optimality, explicit negative real witness for every alternative weight.
for q in [0.0, 0.01, 0.12, 0.2, 0.25, 0.325, 0.34, 0.45, 0.5, 0.67, 0.8, 1.0]:
    bound=min(1/q if q>0 else math.inf, 1/(1-2*q) if q<0.5 else math.inf)
    t=(3+bound)/2
    assert 0<bound<3 and not schur(-t,q) and schur(-t,1/3), (q,bound,t)
    tests+=1
# Both edge descriptions via factorization and threshold on imaginary axis.
for t in (0.25,1,1.9,2.2,2.9,3.1,4.0):
    assert schur(-t,1/3)==(t<3)
    tests+=1
eta=math.sqrt(6*math.sqrt(3)-9)
for t in (0.01,0.5,eta-1e-5,eta+1e-5,1.3,2):
    assert schur(1j*t,1/3)==(t<eta)
    tests+=1
print('PASS',tests,'checks; imaginary-axis boundary',format(eta,'.15f'))
