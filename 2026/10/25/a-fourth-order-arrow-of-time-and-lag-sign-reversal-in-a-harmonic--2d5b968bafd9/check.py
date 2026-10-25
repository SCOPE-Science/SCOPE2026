#!/usr/bin/env python3
"""Reproduce the exact time-order asymmetry identities for a harmonic filter
of Brownian noise reset to zero at independent Poisson times.
Dependencies: Python 3, sympy, numpy, scipy, mpmath.
"""
import sympy as sy
import numpy as np
from scipy.linalg import expm
from mpmath import invertlaplace, mp

rho, p = sy.symbols('rho p', positive=True)
checks = 0

def verify(assertion, comment):
    global checks
    if not assertion:
        raise AssertionError(comment)
    checks += 1

def same(a, b, comment):
    verify(sy.cancel(a - b) == 0, comment)

# Stationary generator: L(x^i y^j) = -(i+rho*1_{j>0})x^i y^j
#                 + i x^(i-1)y^(j+1) + j(j-1)x^i y^(j-2).
# The diffusion coefficient is 1 in dY=sqrt(2)dW.
ms = {(0,0):sy.Integer(1)}
for degree in range(1, 5):
    for i in range(degree+1):
        j = degree-i
        if degree % 2:
            ms[(i,j)] = sy.Integer(0)
        else:
            den = i + rho*int(j>0)
            num = i*ms.get((i-1,j+1),0)+j*(j-1)*ms.get((i,j-2),0)
            ms[(i,j)] = sy.factor(num/den)

expected = {
    (0,2):2/rho,
    (1,1):2/(rho*(1+rho)),
    (2,0):2/(rho*(1+rho)),
    (0,4):24/rho**2,
    (1,3):12*(3*rho+2)/(rho**2*(rho+1)**2),
    (2,2):4*(rho**2+19*rho+12)/(rho**2*(rho+1)**2*(rho+2)),
    (3,1):12*(rho**2+19*rho+12)/(rho**2*(rho+1)**2*(rho+2)*(rho+3)),
    (4,0):12*(rho**2+19*rho+12)/(rho**2*(rho+1)**2*(rho+2)*(rho+3)),
}
for idx, val in expected.items():
    same(ms[idx],val,'stationary moment '+str(idx))

# Independently verify stationary balance Lm=0 for all nonconstant
# monomials through degree four, rather than just checking the recurrence.
for (i,j),val in ms.items():
    if (i,j)==(0,0): continue
    lhs = (-i-rho*int(j>0))*val \
          + i*ms.get((i-1,j+1),0) \
          + j*(j-1)*ms.get((i,j-2),0)
    same(lhs,0,'stationary generator identity '+str((i,j)))

states=[(3,0),(2,1),(1,2),(0,3),(1,0),(0,1)]
L=sy.zeros(len(states))
for row,(i,j) in enumerate(states):
    L[row,row]=-i-rho*int(j>0)
    if i and (i-1,j+1) in states:
        L[row,states.index((i-1,j+1))]=i
    if j>=2 and (i,j-2) in states:
        L[row,states.index((i,j-2))]=j*(j-1)
v=sy.Matrix([ms[(i+1,j)] for i,j in states])
first=ms[(4,0)]/(p+1)+ms[(3,1)]/((p+1)*(p+rho))
second=((p*sy.eye(6)-L).inv()*v)[0]
F=sy.factor(first-second)
N=(6*rho**2-9*rho-9)*p**2 \
  +(17*rho**3-rho**2-45*rho-27)*p \
  +14*rho**4+23*rho**3-21*rho**2-42*rho-18
F_expected=24*N/(rho*(rho+1)**2*(rho+2)*(rho+3)*
                (p+rho)**2*(p+1)*(p+3)*(p+rho+1)*(p+rho+2))
same(F,F_expected,'full exact fourth-order asymmetry Laplace transform')

