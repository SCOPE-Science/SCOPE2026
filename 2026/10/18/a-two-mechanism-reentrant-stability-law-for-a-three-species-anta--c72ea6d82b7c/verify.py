#!/usr/bin/env python3
"""Exact verification of a three-species antagonistic community matrix theorem.

Needs Python 3 and sympy. All assertions are algebraic or finite checks.
"""
from itertools import product
from sympy import (Matrix, eye, symbols, factor, simplify, sqrt, Rational,
                   solve, Poly, expand, sign)

z,t,d,a,b,c,e=symbols('z t d a b c e',real=True)
J=Matrix([[-d,a,-t],[-b,-d,c],[t,-e,-d]])
S=a*b+c*e
G=b*e-a*c
characteristic=expand((z*eye(3)-J).det())
expected=expand((z+d)**3+(S+t**2)*(z+d)+G*t)
assert simplify(characteristic-expected)==0
A2=3*d
A1=3*d**2+S+t**2
U=d*(d**2+S+t**2)+G*t
H=2*d*t**2-G*t+2*d*(4*d**2+S)
assert simplify(H-(A2*A1-U))==0
assert simplify(expected-(z**3+A2*z*z+A1*z+U))==0
# At U=0 the cubic has a zero eigenvalue and a stable quadratic.
assert simplify((expected-U)-z*(z*z+3*d*z+A1))==0
# At H=0 the cubic factors as one negative real and one imaginary pair.
assert simplify((expected-(U-3*d*A1))-(z+3*d)*(z*z+A1))==0

osc={d:1,a:1,b:4,c:1,e:4}
real={d:1,a:4,b:1,c:4,e:1}
for vals,U_ans,H_ans in [(osc,t*t+15*t+9,2*t*t-15*t+24),
                          (real,t*t-15*t+9,2*t*t+15*t+24)]:
    assert factor(U.subs(vals)-U_ans)==0
    assert factor(H.subs(vals)-H_ans)==0
assert solve(H.subs(osc),t)==[(15-sqrt(33))/4,(15+sqrt(33))/4]
assert solve(U.subs(real),t)==[(15-3*sqrt(21))/2,(15+3*sqrt(21))/2]
# Exact rational witness signs: stable / unstable / stable.
for vals,T,indicator in [(osc,[Rational(0),Rational(3),Rational(6)],H),
                         (real,[Rational(0),Rational(3),Rational(16)],U)]:
    got=[sign(indicator.subs(vals).subs(t,q)) for q in T]
    assert got==[1,-1,1],(vals,got)

# Symbolic comparison with independent coefficient extraction on a finite grid.
checked=0
for da,aa,bb,cc,ee,tt in product([1,2], [1,2,4], [1,2,4], [1,2], [1,2,4], [0,1,2,5]):
    vals={d:da,a:aa,b:bb,c:cc,e:ee,t:tt}
    pol=Poly(characteristic.subs(vals),z)
    coeff=pol.all_coeffs()
    assert coeff[0]==1
    assert coeff[1]==3*da
    assert coeff[2]==(3*d*d+S+t*t).subs(vals)
    assert coeff[3]==U.subs(vals)
    assert 3*da*coeff[2]-coeff[3]==H.subs(vals)
    checked+=1
print('PASS: universal polynomial identities, both exact witnesses,',checked,'rational parameter cases')
