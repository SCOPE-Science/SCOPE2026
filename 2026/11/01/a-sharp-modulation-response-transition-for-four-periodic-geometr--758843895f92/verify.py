#!/usr/bin/env python3
"""Symbolic and numerical consistency tests for a geometric-weight trial-vector phase diagram."""
from fractions import Fraction
import sympy as sp
from scipy.optimize import brentq

z, q, s, t, y = sp.symbols('z q s t y', positive=True)
a = q**4
P = 1 + s*q*z + q**2*z**2 + t*q**3*z**3
F = sp.sqrt(z)*(1-z)*P/(1-a*z**4)
G = sp.factor(2*sp.sqrt(z)*(1-a*z**4)**2*sp.diff(F,z))
h = lambda j: (2*j+1)-(2*j+3)*z + a*z**4*((7-2*j)+(2*j-5)*z)
assert sp.simplify(G - sum([c*z**j*h(j) for j,c in enumerate([1,s*q,q**2,t*q**3])])) == 0
assert sp.simplify(h(1).subs(z,1)) == -2*(1-q**4)
assert sp.simplify(sp.diff(h(1),z)-5*(q**4*z**3*(4-3*z)-1))==0
assert sp.simplify(sp.diff(h(1),q)-4*q**3*z**4*(5-3*z))==0
assert sp.simplify(h(0)-h(1)+2*(1-z)*(1-a*z**4))==0
assert sp.simplify(h(2)-h(1)-2*(1-z)*(1-a*z**4))==0
assert sp.simplify(h(3)-h(1)-4*(1-z)*(1-a*z**4))==0

# Half-line transform and Descartes sign-chain certificate.
Q = sp.Poly(G,z)
H = sp.Poly(sp.expand(sum(Q.nth(i)*y**i*(1+y)**(8-i) for i in range(9))), y)
x,u,v=sp.symbols('x u v',positive=True)
cs=[1,5+3*x,7+16*x+5*u,-7+33*x+23*u+7*v,
    -35+30*x+40*u+26*v+7*u**2,
    -49+(5+5*u**2)*x+30*u+34*v+23*u**2,
    -35+(12*u**2-12)*x+5*u+16*v+27*u**2+3*u**3,
    -(1-u**2)*(13+9*x+5*u+v),
    -2*(1-u**2)*(1+x+u+v)]
for i in range(9):
    assert sp.simplify(H.nth(i)-sp.sympify(cs[i]).subs({x:q*s,u:q**2,v:q**3*t}))==0
assert sp.simplify((cs[4]-4*cs[3]) - (7*u**2-52*u-2*v-102*x-7))==0
assert sp.simplify((5*cs[5]-7*cs[4]) - (66*u**2-130*u-12*v + x*(25*u**2-185)))==0
assert sp.simplify((2*cs[6]-cs[5]) - (6*u**3+31*u**2-20*u-2*v+x*(19*u**2-29)-21))==0

h_numeric = sp.lambdify((q,z), [h(i) for i in range(4)], 'numpy')
g_numeric = sp.lambdify((q,s,t,z), G, 'numpy')

def marker(qq):
    return brentq(lambda zz: h_numeric(qq,zz)[1], 1e-14, 1-1e-14, xtol=1e-14)

def phase(qq):
    zz=marker(qq)
    return (1-qq**2*zz**2)/(2*qq**3*zz**3)

def optimizer(qq,ss,tt):
    return brentq(lambda zz: g_numeric(qq,ss,tt,zz),1e-14,1-1e-14,xtol=1e-14)

cases=0
for qq in [0.1,0.25,0.5,0.8,0.99,0.999]:
    critical=phase(qq)
    zz=marker(qq)
    for ss in [0.02,0.5,1.0,10.0,100.0]:
        assert abs(optimizer(qq,ss,critical)-zz)<1e-9
        for tt, expected in [(critical/3,1),(3*critical,-1)]:
            xm=optimizer(qq,ss/1.001,tt)
            xp=optimizer(qq,ss*1.001,tt)
            assert expected*(xp-xm)>0
            cases+=1
        xm=optimizer(qq,ss,critical/3)
        xp=optimizer(qq,ss,3*critical)
        assert xp>xm
        cases+=1
assert all(phase(x)>phase(y) for x,y in zip([.1,.3,.5,.9],[.3,.5,.9,.99]))
assert abs(phase(.001)*.001**3-Fraction(125,54))<2e-5
for qq in [.999999,.9999999]:
    v=phase(qq)/(1-qq)**(1/3)
    assert abs(v-(4/5)**(1/3))<.03
print(f'PASS: symbolic coefficient, sign-chain and phase identities; {cases} directional cases; endpoint tests')
