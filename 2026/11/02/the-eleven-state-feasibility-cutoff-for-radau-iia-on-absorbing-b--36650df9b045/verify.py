#!/usr/bin/env python3
"""Exact identities for Radau IIA on absorbing unit-rate birth chains.

Requires SymPy (e.g. pip install sympy); does not rely on any external data.
"""
from fractions import Fraction
import sympy as sp

h, z = sp.symbols('h z', real=True)
A = h*h + 4*h + 6
B = 2*h*(h+2)
C = h*h
R = lambda zz: (6 + 2*zz)/(6 - 4*zz + zz*zz)
f = sp.factor(R(h*(z-1)))
cs = [(6-2*h)/A, (2*h+B*(6-2*h)/A)/A]
bs = [1-cs[0]]
checks = 0
for k in range(2, 11):
    cs.append(sp.factor((B*cs[-1]-C*cs[-2])/A))
for k in range(1, 11):
    bs.append(sp.factor(bs[-1]-cs[k]))
for k in range(11):
    assert sp.cancel(sp.diff(f,z,k).subs(z,0)/sp.factorial(k)-cs[k]) == 0
    checks += 1
# Absorbing-column generating function: (1-f(z))/(1-z).
g = sp.factor((1-f)/(1-z))
for k in range(11):
    assert sp.cancel(sp.diff(g,z,k).subs(z,0)/sp.factorial(k)-bs[k]) == 0
    checks += 1
P = h**5+30*h**4+180*h**3+360*h**2+180*h-72
assert sp.cancel(bs[4]-h**5*P/A**5) == 0
checks += 1
# Nonabsorbing block and absorbing column in full matrix at dimension six.
n = 6
Q = sp.zeros(n)
for i in range(n-1):
    Q[i,i] = -1
    Q[i,i+1] = 1
M = (6*sp.eye(n)+2*h*Q)*(6*sp.eye(n)-4*h*Q+h*h*(Q*Q)).inv()
for i in range(n):
    for j in range(n):
        expected = ((cs[j-i] if j >= i else 0) if j < n-1 and i<n-1 else
                    (bs[n-2-i] if i<n-1 and j==n-1 else
                     (1 if i==n-1 and j==n-1 else 0)))
        assert sp.cancel(M[i,j]-expected) == 0
        checks += 1
# At h=3 every required coefficient is positive up to index nine.
for k in range(11):
    ck = sp.factor(cs[k].subs(h,3))
    bk = sp.factor(bs[k].subs(h,3))
    assert ck >= 0 if k<=10 else True
    assert bk > 0 if k<=9 else True
    checks += 2
assert bs[10].subs(h,3)<0
checks += 1
# The necessary polynomial has exactly one positive real root by positive derivative,
# and certified rational bracket below.
assert P.subs(h,sp.Rational(253946,1000000)) < 0
assert P.subs(h,sp.Rational(253947,1000000)) > 0
assert sp.Poly(sp.diff(P,h),h).all_coeffs()==[5,120,540,720,180]
checks += 3
# Independently cross-check against rational matrix inverses for multiple n/h.
for n in (2,3,4,5,6,7,11,12):
    Q = sp.zeros(n)
    for i in range(n-1):
        Q[i,i] = -1
        Q[i,i+1] = 1
    for hv in (sp.Rational(1,3),sp.Rational(1),sp.Rational(3),sp.Rational(4)):
        actual = (6*sp.eye(n)+2*hv*Q)*(6*sp.eye(n)-4*hv*Q+hv*hv*(Q*Q)).inv()
        for i in range(n):
            for j in range(n):
                expected = ((cs[j-i] if j >= i else 0) if j < n-1 and i<n-1 else
                            (bs[n-2-i] if i<n-1 and j==n-1 else
                             (1 if i==n-1 and j==n-1 else 0)))
                assert actual[i,j] == sp.cancel(sp.sympify(expected).subs(h,hv))
                checks += 1
print('EXACT_VERIFICATION_PASS',checks)
