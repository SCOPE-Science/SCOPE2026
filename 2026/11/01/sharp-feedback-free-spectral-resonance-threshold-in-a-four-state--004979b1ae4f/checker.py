#!/usr/bin/env python3
"""Independent finite checks for the four-state cyclic-promoter spectrum.

Only Python standard-library modules are required. Numerical tests are
corroboration of, not substitutes for, the analytical polynomial proof.
"""
from fractions import Fraction as F
import cmath
import math
import random


def qpoly(x, b, g):
    return (x**6 + (8+2*b)*x**5 + (24+13*b+b*g*g)*x**4
            +(64+48*b+6*b*g*g)*x**3
            +(144+68*b+26*b*g*g)*x**2
            +(128+48*b+16*b*g*g)*x
            +(256+96*b-24*b*g*g))


def rational_derivative_numerator(x, b, g):
    A=(x+4)*(x*x+4)
    dA=(x*x+4)+2*x*(x+4)
    p=x*x+3*x+6
    dp=2*x+3
    return ((dA+b*dp)*A*(g*g+x)
            -(A+b*p)*(dA*(g*g+x)+A))


def solve(A, rhs):
    n=len(rhs)
    M=[[complex(v) for v in row]+[complex(rhs[i])] for i,row in enumerate(A)]
    for k in range(n):
        j=max(range(k,n), key=lambda z: abs(M[z][k]))
        M[k],M[j]=M[j],M[k]
        pivot=M[k][k]
        if abs(pivot)<1e-13:
            raise ArithmeticError('singular matrix')
        for c in range(k,n+1):
            M[k][c]/=pivot
        for i in range(n):
            if i!=k:
                factor=M[i][k]
                for c in range(k,n+1):
                    M[i][c]-=factor*M[k][c]
    return [M[i][-1] for i in range(n)]


def two_spectra(n,a,b,g,w):
    # An independent generator/moment/resolvent construction.
    Q=[[0.0]*n for _ in range(n)]
    for i in range(n):
        Q[i][i]-=a
        Q[i][(i+1)%n]+=a
    R=[[complex(g*(i==j)-Q[j][i]) for j in range(n)] for i in range(n)]
    mix=solve(R,[b/n if i==0 else 0 for i in range(n)])
    mean=b/(n*g)
    EY2=mean+b/g*mix[0]
    response=solve([[complex(-Q[i][j],w*(i==j)) for j in range(n)] for i in range(n)], [1 if j==0 else 0 for j in range(n)])
    Sr=(2*((EY2+b*sum(mix[j]*response[j] for j in range(n)))/(g+1j*w)).real)
    harmonics=0.0
    for k in range(1,n):
        theta=2*math.pi*k/n
        lam=a*(1-math.cos(theta))
        imag=a*math.sin(theta)
        harmonics+=2*lam/(n*n*(lam*lam+(w-imag)**2))
    Sa=(2*b/n+b*b*harmonics)/(g*g+w*w)
    return Sr,Sa,harmonics


def F4(a,w):
    u=w*w
    return a*(u*u+3*a*a*u+6*a**4)/(2*(u+4*a*a)*(u*u+4*a**4))


def F3(a,w):
    u=w*w
    return 2*a*(u+3*a*a)/(3*(u*u+3*a*a*u+9*a**4))


def spectrum(a,b,g,w):
    return (b/2+b*b*F4(a,w))/(g*g+w*w)


def root_positive(a,b,g):
    dim_b=b/a;dim_g=g/a
    if dim_g**2 <= 4+32/(3*dim_b):
        return None
    lo=0.0;hi=1.0
    while qpoly(hi,dim_b,dim_g)<0:
        hi*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if qpoly(mid,dim_b,dim_g)>0:
            hi=mid
        else:
            lo=mid
    return a*math.sqrt((hi+lo)/2)


def check():
    count=0
    for b in [F(1,3), F(2,1), F(13,5), F(8)]:
        for g in [F(1,2),F(2),F(8)]:
            for x in [F(0),F(1,7),F(3,1),F(59,4)]:
                assert rational_derivative_numerator(x,b,g)==-qpoly(x,b,g)
                count+=1
    rng=random.Random(13078075)
    max_rel=0.0
    for n in range(2,7):
        for _ in range(120):
            a=10**rng.uniform(-0.6,0.7)
            b=10**rng.uniform(-0.4,1.0)
            g=10**rng.uniform(-0.5,1)
            w=10**rng.uniform(-1,1.2)
            Sr,Sa,indicator_psd=two_spectra(n,a,b,g,w)
            rel=abs(Sr-Sa)/max(1e-12,abs(Sa))
            max_rel=max(max_rel,rel)
            assert rel<5e-9, (n,a,b,g,w,Sr,Sa,rel)
            count+=1
            if n==3:
                assert abs(indicator_psd-F3(a,w))/F3(a,w)<2e-11
                count+=1
            if n==4:
                assert abs(indicator_psd-F4(a,w))/F4(a,w)<2e-11
                count+=1
    for a,b,g in [(1,8,8),(1,1,1),(2,4,4),(1,1,math.sqrt(4+32/3))]:
        r=root_positive(a,b,g)
        threshold=4*a*a+32*a**3/(3*b)
        if g*g>threshold*(1+1e-13):
            assert r and 0<r
            assert spectrum(a,b,g,r)>spectrum(a,b,g,0)
        else:
            assert r is None
        count+=1
    peak=root_positive(1,8,8)
    ratio=spectrum(1,8,8,peak)/spectrum(1,8,8,0)
    assert abs(peak-0.7779563871383612)<1e-10
    assert abs(ratio-1.05384569916)<1e-9
    print('PASS',count,'analytical-identity and independent resolvent comparisons')
    print('largest numerical relative discrepancy',max_rel)
    print('example omega*',peak,'peak / zero-frequency ratio',ratio)

if __name__=='__main__':
    check()
