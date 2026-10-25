#!/usr/bin/env python3
"""Finite symbolic and numerical checks of the planar adaptive-belief map.

The inverse-branch and invariant-measure theorems require the accompanying
analytical proof; finite tests do not establish universal quantifiers.
"""
import math
import sympy as sp
import mpmath as mp

x, a, c, k, p, b, p0, q, Q = sp.symbols('x a c k p b p0 q Q', real=True)
A = a*(1-c*k*p/(1-k))
xs = sp.symbols('xs', positive=True)
det_yq = sp.det(sp.Matrix([[1-a*x*(1-x), -a*c], [k*p*x*(1-x), 1-k]]))
assert sp.simplify(det_yq - ((1-k)-a*(1-k-c*k*p)*x*(1-x))) == 0
assert sp.simplify(det_yq-(1-k)*(1-A*x*(1-x))) == 0
assert sp.simplify(det_yq.subs(k, 1/(1+c*p)) -(1-k).subs(k,1/(1+c*p))) == 0
print('EXACT_LOGIT_JACOBIAN_AND_RIDGE_IDENTITIES_PASS')

u=sp.symbols('u',real=True)
f_cusp=sp.log((sp.Rational(1,2)+u)/(sp.Rational(1,2)-u))-4*(sp.Rational(1,2)+u)
assert sp.simplify(sp.diff(f_cusp,u,3).subs(u,0)-32)==0
assert sp.simplify(sp.diff(f_cusp,u,2).subs(u,0))==0
assert sp.simplify(sp.diff(f_cusp,u).subs(u,0))==0
print('CUBIC_CRITICAL_INVERSE_NORMAL_FORM_PASS')

mp.mp.dps=50
for aa in [mp.mpf('4.1'),mp.mpf('5'),mp.mpf('8'),mp.mpf('30')]:
    r=mp.sqrt(1-4/aa)
    m=(1-r)/2; z=(1+r)/2
    phi=lambda xx:mp.log(xx/(1-xx))-aa*xx
    width=aa*r-4*mp.atanh(r)
    assert width>0 and abs(phi(m)-phi(z)-width)<mp.mpf('1e-42')
print('EXACT_TWO_FOLD_BAND_WIDTH_PASS 4')

# Physical state-space witness: p0+p1 < 1, c > 1, a > threshold.
pa=mp.mpf('8'); pc=mp.mpf('2'); pk=mp.mpf('0.2')
pp=mp.mpf('0.2'); pp0=mp.mpf('0.1'); pb=mp.mpf('0.3')
pA=pa*(1-pc*pk*pp/(1-pk))
assert pA>4
pr=mp.sqrt(1-4/pA); xm=(1-pr)/2; xp=(1+pr)/2
phi=lambda xx:mp.log(xx/(1-xx))-pA*xx
hm=(phi(xm)+phi(xp))/2
Qt=(1-pk)/2+pk*(pp0+pp/2)
Yt=hm+pa*pb+pa*pc*pk*pp0/(1-pk)-pa*pc*Qt/(1-pk)
Xtarget=1/(1+mp.exp(-Yt))
roots=[]
for lo,hi in [(mp.mpf('1e-20'),xm),(xm,xp),(xp,mp.mpf('1')-mp.mpf('1e-20'))]:
    left,right=lo,hi
    fleft=phi(left)-hm
    assert fleft*(phi(right)-hm)<0
    for j in range(220):
        mid=(left+right)/2
        if (phi(mid)-hm)*fleft>0:
            left=mid; fleft=phi(mid)-hm
        else:
            right=mid
    rx=(left+right)/2
    rq=(Qt-pk*(pp0+pp*rx))/(1-pk)
    Y=mp.log(rx/(1-rx))-pa*(rx-pb+pc*rq)
    QQ=(1-pk)*rq+pk*(pp0+pp*rx)
    assert 0<rx<1 and 0<rq<1
    assert abs(Y-Yt)<mp.mpf('1e-45') and abs(QQ-Qt)<mp.mpf('1e-45')
    roots.append((rx,rq))
assert len(roots)==3 and roots[0][0]<roots[1][0]<roots[2][0]
print('PHYSICAL_THREE_PREIMAGE_WITNESS_PASS 3')

for delta in [mp.mpf('0.01'),mp.mpf('0.001'),mp.mpf('0.0001')]:
   aa=4+delta; r=mp.sqrt(1-4/aa); width=aa*r-4*mp.atanh(r)
   assert abs(width/delta**mp.mpf('1.5')-mp.mpf(1)/3)<mp.mpf('0.005')
print('FOLD_BAND_THREE_HALVES_SCALING_PASS 3')
print('GLOBAL_AND_INFINITE_TIME_CLAIMS_REQUIRE_ANALYTICAL_PROOF')
