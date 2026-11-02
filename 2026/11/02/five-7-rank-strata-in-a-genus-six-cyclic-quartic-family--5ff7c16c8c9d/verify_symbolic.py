#!/usr/bin/env python3
"""Exact symbolic identities for the degree-four cyclic-cover family in characteristic seven."""
import sympy as sp

p=7
x,a,b=sp.symbols('x a b')
f=x**5+a*x**2+b*x+1
basis=[(1,0),(2,0),(2,1),(3,0),(3,1),(3,2)]

def red(z):
    return sp.Poly(sp.expand(z),a,b,modulus=p).as_expr()

M=sp.zeros(6)
for col,(j,i) in enumerate(basis):
    target=next(v for v in (1,2,3) if (p*v-j)%4==0)
    e=(p*target-j)//4
    power=sp.Poly(x**i*f**e,x)
    for row,(r,s) in enumerate(basis):
        if r==target:
            M[row,col]=red(power.nth(p*(s+1)-1))

U=a**3-b
V=3*a
W=3*a*a*b+3
H=-2*a**4-3*a*b+3*b**3
v0=3*a**3+2*a*a*b*b-2*a*b**4-b
E=sp.zeros(6)
E[0,4]=1
E[1,1]=U; E[1,2]=W; E[2,2]=V
E[3,0]=v0; E[4,0]=H; E[5,0]=-2
assert all(red(M[i,j]-E[i,j])==0 for i in range(6) for j in range(6))
assert red(M[1,1]*M[2,2]-3*a*(a**3-b))==0
assert red((M[0,3:6]*M[3:6,0])[0]-H)==0
D=3*a**5+a**4*b**2+3*a**2*b+3*a*b**3-3*b**5+3
assert red(sp.discriminant(f,x)-D)==0
assert red(D.subs({a:0,b:0})-3)==0
assert red(H.subs(b,a**3)-a**4*(2+3*a**5))==0
# At the five nonzero intersections a^5=4, discriminant is 4.
t=sp.symbols('t')
polyD=sp.Poly(red(D.subs(b,a**3)),a,modulus=p)
assert sp.rem(polyD,sp.Poly(a**5-4,a,modulus=p)).as_expr()%7==4
# Exactly one affine singularity, a nondegenerate node.
GB=sp.groebner([H,sp.diff(H,a),sp.diff(H,b)],b,a,modulus=p)
assert [sp.expand(g.as_expr()) for g in GB.polys]==[b,a]
assert red(sp.diff(H,a,b))==-3
# No singularity at infinity for 3 B^3 Z - 3 A B Z^2 - 2 A^4.
A,B,Z=sp.symbols('A B Z')
proj=3*B**3*Z-3*A*B*Z**2-2*A**4
assert (sp.diff(proj,Z).subs({A:0,B:1,Z:0})%p)!=0
print('CYCLIC4_G6_SYMBOLIC_OK')
