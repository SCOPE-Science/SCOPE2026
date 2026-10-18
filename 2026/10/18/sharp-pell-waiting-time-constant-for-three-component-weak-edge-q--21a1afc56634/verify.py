#!/usr/bin/env python3
"""Check analytic identities for the three-component wave-transfer limit.

The mathematical proof is in RESULT.md. Numerical checks alone do not prove
an infinite-time lower bound.
"""
import math
import sympy as sp
import mpmath as mp

L = sp.Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])
I = sp.eye(3)
P0 = (L-I)*(L-3*I)/3
P1 = -L*(L-3*I)/2
P3 = L*(L-I)/6
assert P0+P1+P3==I
assert L*P0==sp.zeros(3)
assert L*P1==P1
assert L*P3==3*P3
assert (P0[2,0],P1[2,0],P3[2,0])==(sp.Rational(1,3),-sp.Rational(1,2),sp.Rational(1,6))

u,v=sp.symbols('u v',real=True)
quadratic=(u**2)/4+(v**2)/12
D=v-sp.sqrt(3)*u
assert sp.simplify(quadratic-D**2/24-(sp.sqrt(3)*u+v)**2/24)==0

mp.mp.dps=110
expected=mp.pi**4/144
p,q=2,1
ratios=[]
for n in range(8):
    assert p%2==0 and q%2==1
    assert p*p-3*q*q==1
    pp=mp.mpf(p); qq=mp.mpf(q)
    delta=-mp.pi/(pp+mp.sqrt(3)*qq)
    s=mp.pi*qq-delta/(2*mp.sqrt(3))
    A=mp.mpf(1)/3-mp.cos(s)/2+mp.cos(mp.sqrt(3)*s)/6
    value=s*s*(1-A*A)
    assert value>0
    ratios.append(value/expected)
    print(f"n={n}, pell=({p},{q}), scaled_cost/constant={mp.nstr(ratios[-1],26)}")
    p,q=7*p+12*q,4*p+7*q
assert abs(ratios[-1]-1)<mp.mpf('1e-10')
for a,b in zip(ratios,ratios[1:]):
    assert abs(b-1)<abs(a-1)
print('CHECKED exact projectors, quadratic phase identity, Pell parity/norm, eight high-precision scaling samples')
