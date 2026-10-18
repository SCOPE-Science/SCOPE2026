#!/usr/bin/env python3
"""Exact symbolic and finite-convolution checks for the five-mode fourth-moment theorem.
Requires Python 3 and sympy. This corroborates, but does not replace, the
analytic compactness, symmetrization, and positivity arguments in RESULT.md.
"""
import sympy as sp

x, y, t = sp.symbols('x y t', real=True)
a = [sp.Integer(1), x, y, x, sp.Integer(1)]
R = [sum(a[j]*a[j+h] for j in range(5-h)) for h in range(1,5)]
E = sp.expand(sum(z*z for z in a))
F = sp.expand(E*E+2*sum(r*r for r in R))
expected = 6*x**4+12*x*x*y*y+24*x*x*y+24*x*x+y**4+12*y*y+6
assert sp.expand(F-expected)==0
assert sp.expand(E-(2+2*x*x+y*y))==0

Px = sp.factor(sp.diff(F,x)*E-2*F*sp.diff(E,x))
Py = sp.factor(sp.diff(F,y)*E-2*F*sp.diff(E,y))
A=2*y**4+6*y**3+12*y+6
B=3*(y*y+4*y+2)
H=2*y**4+8*y**3-15*y-6
J=7*y**4+24*y**3+12*y*y+48*y+24
assert sp.expand(Px+8*x*(3*x*x*(y*y+4*y+2)-A))==0
assert sp.expand(Py-8*(3*x**4*y+6*x**4-2*x*x*y**3-9*x*x*y*y+6*x*x-2*y**3+3*y))==0
T=A/B
Q_poly = sp.expand(Py/8).subs(x**4,t*t).subs(x*x,t)
assert sp.factor(Q_poly.subs(t,T)+H*J/(3*(y*y+4*y+2)**2))==0
K=sp.factor((F/E**2).subs(x**4,t*t).subs(x*x,t).subs(t,T))
assert sp.factor(K-3*(5*y**4+24*y**3+36*y*y+48*y+18)/J)==0

assert sp.factor((F/E**2).subs(y,0)-3*(x**4+4*x*x+1)/(2*(x*x+1)**2))==0
assert sp.simplify((F/E**2).subs(x,0)-(y**4+12*y*y+6)/(y*y+2)**2)==0

r = sp.nroots(H, n=25)
positive=[float(sp.re(z)) for z in r if abs(float(sp.im(z)))<1e-12 and float(sp.re(z))>0]
assert len(positive)==1
root=positive[0]
xx=float(sp.sqrt(T.subs(y,root)))
k=float(K.subs(y,root))
assert abs(root-1.3484274698276137)<1e-11
assert abs(xx-1.2546645546692903)<1e-11
assert abs(k-3.483450219447046)<1e-11

# Finite cyclic character orthogonality: for all N>=9 no differences
# among -4,-3,...,4 coincide, so cyclic and circle fourth moments agree.
for N in [9,10,11,13,17,29,101]:
    residues=[j%N for j in range(-4,5)]
    assert len(set(residues))==9
    test=[sp.Integer(z) for z in [2,5,7,3,4]]
    C=sum(z*z for z in test)
    ap=C*C+2*sum(sum(test[j]*test[j+h] for j in range(5-h))**2 for h in range(1,5))
    cyc=[sum(test[j]*test[k] for j in range(5) for k in range(5) if (j-k-h)%N==0) for h in range(N)]
    assert sum(z*z for z in cyc)==ap

print('PASS: exact fourth-moment polynomial, stationary identities, elimination factorization,')
print('      boundary rational forms, positive root and constants, finite-grid nonaliasing.')
print('positive_root=%.15f inner_ratio=%.15f sharp_fourth_power=%.15f' % (root,xx,k))
