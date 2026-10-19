#!/usr/bin/env python3
"""Exact 8-by-8 tetrahedral tracefree-Hessian Gram reduction.
Requires SymPy; run: python3 check_gram.py
"""
import sympy as sp
D,Q,R,T=sp.symbols('D Q R T')
v0=sp.Matrix([1,1,1])/sp.sqrt(3)
u=sp.Matrix([1,-1,0])/sp.sqrt(2)
z=sp.Matrix([1,1,-2])/sp.sqrt(6)
A=[u*u.T-z*z.T,u*z.T+z*u.T]
H=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
blocks=[]
for h in H:
    U=sp.diag(*h)
    w=U*v0;B=[U*a*U for a in A]
    if h==(1,1,1):blocks.append(D*sp.eye(2));continue
    C=sp.zeros(2)
    for a in range(2):
        for b in range(2):
            C[a,b]=sp.simplify(
                T*(w.T*A[a]*w)[0]*(v0.T*B[b]*v0)[0]
                +4*R*(v0.T*B[b]*A[a]*w)[0]
                +2*Q*sp.trace(A[a]*B[b]))
    blocks.append(C)
LA=D+sp.Rational(4,3)*Q-sp.Rational(32,9)*R+sp.Rational(32,27)*T
LB=D-4*Q-sp.Rational(32,9)*R-sp.Rational(32,27)*T
LC=D+sp.Rational(28,9)*Q+sp.Rational(160,27)*R+sp.Rational(32,81)*T
chars=[lambda h:1,lambda h:h[0],lambda h:h[1],lambda h:h[2]]
for j,character in enumerate(chars):
    M=sum((character(h)*B for h,B in zip(H,blocks)),sp.zeros(2))
    if j==0:
        assert all(sp.simplify(v)==0 for v in (M-LA*sp.eye(2)))
    else:
        assert sp.simplify(sp.trace(M)-LB-LC)==0
        assert sp.factor(M.det()-LB*LC)==0
print('PASS: exact 3 Gram levels, multiplicities 2,3,3')
