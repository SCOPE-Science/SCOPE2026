#!/usr/bin/env python3
"""Independent finite-section checks of rank-two Fock disk shape perturbation.
Finite-section observations are NOT an infinite-dimensional proof.
"""
import math
import numpy as np
from scipy.special import gammainc, gammaln


def fourier_coefficient_defect(t,k):
    if k==1:return 0.0
    a=lambda j:t**j/math.factorial(j)
    return t-a(k)/sum(a(j) for j in range(1,k+1))-t*a(k+1)/sum(a(j) for j in range(2,k+2))


def top_two(t,epsilon,h,nmax=13,quadrature=512):
    th=2*np.pi*np.arange(quadrature)/quadrature
    x=t+epsilon*h(th)
    if np.min(x)<=0:
        raise ValueError('nonpositive squared radius')
    mat=np.empty((nmax,nmax),dtype=complex)
    for m in range(nmax):
        for n in range(m,nmax):
            a=1+(m+n)/2
            integral=np.exp(gammaln(a)-.5*(gammaln(m+1)+gammaln(n+1)))*gammainc(a,x)
            v=np.mean(integral*np.exp(1j*(n-m)*th))
            mat[m,n]=v
            mat[n,m]=np.conjugate(v)
    return np.linalg.eigvalsh(mat)[-2:].sum()


def trial(t,k,eps=.0125):
    zero=top_two(t,0,lambda th:np.cos(k*th))
    plus=top_two(t,eps,lambda th:np.cos(k*th))
    minus=top_two(t,-eps,lambda th:np.cos(k*th))
    observed=(zero-.5*(plus+minus))/eps**2
    expected=0 if k==1 else np.exp(-t)*fourier_coefficient_defect(t,k)/4
    err=abs(observed-expected)
    tol=7e-5 if k!=1 else 4e-5
    assert err < tol, (t,k,observed,expected,err)
    return t,k,observed,expected,err


def main():
    tests=0
    for t in (.5,1.0,3.0):
        coeffs=[fourier_coefficient_defect(t,k) for k in range(1,20)]
        assert abs(coeffs[0])<1e-12;tests+=1
        assert all(coeffs[i+1]>coeffs[i] for i in range(0,8));tests+=1
        assert abs(coeffs[1]-t*(3+2*t)/((t+2)*(t+3)))<1e-12;tests+=1
        for k in (1,2,3,5):
            print('t k observed expected residual',trial(t,k));tests+=1
        # A mixed perturbation has independent quadratic contributions.
        h=lambda th:np.cos(2*th)+.6*np.sin(3*th)
        eps=.0125
        l0=top_two(t,0,h)
        lp=top_two(t,eps,h);lm=top_two(t,-eps,h)
        measured=(l0-(lp+lm)/2)/eps**2
        predicted=np.exp(-t)*(fourier_coefficient_defect(t,2)+.36*fourier_coefficient_defect(t,3))/4
        assert abs(measured-predicted)<1.5e-4,(t,measured,predicted)
        tests+=1
        print('mixed',t,measured,predicted)
    print(f'PASS: {tests} independent deterministic assertions.')
if __name__=='__main__':main()
