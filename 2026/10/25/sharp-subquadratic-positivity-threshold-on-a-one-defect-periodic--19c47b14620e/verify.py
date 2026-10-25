#!/usr/bin/env python3
"""Exact certificate for a one-defect five-element periodic heat discretization.

Requires Python 3 and SymPy. Run: python verify.py.
"""
import sympy as sp
h, z = sp.symbols('h z', positive=True)
lengths = [h, sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1)]
M, K = sp.zeros(5), sp.zeros(5)
for i, ell in enumerate(lengths):
    j = (i + 1) % 5
    for q in (i, j):
        M[q, q] += ell / 3
        K[q, q] += 1 / ell
    M[i, j] += ell / 6
    M[j, i] += ell / 6
    K[i, j] -= 1 / ell
    K[j, i] -= 1 / ell
R = (6*h*(M+z*K)).applyfunc(sp.expand)
S = (6*h*M).applyfunc(sp.expand)
D = sp.factor(R.det(method='domain-ge'))
Q = 12*h**2*z+4*h**2+36*h*z**2+60*h*z+7*h+144*z**2+48*z
D_expected = 6*h**4*(36*h*z**2+60*h*z+7*h+144*z**2+60*z+4)*Q
assert sp.expand(D-D_expected) == 0
T = (R.inv(method='DM')*S).applyfunc(sp.cancel)
F = (216*h+864)*z**3+(576-36*h**2)*z**2+(96-132*h**2-18*h)*z+2*h-13*h**2
H = 216*h*z**3+324*h*z**2+234*h*z+23*h+864*z**3+1296*z**2+432*z+32
G = 180*h**2*z**2+228*h**2*z+29*h**2+216*h*z**3+864*h*z**2+342*h*z+26*h+864*z**3+576*z**2+96*z
J = 6*h**2*z-h**2+36*h*z**2+42*h*z+4*h+144*z**2+72*z+8
W = 108*h**2*z**2+108*h**2*z+15*h**2+216*h*z**3+648*h*z**2+342*h*z+32*h+864*z**3+864*z**2+216*z+8
U = 3*h**3+12*h**2*z+4*h**2+36*h*z**2+60*h*z+4*h+144*z**2+48*z
representatives = {
 (0,1):18*(h+1)*H,
 (0,2):36*F,
 (0,3):36*(6*z-1)*Q,
 (0,4):36*G,
 (2,0):18*(h+1)*(6*z-1)*J,
 (2,1):18*(h+1)*W,
 (2,3):36*(3*h+6*z+2)*Q,
 (2,4):36*(6*z-1)*U,
 (3,0):18*(h+1)*(6*z-1)*Q,
 (3,2):36*(3*h+6*z+2)*Q,
}
reflection = {0:1,1:0,2:4,3:3,4:2}
covered = set()
for (i,j), formula in representatives.items():
    for (u,v) in [(i,j),(reflection[i],reflection[j])]:
        assert u!=v
        assert sp.expand(sp.cancel(T[u,v]*D)-h**4*z*formula)==0, (u,v)
        covered.add((u,v))
assert len(covered)==20
for i in range(5):
    diag = sp.Poly(sp.cancel(T[i,i]*D), h,z)
    assert all(v>0 for v in diag.coeffs())
assert sp.expand(F.subs(z,sp.Rational(1,6))+36*(h-1)*(h+1))==0
assert sp.expand(F.subs(z,h**2/6)-h*(h-1)**2*(h+1)**3*(h+2))==0
assert sp.expand(F.subs(h,1)-(6*z-1)*(180*z**2+120*z+11))==0
c=sp.symbols('c')
assert sp.Poly(sp.expand(F.subs(z,h/6+c)),h).coeff_monomial(h**3)==6*(c-3)
# Rational checks on both sides of the unique positive cubic root.
tests=0
for hh in [sp.Integer(1),sp.Rational(11,10),sp.Rational(3,2),sp.Integer(2),sp.Integer(3),sp.Integer(10)]:
    ff=sp.Poly(F.subs(h,hh),z)
    roots=sp.polys.polytools.intervals(ff, eps=sp.Rational(1,10**10))
    positives=[it for it,mult in roots if it[0]>=0 and mult==1]
    assert len(positives)==1
    lo,hi=positives[0]
    if hh>1: assert sp.Rational(1,6)<lo<=hi<hh**2/6
    for step in [sp.Rational(1,12),sp.Rational(1,6),lo-1/sp.Integer(10**8),hi+1/sp.Integer(10**8),hh**2/6]:
        if step<=0:continue
        Pval=T.subs({h:hh,z:step})
        nonnegative=all(x>=0 for x in Pval)
        predicted=step==0 or F.subs({h:hh,z:step})>=0 and step>=sp.Rational(1,6)
        assert nonnegative==predicted,(hh,step)
        tests+=1
print('PASS: exact 5x5 determinant; 20 off-diagonal and five diagonal polynomial identities')
print('PASS: two endpoint factorizations and asymptotic coefficient')
print(f'PASS: {tests} exact-rational matrix sign comparisons, six mesh ratios')
