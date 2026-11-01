"""Exact arithmetic / direct character checks for squared-Hamming exponential kernels.

Finite checks reproduce spectral formulas and sampled boundary behavior.
The all-parameter theorem is proved in RESULT.md, not by enumeration.
"""
from fractions import Fraction
from itertools import product
from math import comb, cos, sin, pi


def B(n, u):
    return sum((-1)**k * comb(n,k) * u**(k*k) for k in range(n+1))


def eigen(n, s, j, u):
    return sum(comb(n-j,a)*comb(j,b)*(s-1)**a*(-1)**b*u**((a+b)**2)
               for a in range(n-j+1) for b in range(j+1))


def rho(n):
    lo, hi = ((0.5, 0.6) if n==2 else (1.0/n, 1.0/(n-1)))
    assert B(n, lo)>0 and B(n,hi)<0
    for _ in range(64):
        md=(lo+hi)/2
        if B(n,md)>0: lo=md
        else: hi=md
    return (lo+hi)/2


def direct_character(n, s, j, u):
    # The direct Fourier transform uses one nontrivial character in each
    # of j coordinates, independently of the binomial coefficient formula.
    real=imag=0.0
    for z in product(range(s), repeat=n):
        d=sum(v!=0 for v in z)
        phase=2*pi*sum(z[:j])/s
        amp=float(u**(d*d))
        real+=amp*cos(phase)
        imag-=amp*sin(phase)
    return real,imag


def check():
    assert B(2, Fraction(1,2))==Fraction(1,16)
    assert B(2, Fraction(3,5))<0
    last=1.0
    for n in range(2,19):
        r=rho(n)
        assert r<last
        last=r
        if n>=3:
            assert Fraction(1,n)<Fraction(r)<Fraction(1,n-1)
        assert abs(B(n,r))<2e-11
        for s in (2,3,5):
            for u in (r*.5,r*.98):
                vals=[eigen(n,s,j,u) for j in range(n+1)]
                assert min(vals)>1e-11, (n,s,u,vals)
            vals=[eigen(n,s,j,r) for j in range(n+1)]
            assert min(vals[:-1])>1e-7
            assert abs(vals[-1])<2e-11
            total=sum(comb(n,j)*(s-1)**j*vals[j] for j in range(n+1))
            assert abs(total-s**n)<2e-7*s**n
    for n in range(2,8):
        for s in (2,3,4):
            u=Fraction(2,7)
            vals=[eigen(n,s,j,u) for j in range(n+1)]
            assert sum(comb(n,j)*(s-1)**j*vals[j] for j in range(n+1))==s**n
            if n<=3:
                for j in range(n+1):
                    re,im=direct_character(n,s,j,u)
                    assert abs(im)<2e-12
                    assert abs(re-float(vals[j]))<2e-12,(n,s,j,re,vals[j])
    print('CHECK_OK: exact rational spectra, independent Fourier sums, endpoint roots/ranks')

if __name__=='__main__':
    check()
