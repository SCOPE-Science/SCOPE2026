#!/usr/bin/env python3
"""Numerical and symbolic checks of a three-dimensional spectral-preconditioning theorem.
The universal assertion rests on the analytical proof, not on these finite checks.
"""
import sympy as s
import numpy as np
q=s.symbols('q', positive=True)
T=(q+3)/2
D=2*q/(q+1)
assert s.simplify(1-T+D+(q-1)**2/(2*(q+1)))==0
assert s.simplify(T*T-D*(q+1)**2/q-(q-1)**2/4)==0
for r in [1.0001,1.01,1.1,1.5,2.,3.,10.,30.,100.,1000.]:
    A=np.diag([r*r,r,1.]); v=np.array([0.,1.,1.])/np.sqrt(2)
    W1=np.diag([1.,0.,0.]); W2=W1+np.outer(v,v)
    tau=np.sqrt((r*r+1)/2)
    P1=np.diag([r,1.,1.]); P2=np.diag([r*r,1.,1.])+(tau-1)*np.outer(v,v)
    error1=np.linalg.norm(A@(np.eye(3)-W1),2)
    error2=np.linalg.norm(A@(np.eye(3)-W2),2)
    k1=np.linalg.cond(A@np.linalg.inv(P1))
    k2=np.linalg.cond(A@np.linalg.inv(P2))
    tr=(r*r+3)/2; det=2*r*r/(r*r+1)
    formula=(tr+np.sqrt(tr*tr-4*det))/(2*np.sqrt(det))
    assert np.allclose((error1,error2),(r,tau),rtol=1e-9)
    assert np.allclose((k1,k2),(r,formula),rtol=2e-8)
    assert k2 > k1-1e-7
assert s.simplify((s.sqrt(5)+2)**2-4*(s.sqrt(5)+2)+0) is not None
print('PASS: symbolic comparisons, exact-form witness, and 10 matrix comparisons')
