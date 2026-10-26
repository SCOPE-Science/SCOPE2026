"""Standalone finite quadrature checks of the stated weighted-annulus Fourier Gram formulas.
This script tests finite identities and asymptotic trends, not the infinite theorem.
"""
import math
import numpy as np
from scipy.special import roots_jacobi, gamma


def phi(k, s):
    if k == 0:
        return 1 - s, s
    denominator = -math.expm1(-2*k)
    a = np.exp(-k*s) * (-np.expm1(-2*k*(1-s))) / denominator
    b = np.exp(-k*(1-s)) * (-np.expm1(-2*k*s)) / denominator
    return a, b


def gram(alpha, eps, kappa, n=200):
    x, W = roots_jacobi(n, 0, alpha)
    s = (x + 1)/2
    W = W*2**(-alpha-1)
    if eps == 0:
        wfactor = (alpha+1)*np.ones_like(s)
    else:
        h = -math.expm1(-2*eps)/(2*eps)
        y = 2*eps*s
        hs = -np.expm1(-y)/y
        wfactor = (alpha+1)*np.exp(-2*eps*s)*hs**alpha/h**(alpha+1)
    p, q = phi(kappa, s)
    w = 2*W*wfactor
    return np.array([[np.dot(w,p*p),np.dot(w,p*q)],
                     [np.dot(w,p*q),np.dot(w,q*q)]])


def test():
    N = 0
    for alpha in [-0.5,0.,0.7,2.]:
        for eps in [0.,0.03,0.2]:
            for kappa in [0.,0.5,2.,8.,25.]:
                M = gram(alpha,eps,kappa)
                assert abs(np.linalg.det(M)) >= -1.e-11
                assert np.all(np.linalg.eigvalsh(M)>-1.e-10)
                N+=2
    for kappa in [0.,0.2,1.,5.,15.]:
        M=gram(0.,0.,kappa)
        lam=np.linalg.eigvalsh(M)[::-1]
        if kappa==0: expected=[1.,1/3]
        else:
            expected=[(kappa+math.sinh(kappa))/(kappa*(1+math.cosh(kappa))),
                      (math.sinh(kappa)-kappa)/(kappa*(math.cosh(kappa)-1))]
        assert np.allclose(lam,expected,rtol=1.e-8,atol=1.e-9),(kappa,lam,expected)
        N+=2
    # Check the two high-frequency constants independently via numerical quadrature.
    for alpha in [-.5,.5,1.]:
        for eps in [0.,0.05]:
            h = (-math.expm1(-2*eps)/(2*eps)) if eps else 1.
            Bo=2**(-alpha)*gamma(alpha+2)/h**(alpha+1)
            Bi=(alpha+1)*math.exp(-2*eps)/h
            kappa=100.
            M=gram(alpha,eps,kappa,n=700)
            assert abs(M[0,0]*kappa**(alpha+1)/Bo-1)<.055,(alpha,eps,'outer')
            assert abs(M[1,1]*kappa/Bi-1)<.03,(alpha,eps,'inner')
            assert abs(M[0,1])<1.e-30
            N+=3
    for alpha in [-.5,0.,1.]:
        for kappa in [0.,.3,1.,3.,10.]:
            M0=gram(alpha,0.,kappa)
            Me=gram(alpha,.02,kappa)
            a=np.linalg.eigvalsh(M0)
            b=np.linalg.eigvalsh(Me)
            assert max(abs(b/a-1))<.15
            N+=1
    print(f'PASS: {N} finite Gram/eigenvalue and asymptotic checks')

if __name__=='__main__': test()
