"""Finite checks for the exact uniform-hub metapopulation spectral theorem.

Requires Python 3, numpy and sympy. Independent random instances verify numerical
spectra; exact-rational characteristic-polynomial division verifies invariant
factorization on small networks. Proof in RESULT.md covers all network sizes.
"""
from fractions import Fraction
from random import Random
import math
import numpy as np
import sympy as sp

rng=Random(20261028)

def network_float(M,p):
    k=M-1
    F=np.zeros((M,M),dtype=float)
    for i in range(k):
        for j in range(i+1,k):
            w=(1-p)*rng.random()/(3*k)
            F[i,j]=F[j,i]=w
    for i in range(k):
        F[i,i]=1-p-F[i,:].sum()
        F[i,k]=F[k,i]=p
    F[k,k]=1-k*p
    assert np.min(F)>-1e-12
    assert np.max(np.abs(F.sum(axis=1)-1))<2e-14
    return F

def universal(M,p,z,r):
    k=M-1
    tr=(1-p)**2+k*p*p+z*(k*p*p+(1-k*p)**2)
    disc=max(0.,tr*tr-4*z*(1-M*p)**2)
    return r/2*(tr+math.sqrt(disc))

max_err=0.
checks=0
for M in range(3,26):
    for j in range(25):
        p=[1./M,1./(M-1),rng.uniform(.001,1./(M-1))][j%3]
        z=[1.,1.0001,2.,rng.uniform(1.01,25.)][j%4]
        r=rng.uniform(.05,1.1)
        F=network_float(M,p)
        K=r*(F@np.diag([1.]*(M-1)+[z])@F)
        got=np.linalg.eigvalsh(K)[-1]
        want=universal(M,p,z,r)
        err=abs(got-want)
        max_err=max(max_err,err)
        assert err<4e-12*(1+abs(want)),(M,p,z,r,got,want)
        checks+=1

def network_exact(M,p,variant):
    k=M-1
    F=sp.zeros(M)
    # Inhomogeneous symmetric peripheral fluxes; rows compensated on diagonal.
    for i in range(k):
        for j in range(i+1,k):
            num=(3*i+5*j+7*variant)%4
            w=sp.Rational(num,40*M)
            F[i,j]=F[j,i]=w
    for i in range(k):
        F[i,i]=1-p-sum(F[i,j] for j in range(k) if j!=i)
        F[i,k]=F[k,i]=p
    F[k,k]=1-k*p
    assert all(z>=0 for z in F)
    assert all(sum(F[i,j] for j in range(M))==1 for i in range(M))
    return F

# Fully exact characteristic factor on 3--8 node networks; no floating point.
exact=0
x=sp.Symbol('x')
for M in range(3,9):
    k=M-1
    for variant in range(7):
        p=[sp.Rational(1,M),sp.Rational(1,M+2),sp.Rational(1,k)][variant%3]
        z=[sp.Rational(3,2),sp.Rational(17,5),sp.Rational(1,1)][variant%3]
        r=sp.Rational(3,5)
        F=network_exact(M,p,variant)
        K=r*F*sp.diag(*([1]*k+[z]))*F
        # Matrix in the (nonorthonormal) basis (outer all-ones, hub).
        A=sp.Matrix([[1-p,p],[k*p,1-k*p]])
        E=r*A*sp.diag(1,z)*A
        poly=K.charpoly(x).as_expr()
        factor=E.charpoly(x).as_expr()
        assert sp.rem(poly,factor,x)==0,(M,variant)
        exact+=1

# Exact rational equality checks at a noncentral endpoint and at optimal mixing.
boundary=0
for M,p,r,z in [(5,sp.Rational(1,10),sp.Rational(1,2),sp.Rational(46,11)),
                 (5,sp.Rational(1,5),sp.Rational(1,2),sp.Rational(6,1)),
                 (7,sp.Rational(1,7),sp.Rational(2,3),sp.Rational(9,2))]:
    assert z==1+M*(1-r)/r if p==sp.Rational(1,M) else True
    for variant in range(3):
        F=network_exact(M,p,variant)
        K=r*F*sp.diag(*([1]*(M-1)+[z]))*F
        assert (sp.eye(M)-K).det()==0,(M,p,z)
        ev=np.linalg.eigvalsh(np.array(K,float))
        assert abs(ev[-1]-1)<1e-12
        boundary+=1

# Numerical classification cross-check, including subcritical, supercritical,
# and near-neutral background regimes. Exact proof uses rank-one inertia.
threshold_checks=0
for M in range(3,30):
    for j in range(75):
        r=rng.uniform(0.025,0.995)
        z=[1.0, 1/r, 1+M*(1-r)/r, rng.uniform(1.,2+M*(1-r)/r)][j%4]
        p=[1/M,1/(M-1),rng.uniform(1e-6,1/(M-1))][j%3]
        q=z-1
        d=1-M*p
        qcrit=M*(1-r)/r
        if q>=qcrit:
            predicted=False
        else:
            h=(M*(1-r)-r*q)/(r*(M*z*(1-r)-q))
            predicted=d*d<h
        val=universal(M,p,z,r)
        if abs(val-1)<1e-10: continue
        assert predicted==(val<1),(M,r,z,p,predicted,val)
        threshold_checks+=1

# Explicit same-R0 example for nonisomorphic periphery matrices.
M=5;p=sp.Rational(1,6);r=sp.Rational(3,5);z=sp.Integer(3)
t=(1-p)**2+(M-1)*p*p+z*((M-1)*p*p+(1-(M-1)*p)**2)
w=sp.simplify(r/2*(t+sp.sqrt(t*t-4*z*(1-M*p)**2)))
assert w==(53+sp.sqrt(2377))/120
for var in (0,1,2):
    F=network_exact(M,p,var)
    K=r*F*sp.diag(1,1,1,1,z)*F
    assert abs(np.linalg.eigvalsh(np.array(K,float))[-1]-float(w))<1e-12

print(f'PASS {checks} floating spectral comparisons; max absolute error {max_err:.3g}')
print(f'PASS {exact} exact characteristic factor checks')
print(f'PASS {boundary} exact boundary determinants and dominant eigenvalues')
print(f'PASS {threshold_checks} parameter-threshold classification comparisons')
print(f'PASS 3 distinct periphery examples with R0=(53+sqrt(2377))/120={float(w):.12f}')
