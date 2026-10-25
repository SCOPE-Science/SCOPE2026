#!/usr/bin/env python3
"""Symbolic and numerical checks for Parareal phase-mismatch cutoffs.

Run: python verify.py
Requires Python 3, sympy, numpy.
Universal statements depend on the identities and proof in RESULT.md,
not on sampling-based checks.
"""
from math import comb, pi
import cmath
import numpy as np
import sympy as sp

n,z,u = sp.symbols('n z u', real=True)

def scalar_polynomial(k):
    return sp.expand(sum(sp.prod(n-r for r in range(j))/sp.factorial(j)
                         * (z-1)**j for j in range(k+1)))

def squared_defect(k):
    poly = sp.Poly(scalar_polynomial(k),z)
    a = [poly.nth(j) for j in range(k+1)]
    t = 1-u
    return sp.expand(sum(x*x for x in a) + 2*sum(
        a[i]*a[j]*sp.chebyshevt(j-i,t)
        for i in range(k+1) for j in range(i+1,k+1))-1)

expected = {
 1: 2*n*(n-1)*u,
 2: n*(n-2)*(n-1)**2*u**2,
 3: n*(n-3)*(n-2)*(n-1)*u**2*(2*(n-1)*(n-2)*u-3)/9,
 4: n*(n-4)*(n-3)*(n-2)**2*(n-1)*u**3*((n-1)*(n-3)*u-4)/36,
}
checks = 0
for k in range(1,5):
    assert sp.cancel(squared_defect(k)-expected[k])==0
    checks += 1

# Two sharp unit-circle boundary cases, without floating-point arithmetic.
for N,k,c in [(4,3,sp.Rational(3,4)),(5,4,sp.Rational(1,2)),
              (6,3,1-sp.Rational(3,2*5*4)),
              (8,4,1-sp.Rational(4,7*5))]:
    zz=c+sp.I*sp.sqrt(1-c*c)
    poly=scalar_polynomial(k).subs({n:N,z:zz})
    assert sp.simplify(sp.expand_complex(poly*sp.conjugate(poly))-1)==0
    checks += 1

# Independent Parareal recurrence versus the binomial endpoint formula.
def parareal(N,K,F,G):
    older=np.array([G**j for j in range(N+1)],dtype=complex)
    for _ in range(K):
        newer=np.ones(N+1,dtype=complex)
        for j in range(N):
            newer[j+1]=G*newer[j]+(F-G)*older[j]
        older=newer
    return older[-1]

for N in (4,5,8,16,32):
    for k in range(1,min(4,N-1)+1):
        for delta in (-pi, -1.1, -0.2, 0, 0.09, 0.7, 2.4):
            for theta in (0.2,1.3):
                F=cmath.exp(1j*(delta+theta))
                G=cmath.exp(1j*theta)
                val=parareal(N,k,F,G)
                direct=sum(comb(N,j)*G**(N-j)*(F-G)**j for j in range(k+1))
                assert abs(val-direct)<1e-8
                defect=abs(val)**2-1
                uu=1-np.cos(delta)
                truth=float(expected[k].subs({n:N,u:uu}))
                assert abs(defect-truth)<max(5e-7,abs(truth)*1e-8)
                checks += 2

# Random commuting unitary matrix trials. Diagonalization is part of the proof.
rng=np.random.default_rng(20261020)
for N in (5,7,12):
    for k in range(1,5):
        for trial in range(20):
            x=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
            Q,_=np.linalg.qr(x)
            fangles=rng.uniform(-pi,pi,size=3)
            offset=rng.uniform(-pi,pi,size=3)
            f=np.exp(1j*fangles)
            g=np.exp(1j*(fangles-offset))
            F=Q@np.diag(f)@Q.conj().T
            G=Q@np.diag(g)@Q.conj().T
            M=sum(comb(N,j)*np.linalg.matrix_power(G,N-j)
                  @np.linalg.matrix_power(F-G,j) for j in range(k+1))
            amplitudes=[abs(parareal(N,k,a,b)) for a,b in zip(f,g)]
            assert abs(np.linalg.norm(M,ord=2)-max(amplitudes))<1e-7
            if k==3:
                right=(np.linalg.norm(F-G,ord=2)**2 <=
                       3/((N-1)*(N-2)))
            elif k==4:
                right=(np.linalg.norm(F-G,ord=2)**2 <=
                       8/((N-1)*(N-3)))
            else:
                right=np.linalg.norm(F-G,ord=2)<1e-10
            observed=np.linalg.norm(M,ord=2)<=1+1e-9
            assert right==observed
            checks+=2
print('PASS: %d symbolic, exact-algebraic, recurrence, and matrix checks'%checks)
