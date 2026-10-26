#!/usr/bin/env python3
"""Independent finite-dimensional checks for a probabilistic quantum shift channel.

These checks corroborate finite identities and asymptotic illustrations;
the rigorous cutoff theorem is proved separately in RESULT.md.
"""
import math
import numpy as np
from scipy.stats import binom, norm

checks = 0

def close(a, b, tol=1e-11):
    global checks
    assert np.max(np.abs(np.asarray(a) - np.asarray(b))) < tol, (a,b)
    checks += 1


def rotation(n):
    x = np.array([[0,1],[1,0]], dtype=complex)
    u = (np.eye(2) - 1j*x)/math.sqrt(2)
    out = np.array([[1]], dtype=complex)
    for _ in range(n):
        out = np.kron(out,u)
    return out


def shift(rho,n):
    if n == 1:
        return np.trace(rho)*np.eye(2)/2
    t = np.asarray(rho).reshape([2]*(2*n))
    tr = np.trace(t,axis1=n-1,axis2=2*n-1)
    return np.kron(np.eye(2)/2, tr.reshape(2**(n-1),2**(n-1)))


def depolarize(rho,n):
    return np.trace(rho)*np.eye(2**n)/2**n


def mixed_input(n):
    z = np.zeros((2**n,2**n),complex)
    z[0,0] = 1
    return z


def binom_power(rho,n,g,t):
    a = 1-g
    states = [rho]
    for k in range(1,min(t,n)+1):
        states.append(shift(states[-1],n))
    result = np.zeros_like(rho)
    for k in range(t+1):
        w = math.comb(t,k)*(g**k)*(a**(t-k))
        result += w*(states[k] if k<len(states) else states[-1])
    return result


def probability_leq(n,p,t):
    return binom.cdf(n,t,p)

rng = np.random.default_rng(1432)
for n in range(1,5):
    u = rotation(n)
    d = 2**n
    for j in range(4):
        a = rng.standard_normal((d,d))+1j*rng.standard_normal((d,d))
        rho = a@a.conj().T
        rho /= np.trace(rho)
        close(shift(u@rho@u.conj().T,n),u@shift(rho,n)@u.conj().T)
        v = rho
        for k in range(n):
            v=shift(v,n)
        close(v,depolarize(rho,n))
        for g in [0.12,0.43,0.87]:
            for t in range(8):
                v=rho.copy()
                for q in range(t):
                    v = u@((1-g)*v+g*shift(v,n))@u.conj().T
                direct = np.linalg.matrix_power(u,t)@binom_power(rho,n,g,t)@np.linalg.matrix_power(u.conj().T,t)
                close(v,direct)
                close(np.trace(v),1)

for n in range(2,11):
    for g in [0.15,0.31,0.58,0.89]:
        for t in range(0,2*n+1):
            rho=binom_power(mixed_input(n),n,g,t)
            diagonal=np.real(np.diag(rho))
            tv = np.sum(np.abs(diagonal-2**(-n)))/2
            top = binom.cdf(n-1,t,g)
            close(float(tv<=top+1e-12),1.)
            for ell in [1,min(2,n),n]:
                low=binom.cdf(n-ell,t,g)-2**(-ell)
                close(float(tv+1e-12 >= low),1.)

for n in [300,1200,5000]:
    for g in [0.22,0.63]:
        for s in [-1.5,-0.2,0.0,0.7,1.5]:
            t = math.floor((n+s*math.sqrt(n*(1-g)))/g)
            ell=max(1,math.floor(n**0.25))
            low=binom.cdf(n-ell,t,g)-2**(-ell)
            high=binom.cdf(n-1,t,g)
            close(float(low<=high+1e-12),1.)
            # The exact tail approaches the Gaussian limit; conservative finite-N tolerance.
            close(float(abs(high-norm.cdf(-s))<0.13),1.)

print('PASS:', checks, 'numerical assertions; analytic proof remains in RESULT.md')
