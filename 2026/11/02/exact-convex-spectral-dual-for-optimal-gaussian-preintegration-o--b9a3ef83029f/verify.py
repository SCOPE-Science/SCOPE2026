"""Exact and numerical tests for affine Gaussian quadratic preintegration.

The mathematical proof is in RESULT.md; tests supplement the proof.
"""
from fractions import Fraction as F
import random
import numpy as np
from scipy.optimize import minimize_scalar


def scalar_reduction(A, b, v):
    B = A @ A + np.outer(b, b)
    return float(v @ B @ v - 0.5 * (v @ A @ v)**2)


def surviving_variance(A, b, v):
    P = np.eye(len(v)) - np.outer(v, v)
    return float(0.5 * np.sum((P @ A @ P)**2) + np.dot(P @ b, P @ b))


# Exact spectral extreme-value and deficit identities with rational weights.
rng = random.Random(6127)
exact = 0
for n in range(1, 12):
    for trial in range(420):
        eigs = [F(rng.randint(-8, 8)) for _ in range(n)]
        raw = [rng.randint(0, 15) for _ in range(n)]
        if not any(raw):
            raw[0] = 1
        p = [F(x, sum(raw)) for x in raw]
        a, c = min(eigs), max(eigs)
        mu = sum(q * lam for q, lam in zip(p, eigs))
        second = sum(q * lam * lam for q, lam in zip(p, eigs))
        r = second - F(1, 2) * mu * mu
        deficit = F(1, 2) * (a*a + c*c) - r
        identity = F(1, 2)*(mu-a-c)**2 + sum(q*(lam-a)*(c-lam) for q, lam in zip(p, eigs))
        assert deficit == identity
        if a < 0 < c:
            assert deficit >= 0
        else:
            assert r <= F(1, 2)*max(a*a, c*c)
        exact += 1
print('exact-rational diagonal identities:', exact)

# Dense symmetric matrices; direct covariance and optimized spectral construction.
dense = 0
for n in range(2, 12):
    for trial in range(120):
        local = np.random.default_rng(10000*n+trial)
        A = local.normal(size=(n,n))
        A = (A+A.T)/2
        lam, U = np.linalg.eigh(A)
        a, c = lam[0], lam[-1]
        b = np.zeros(n)
        if a < 0 < c:
            v = np.sqrt(-a/(c-a))*U[:,0] + np.sqrt(c/(c-a))*U[:,-1]
            optimum = 0.5*(sum(lam**2)-a*a-c*c)
        else:
            v = U[:,0] if abs(a)>=abs(c) else U[:,-1]
            optimum = 0.5*(sum(lam**2)-max(a*a,c*c))
        assert abs(surviving_variance(A,b,v)-optimum)<1e-9
        assert abs((0.5*sum(lam**2)-scalar_reduction(A,b,v))-optimum)<1e-9
        for j in range(10):
            z=local.normal(size=n)
            z/=np.linalg.norm(z)
            assert surviving_variance(A,b,z)>=optimum-1e-9
        dense += 1
print('dense symmetric matrices (plus 10 random competitors each):', dense)

# General nonzero linear term and the strictly convex spectral minimax.
dual_checks = 0
for n in range(1,9):
    for trial in range(110):
        local=np.random.default_rng(20000*n+trial)
        A=local.normal(size=(n,n))
        A=(A+A.T)/2
        b=local.normal(size=n)
        B=A@A+np.outer(b,b)
        a,c=np.linalg.eigvalsh(A)[[0,-1]]
        phi=lambda t: .5*t*t+np.linalg.eigvalsh(B-t*A)[-1]
        opt=minimize_scalar(phi,bounds=(a-5,c+5),method='bounded',options={'xatol':1e-12})
        assert opt.success
        t=opt.x
        assert a-1e-4<=t<=c+1e-4
        eig,U=np.linalg.eigh(B-t*A)
        E=U[:,eig[-1]-eig<5e-5]
        comp=E.T@A@E
        rays,W=np.linalg.eigh(comp)
        lo,hi=rays[[0,-1]]
        if lo-1e-3<=t<=hi+1e-3:
            if hi-lo>1e-8:
                weight=np.clip((t-lo)/(hi-lo),0,1)
                v=E@(W[:,0]*np.sqrt(1-weight)+W[:,-1]*np.sqrt(weight))
            else:
                v=E[:,0]
            assert abs(scalar_reduction(A,b,v)-opt.fun)<2e-3
            assert abs((0.5*np.sum(A*A)+np.dot(b,b))-scalar_reduction(A,b,v)-surviving_variance(A,b,v))<1e-7
        z=local.normal(size=(200,n))
        z/=np.linalg.norm(z,axis=1)[:,None]
        values=np.einsum('ij,jk,ik->i',z,B,z)-.5*np.einsum('ij,jk,ik->i',z,A,z)**2
        assert np.max(values)<=opt.fun+1e-5
        dual_checks+=1
print('general affine convex-spectral cases:', dual_checks)

# Repeated top eigenvalue: construct mixed direction at nondifferentiable minimum.
A=np.diag([-3.,0.,2.]); b=np.zeros(3)
v=np.array([np.sqrt(3/5),0,np.sqrt(2/5)])
assert np.isclose(np.linalg.norm(v),1)
assert abs(surviving_variance(A,b,v))<1e-13
assert abs(surviving_variance(A,b,np.array([1.,0.,0.]))-2)<1e-13
t=-1
M=A@A-t*A
assert np.isclose(np.linalg.eigvalsh(M)[-1],6.)
assert np.isclose(v@A@v,t)
assert np.isclose(scalar_reduction(A,b,v),6.5)
assert np.isclose(0.5*t*t+np.linalg.eigvalsh(M)[-1],6.5)
print('rank-two zero variance and multiple-top-eigenvalue certificate: PASS')
print('TOTAL: PASS')