# Exact derivative coefficients are obtained directly by repeated action
# of the polynomial Markov generator, independently of Laplace inversion.
L1=sy.Matrix([[-1,1],[0,-rho]])
w=sy.Matrix([ms[(4,0)],ms[(3,1)]])
for n in (0,1,2):
    lhs=(L1**n)[0,:].dot(w)-(L**n)[0,:].dot(v)
    same(lhs,0,'lower short-lag derivative '+str(n))
a3=72*(2*rho**2-3*rho-3)/(rho*(rho+1)**2*(rho+2)*(rho+3))
a4=-24*(7*rho**2-14*rho-12)/(rho*(rho+1)**2*(rho+2))
for n,formula in [(3,a3),(4,a4)]:
    lhs=(L1**n)[0,:].dot(w)-(L**n)[0,:].dot(v)
    same(lhs,formula,'derivative '+str(n))

# Critical rate and nonzero next-order derivative there.
rstar=(3+sy.sqrt(33))/4
same(2*rstar**2-3*rstar-3,0,'critical rate root')
same(a4.subs(rho,rstar),
     12*(7*rstar+3)/(rstar*(rstar+1)**2*(rstar+2)),
     'critical fourth derivative')
verify(a4.subs(rho,rstar).evalf()>0,'fourth derivative positive at critical rate')

# The residues control the long-lag sign, including r=1 coalescence.
doubleres=sy.factor(sy.limit((p+rho)**2*F,p,-rho))
simpleres=sy.factor(sy.limit((p+1)*F,p,-1))
same(doubleres,36/(rho*(rho-3)*(rho+1)),'slow repeated pole rho<1')
same(simpleres,24*(7*rho+3)/(rho*(rho-1)*(rho+1)**2*(rho+2)*(rho+3)),
     'slow simple pole rho>1')
same(F.subs(rho,1),
     sy.Rational(7,2)/(p+3)+1/(p+3)**2-10/(p+2)
     +sy.Rational(13,2)/(p+1)-4/(p+1)**2,
     'coincident-pole boundary rho=1')

# Numeric semigroup and independent numerical Bromwich inversion comparisons.
mp.dps=45
for rr in (sy.Rational(1,2),sy.Rational(1),sy.Rational(3,2),
           sy.Rational(2),sy.Rational(5,2),sy.Rational(3),sy.Rational(5)):
    LL=np.array(L.subs(rho,rr)).astype(np.float64)
    vv=np.array(v.subs(rho,rr)).astype(np.float64).ravel()
    BB=np.array(L1.subs(rho,rr)).astype(np.float64)
    ww=np.array(w.subs(rho,rr)).astype(np.float64).ravel()
    func=sy.lambdify(p,F.subs(rho,rr),modules='mpmath')
    for lag in (0.15,0.6,1.3,2.5,5.0):
        A_num=(expm(lag*BB)@ww)[0]-(expm(lag*LL)@vv)[0]
        A_inv=float(invertlaplace(func,lag,method='dehoog'))
        verify(abs(A_num-A_inv)<1e-7*(1+abs(A_inv)),
               ('two independent exact-time representations',rr,lag,A_num,A_inv))

# Independent last-reset Gaussian-interval construction for stationary
# variance. Finite truncation is an additional numerical check, not a proof.
rng=np.random.default_rng(19341)
for rr in (0.75,1.5,3.0):
    samples=60000
    age=np.zeros(samples)
    variance=np.zeros(samples)
    for _ in range(int(25*rr+100)):
        lag=rng.exponential(1/rr,samples)
        e=np.exp(-lag)
        f=np.maximum(lag-2*(-np.expm1(-lag))+
                     (-np.expm1(-2*lag))/2, 0.)
        variance+=2*np.exp(-2*age)*f
        age+=lag
    empirical2=variance.mean()
    empirical4=3*np.mean(variance**2)
    theory2=2/(rr*(rr+1))
    theory4=12*(rr**2+19*rr+12)/(rr**2*(rr+1)**2*(rr+2)*(rr+3))
    verify(abs(empirical2/theory2-1)<0.035,'independent renewal covariance mixture second moment')
    verify(abs(empirical4/theory4-1)<0.06,'independent renewal covariance mixture fourth moment')

print('PASS',checks,'checks')
