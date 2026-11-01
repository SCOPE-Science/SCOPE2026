"""Independent finite consistency checks for the three-tap cyclic spectrogram theorem.

Run: python3 CHECK.py   (Python standard library only).
The all-dimensional statement follows from the analytic proof, not this test.
"""
from cmath import exp, pi
from math import gcd
from random import Random


def correlations(x):
    n = len(x)
    return [
        (sum(abs(x[(m+j)%n])**2 for j in range(3)),
         x[(m+1)%n]*x[m].conjugate()+x[(m+2)%n]*x[(m+1)%n].conjugate(),
         x[(m+2)%n]*x[m].conjugate())
        for m in range(n)
    ]


def spectrogram(x):
    n = len(x)
    w = exp(-2j*pi/n)
    return [[abs(x[m]+x[(m+1)%n]*w**k+x[(m+2)%n]*w**(2*k))**2
             for k in range(n)] for m in range(n)]


def corr_from_spectrogram(x):
    n = len(x)
    p = spectrogram(x)
    w = exp(2j*pi/n)
    return [[sum(p[m][k]*w**(r*k) for k in range(n))/n for r in range(3)]
            for m in range(n)]


def close(a,b,tol=2e-7):
    return abs(a-b) <= tol*(1+abs(a)+abs(b))


def same_spectrogram(x,y):
    a,b=spectrogram(x),spectrogram(y)
    return all(close(a[m][k],b[m][k]) for m in range(len(x)) for k in range(len(x)))

checks=0
rng=Random(20261031)
for n in range(8,53,2):
    if gcd(n,3)!=1: continue
    for trial in range(10):
        a=(0.2+rng.random()*1.8)*exp(2j*pi*rng.random())
        b=(0.2+rng.random()*1.8)*exp(2j*pi*rng.random())
        h=n//2
        ell=trial%h
        lam=exp(2j*pi*ell/h)
        x=[(a if k%2==0 else b)*lam**(k//2) for k in range(n)]
        b_alt=a/a.conjugate()*b.conjugate()*lam
        y=[(a if k%2==0 else b_alt)*lam**(k//2) for k in range(n)]
        assert same_spectrogram(x,y), (n,trial,"spectrogram")
        checks+=1
        cx,cy=correlations(x),correlations(y)
        assert all(close(cx[m][r],cy[m][r]) for m in range(n) for r in range(3))
        checks+=n*3
        # Recover all three lags by a different Fourier inversion algorithm.
        recovered=corr_from_spectrogram(x)
        assert all(close(recovered[m][r],cx[m][r]) for m in range(n) for r in range(3))
        checks+=n*3
        # A generic signal violates the necessary geometric-progression signature.
        z=[(j+1)+1j*((j*j+3*j)%7+1) for j in range(n)]
        B=[z[(j+1)%n]*z[j].conjugate() for j in range(n)]
        assert any(not close(B[j],B[(j+2)%n]) for j in range(n))
        checks+=1
print("CHECK_OK",checks)
