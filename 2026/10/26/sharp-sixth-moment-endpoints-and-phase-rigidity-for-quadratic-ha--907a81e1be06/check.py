#!/usr/bin/env python3
"""Reproducible exact checks for the spherical quadratic sixth-moment theorem.
Requires SymPy; computes moments directly from the normalized S^3 monomial rule.
"""
from fractions import Fraction
from math import factorial
from itertools import product
from sympy import symbols, Poly, Rational, expand, Matrix, simplify

x = symbols('x0:4')

def odd_df(k):
    out = 1
    for j in range(1, k+1): out *= 2*j-1
    return out

def sphere_integral(poly):
    P = Poly(expand(poly), *x)
    ans = Rational(0)
    for ex, cf in P.terms():
        if any(e % 2 for e in ex): continue
        ks = [e//2 for e in ex]
        m = sum(ks)
        denominator = 1
        for j in range(m): denominator *= 4+2*j
        numerator = 1
        for k in ks: numerator *= odd_df(k)
        ans += cf * Rational(numerator, denominator)
    return simplify(ans)

def f_of(A):
    return expand(sum(A[i,j]*x[i]*x[j] for i in range(4) for j in range(4)))

def test_real(lam):
    assert sum(lam) == 0
    p = [None] + [sum(z**k for z in lam) for k in range(1,7)]
    Q = sum(z*x[i]**2 for i,z in enumerate(lam))
    v2 = sphere_integral(Q**2)
    v6 = sphere_integral(Q**6)
    exact2 = p[2]/12
    exact6 = (4320*p[2]*p[4]+1920*p[3]**2-360*p[2]**3)/322560
    assert simplify(v2-exact2) == 0
    assert simplify(v6-exact6) == 0
    normratio = simplify(v6/v2**3)
    assert normratio >= Rational(27,7) and normratio <= 15
    return normratio

def test_complex(A,B):
    assert A == A.T and B == B.T and A.trace()==0 and B.trace()==0
    U,V=f_of(A),f_of(B)
    a,b,c=sphere_integral(U**2),sphere_integral(V**2),sphere_integral(U*V)
    v6=sphere_integral((U**2+V**2)**3)
    assert v6 <= 15*(a+b)**3-36*(a+b)*(a*b-c*c)
    return v6/(a+b)**3

checks = 0
# No Gaussian moment formula is used in these independent integrations.
real_specs = [
    (1,1,-1,-1), (3,-1,-1,-1), (1,-1,0,0),
    (5,0,-2,-3), (2,4,-3,-3), (3,2,-1,-4),
    (8,-7,4,-5), (11,-5,-5,-1), (1,2,3,-6),
]
for spec in real_specs:
    vals = tuple(Rational(z) for z in spec)
    ratio = test_real(vals)
    checks += 1
    if spec == (1,1,-1,-1): assert ratio == Rational(27,7)
    if spec == (3,-1,-1,-1): assert ratio == 15

# Complex and off-diagonal spherical quadratic forms.
M = [
 Matrix([[3,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]]),
 Matrix([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]]),
 Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]]),
 Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]),
 Matrix([[2,1,0,0],[1,-2,0,0],[0,0,1,0],[0,0,0,-1]])
]
for i,A in enumerate(M):
    for j,B in enumerate(M):
        if i==j: continue
        z = test_complex(A,B)
        assert z <= 15
        checks += 1

# Exact certificates behind extremizers and sixth-moment normalizations.
s,t,u = symbols('s t u', real=True)
p2 = s**2+(t**2+u**2)/2
lam = [(s+t)/2,(s-t)/2,(-s+u)/2,(-s-u)/2]
p3 = sum(z**3 for z in lam)
p4 = sum(z**4 for z in lam)
p6 = sum(z**6 for z in lam)
assert simplify(p3 - 3*s*(t*t-u*u)/4) == 0
assert simplify(p4-(s**4/4+3*s*s*(t*t+u*u)/4+(t**4+u**4)/8)) == 0
assert simplify(p6-(Rational(3,4)*p2*p4+p3*p3/3-p2**3/8)) == 0
checks += 3
print('PASS: %d independent exact integrals/certificates; sharp real endpoints 27/7 and 15; complex phase-deficit inequality.' % checks)
