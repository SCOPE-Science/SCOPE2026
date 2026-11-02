#!/usr/bin/env python3
"""Deterministic finite-dimensional checks for the angular Hessian of spin coherent-state cap concentration.
Run with Python 3, numpy and scipy. Uses incomplete-beta quadrature for the
full localization matrix, independently of the analytic Hessian formulas.
"""
import math
import numpy as np
from scipy.special import beta, betainc, gammaln


def analytic_weights(n, p):
    js=np.arange(n+2)
    b=np.exp(gammaln(n+2)-gammaln(js+1)-gammaln(n+2-js) + js*np.log(p)+(n+1-js)*np.log1p(-p))
    ds = [0.0]
    for j in range(1,n+1):
        ds.append(1-(n+1-j)/n*b[j]/sum(b[1:j+1]))
    return np.array(ds), n*(n+1)*(1-p)**(n-1)


def exact_matrix(n, p, eps, modes, ntheta=2048):
    theta = 2*np.pi*np.arange(ntheta)/ntheta
    h = sum(ampl*np.cos(m*theta+phase) for m,ampl,phase in modes)
    v = p + eps*h
    assert np.min(v)>0 and np.max(v)<1
    indices=np.arange(n+1)
    out=np.empty((n+1,n+1), dtype=complex)
    for j in indices:
        for k in indices:
            a=(j+k)/2+1
            b=n-(j+k)/2+1
            integral = beta(a,b)*betainc(a,b,v)
            integrand = integral*np.exp(1j*(j-k)*theta)
            out[j,k] = (n+1)*math.sqrt(math.comb(n,j)*math.comb(n,k))*np.mean(integrand)
    return (out+out.conjugate().T)/2


def highest(n,p,eps,modes):
    return float(np.linalg.eigvalsh(exact_matrix(n,p,eps,modes))[-1])


def main():
    checks=0
    for n in [2,3,4,6,9,15,24]:
        for p in [0.07,0.25,0.51,0.84]:
            ds,q=analytic_weights(n,p)
            assert abs(ds[0])<1e-12
            assert abs(ds[1])<1e-12
            assert np.all(np.diff(ds[1:]) > -1e-13)
            assert abs(ds[2] - (2-p)/(2+(n-2)*p))<1e-12
            assert np.all((ds[2:] > 0)&(ds[2:] <= 1))
            checks+=4
    # Finite-difference Hessian for independent full-matrix evaluation.
    for n,p in [(2,.23),(3,.52),(5,.37),(8,.18)]:
        ds,q=analytic_weights(n,p)
        for m in [1,2,3,n,n+1]:
            if m==1: expected=0
            elif m<=n: expected=-q*ds[m]
            else: expected=-q
            modes=[(m,2.0,0.31)] # Fourier coefficient modulus = 1.
            # Use centered finite difference: removes odd-order terms.
            for eps in [0.0012,0.0006]:
                cur=highest(n,p,eps,modes)
                alt=highest(n,p,-eps,modes)
                bare=1-(1-p)**(n+1)
                ratio=(cur+alt-2*bare)/(2*eps*eps)
                assert abs(ratio-expected) < 1.5e-3*max(1,abs(expected)), (n,p,m,eps,ratio,expected)
                checks+=1
    # Mixed modes and the normalized-to-Fock limit.
    for n,p in [(4,.34),(7,.42)]:
        modes=[(1,.37,.2),(2,.41,.31),(3,.23,.7),(n+3,.19,.24)]
        ds,q=analytic_weights(n,p)
        expected=-q*sum((amp*amp/4)*(0 if m==1 else (ds[m] if m<=n else 1)) for m,amp,_ in modes)
        eps=0.001
        bare=1-(1-p)**(n+1)
        ratio=(highest(n,p,eps,modes)+highest(n,p,-eps,modes)-2*bare)/(2*eps*eps)
        assert abs(ratio-expected)<.002*max(1,abs(expected)), (n,p,ratio,expected)
        checks+=1
    for s in [0.4,1.3,3.5]:
        for j in [2,3,5]:
            seq=[]
            for n in [100,300,1000]:
                ds,_=analytic_weights(n,s/n)
                seq.append(ds[j])
            target=1-s**j/math.factorial(j)/sum(s**k/math.factorial(k) for k in range(1,j+1))
            assert abs(seq[-1]-target)<.005, (s,j,seq,target)
            checks+=1
    print(f"PASS: {checks} deterministic assertions; numerical eigenvalue Hessians and finite-spin limits")

if __name__ == '__main__': main()
