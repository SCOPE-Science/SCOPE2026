#!/usr/bin/env python3
"""Reproduce exact mathematical identities and a finite physical-domain check.

Requires Python 3 and sympy. Tests support, but do not replace, the proof.
"""
from fractions import Fraction
import sympy as sp
x=sp.symbols('x')
d=sp.Rational(1,5)
a=sp.Rational(1,20)
b=sp.Rational(19,20)
F=(1-d)*x+(1-x)*(a*x+b*x*x)
assert sp.factor(F-x)==-x*(19*x*x-18*x+3)/20
lo=(9-2*sp.sqrt(6))/19
hi=(9+2*sp.sqrt(6))/19
for root in (lo,hi):
    assert sp.simplify(F.subs(x,root)-root)==0
J=sp.diff(F,x)
assert J.subs(x,0)==sp.Rational(17,20)
assert J.subs(x,1)==-sp.Rational(1,5)
assert sp.simplify(J.subs(x,lo)-(83+9*sp.sqrt(6))/95)==0
assert sp.simplify(J.subs(x,hi)-(83-9*sp.sqrt(6))/95)==0
assert sp.simplify(hi-lo)>0

L=sp.Rational(16,5)
G=L*x*(1-x)
u=(21-sp.sqrt(21))/32
v=(21+sp.sqrt(21))/32
assert sp.simplify(G.subs(x,u)-v)==0
assert sp.simplify(G.subs(x,v)-u)==0
assert sp.simplify(sp.diff(G,x).subs(x,u)*sp.diff(G,x).subs(x,v)-sp.Rational(4,25))==0

# Exact rational trial values, spanning admissible zero and higher-order terms.
cases=0
for delta in (Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(1)):
    for b1 in (Fraction(0),Fraction(1,8),Fraction(1,2),Fraction(3,4)):
        for b2 in (Fraction(0),Fraction(1,8),Fraction(1,4),Fraction(1,2)):
            for b3 in (Fraction(0),Fraction(1,8),Fraction(1,4)):
                if b1+b2+b3>1:
                    continue
                for k in range(41):
                    t=Fraction(k,40)
                    inf=b1*t+b2*t*t+b3*t*t*t
                    nxt=(1-delta)*t+(1-t)*inf
                    assert Fraction(0)<=nxt<=Fraction(1)
                    cases+=1
print('PASS: radical roots, exact multipliers, exact two-cycle,',cases,'rational interval checks')
