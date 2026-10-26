"""Finite checks for a two-harmonic positive-definite kernel's Fourier spectral ordering.
Not an infinite-dimensional proof. Python 3 with mpmath (optional numerical checks).
"""
from fractions import Fraction
import math

checks=0
for n in range(5,51):
    m=n//2
    U=[]
    for r in range(m+1):
        U.append([int(min(j,n-j)<=r) for j in range(n)])
    for r in range(m+1):
        for s in range(m+1):
            conv=[sum(U[r][k]*U[s][(j-k)%n] for k in range(n)) for j in range(n)]
            assert all(conv[j]==conv[-j%n] for j in range(n))
            assert all(conv[j]>=conv[j+1] for j in range(m))
            checks+=2
print('arc convolution checks:',checks)
import mpmath as mp
mp.mp.dps=75
cases=0
for n in (7,8,9,10,11,12,21):
    m=n//2
    c=mp.cos(2*mp.pi/n)
    d=mp.mpf(1) if n%2==0 else mp.cos(mp.pi/n)
    rc=1/(2*(d-c))
    assert rc>1
    for rho in (mp.mpf('0'),mp.mpf('0.3'),mp.mpf('0.8'),mp.mpf('1')):
        for t in (mp.mpf('0.02'),mp.mpf('0.3'),mp.mpf('2'),mp.mpf('10')):
            p=[]
            F=[mp.exp(t*(mp.cos(2*mp.pi*k/n)+rho*mp.cos(4*mp.pi*k/n)-(1+rho))) for k in range(n)]
            for j in range(m+1):
                p.append(mp.fsum(F[k]*mp.cos(2*mp.pi*k*j/n) for k in range(n))/n)
            tol=mp.mpf('1e-55')
            assert all(p[j]>=p[j+1]-tol for j in range(m)),(n,rho,t,p)
            if rho<1:
                assert all(p[j]>p[j+1]+tol for j in range(m)),(n,rho,t,p)
            cases+=1
    # Sign at small t for rho>1
    for rho in (mp.mpf('1.01'),(rc+1)/2,rc+mp.mpf('0.3')):
        t=mp.mpf('0.0001')
        F=[mp.exp(t*(mp.cos(2*mp.pi*k/n)+rho*mp.cos(4*mp.pi*k/n)-(1+rho))) for k in range(n)]
        q=lambda j: mp.fsum(F[k]*mp.cos(2*mp.pi*k*j/n) for k in range(n))/n
        assert q(2)>q(1),(n,rho)
        cases+=1
    # Large-t gap asymptotic sign from the largest nontrivial generator frequency
    s=lambda c: c+rc*(2*c*c-1)
    assert abs(s(c)-s(-d))<mp.mpf('1e-55')
    for rho in ((1+rc)/2,rc+1):
        F=[mp.exp(15*(mp.cos(2*mp.pi*k/n)+rho*mp.cos(4*mp.pi*k/n)-(1+rho))) for k in range(n)]
        q=lambda j: mp.fsum(F[k]*mp.cos(2*mp.pi*k*j/n) for k in range(n))/n
        if rho<rc: assert q(1)>q(2),(n,rho,q(1)-q(2))
        else: assert q(1)<q(2),(n,rho,q(1)-q(2))
        cases+=1
print('numerical spectra checks:',cases)
print('all checks passed')
