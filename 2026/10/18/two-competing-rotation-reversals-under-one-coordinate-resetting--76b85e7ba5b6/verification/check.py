#!/usr/bin/env python3
"""Exact reproducibility checks for partially reset harmonic planar diffusion."""
from fractions import Fraction
import random
import sympy as sp

a,b,c,r,Tx,Ty=sp.symbols('a b c r T_x T_y', positive=True, real=True)
u,v,w=sp.symbols('u v w',real=True)
Q=sp.Matrix([[2*a+r,2*c,0],[c,a+b+r,c],[0,2*c,2*b]])
forcing=sp.Matrix([2*Tx,0,2*Ty])
D=2*(a+b)*(a*b-c*c)+r*(3*a*b+b*b-c*c)+b*r*r
U=2*((a*b+b*b+b*r-c*c)*Tx+c*c*Ty)/D
V=-c*(2*b*Tx+(2*a+r)*Ty)/D
W=(2*c*c*Tx+(2*a*a+2*a*b+3*a*r+b*r-2*c*c+r*r)*Ty)/D
assert all(sp.factor(z)==0 for z in Q*sp.Matrix([U,V,W])-forcing)
Jf=sp.factor(c*(W-U)+(a-b)*V)
Jj=sp.factor(r*V)
Ja=sp.factor(Jf+Jj)
Jf_expected=c*(4*(a*b-c*c)*(Ty-Tx)+2*r*((a+b)*Ty-b*Tx)+Ty*r*r)/D
Jj_expected=-c*r*(2*b*Tx+2*a*Ty+Ty*r)/D
Ja_expected=-2*c*(2*(a*b-c*c)*(Tx-Ty)+b*r*(2*Tx-Ty))/D
assert sp.factor(Jf-Jf_expected)==0
assert sp.factor(Jj-Jj_expected)==0
assert sp.factor(Ja-Ja_expected)==0
assert sp.factor((Ja/Jf).subs({Tx:Ty})+2*b/(2*a+r))==0
assert sp.factor(sp.limit(Jf,r,sp.oo)-c*Ty/b)==0
assert sp.factor(sp.limit(Jj,r,sp.oo)+c*Ty/b)==0
assert sp.factor(sp.limit(Ja,r,sp.oo))==0
assert sp.factor(sp.limit(Jf,r,0)-2*c*(Ty-Tx)/(a+b))==0
rng=random.Random(20261017)
for i in range(120):
    ai=Fraction(rng.randint(1,13),rng.randint(1,6))
    bi=Fraction(rng.randint(1,13),rng.randint(1,6))
    # guarantee c^2 < ab
    ci=Fraction(1,rng.randint(2,7))*min(ai,bi)
    ri=Fraction(rng.randint(1,17),rng.randint(1,7))
    ti=Fraction(rng.randint(1,13),rng.randint(1,8))
    si=Fraction(rng.randint(1,13),rng.randint(1,8))
    sub={a:sp.Rational(ai.numerator,ai.denominator),b:sp.Rational(bi.numerator,bi.denominator),c:sp.Rational(ci.numerator,ci.denominator),r:sp.Rational(ri.numerator,ri.denominator),Tx:sp.Rational(ti.numerator,ti.denominator),Ty:sp.Rational(si.numerator,si.denominator)}
    actual=Q.subs(sub).inv()*forcing.subs(sub)
    predicted=sp.Matrix([U,V,W]).subs(sub)
    assert actual==predicted
    direct_f=sub[c]*(actual[2]-actual[0])+(sub[a]-sub[b])*actual[1]
    assert direct_f==Jf_expected.subs(sub)
    assert direct_f+sub[r]*actual[1]==Ja_expected.subs(sub)
    assert D.subs(sub)>0
print('PASS: symbolic generator equations, current decompositions, equal-bath identity and limits')
print('PASS: 120 exact rational independent moment solves and current comparisons')
