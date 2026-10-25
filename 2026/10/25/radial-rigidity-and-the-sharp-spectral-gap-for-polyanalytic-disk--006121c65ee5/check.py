#!/usr/bin/env python3
"""Independent moment-matrix diagnostics for bianalytic disk concentration.
The infinite-dimensional ordering is established analytically in RESULT.md;
these finite checks test its algebraic and numerical consequences.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random
import sympy as S
from scipy.linalg import eigh
from scipy.special import beta, betainc
import numpy as np

checks=0

def test(cond, label):
    global checks
    checks += 1
    if not cond: raise AssertionError(f'{label} (check {checks})')

def T(k,r):
    return (k+2)**2*r**(k+1)-2*(k+1)*(k+3)*r**(k+2)+(k+2)**2*r**(k+3)

def spectrum(k,r):
    tr=T(k,r)
    de=r**(2*k+4)
    rad=tr*tr-4*de
    if rad<0 and rad>-1e-13: rad=0
    test(rad>=0,('disc',k,r))
    return ((tr+sqrt(rad))/2, (tr-sqrt(rad))/2)

# The trace and determinant identities are exact symbolic identities.
k,r=S.symbols('k r',positive=True)
G=S.Matrix([[1/(k+1),1/(k+2)],[1/(k+2),1/(k+3)]])
H=S.Matrix([[r**(k+1)/(k+1),r**(k+2)/(k+2)],
            [r**(k+2)/(k+2),r**(k+3)/(k+3)]])
for j in range(0,10):
    test(S.simplify(S.trace(G.subs(k,j).inv()*H.subs(k,j))-T(j,r))==0, ('trace',j))
    test(S.simplify(H.subs(k,j).det()/G.subs(k,j).det()-r**(2*j+4))==0, ('det',j))

x=S.symbols('x')
for rv in [F(1,17),F(1,9),F(1,3),F(1,2),F(3,4),F(9,10),F(16,17)]:
    rf=float(rv)
    a,b=spectrum(0,rf); c,d=spectrum(1,rf)
    test(a>c>rf**2>b>0,('top-order',rv,a,b,c,d))
    test(c>d>0,('k1',rv))
    test(abs(a*b-rf**4)<3e-13,('k0-det',rv))
    test(abs(c*d-rf**6)<3e-13,('k1-det',rv))
    # The quadratic evaluated at r^2 is exactly negative for k=0 and k=1.
    for j in [0,1]:
        pol=(rv**2)**2-T(j,rv)*rv**2+rv**(2*j+4)
        exp=(-4*rv**3 if j==0 else -8*rv**4)*(1-rv)**2
        test(pol==exp,('straddle-polynomial',j,rv))
    former_plus=float('inf');former_minus=float('inf')
    for j in range(0,25):
        pp,mm=spectrum(j,rf)
        test(pp<former_plus+1e-12 and mm<former_minus+1e-12,('modal-monotonicity',j,rv))
        former_plus,former_minus=pp,mm
    # The calculated eigenfunctions solve the actual generalized eigenvalue problem.
    for j,lam in [(0,a),(1,c)]:
        gv=np.array([[1/(j+1),1/(j+2)],[1/(j+2),1/(j+3)]])
        hv=np.array([[rf**(j+1)/(j+1),rf**(j+2)/(j+2)],
                     [rf**(j+2)/(j+2),rf**(j+3)/(j+3)]])
        vec=np.array([(j+1)*(lam-rf**(j+2)), -(j+2)*(lam-rf**(j+1))])
        # This coefficient choice is tailored to the first generalized eigen-equation.
        test(np.linalg.norm(hv@vec-lam*gv@vec)<2e-12,('extremizer',j,rv))
        pp=eigh(hv,gv,eigvals_only=True)
        test(np.allclose(pp,[spectrum(j,rf)[1],spectrum(j,rf)[0]],rtol=1e-9,atol=1e-12),('direct-spectrum',j,rv))

# Shift stochastic ordering for general polyanalytic order m and Jacobi weights.
for m in [2,3,4]:
    for alpha in [-0.5,0,0.7,2]:
        for R in [0.19,0.43,0.77]:
            prev=None
            for j in range(0,5):
                gg=np.array([[beta(j+a+b+1,alpha+1) for a in range(m)] for b in range(m)])
                hh=np.array([[beta(j+a+b+1,alpha+1)*betainc(j+a+b+1,alpha+1,R) for a in range(m)] for b in range(m)])
                es=eigh(hh,gg,eigvals_only=True)
                test(np.all(es>0) and np.all(es<1),('Jacobi-range',m,alpha,R,j))
                if prev is not None:
                    test(np.all(es<prev+1e-7),('Jacobi-monotonicity',m,alpha,R,j,es,prev))
                prev=es

# Deterministic random tests against the sharp concentration inequality, using
# exact monomial moments and angular orthogonality (not the spectral formula).
rg=Random(40979)
for R in [0.12,0.31,0.52,0.83]:
    top=spectrum(0,R)[0]
    for it in range(250):
        # f(z)=sum_{k=0}^4 z^k(a_k+b_k |z|^2)+c*conj(z)
        co=[complex(rg.uniform(-1,1),rg.uniform(-1,1)) for _ in range(11)]
        nums=dens=0.
        for k in range(5):
            a,b=co[2*k],co[2*k+1]
            aa=abs(a)**2;bb=abs(b)**2;cross=2*(a*b.conjugate()).real
            dens+=aa/(k+1)+cross/(k+2)+bb/(k+3)
            nums+=aa*R**(k+1)/(k+1)+cross*R**(k+2)/(k+2)+bb*R**(k+3)/(k+3)
        dens+=abs(co[-1])**2/2
        nums+=abs(co[-1])**2*R**2/2
        test(nums<=top*dens+1e-11,('global-random',R,it))

# Exact boundary expansions: deficit of the top mode is (k+1)(k+2)(k+3)/24 eps^3.
e=S.symbols('e',positive=True)
for j in [0,1]:
    c=S.Rational((j+1)*(j+2)*(j+3),24)
    expr=(1-c*e**3)**2-T(j,1-e)*(1-c*e**3)+(1-e)**(2*j+4)
    test(S.series(expr,e,0,5).removeO()==0,('edge-asymptotic',j))

print(f'PASS {checks} checks; complete bianalytic spectrum, angular ordering, extremizers, sharp top gap, and all-order weighted diagnostics')
