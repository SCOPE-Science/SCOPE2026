"""Checks exact absorption algebra and cyclic best-response conditions.

All three participants have self-consumption utility 1, successor-consumption
utility 2, and all other outcomes utility 0.
"""
from fractions import Fraction
from math import sqrt, isclose
from itertools import product
import sympy as s

a,b,c,t=s.symbols('a b c t',real=True)
den=1-t**3*(1-a)*(1-b)*(1-c)
num=t*a+2*t**2*(1-a)*b
U=num/den
D=s.factor((s.diff(num,a)*den-num*s.diff(den,a))/t)
assert s.factor(D-(1-t**3*(1-b)*(1-c)-2*t*b))==0
D0=s.factor(D.subs(t,1))
assert D0== -b*c-b+c or s.simplify(D0- (c*(1-b)-b))==0
q=s.symbols('q',real=True)
F=s.factor(D.subs({b:q,c:q}))
assert s.factor(F-(1-t**3*(1-q)**2-2*t*q))==0
assert s.factor(F.subs(t,1))==-q**2

# For rational epsilon test root balance and best-response indifference.
for ep in (s.Rational(1,10000),s.Rational(1,100),s.Rational(1,10),s.Rational(2,5)):
    tv=1-ep
    qs=[r for r in s.solve(F.subs(t,tv),q) if 0<float(r)<1]
    assert len(qs)==1
    qi=qs[0]
    assert abs(float(F.subs({t:tv,q:qi})))<1e-12
    uv=s.lambdify(a,U.subs({b:qi,c:qi,t:tv}),'math')
    assert abs(uv(0)-uv(0.39))<2e-12
    assert abs(uv(0.39)-uv(1))<2e-12
    weight=float(tv*qi/(ep+tv*qi))
    assert 0<weight<1
    print('epsilon=',float(ep),'q=',float(qi),'q/sqrt(eps)=',float(qi)/sqrt(float(ep)),'real weight=',weight)
for ep in (s.Rational(1,2),s.Rational(3,4)):
    tv=1-ep
    assert F.subs({t:tv,q:1})>=0

# Across all rational coarse-grid profiles, every best response to a
# positive-visitation profile satisfies the exact sign classification.
values=[Fraction(0),Fraction(1,8),Fraction(1,2),Fraction(7,8),Fraction(1)]
checked=0
for triple in product(values, repeat=3):
    a0,b0,c0=triple
    if (a0,b0,c0)==(0,0,0):
        continue
    B=[c0*(1-b0)-b0,a0*(1-c0)-c0,b0*(1-a0)-a0]
    # At a best response, positive retention cannot coexist with negative
    # derivative; zero retention cannot coexist with positive derivative.
    eq=True
    for own,v in zip(triple,B):
        if own==0 and v>0: eq=False
        if own==1 and v<0: eq=False
        if 0<own<1 and v!=0: eq=False
    assert not eq
    checked+=1
print('symbolic identities confirmed; rational positive profiles checked:',checked)
