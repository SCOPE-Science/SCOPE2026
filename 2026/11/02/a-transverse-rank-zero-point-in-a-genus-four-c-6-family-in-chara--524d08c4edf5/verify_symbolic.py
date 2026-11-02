#!/usr/bin/env python3
"""Exact polynomial identities over F_5 for a genus-four hyperelliptic family.
Run: python verify_symbolic.py. Requires sympy.
"""
from itertools import combinations
from sympy import symbols, Poly, Matrix, discriminant, gcd, factor_list

x,a,b=symbols('x a b')
f=x**10+x**7+a*x**4+b*x
fp=Poly(f**2,x)
P=lambda z: Poly(z,a,b,modulus=5)
def eq(z,w):
    assert P(z-w).is_zero, (z,w,P(z-w))
M=Matrix(4,4,lambda i,j: fp.coeff_monomial(x**(5*(i+1)-(j+1))))
want=Matrix([[0,0,b*b,0],[0,a*a+2*b,0,0],[1+2*a,0,0,2*(a+b)],[0,0,2,0]])
for z,w in zip(M,want):eq(z,w)
assert P(M.det()).is_zero
C=a*a+2*b
S=b*b*(1+2*a**5)+4*(a**5+b**5)
# The nontrivial Cartier square produces S in coordinate (3,3).
Mp=M.applyfunc(lambda z:z**5)
M2=Mp*M
for i in range(4):
    for j in range(4):
        if (i,j)==(2,2):eq(M2[i,j],S)
# Discriminant and the two algebraic rank-drop equations.
z=symbols('z')
d=discriminant(z**3+z**2+a*z+b,z)
Delta=a**3+a**2-2*a*b-2*b*b+b
eq(d,Delta)
# C=0 means b=2a^2 in characteristic 5.
t=symbols('t')
sa=Poly(S.subs({a:t,b:2*t*t}),t,modulus=5)
da=Poly(Delta.subs({a:t,b:2*t*t}),t,modulus=5)
assert sa==Poly(-2*t**4*(t+1)*(t-2)**5,t,modulus=5)
assert da==Poly(2*t*t*(t-2)**2,t,modulus=5)
# S = (2b^2+4)a^5 + b^2+4b^5: primitive and not a fifth power.
nb=Poly(b*b+4*b**5,b,modulus=5)
db=Poly(2*b*b+4,b,modulus=5)
assert gcd(nb,db).degree()==0
# Numerator of d(nb/db)/db is nonzero, excluding rational fifth powers.
der=nb.diff()*db-nb*db.diff()
assert not der.is_zero
assert Poly(der.as_expr()-(3*b+4*b**6),b,modulus=5).is_zero
# On S=0, partial S/partial b = 2b(1+2a^5) and partial S/partial a = 0.
eq(S.diff(a),0)
eq(S.diff(b),2*b*(1+2*a**5))
# Exceptional parameter smooth and all four rank strata witnessed over F5.
assert P(Delta.subs({a:4,b:2})-3).is_zero
for aa,bb,cc,ss in [(0,2,1,1),(1,2,0,1),(0,1,1,0),(4,2,0,0)]:
    assert (bb*Delta.subs({a:aa,b:bb}))%5!=0
    assert (C.subs({a:aa,b:bb})%5==0)==(cc==0)
    assert (S.subs({a:aa,b:bb})%5==0)==(ss==0)
print('CHAR5_C6_SYMBOLIC_IDENTITIES_OK')
