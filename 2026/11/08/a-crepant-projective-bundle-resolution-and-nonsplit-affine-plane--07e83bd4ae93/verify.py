#!/usr/bin/env python3
"""Exact checks for characteristic-two conic discriminant geometry."""
import itertools, sympy as s
A,B,C,D,E,F,T,U,V=s.symbols('a b c d e f t u v')
X,Y,Z=s.symbols('x y z')
q=A*X**2+B*Y**2+C*Z**2+D*Y*Z+E*Z*X+F*X*Y
delta=A*D**2+B*E**2+C*F**2+D*E*F

def r2(poly):
    p=s.Poly(s.expand(poly), A,B,C,D,E,F,T,U,V,X,Y,Z, modulus=2)
    return p.as_expr()

def eq(u,v=0):
    assert r2(u-v)==0, f'failed: {u} != {v}'

eq(q.subs({X:D,Y:E,Z:F}),delta)
eq(s.diff(q,X).subs({X:D,Y:E,Z:F}),0)
eq(s.diff(q,Y).subs({X:D,Y:E,Z:F}),0)
eq(s.diff(q,Z).subs({X:D,Y:E,Z:F}),0)
for var,expected in zip((A,B,C,D,E,F),(D**2,E**2,F**2,E*F,D*F,D*E)):
    eq(s.diff(delta,var),expected)
for root,others,leading in ((D,(E,F),A),(E,(D,F),B),(F,(D,E),C)):
    mapping={root:T,others[0]:T*U,others[1]:T*V}
    expanded=s.expand(delta.subs(mapping, simultaneous=True))
    # Exact polynomial divisibility: both the constant and linear t coefficients vanish.
    poly=s.Poly(expanded,T)
    assert poly.nth(0)==0 and poly.nth(1)==0
    strict=poly.exquo(s.Poly(T**2,T)).as_expr()
    assert s.expand(strict.subs(T,0))!=0
    assert s.expand(s.diff(strict,leading))==1, (root,strict)
    print('blowup_chart',root,'strict_transform',strict)
# P2(F_{2^m}) enumerations, finite field operations over irreducible polynomials.
# degree 1: X+1, degree 2: X^2+X+1, degree 3: X^3+X+1.
mods={1:0b11,2:0b111,3:0b1011}
def gf_mul(a,b,m):
    mod=mods[m]; out=0
    while b:
        if b&1:out^=a
        b>>=1; a<<=1
        if a&(1<<m):a^=mod
    return out

def gadd(a,b):return a^b

def projective_reps(m,n):
    Q=1<<m
    for first in range(n):
        for rest in itertools.product(range(Q),repeat=n-first-1):
            yield (0,)*first+(1,)+rest

def dval(vals,m):
    a,b,c,d,e,f=vals
    return gf_mul(a,gf_mul(d,d,m),m)^gf_mul(b,gf_mul(e,e,m),m)^gf_mul(c,gf_mul(f,f,m),m)^gf_mul(d,gf_mul(e,f,m),m)
for m in (1,2,3):
    Q=1<<m
    Dpoints=sum(dval(vals,m)==0 for vals in projective_reps(m,6))
    predicted=(Q*Q+Q+1)*(Q*Q+1)
    assert Dpoints==predicted,(Q,Dpoints,predicted)
    Epoints=0
    for a,b,c in projective_reps(m,3):
        for d,e,f in projective_reps(m,3):
            Epoints+=(gf_mul(a,gf_mul(d,d,m),m)^gf_mul(b,gf_mul(e,e,m),m)^gf_mul(c,gf_mul(f,f,m),m))==0
    Epred=(Q*Q+Q+1)*(Q+1)
    assert Epoints==Epred,(Q,Epoints,Epred)
    print('field',Q,'discriminant',Dpoints,'exceptional',Epoints)
print('ALL_CHECKS_PASSED')
# Degree-three cohomology calculation for the twisted Frobenius-Euler kernel:
# H^0(O(1)^3) -> H^0(O(3)) sends (L1,L2,L3) to D^2L1+E^2L2+F^2L3.
monomials={(i,j,3-i-j) for i in range(4) for j in range(4-i)}
image={(i+2,j,k) for i,j,k in ((1,0,0),(0,1,0),(0,0,1))}
image|={(i,j+2,k) for i,j,k in ((1,0,0),(0,1,0),(0,0,1))}
image|={(i,j,k+2) for i,j,k in ((1,0,0),(0,1,0),(0,0,1))}
assert len(monomials)==10 and len(image)==9 and monomials-image=={(1,1,1)}
print('frobenius_euler_cokernel', 'dim',1, 'generator','D E F')
print('ALL_COHOMOLOGY_CHECKS_PASSED')
