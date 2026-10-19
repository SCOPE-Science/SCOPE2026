#!/usr/bin/env python3
"""Reproducible exact and numerical checks for the inverse-root spectral alias example."""
import math
import sympy as sp
import numpy as np

checks=0
def ck(flag, desc=''):
    global checks
    assert bool(flag), desc
    checks+=1

u,v,z=sp.symbols('u v z', positive=True)
q=(u*u+u*v+v*v-z)/(u*v*(u+v))
F=sp.factor(z*q*q-1)
F_expected=(z-u*u)*(z-v*v)*(z-(u+v)**2)/(u*u*v*v*(u+v)**2)
ck(sp.simplify(F-F_expected)==0, 'three-root polynomial factorization')
for lam,desired in ((u*u,1/u),(v*v,1/v),((u+v)**2,-1/(u+v))):
    ck(sp.simplify(q.subs(z,lam)-desired)==0, 'interpolatory values')

A=sp.diag(1,4,9); qq=(7-z)/6
Q=sp.diag(*[qq.subs(z,j) for j in (1,4,9)])
B=A*Q*Q
ck(B==sp.eye(3), 'perfect preconditioned matrix')
ck(Q==sp.diag(1,sp.Rational(1,2),-sp.Rational(1,3)), 'signed inverse-root matrix')
ck(Q != sp.diag(1,sp.Rational(1,2),sp.Rational(1,3)), 'nonprincipal branch')

t=sp.symbols('t', nonnegative=True)
M0=2+t; M1=1+4+9*t; M2=1+16+81*t; M3=1+64+729*t
Delta=sp.factor(M0*M2-M1*M1)
s1=sp.factor((M0*M3-M1*M2)/Delta)
s0=sp.factor((M1*M3-M2*M2)/Delta)
ck(Delta==9+89*t, 'Krylov Gram determinant')
ck(sp.simplify(s1-(45+965*t)/(9+89*t))==0, 'Ritz node sum')
ck(sp.simplify(s0-(36+1476*t)/(9+89*t))==0, 'Ritz node product')
poly=sp.factor((9-s1)**2-s0)
ck(sp.factor(poly+4*(26117*t*t+7074*t-243)/(9+89*t)**2)==0, 'threshold quadratic')
tc=(-sp.Integer(3537)+180*sp.sqrt(582))/26117
ck(sp.simplify(26117*tc**2+7074*tc-243)==0, 'critical value')
ck(tc>0 and tc<sp.Rational(9,41), 'positive root and sign condition')
ck(sp.factor(sp.diff(9-s1,t))==-4680/(9+89*t)**2, 'descending numerator')
ck(sp.factor(sp.diff(s0,t))==10080/(9+89*t)**2, 'increasing product')

# Derivatives at t=0 give the leading spectral sensitivity of B(t).
s1d=sp.diff(s1,t).subs(t,0); s0d=sp.diff(s0,t).subs(t,0)
# Roots theta_1=1, theta_2=4: theta'_1+theta'_2=s1',
# 4 theta'_1 + theta'_2=s0'.
theta1d=sp.simplify((s0d-s1d)/3)
theta2d=sp.simplify(s1d-theta1d)
ck(theta1d==sp.Rational(200,9) and theta2d==sp.Rational(320,9), 'Ritz derivative')
a,b=sp.symbols('a b',positive=True)
q_ab=(a*a+a*b+b*b-z)/(a*b*(a+b))
a_prime=theta1d/2; b_prime=theta2d/4
qprime=sp.simplify(sp.diff(q_ab,a).subs({a:1,b:2})*a_prime + sp.diff(q_ab,b).subs({a:1,b:2})*b_prime)
ck(sp.simplify(qprime-(100*z/27-sp.Rational(100,9)))==0, 'interpolant derivative')
for zz,expect in [(1,-sp.Rational(400,27)),(4,sp.Rational(400,27)),(9,-sp.Rational(400,3))]:
    val=sp.simplify(2*zz*q_ab.subs({a:1,b:2,z:zz})*qprime.subs(z,zz))
    ck(val==expect, 'preconditioned eigenvalue derivative')

# Independent numerical two-step Lanczos calculation, including small nonzero
# hidden-mode amplitudes. No simulations are used as proof of universal claims.
def ritz_and_q(amp):
    diag=np.array([1.,4.,9.]); A_np=np.diag(diag)
    g=np.array([1.,1.,amp]); v1=g/np.linalg.norm(g)
    v2=A_np@v1-v1*(v1@(A_np@v1))
    v2=v2/np.linalg.norm(v2)
    V=np.column_stack((v1,v2)); T=V.T@A_np@V
    theta=np.linalg.eigvalsh(T)
    aa,bb=np.sqrt(theta)
    q_lambda=(aa*aa+aa*bb+bb*bb-diag)/(aa*bb*(aa+bb))
    return theta, q_lambda

for i in range(1,37):
    tt=10**(-i/5) # reaches below the critical visibility threshold
    eig,qvals=ritz_and_q(math.sqrt(tt))
    eig_B=np.array([1.,4.,9.])*qvals*qvals
    if tt<0.9*float(tc):
        ck(qvals[2]<0, 'negative hidden-mode polynomial')
        if tt<1e-6:
            ck(max(eig_B)/min(eig_B)<1+155*tt, 'near-isometric family')
    ck(abs(sum(eig)-float(s1.subs(t,tt)))<1e-9, 'independent Lanczos Ritz sum')
    ck(abs(np.prod(eig)-float(s0.subs(t,tt)))<1e-9, 'independent Lanczos Ritz product')
    if qvals[2] != 0:
        c=qvals[2]*np.array([0.,0.,1.])
        V=c/np.linalg.norm(c)
        H=V@np.diag(eig_B)@V
        arnoldi_1=V*(np.linalg.norm(c)/math.sqrt(H))
        expected=np.sign(qvals[2])/3*np.array([0.,0.,1.])
        ck(np.linalg.norm(arnoldi_1-expected)<1e-12, 'independent one-step left Arnoldi')

for tt in (1e-8,1e-7,1e-6):
    _,qvals=ritz_and_q(math.sqrt(tt)); eig_B=np.array([1.,4.,9.])*qvals*qvals
    cond=max(eig_B)/min(eig_B)
    ratio=(cond-1)/tt
    ck(abs(ratio-4000/27)<0.03, 'sharp condition expansion')
    output=np.sign(qvals[2])/3
    ck(abs(output+1/3)<1e-14, 'one-step exact wrong branch')

print('VERIFICATION_OK checks=',checks,'critical_t=',sp.N(tc,18),
      'lambda_B_slope=',sp.Rational(4000,27))
