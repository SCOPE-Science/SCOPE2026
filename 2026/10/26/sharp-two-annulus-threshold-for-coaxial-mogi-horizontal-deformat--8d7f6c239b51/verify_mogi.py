#!/usr/bin/env python3
"""Reproduce algebraic identities and deterministic numerical checks for two Mogi sources.
Scientific constants below refer only to the specified linear elastic point-source model.
Run: python verify_mogi.py (requires sympy)."""
import math
import random
import sympy as S

x, z, r, q = S.symbols('x z r q', positive=True)
P = S.expand(4 * (x+1) * (x+z) - 5 * (2*x-1) * (z-2*x))
assert S.expand(P - (24*x*x - 6*(z+1)*x + 9*z)) == 0
assert S.simplify(S.discriminant(P, x) - 36*(z*z - 22*z + 1)) == 0
log_derivative = 2/(2*x-1) + 2/(z-2*x) + S.Rational(5,2)*(1/(x+z) - 1/(x+1))
assert S.cancel(log_derivative - (z-1)*P/(2*(2*x-1)*(z-2*x)*(x+1)*(x+z))) == 0
U = r/(1+r*r)**S.Rational(3,2) + q*r/(z+r*r)**S.Rational(3,2)
D = (1-2*r*r)/(1+r*r)**S.Rational(5,2) + q*(z-2*r*r)/(z+r*r)**S.Rational(5,2)
assert S.simplify(S.diff(U,r)-D) == 0
zcrit = 11 + 2*S.sqrt(30)
assert S.simplify(zcrit*zcrit-22*zcrit+1) == 0
xcrit = S.simplify((zcrit+1)/8)
assert S.simplify(P.subs({z:zcrit,x:xcrit})) == 0
assert S.simplify(S.diff(P,x).subs({z:zcrit,x:xcrit})) == 0
assert S.simplify(S.diff(P,x,2)) == 48

zc = float(zcrit)
def psi(zz, xx):
    return ((2*xx-1)/(zz-2*xx))*((xx+zz)/(xx+1))**2.5

def limits(zz):
    assert zz > zc
    root = math.sqrt((zz-11)**2 - 120)
    a = (zz+1-root)/8
    b = (zz+1+root)/8
    assert .5 < a < b < zz/2
    return a,b,psi(zz,a),psi(zz,b)

def deriv(zz, qq, xx):
    return (1-2*xx)/(1+xx)**2.5+qq*(zz-2*xx)/(zz+xx)**2.5

def bisect_zero(func, left, right, n=100):
    fl = func(left)
    fr = func(right)
    assert fl*fr < 0, (left,right,fl,fr)
    for _ in range(n):
        mid = (left+right)/2
        fm = func(mid)
        if fm == 0: return mid
        if fl*fm>0: left,fl=mid,fm
        else: right,fr=mid,fm
    return (left+right)/2

# A physically interpretable exact numerical witness: shallower depth 1,
# deeper depth 6, deeper-to-shallower inflation strength ratio 45.
xleft,xright,qmax,qmin = limits(36.0)
assert qmin < 45 < qmax
xs = [bisect_zero(lambda xx: deriv(36,45,xx), aa, bb) for aa,bb in
      ((.5,xleft),(xleft,xright),(xright,18.0))]
expected = [1.0482076510716531, 4.070965611936313, 10.85292075312628]
assert all(abs(a-b)<1e-10 for a,b in zip(xs,expected))
assert all(abs(deriv(36,45,xx))<1e-11 for xx in xs)
assert all(deriv(36,45,xx)>0 for xx in (.5,(xs[1]+xs[2])/2))
assert all(deriv(36,45,xx)<0 for xx in ((xs[0]+xs[1])/2, 18))

# Empirical checks are supplementary, never a proof of the universal statements.
gen = random.Random(20261024)
count=0
for _ in range(1800):
    zz = math.exp(gen.uniform(math.log(1.0005), math.log(1000)))
    xx = gen.uniform(.50000001, zz/2-.00000001) if zz > 1.000001 else .5000001
    qq = math.exp(gen.uniform(-8,9))
    if xx >= zz/2:continue
    v = deriv(zz,qq,xx)
    expected_sign = qq-psi(zz,xx)
    if abs(v)>1e-10 and abs(expected_sign)>1e-9:
        assert (v>0)==(expected_sign>0)
    count+=1
for _ in range(700):
    zz = zc + .1 + gen.uniform(0,600)
    a,b,upper,lower=limits(zz)
    assert upper>lower>0
    qq=(upper+lower)/2
    zeros=[bisect_zero(lambda xx: deriv(zz,qq,xx),lo,hi)
           for lo,hi in ((.5,a),(a,b),(b,zz/2))]
    assert .5<zeros[0]<a<zeros[1]<b<zeros[2]<zz/2

# Positive cusp opening coefficient in the physical strength-ratio window.
Qcrit=psi(zc,float(xcrit))
Ccrit=(zc-1)/(2*(2*float(xcrit)-1)*(zc-2*float(xcrit))
               *(float(xcrit)+1)*(float(xcrit)+zc))
coefficient=Qcrit*Ccrit*(30**.75)/2
assert abs(coefficient-.2771812085607431)<1e-12
for eps in (.2,.1,.05,.01):
    a,b,upper,lower=limits(zc+eps)
    assert abs((upper-lower)/eps**1.5/coefficient-1)<.01
print('PASS: exact derivative, discriminant, and cusp identities')
print('PASS: two-peak rational-parameter witness', xs)
print('PASS: derivative-ratio comparisons',count)
print('PASS: 700 three-stationary-point tests')
print('PASS: cusp width coefficient and asymptotic tests',coefficient)
