#!/usr/bin/env python3
import sympy as s
u,v,z,w,x,y=s.symbols('u v z w x y')

def tangent_discriminant(M, subs):
    F=s.expand(M.subs(subs).det())
    P=s.Poly(F,u,v)
    q=s.expand(sum(c*u**i*v**j for (i,j),c in P.terms() if i+j==2))
    A=q.coeff(u,2)
    B=q.coeff(u,1).coeff(v,1)
    C=q.coeff(v,2)
    return s.factor(B**2-4*A*C)

examples={
'64':(s.Matrix([[x+w,0,0,2*z+2*w],[0,x+w,-2*y,-y-2*z],[0,-2*y,x+w,-2*w],[2*z+2*w,-y-2*z,-2*w,x]]),{x:u-w,y:v}),
'44':(s.Matrix([[x-w,0,0,z-2*w],[0,x-w,2*y,-y-z],[0,2*y,x-w,-y-2*w],[z-2*w,-y-z,-y-2*w,x]]),{x:u+w,y:v}),
'42':(s.Matrix([[x,0,0,-2*z-w],[0,x,y,-z],[0,y,x,-2*y-w],[-2*z-w,-z,-2*y-w,x]]),{x:u,y:v}),
'22':(s.Matrix([[x-2*w,0,0,z+w],[0,x-2*w,y,2*y+z],[0,y,x-2*w,-2*y+w],[z+w,2*y+z,-2*y+w,x]]),{x:u+2*w,y:v}),
'20':(s.Matrix([[x+w,0,0,-z-2*w],[0,x+w,-y,y+2*z],[0,-y,x+w,-2*y-2*w],[-z-2*w,y+2*z,-2*y-2*w,x]]),{x:u-w,y:v}),
}
expected={
'64':256*(w**2+2*w*z+2*z**2)*(2*w**2+2*w*z+z**2),
'44':32*(2*w**2-2*w*z+z**2)*(8*w**2-4*w*z+z**2),
'42':8*(w**2+2*w*z+2*z**2)*(w**2+4*w*z+5*z**2),
'22':4*(w**2+2*w*z+2*z**2)*(2*w**2+2*w*z+z**2),
'20':4*(4*w**2+4*w*z+5*z**2)*(8*w**2+4*w*z+z**2),
}

def binary_positive_definite(f):
    P=s.Poly(s.expand(f),z,w)
    A=P.coeff_monomial(z**2); B=P.coeff_monomial(z*w); C=P.coeff_monomial(w**2)
    return A>0 and s.expand(B**2-4*A*C)<0

for k,(M,subs) in examples.items():
    D=tangent_discriminant(M,subs)
    assert s.expand(D-expected[k])==0, (k,D)
    coeff, factors=s.factor_list(D)
    assert coeff>0 and len(factors)==2 and all(e==1 for _,e in factors)
    f1,f2=[f for f,e in factors]
    assert binary_positive_definite(f1)
    assert binary_positive_definite(f2)
    assert s.gcd(s.Poly(f1,z,w),s.Poly(f2,z,w)).total_degree()==0
    # Each positive-definite binary quadratic has two distinct nonreal projective roots;
    # coprimality makes the four roots distinct.
print('VERIFY_OK')
