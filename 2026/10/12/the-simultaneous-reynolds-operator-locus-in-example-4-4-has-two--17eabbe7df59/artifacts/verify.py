import sympy as sp
from itertools import product

a11,a12,a13,a21,a22,a23,a31,a32,a33=sp.symbols(
    "a11 a12 a13 a21 a22 a23 a31 a32 a33"
)
vars_=[a11,a12,a13,a21,a22,a23,a31,a32,a33]
M=sp.Matrix([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
basis=[sp.eye(3)[:,i] for i in range(3)]

def L(x,y):
    return sp.Matrix([0,sp.expand(x[0]*y[1]-x[1]*y[0]),0])

def T(x,y,z):
    return sp.Matrix([0,sp.expand(sp.Matrix.hstack(x,y,z).det()),0])

def R(x):
    return M*x

def nonzero_polys(vec):
    return [sp.expand(v) for v in vec if sp.expand(v)!=0]

lie=[]
for x,y in product(basis,repeat=2):
    defect=L(R(x),R(y))-R(L(R(x),y)+L(x,R(y))-L(R(x),R(y)))
    lie += nonzero_polys(defect)

tri=[]
for x,y,z in product(basis,repeat=3):
    defect=T(R(x),R(y),R(z))-R(
        T(R(x),R(y),z)+T(R(x),y,R(z))+T(x,R(y),R(z))-T(R(x),R(y),R(z))
    )
    tri += nonzero_polys(defect)

joint=sp.groebner(lie+tri,*vars_,order="lex")
expected=[
    a12*(a11+a22),
    a22**2*(a11+a22),
    a11*a23-a13*a21-a22*a23,
    a32*(a11+a22),
    a12*a13,
    a12*a21+a22**2,
    a12*a23,
    a13*a22**2,
    a13*a32,
    a22**2*a23,
    a23*a32,
]
E=sp.groebner(expected,*vars_,order="lex")
assert all(E.reduce(p)[1]==0 for p in lie+tri)
assert all(joint.reduce(p)[1]==0 for p in expected)

I1=[a12,a22,a32,a11*a23-a21*a13]
I2=[a11+a22,a13,a23,a12*a21+a22**2]
G1=sp.groebner(I1,*vars_,order="lex")
G2=sp.groebner(I2,*vars_,order="lex")
assert all(G1.reduce(p)[1]==0 for p in lie+tri)
assert all(G2.reduce(p)[1]==0 for p in lie+tri)

# Ideal-theoretic intersection I1 cap I2 by elimination.
u=sp.symbols("u")
GI=sp.groebner([u*f for f in I1]+[(1-u)*f for f in I2],u,*vars_,order="lex")
intersection=[sp.expand(p.as_expr()) for p in GI.polys if not p.as_expr().has(u)]
expected_intersection=sp.groebner([
    a11*a12+a12*a22,
    a11*a22+a22**2,
    a11*a23-a13*a21,
    a11*a32+a22*a32,
    a12*a13,
    a12*a21+a22**2,
    a12*a23,
    a13*a22,
    a13*a32,
    a22*a23,
    a23*a32,
],*vars_,order="lex")
GI2=sp.groebner(intersection,*vars_,order="lex")
assert all(expected_intersection.reduce(p)[1]==0 for p in intersection)
assert all(GI2.reduce(p.as_expr())[1]==0 for p in expected_intersection.polys)

# Adding component ideals gives their geometric intersection A^3.
Gsum=sp.groebner(I1+I2,*vars_,order="lex")
sum_expected=sp.groebner([a11,a12,a13,a22,a23,a32],*vars_,order="lex")
assert all(sum_expected.reduce(p.as_expr())[1]==0 for p in Gsum.polys)
assert all(Gsum.reduce(p.as_expr())[1]==0 for p in sum_expected.polys)

witnesses=[
    {a11:0,a12:0,a13:1,a21:0,a22:0,a23:0,a31:0,a32:0,a33:0},
    {a11:0,a12:0,a13:0,a21:1,a22:0,a23:0,a31:0,a32:1,a33:0},
]
for w in witnesses:
    assert all(sp.expand(p.subs(w))==0 for p in lie+tri)

print("groebner_joint_size",len(joint.polys))
print("component_intersection_dimension",3)
print("boundary_witnesses",len(witnesses))
print("VERIFY_OK")
