#!/usr/bin/env python3
"""Reproducible supplementary checks for a Fourier second-variation identity.

No numerical test in this file replaces the universal analytic proof.
"""
import math
import numpy as np
import sympy as sp


def coefficient_unscaled(n, weights, angles):
    # [z^n] exp(-2 sum_{k>=1} m_k z^k), removing e^{-mass}.
    moments = [0j] + [sum(weights[j]*np.exp(-1j*k*angles[j])
                             for j in range(n)) for k in range(1,n+1)]
    coefficients = [0j]*(n+1)
    coefficients[0] = 1.0
    for k in range(1,n+1):
        coefficients[k] = -2.0*sum(
            ell*moments[ell]*coefficients[k-ell]
            for ell in range(1,k+1))/k
    return coefficients[n]


def predicted_quadratic(n, u, eta, eps):
    W=np.fft.fft(eta)
    E=np.fft.fft(eps)
    q=u*u
    for k in range(1,n):
        t=k/n
        q+=(1-2*t*(1-t))*abs(E[k])**2+2*abs(W[k])**2
        q+=2*(1-2*t)*np.imag(W[k]*np.conj(E[k]))
    return float(q)


def run():
    t=sp.symbols('t',real=True)
    aa=1-2*t*(1-t)
    bb=1-2*t
    M=sp.Matrix([[2,sp.I*bb],[-sp.I*bb,aa]])
    assert sp.simplify(M.det()-1)==0
    assert sp.simplify(M.trace()-(3-2*t*(1-t)))==0
    c=(3-math.sqrt(5))/2
    rng=np.random.default_rng(20326)
    tests=0
    for n in range(2,15):
        for _ in range(5):
            eta=rng.normal(size=n);eta-=eta.mean();eta/=math.sqrt(n)
            eps=rng.normal(size=n);eps/=math.sqrt(n)
            u=float(rng.normal()/n)
            q=predicted_quadratic(n,u,eta,eps)
            fftmass=u*u+sum(abs(np.fft.fft(eta)[k])**2 + abs(np.fft.fft(eps)[k])**2 for k in range(1,n))
            assert q > c*fftmass-1e-9
            base=(2*np.arange(n)+1)*math.pi/n
            def deficit(h):
                weights=(1+u*h)/n+h*eta
                phases=base+h*eps
                assert min(weights)>0
                return 2-np.exp(-u*h)*abs(coefficient_unscaled(n,weights,phases))
            h=5e-5
            d1=deficit(h)/h**2
            d2=deficit(h/2)/(h/2)**2
            assert abs(d2-q)<max(0.003,0.0015*q), (n,q,d2)
            assert abs(d2-q)<abs(d1-q)+max(0.00008,0.0001*q), (n,q,d1,d2)
            tests+=1
    last=float('inf')
    for n in [7,13,30,100,1000,10000]:
        tr=3-2*(1/n)*(1-1/n)
        low=(tr-math.sqrt(tr**2-4))/2
        assert low>c
        assert low<last
        last=low
    assert abs(last-c)<1e-4
    print('CHECK_OK: symbolic determinant/trace,',tests,'finite-difference trials, sharp uniform edge')

if __name__=='__main__':run()
