#!/usr/bin/env python3
"""Exact symbolic and numerical checks for the energy-constrained paired-overtide theorem.
Run: python check.py   (requires Python 3, SymPy, mpmath)
"""
from fractions import Fraction
from math import comb
import sympy as s
from mpmath import findroot, cos, acos, sqrt

x,u,E,a,b=s.symbols('x u E a b',real=True)
R2=4*(1+x)**2+(2*x+1)**4
R=s.sqrt(R2)
G=(1-x)*R
profile=lambda z:z-a*(2*z**2-1)-b*(4*z**3-3*z)
D=s.factor(profile(x)-profile(s.Integer(1)))
assert s.simplify(D-(1-x)*(-1+2*a*(1+x)+b*(2*x+1)**2))==0
print('PASS: exact tidal-height difference factorization')
P=384*x**7+1152*x**6+1584*x**5+1392*x**4+816*x**3+264*x**2+33*x+1
assert s.simplify(s.diff(G,x,2)*R**3+4*P)==0
assert s.simplify(s.diff(G,x).subs(x,0)-3/s.sqrt(5))==0
assert s.simplify(s.diff(G,x).subs(x,1)+s.sqrt(97))==0
print('PASS: exact derivative identities and strict positive-coefficient concavity certificate')
Q=s.expand(s.factor((5-G.subs(x,-u)**2)/u))
assert s.simplify(Q-(6-u-8*u**2+20*u**3-16*u**5))==0
coef=[s.expand(Q).coeff(u,k) for k in range(6)]
bern=[sum(coef[k]*s.Rational(comb(j,k),comb(5,k)) for k in range(j+1)) for j in range(6)]
assert bern==[s.Integer(6),s.Rational(29,5),s.Rational(24,5),s.Integer(5),s.Rational(42,5),s.Integer(1)]
assert all(z>0 for z in bern)
print('PASS: nonpositive-cosine range dominated by zero-cosine, exact Bernstein certificate:',bern)
xa=s.Rational(1,2); Ea=s.Rational(5,6); aa=s.Rational(1,2); ba=s.Rational(2,3)
assert s.simplify(aa**2+ba**2-Ea**2)==0
assert s.simplify(s.diff(G,x).subs(x,xa)+1/Ea)==0
assert s.simplify(Ea*2*(1+xa)/R.subs(x,xa)-aa)==0
assert s.simplify(Ea*(2*xa+1)**2/R.subs(x,xa)-ba)==0
assert s.simplify(D.subs({x:xa,a:aa,b:ba})-s.Rational(19,12))==0
print('PASS: exact interior optimal allocation at energy 5/6, split a=1/2, b=2/3 and excess 19/12')
ex_a=s.Rational(1,20); ex_b=s.Rational(1,10)
ex_x=(-1+s.sqrt(157))/12
assert 0<ex_a<s.Rational(1,4) and 0<ex_b<s.Rational(1,9)
assert 4*ex_a+9*ex_b>1
assert s.simplify(s.diff(profile(x),x).subs({x:ex_x,a:ex_a,b:ex_b}))==0
ex_delta=s.simplify(D.subs({x:ex_x,a:ex_a,b:ex_b}))
assert ex_delta == (-1963+157*s.sqrt(157))/2160 and ex_delta>0
print('PASS: subcritical separate overtides cooperate to create a strict double high, exact excess',ex_delta)
for energy in [s.Rational(1,20),s.Rational(1,10),s.Rational(1,9),s.Rational(1,8),s.Rational(1,2),s.Rational(5,6),s.Rational(2,1)]:
    ef=float(energy)
    assert abs(float(s.diff(G,x).subs(x,0))-3/5**.5)<1e-12
    vals=[]
    for k in range(3001):
        xx=-1+2*k/3000
        val=(1-xx)*(-1+ef*(4*(1+xx)**2+(2*xx+1)**4)**.5)
        vals.append(val)
    if ef <= 1/97**.5:
        assert max(vals)<1e-10
    else:
        xx=float(findroot(lambda z: 1+ef*s.lambdify(x,s.diff(G,x),'mpmath')(z),(.38,.99)))
        assert 0<xx<1
        fmax=(1-xx)*(-1+ef*(4*(1+xx)**2+(2*xx+1)**4)**.5)
        assert fmax>0 and max(vals)<=fmax+1e-9
print('PASS: seven numerical grid corroborations of all-domain global optimization (not a substitute for proof)')
print('ALL CHECKS PASS')
