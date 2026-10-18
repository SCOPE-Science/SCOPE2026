#!/usr/bin/env python3
"""Finite checks for exact Gaussian weighted-composition formulas.
No third-party packages needed. These checks supplement, not replace,
the analytic spectral proof.
"""
from math import sqrt, factorial, lgamma, exp


def ratio(root, weight):
    a, b = root, weight
    assert 0 < a < 1 and 0 <= b < 1-a*a
    R = 1-b*b+a**4
    disc = sqrt(((1-a*a)**2-b*b)*((1+a*a)**2-b*b))
    r = (R-disc)/(2*a*a)
    assert 0 < r < 1
    assert abs(a*a*r*r-R*r+a*a) < 5e-12
    lam = sqrt(r)/a
    trace = 1/sqrt((1-a*a)**2-b*b)
    assert abs(lam/(1-r)/trace-1)<1e-10
    return r, lam


def direct_gram(a,b,m,n,N=100):
    if (m-n)%2: return 0.0
    k0=max(m,n)
    total=0.0
    for k in range(k0,N):
        if (k-m)%2 or (k-n)%2:continue
        jm=(k-m)//2;jn=(k-n)//2
        if b == 0:
            if jm or jn: continue
            amplitude=(a**(m+n) if m==n else 0.0)
        else:
            logamp=(m+n)*__import__('math').log(a)+(jm+jn)*__import__('math').log(b/2) + lgamma(k+1)-0.5*(lgamma(m+1)+lgamma(n+1))-lgamma(jm+1)-lgamma(jn+1)
            amplitude=exp(logamp)
        total+=amplitude
    return total


def kernel_gram(a,b,m,n):
    if (m-n)%2: return 0.0
    c=1/sqrt(1-b*b)
    alpha=a*a/(1-b*b);gamma=b*a*a/(1-b*b)
    s=0.0
    for k in range(min(m,n)+1):
        if (m-k)%2 or (n-k)%2:continue
        j=(m-k)//2;h=(n-k)//2
        s+=alpha**k*(gamma/2)**(j+h)/(factorial(k)*factorial(j)*factorial(h))
    return c*sqrt(factorial(m)*factorial(n))*s


def main():
    for a,b in ((0.5,0.0),(0.5,0.1),(0.5,0.3),(0.7,0.2),(0.8,0.35)):
        r,lam=ratio(a,b)
        for m in range(7):
            for n in range(7):
                direct=direct_gram(a,b,m,n,140)
                closed=kernel_gram(a,b,m,n)
                assert abs(direct-closed)<=1e-8*max(1,abs(closed)), (a,b,m,n,direct,closed)
        assert abs((lam**.5)-a**(-.5)*r**.25)<1e-12
    for a in (0.25,0.5,0.8):
        b=1-a*a
        c=1/sqrt(1-b*b)
        assert abs(c-1/(a*sqrt(1+b)))<1e-12
        alpha=a*a/(1-b*b)
        gamma=b*a*a/(1-b*b)
        assert abs(alpha-1/(1+b))<1e-12
        assert abs(gamma-b/(1+b))<1e-12
        for n in range(8):
            assert abs(kernel_gram(a,b,0,n)-(
                (1/a)*1/sqrt(1+b)*sqrt(factorial(n))*(b/(2*(1+b)))**(n//2)/factorial(n//2)
                if n%2==0 else 0))<1e-10
    print('QUADRATIC_FOCK_GAUSSIAN_SPECTRAL_IDENTITIES_OK')


if __name__=='__main__':main()
