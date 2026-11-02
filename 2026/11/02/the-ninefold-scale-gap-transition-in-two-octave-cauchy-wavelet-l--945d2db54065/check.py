#!/usr/bin/env python3
"""Independent algebraic spot checks for the two-octave multiplier theorem.

The proof of the infinite family is analytical; these tests verify the finite
Sturm certificates and representative polynomial identities and profiles.
"""
from fractions import Fraction
import math
import sympy as sp

T = sp.symbols('t', real=True)
expected = {2:(1,0),3:(2,1),4:(3,2),5:(3,2),6:(4,3),7:(4,3),8:(4,3)}
checks = 0

def verify(test, msg=''):
    global checks
    assert test, msg
    checks += 1

def changes(poly, value):
    signs = [sp.sign(q.subs(T,value)) for q in sp.sturm(poly,T)]
    signs = [v for v in signs if v]
    return sum(v != w for v,w in zip(signs, signs[1:]))

for k,(a,b) in expected.items():
    p=T-T**2+T**k-T**(2*k)
    d=sp.diff(p,T)
    verify(sp.expand(d-(1-2*T+k*T**(k-1)-2*k*T**(2*k-1)))==0, f'derivative k={k}')
    verify(sp.degree(sp.gcd(d,sp.diff(d,T)),T)==0, f'squarefree k={k}')
    verify(changes(d,0)==a, f'V(0), k={k}')
    verify(changes(d,1)==b, f'V(1), k={k}')
    verify(a-b==1)

r=sp.Rational(13,20)
for k in range(9,40):
    p=T-T**2+T**k-T**(2*k)
    d=sp.diff(p,T)
    verify(d.subs(T,sp.Rational(1,2))>0, f'left + k={k}')
    verify(d.subs(T,r)<0, f'13/20 - k={k}')
    verify(d.subs(T,1-sp.Rational(1,k))>0, f'1-1/k + k={k}')
    verify(d.subs(T,1)<0, f'right - k={k}')
    verify(2*k*r**k <1,f'global comparison k={k}')

for k in [8,9,10,20,40,80]:
    def p_of_x(x):
        return math.exp(-x)-math.exp(-2*x)+math.exp(-x/k)-math.exp(-2*x/k)
    grid=[j/4000 for j in range(0,40001)]
    vals=[p_of_x(x) for x in grid]
    argmax=grid[max(range(len(grid)),key=lambda j:vals[j])]
    verify(0<argmax<2,'global peak compact')
    if k>=9:
        verify(abs(argmax-math.log(2)-2/k)<0.25, 'asymptotic peak')

# k=9 has strict valleys and both side peaks by exact sign locations.
k=9
f=1-2*T+k*T**(k-1)-2*k*T**(2*k-1)
verify(f.subs(T,sp.Rational(1,2))>0)
verify(f.subs(T,sp.Rational(13,20))<0)
verify(f.subs(T,sp.Rational(8,9))>0)
verify(f.subs(T,1)<0)
print(f'PASS: {checks} deterministic checks; Sturm table:',expected)
