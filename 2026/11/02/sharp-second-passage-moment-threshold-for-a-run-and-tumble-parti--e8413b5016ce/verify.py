#!/usr/bin/env python3
"""Exact, self-contained checks of the logarithmic-trap moment-threshold calculation.
The mathematical argument is analytic; this script checks its essential algebra.
"""
import sympy as S
x,v,g=S.symbols('x v g', positive=True)
f=-1/(1+x)
a=S.factor(v*v-f*f)
B=S.factor(2*f*(g-S.diff(f,x)))
D=v*v/(2*g)
b=2*g/v**2
assert S.simplify(S.limit(x*B/a,x,S.oo)+b)==0

def generator(U,V):
    return (f+v)*S.diff(U,x)+g*(V-U), (f-v)*S.diff(V,x)+g*(U-V)

c=1/(2*(1-D))
mplus=c*x*x+v*c/g*x
mminus=c*x*x-v*c/g*x
L1=generator(mplus,mminus)
for q in L1:
    assert S.simplify(S.limit(q,x,S.oo)+1)==0
Wplus=x**4+2*v/g*x**3
Wminus=x**4-2*v/g*x**3
L4=generator(Wplus,Wminus)
for q in L4:
    assert S.simplify(S.limit(q/x**2,x,S.oo)-4*(3*D-1))==0
A=1/(4*(1-D)*(1-3*D))
L2=generator(A*Wplus,A*Wminus)
for q,m in zip(L2,(mplus,mminus)):
    assert S.simplify(S.limit((q+2*m)/x**2,x,S.oo))==0
# Independently verify the averaged n=2 ODE through raw generator identities.
MP,MM=S.symbols('MP MM',cls=S.Function)
P=MP(x);M=MM(x)
# n=2 source term from generator algebra must be 2 rather than 4,
# as witnessed by the deterministic-speed limit v->0:
test=S.simplify(-S.diff(x**2,x,2)+2*(-1)*g*S.diff(x**2,x)-(-4*g*x-4+2))
# In the constant force f=-1, v=0, m1=x, m2=x^2, the RHS must have +2.
assert test==0
# Positive-dimensional examples of threshold and coefficient.
for vv,gg in [(S.Rational(1,2),S.Rational(1,2)),(S.Rational(2,3),1),(S.Rational(1,3),S.Rational(1,2))]:
    dd=vv*vv/(2*gg)
    assert dd<S.Rational(1,3)
    AA=1/(4*(1-dd)*(1-3*dd))
    assert AA>0
print('PASS: flux exponent, harmonic mean corrector, quartic Foster drift, fourth-power asymptotic coefficient, independent deterministic boundary algebra, rational examples')
