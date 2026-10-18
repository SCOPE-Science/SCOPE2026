#!/usr/bin/env python3
"""Standalone finite checks for total-degree orthogonal projection kernels.

Requires numpy and scipy. This checks polynomial normalization, tensor-kernel recursion,
and numerical high-dimensional endpoint scaling; it does not prove any limit.
"""
import itertools
import math
import numpy as np
from numpy.polynomial.legendre import legval
from scipy.integrate import quad


def basis_uniform(j, y):
    co = np.zeros(j + 1)
    co[j] = 1
    return math.sqrt(2*j+1) * legval(y, co)


def basis_arcsine(j, y):
    if j == 0:
        return np.ones_like(y)
    return math.sqrt(2) * np.cos(j * np.arccos(y))



def discrete_skew_basis():
    """Orthonormal polynomials at five unequal support atoms by weighted QR."""
    nodes=np.array([-2.0,-1.0,0.0,3.0,5.0])
    mass=np.array([.05,.1,.2,.25,.4])
    poly=np.polynomial.polynomial.polyvander(nodes/5,4)
    q,r=np.linalg.qr(np.sqrt(mass[:,None])*poly)
    vals=q/np.sqrt(mass[:,None])
    assert np.allclose(vals.T@(mass[:,None]*vals),np.eye(5),atol=2e-14)
    def basis(j, z):
        ind=np.searchsorted(nodes,z)
        assert np.array_equal(nodes[ind],z)
        return vals[ind,j]
    return nodes,mass,basis

def tensor_kernel(x, yy, k, basis):
    """Coefficient recursion for tensor orthogonal kernel of total degree <=k."""
    yy = np.asarray(yy)
    cur = np.zeros((k + 1, len(yy)))
    cur[0] = 1.0
    for i, xi in enumerate(x):
        beta = [basis(j, np.array([xi]))[0] * basis(j, yy[:, i]) for j in range(k + 1)]
        nxt = np.zeros_like(cur)
        for total in range(k + 1):
            for j in range(total + 1):
                nxt[total] += cur[total-j] * beta[j]
        cur = nxt
    return np.sum(cur, axis=0)


def direct_kernel(x, yy, k, basis):
    d = len(x)
    accum = np.zeros(len(yy))
    for alpha in itertools.product(range(k+1), repeat=d):
        if sum(alpha) > k:
            continue
        p = np.ones(len(yy))
        for i, j in enumerate(alpha):
            if j:
                p *= basis(j, np.array([x[i]]))[0] * basis(j, yy[:, i])
        accum += p
    return accum


def hermite_probabilist(n, x):
    h0=np.ones_like(x)
    if n==0: return h0
    h1=x
    for j in range(1,n):
        h0,h1=h1,x*h1-j*h0
    return h1


def hermite_abs_moment(k):
    """Integrate the nonsmooth absolute Hermite moment in its sign cells."""
    roots=np.polynomial.hermite_e.hermeroots([0]*k+[1]).real
    endpoints=[-np.inf,*sorted(roots),np.inf]
    normalizer=1/math.sqrt(2*math.pi)
    total=0.0
    for lo,hi in zip(endpoints[:-1],endpoints[1:]):
        contribution,err=quad(lambda z: abs(float(hermite_probabilist(k,np.array([z]))[0]))*math.exp(-z*z/2)*normalizer,lo,hi,epsabs=5e-13,epsrel=5e-13)
        assert err<2e-10, (k,err)
        total+=contribution
    return total


def finite_checks():
    rng=np.random.default_rng(20261016)
    checks=0
    for kind, basis in [('uniform',basis_uniform),('arcsine',basis_arcsine)]:
        for d in (2,3,4):
            for k in (3,4):
                x=rng.uniform(-1,1,size=d)
                if kind=='uniform':
                    yy=rng.uniform(-1,1,size=(71,d))
                else:
                    yy=np.cos(rng.uniform(0,math.pi,size=(71,d)))
                a=tensor_kernel(x, yy, k, basis)
                b=direct_kernel(x, yy, k, basis)
                assert np.allclose(a,b,rtol=1e-11,atol=3e-10), (kind,d,k,float(max(abs(a-b))))
                checks+=len(yy)
    nodes,weights,basis=discrete_skew_basis()
    for d in (2,3,4):
        for k in (3,4):
            x=rng.choice(nodes,size=d,p=weights)
            yy=rng.choice(nodes,size=(71,d),p=weights)
            a=tensor_kernel(x,yy,k,basis)
            b=direct_kernel(x,yy,k,basis)
            assert np.allclose(a,b,rtol=1e-11,atol=3e-10)
            checks+=len(yy)
    for k in (3,4,5):
        mom=hermite_abs_moment(k)
        assert 0<mom<math.sqrt(math.factorial(k))
        checks+=1
    return checks


def asymptotic_samples():
    rng=np.random.default_rng(314159)
    cases=[]
    for kind, basis, var in [('uniform',basis_uniform,1/3),('arcsine',basis_arcsine,1/2)]:
        for k in (3,4):
            const=(1/math.sqrt(var))**k*hermite_abs_moment(k)/math.factorial(k)
            for d in (80,180,400):
                size=14000
                if kind=='uniform':
                    yy=rng.uniform(-1,1,size=(size,d))
                else:
                    yy=np.cos(rng.uniform(0,math.pi,size=(size,d)))
                val=float(np.mean(np.abs(tensor_kernel(np.ones(d),yy,k,basis))))/d**(k/2)
                cases.append((kind,k,d,round(val,6),round(const,6)))
                assert val>0
                del yy
    return cases


if __name__=='__main__':
    print('finite kernel comparisons:',finite_checks())
    for row in asymptotic_samples():
        print('distribution, degree, dimension, observed, asymptotic:',*row)
