#!/usr/bin/env python3
"""Exact polynomial and finite-field checks for the published three-conic model."""
import sympy as sp
x,y,z=sp.symbols('x y z')
q0=x*x+y*y-z*z
qp=4*x*x+5*y*y+4*y*z
qm=4*x*x+5*y*y-4*y*z
F=(q0,qp,qm)
assert sp.expand(qp-4*q0-(y+2*z)**2)==0
assert sp.expand(qm-4*q0-(y-2*z)**2)==0
assert sp.expand(qp-qm-8*y*z)==0
for q,det in zip(F,(-1,-16,-16)):
    H=sp.hessian(q,(x,y,z))/2
    assert H.det()==det
# Coordinates over Q(sqrt(-3),sqrt(-5)).
for u in (sp.sqrt(-3),-sp.sqrt(-3)):
    assert sp.simplify(q0.subs({x:u,y:-2,z:1}))==0
    assert sp.simplify(qp.subs({x:u,y:-2,z:1}))==0
    assert sp.simplify(q0.subs({x:u,y:2,z:1}))==0
    assert sp.simplify(qm.subs({x:u,y:2,z:1}))==0
for u in (sp.sqrt(-5),-sp.sqrt(-5)):
    assert sp.simplify(qp.subs({x:u,y:2,z:0}))==0
    assert sp.simplify(qm.subs({x:u,y:2,z:0}))==0
assert q0.subs({x:0,y:0,z:1})==-1
assert sp.simplify(q0.subs({x:sp.sqrt(-5),y:2,z:0}))==-1
assert qm.subs({x:sp.sqrt(-3),y:-2,z:1})==16
assert qp.subs({x:sp.sqrt(-3),y:2,z:1})==16
# Direct local length-four calculation in characteristic 3 at the Q0/Q+ merger.
X,Z=sp.symbols('X Z')
p3q0=sp.Poly(q0.subs({x:X,y:1,z:1+Z}),X,Z,modulus=3).as_expr()
p3qp=sp.Poly(qp.subs({x:X,y:1,z:1+Z}),X,Z,modulus=3).as_expr()
G=sp.groebner([p3q0,p3qp],Z,X,modulus=3)
assert set(map(str,[g.as_expr() for g in G.polys]))=={'X**2 + Z','X**4'}
assert sp.Poly(p3qp-X**2-Z,X,Z,modulus=3).is_zero
assert sp.Poly(p3q0.subs(Z,-X**2)+X**4,X,modulus=3).is_zero
# Direct local length-two calculation in characteristic 5 at the Q+/Q- merger.
p5qp=sp.Poly(qp.subs({x:X,y:1,z:Z}),X,Z,modulus=5).as_expr()
p5qm=sp.Poly(qm.subs({x:X,y:1,z:Z}),X,Z,modulus=5).as_expr()
assert sp.Poly(p5qp-p5qm-8*Z,X,Z,modulus=5).is_zero
assert sp.Poly(p5qp.subs(Z,0)-4*X**2,X,modulus=5).is_zero

def primes_le(n):
    return [p for p in range(3,n+1,2) if all(p%d for d in range(3,int(p**.5)+1,2))]

def legendre(a,p):
    b=pow(a%p,(p-1)//2,p)
    return 0 if b==0 else 1 if b==1 else -1

def enumerate_rational_support(p):
    pts=[]
    for X in range(p):
        for Y in range(p):pts.append((X,Y,1))
    for X in range(p):pts.append((X,1,0))
    pts.append((1,0,0))
    assert len(pts)==p*p+p+1
    found={}
    for X,Y,Z in pts:
        val=(X*X+Y*Y-Z*Z,4*X*X+5*Y*Y+4*Y*Z,4*X*X+5*Y*Y-4*Y*Z)
        mask=tuple(i for i,q in enumerate(val) if q%p==0)
        if len(mask)>=2:found[(X,Y,Z)]=mask
    assert all(len(m)==2 for m in found.values())
    return found

for p in primes_le(151):
    actual=enumerate_rational_support(p)
    if p==3:expected=5
    elif p==5:expected=2
    else:expected=1+4*(legendre(-3,p)==1)+2*(legendre(-5,p)==1)
    assert len(actual)==expected,(p,expected,len(actual))
print('VERIFY_OK: published conics, exact identities and local p3/p5 lengths, complete Fp census through 151')
