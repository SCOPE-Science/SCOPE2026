#!/usr/bin/env python3
"""Independent finite checks for a two-block diagonal scaling formula.
Analytic proof is in RESULT.md; these tests are not its substitute.
Requires NumPy, SciPy, and SymPy.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.optimize import minimize_scalar, minimize
import sympy as sp

checks=0

def check(value, message):
    global checks
    checks+=1
    if not bool(value):
        raise AssertionError(message)

def optimum(m,n,b,c,a2):
    r=1+(m-1)*b; s=1+(n-1)*c
    delta=1-b; eps=1-c
    check(m>=2 and n>=2 and 0<b<1 and 0<c<1 and 0<a2 and m*n*a2<r*s,'domain')
    x0=s/r; xe=eps/delta
    if xe <= x0:
        den=r*c-m*a2
        xr=c*(1-c)/den if den>0 else math.inf
        return max(xe,min(x0,xr)), ('quotient_or_second_leaf',x0,xe,xr)
    else:
        xl=(b*s-n*a2)/(b*delta)
        return min(xe,max(x0,xl)), ('quotient_or_first_leaf',x0,xe,xl)

def cond_quotient(m,n,b,c,a2,x):
    r=1+(m-1)*b; s=1+(n-1)*c
    lam=np.linalg.eigvalsh([[x*r,math.sqrt(m*n*a2*x)],[math.sqrt(m*n*a2*x),s]])
    return lam[1]/min(lam[0],x*(1-b),1-c)

def full_A(m,n,b,c,a2):
    a=math.sqrt(a2)
    return np.block([[(1-b)*np.eye(m)+b*np.ones((m,m)),a*np.ones((m,n))],
                     [a*np.ones((n,m)),(1-c)*np.eye(n)+c*np.ones((n,n))]])

def cond_full(A,scales):
    d=np.exp(scales)
    eig=np.linalg.eigvalsh(A*d[:,None]*d[None,:])
    return eig[-1]/eig[0]

# Exact nontrivial rational interior example: all parameters and eigenvalues explicit.
m=n=3
b=sp.Rational(1,10);c=sp.Rational(1,2);aa=sp.Rational(1,10)
x=sp.Rational(5,6)
r=1+(m-1)*b;s=1+(n-1)*c
T=sp.Matrix([[x*r,sp.sqrt(m*n*aa*x)],[sp.sqrt(m*n*aa*x),s]])
check(T.eigenvals()=={sp.Rational(1,2):1,sp.Rational(5,2):1},'exact quotient spectrum')
check(sp.simplify(x*(1-b)-sp.Rational(3,4))==0,'exact first leaf eigenvalue')
check((1-c)==sp.Rational(1,2),'exact second leaf eigenvalue')
check(sp.simplify((sp.Rational(16)+sp.sqrt(106))/5-5)>0,'Jacobi strictly worse')

# Exact saturation family: m=3,b=1/10,c=1/2,a^2=1/10,n>=2.
for n in range(2,61):
    x,(regime,x0,xe,xs)=optimum(3,n,0.1,0.5,0.1)
    check(abs(x-5/6)<1e-12, f'saturation x {n}')
    check(abs(cond_quotient(3,n,0.1,0.5,0.1,x)-(n+2))<1e-10*(n+2),f'saturation k {n}')

# Rational grid across group sizes, several correlation regimes and cross couplings.
for m in range(2,7):
  for n in range(2,7):
    for b in (0.1,0.25,0.5,0.75):
      for c in (0.1,0.25,0.5,0.75):
        for a2 in (0.01,0.04,0.1,0.2,0.35,0.55):
          r=1+(m-1)*b;s=1+(n-1)*c
          if m*n*a2>=(1-1e-10)*r*s:continue
          x,_=optimum(m,n,b,c,a2)
          k=cond_quotient(m,n,b,c,a2,x)
          # Check direct full spectrum, including multiplicities.
          A=full_A(m,n,b,c,a2)
          logs=np.r_[np.full(m,0.5*np.log(x)),np.zeros(n)]
          kfull=cond_full(A,logs)
          check(abs(kfull-k)<1e-9*max(1,k),f'full matrix vs quotient m={m},n={n},b={b},c={c},a2={a2},x={x},kf={kfull},kq={k}')
          # Compare with nearby and widely separated scalings, no finite grid claimed exhaustive.
          for fac in (0.11,0.4,0.8,0.97,1.03,1.2,2.5,9):
            kval=cond_quotient(m,n,b,c,a2,x*fac)
            check(kval>=k-1e-8*max(1,k),'ratio loss')

# Stochastic global cross-check using scalar numerical minimization and unconstrained search.
rng=np.random.default_rng(7261028)
for i in range(140):
    m=int(rng.integers(2,9));n=int(rng.integers(2,9))
    b=float(rng.uniform(.005,.98));c=float(rng.uniform(.005,.98))
    r=1+(m-1)*b;s=1+(n-1)*c
    a2=float(r*s/(m*n)*rng.uniform(.002,.98))
    x,_=optimum(m,n,b,c,a2)
    k=cond_quotient(m,n,b,c,a2,x)
    numeric=minimize_scalar(lambda t:cond_quotient(m,n,b,c,a2,math.exp(t)),bounds=(-10,10),method='bounded',options={'xatol':1e-10})
    check(abs(numeric.fun-k) <=2e-7*max(1,k),'scalar optimizer mismatch')
    if i<12:
        A=full_A(m,n,b,c,a2)
        base=np.r_[np.full(m,.5*math.log(x)),np.zeros(n)]
        for trial in range(3):
            initial=base+rng.normal(0,0.4,m+n)
            opt=minimize(lambda v:cond_full(A,v),initial,method='Nelder-Mead',options={'maxiter':3500,'xatol':1e-9,'fatol':1e-9})
            check(opt.fun>=k-3e-7*max(1,k),'unrestricted numerical contradiction')

print('PASS: %d exact, grid, spectral, saturation and randomized assertions' % checks)
