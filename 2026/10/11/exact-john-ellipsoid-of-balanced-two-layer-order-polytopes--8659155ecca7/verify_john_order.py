"""Standalone algebraic and numerical checks for two-level order-polytope John ellipsoids.

Uses only the stated rational/algebraic parameter formulas, with no external data.
Run: python3 verify_john_order.py
"""
import math
import numpy as np
import sympy as sp

k, t = sp.symbols('k t', positive=True)
a = (1-t)/2
u = a*t/(1+t)
w = a/2
z = a*t/2
P = (2*k+1)*t*t+(4*k-2)*t-(2*k-1)
alpha = ((k-1)*u+(w+z)/2)/k
gamma = (w-z)/(2*k)
for label, expr in [('diagonal',alpha-a*a),('comparison',2*(alpha-gamma)-t*t)]:
    num = sp.fraction(sp.cancel(expr))[0]
    rem = sp.rem(sp.Poly(num,t),sp.Poly(P,t),t)
    assert sp.simplify(rem.as_expr())==0, (label,rem)

checks = 0
for n in range(1,61):
    tau=(2*math.sqrt(n*(2*n-1))-(2*n-1))/(2*n+1)
    a=(1-tau)/2
    d=2*n
    M=(2/a+2/tau)*np.eye(d)
    M[:n,n:] -= (2/(n*tau))*np.ones((n,n))
    M[n:,:n] -= (2/(n*tau))*np.ones((n,n))
    A=np.linalg.inv(M)
    assert np.linalg.eigvalsh(A)[0]>0
    c=np.r_[np.full(n,a),np.full(n,1-a)]
    normals=[];dist=[];weights=[]
    for i in range(n):
        v=np.zeros(d);v[i]=-1
        normals.append(v);dist.append(a);weights.append(1-tau)
    for i in range(n):
        v=np.zeros(d);v[n+i]=1
        normals.append(v);dist.append(a);weights.append(1-tau)
    for i in range(n):
        for j in range(n):
            v=np.zeros(d);v[i]=1;v[n+j]=-1
            normals.append(v);dist.append(tau);weights.append(2*tau/n)
    N=np.array(normals)
    distances=np.array(dist)
    weights=np.array(weights)
    vals=np.einsum('ij,jk,ik->i',N,A,N)
    assert np.max(np.abs(vals-distances**2))<1e-10,(n,'facet contact')
    assert np.linalg.norm((weights/distances)@N)<1e-10,(n,'equilibrium')
    R=N.T @ np.diag(weights/distances**2) @ N
    assert np.max(np.abs(R-M))<1e-10,(n,'John matrix')
    assert abs(sum(weights)-d)<1e-10
    eig=np.linalg.eigvalsh(A)
    expected=sorted([a*tau/2,a/2]+[a*tau/(1+tau)]*(2*n-2))
    assert np.max(np.abs(eig-expected))<1e-10,(n,'eigenvalues')
    checks+=len(weights)
print('PASS: formal polynomial identities, all contact inequalities, John matrix and equilibrium,')
print('      exact eigenvalue patterns for k=1..60; total facet checks', checks)
