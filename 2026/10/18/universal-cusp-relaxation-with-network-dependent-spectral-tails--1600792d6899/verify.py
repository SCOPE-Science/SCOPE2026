#!/usr/bin/env python3
"""Symbolic identities and numerical corroboration for a logistic threshold-response cusp."""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import expm

z = sp.symbols('z')
g = sp.tanh(2*z)/2-z
a = sp.sech(2*z)**2
assert sp.series(g,z,0,9).removeO().expand() == (-sp.Rational(4,3)*z**3+sp.Rational(32,15)*z**5-sp.Rational(1088,315)*z**7)
assert sp.series(a,z,0,7).removeO().expand() == 1-4*z**2+sp.Rational(32,3)*z**4-sp.Rational(1088,45)*z**6
assert sp.simplify(sp.Rational(64,15)/sp.Rational(8,3)) == sp.Rational(8,5)
print('Exact symbolic coefficients: cubic -4/3; quintic 32/15; logarithmic -8/5; tangent a(y)=1-4y^2+32y^4/3+...')

def sigmoid(q):
    return 1/(1+np.exp(-q))

matrices = [
    np.array([[0.,1.],[1.,0.]]),
    np.array([[0.,.5,0.,.5],[.5,0.,.5,0.],[0.,.5,0.,.5],[.5,0.,.5,0.]]),
    np.array([[1.,0.],[0.,1.]]),
    np.array([[1.,0.,0.],[.4,.6,0.],[0.,1.,0.]])
]
for k,W in enumerate(matrices):
    n=len(W)
    assert np.min(W)>=0 and np.allclose(W.sum(axis=1),1)
    u0=.5+(.1+np.arange(n)*.012) * (-1 if k==1 else 1)
    def ode(t,u):return -u+sigmoid(-2+4*W.dot(u))
    T=2000.; times=[200.,600.,1200.,T]
    sol=solve_ivp(ode,(0,T),u0,t_eval=times,method='DOP853',rtol=1e-12,atol=1e-13)
    assert sol.success
    inv=(sol.y-.5)**(-2)
    rem=inv - (8./3.)*sol.t[None,:]+(8./5.)*np.log(sol.t)[None,:]
    assert np.all(np.sign(sol.y-.5)==np.sign(u0[0]-.5))
    assert np.allclose(inv[:,-1]/T,8/3,rtol=.04)
    if k < 2:
        assert max(rem[:,-1])-min(rem[:,-1]) < 1e-6, 'irreducible node constants should synchronize'
    if k == 2:
        assert abs(rem[0,-1]-rem[1,-1])>.2, 'reducible diagonal network should retain different constants'
    print('Network',k,'spectrum',np.linalg.eigvals(W),'renormalized constants at t=2000',rem[:,-1])

# Along a homogeneous orbit, integrate the response coefficient and verify
# its exact commuting-matrix fundamental solution independently at finite time.
y0=.14
W=matrices[0]
n=len(W)
def hom(t,q):
    y, I=q[:2]
    aa=(1/np.cosh(2*y))**2
    P=q[2:].reshape(n,n)
    return np.concatenate((np.array([.5*np.tanh(2*y)-y,aa-1]),((-np.eye(n)+aa*W)@P).ravel()))
q0=np.concatenate((np.array([y0,0.]),np.eye(n).ravel()))
sol=solve_ivp(hom,(0,40),q0,t_eval=[5,15,30,40],rtol=1e-12,atol=1e-13,method='DOP853')
assert sol.success
for j,T in enumerate(sol.t):
    I=sol.y[1,j]; P=sol.y[2:,j].reshape(n,n)
    exact=expm(-T*np.eye(n)+(T+I)*W)
    assert np.allclose(P,exact,atol=1e-10,rtol=1e-9)
print('Exact commuting-matrix variational formula corroborated at times',sol.t.tolist())

# Longer homogeneous integration checks the finite renormalized integral
# and computes graph-eigenmode residuals in log-amplitude coordinates.
def hom_scalar(t,q):
    y,I=q
    return [.5*np.tanh(2*y)-y,(1/np.cosh(2*y))**2-1]
long=solve_ivp(hom_scalar,(0,6000),[y0,0],t_eval=[200,1000,3000,6000],rtol=1e-12,atol=1e-13,method='DOP853')
assert long.success
rem=long.y[1]+1.5*np.log(long.t)
for eigenvalue in [-1.,0.,.5,1.]:
    # log absolute response = (lambda-1)*t+lambda*integral(a-1).
    centered=eigenvalue*rem
    assert abs(centered[-1]-centered[-2])<.025
    print('Eigenvalue',eigenvalue,'corrected log-amplitude',centered)
print('PASS: symbolic identities, exact finite-time variational matrix and numerical asymptotic corroboration.')
