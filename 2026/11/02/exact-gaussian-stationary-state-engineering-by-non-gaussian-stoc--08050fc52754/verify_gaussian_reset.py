#!/usr/bin/env python3
"""Deterministic checks for Gaussian targets of OU diffusion with independent reset locations.
Run: python verify_gaussian_reset.py (requires numpy, scipy, sympy).
All matrices, stationary moments and quadrature are independently constructed.
"""
import itertools
import numpy as np
import scipy.linalg as la
import sympy as sp
from numpy.polynomial.hermite import hermgauss

checks = 0

def assert_close(a,b,atol=5e-8):
    global checks
    assert np.allclose(a,b,rtol=1e-9,atol=atol), (a,b)
    checks+=1

def verify_case(A,D,S,m,extra):
    global checks
    d=len(m)
    Q=(A@S+S@A.T)/2-D
    vals=np.linalg.eigvalsh(Q)
    assert vals[0]>1e-8
    checks+=1
    h=A@m
    threshold=np.trace(np.linalg.solve(S,Q))+h@la.solve(Q,h)/4
    r=threshold+extra
    invS=la.inv(S)
    L=la.cholesky(S,lower=True)
    nodes,weights=hermgauss(14)
    nodes=nodes*np.sqrt(2)
    weights=weights/np.sqrt(np.pi)
    # Gauss-Hermite quadrature integrates the relevant Gaussian polynomial exactly.
    grid=np.array(list(itertools.product(range(len(nodes)),repeat=d)))
    zz=np.stack([nodes[grid[:,j]] for j in range(d)],axis=1)
    weightsprod=np.prod(np.stack([weights[grid[:,j]] for j in range(d)],axis=1),axis=1)
    x=m+zz@L.T
    y=(x-m)@invS.T
    ratio=1+(np.einsum('ni,ij,nj->n',y,Q,y)+y@h-np.trace(invS@Q))/r
    assert ratio.min()>=-1e-12
    checks+=1
    def EG(f):return np.tensordot(weightsprod,f,axes=(0,0))
    def EM(f):return np.tensordot(weightsprod*ratio,f,axes=(0,0))
    assert_close(EM(np.ones(len(x))),1)
    assert_close(EM(x),m+h/r)
    M=S+np.outer(m,m)
    MR=M+(A@M+M@A.T-2*D)/r
    assert_close(np.einsum('n,ni,nj->ij',weightsprod*ratio,x,x),MR)
    for exp in itertools.product(range(6),repeat=d):
        if sum(exp)>5:continue
        a,b=exp
        X,Y=x[:,0],x[:,1]
        f=X**a*Y**b
        dx=a*X**(a-1)*Y**b if a else np.zeros_like(X)
        dy=b*X**a*Y**(b-1) if b else np.zeros_like(X)
        dxx=a*(a-1)*X**(a-2)*Y**b if a>=2 else np.zeros_like(X)
        dyy=b*(b-1)*X**a*Y**(b-2) if b>=2 else np.zeros_like(X)
        dxy=a*b*X**(a-1)*Y**(b-1) if a and b else np.zeros_like(X)
        Ax=x@A.T
        generator=-Ax[:,0]*dx-Ax[:,1]*dy+D[0,0]*dxx+2*D[0,1]*dxy+D[1,1]*dyy
        assert_close(EG(generator)+r*(EM(f)-EG(f)),0,atol=1e-6)
    # Exact minimizer of density tilt witnesses sharp threshold.
    ystar=-la.solve(Q,h)/2
    minpoly=ystar@Q@ystar+h@ystar-np.trace(invS@Q)
    assert_close(minpoly,-threshold)
    checks+=1
    # Characteristic polynomial of the lag-covariance generator.
    t=0.7
    C=la.expm(-(A+r*np.eye(d))*t)@S
    derivative=-(A+r*np.eye(d))@C
    assert_close(derivative+(A+r*np.eye(d))@C,0)
    assert_close(-np.trace((-(A+r*np.eye(d))@S)@invS+A)/d,r)

A=np.array([[2.,1.],[-.3,1.4]])
D=np.array([[.5,.1],[.1,.9]])
verify_case(A,D,3*np.eye(2),np.array([1.,-2.]),.8)
verify_case(np.diag([1.3,2.1]),np.diag([.4,.7]),np.diag([.9,1.4]),np.array([0.8,0.1]),.5)

# Rank-deficient boundary cases: Q=diag(q,0), h orthogonal to nullspace.
k=sp.Rational(2); dif=sp.Rational(1)
S=sp.diag(1,sp.Rational(1,2)); A=sp.diag(2,2); D=sp.eye(2)
Q=(A*S+S*A.T)/2-D
assert Q==sp.diag(1,0)
checks+=1
h=sp.Matrix([2,0]); threshold=sp.trace(S.inv()*Q)+ (h.T*sp.diag(1,0)*h)[0]/4
assert threshold==2
checks+=1
# If the mean acts along the nullspace, the quadratic tilt has unbounded negative directions.
hbad=sp.Matrix([0,1]); assert (Q*hbad)==sp.zeros(2,1)
checks+=1

# Exact isotropic mean feasibility threshold, with dimension-dependent jump at r=d*k.
q,beta,d,k=sp.symbols('q beta d k',positive=True)
f=d*k*(1-1/q+beta**2/(q-1))
qstar=1/(1-beta)
assert sp.simplify(f.subs(q,qstar)-d*k*(2*beta-beta**2))==0
checks+=1
assert sp.simplify(sp.diff(f,q)-d*k*((q-1)**2-beta**2*q**2)/(q**2*(q-1)**2))==0
checks+=1
for B in (sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4)):
    qq=qstar.subs(beta,B)
    deriv=sp.diff(f,q).subs({q:qq,beta:B,d:2,k:3})
    assert deriv==0
    checks+=1
for B in (sp.Rational(1),sp.Rational(3,2),sp.Rational(3)):
    # For beta >= 1, the infimum is d*k and is attained only at infinite variance.
    assert sp.simplify(f.subs({beta:B})-d*k).subs({d:2,k:3,q:2})>0
    checks+=1
print(f'PASS: {checks} deterministic Gaussian quadrature, generator, matrix and symbolic checks')
