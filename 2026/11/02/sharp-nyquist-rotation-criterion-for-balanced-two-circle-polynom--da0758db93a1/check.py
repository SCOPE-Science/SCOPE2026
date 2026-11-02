#!/usr/bin/env python3
"""Finite arithmetic corroboration of two-circle Nyquist phase reconstruction."""
import cmath
import math
import random

rng = random.Random(20261026)
checks = 0

def assert_near(z, w, tol=2e-9):
    global checks
    assert abs(z-w) < tol, (z, w, abs(z-w))
    checks += 1

def sample(coeff, t, phi, d):
    N = 2*d
    return [abs(sum(a*(t*cmath.exp(1j*(phi+2*math.pi*k/N)))**j for j,a in enumerate(coeff)))**2 for k in range(N)]

def dft(vals, m, phi):
    N=len(vals)
    return sum(v*cmath.exp(-1j*m*(phi+2*math.pi*k/N)) for k,v in enumerate(vals))/N

def coeff_at(coeff, t, m):
    d=len(coeff)-1
    return t**m * sum(coeff[j+m]*coeff[j].conjugate()*t**(2*j) for j in range(d-m+1))

for d in range(1,10):
    for rep in range(30):
        r,s = .30,.82
        delta = (0.23 + .19*(rep%3))*math.pi/d
        coeff=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(d+1)]
        outer=sample(coeff,r,0.0,d)
        inner=sample(coeff,s,delta,d)
        A=coeff[d]*coeff[0].conjugate()
        X=dft(outer,d,0).real/(2*r**d)
        Y=(dft(inner,d,delta)*cmath.exp(1j*d*delta)).real/(2*s**d)
        Ainfer=complex(X,(X*math.cos(d*delta)-Y)/math.sin(d*delta))
        assert_near(Ainfer,A)
        for m in range(d):
            assert_near(dft(outer,m,0),coeff_at(coeff,r,m))
            assert_near(dft(inner,m,delta),coeff_at(coeff,s,m))
        for m in (d,):
            assert_near(dft(outer,m,0),r**d*(A+A.conjugate()))
            assert_near(dft(inner,m,delta),s**d*(A+cmath.exp(-2j*d*delta)*A.conjugate()))
        for t,phi,vals in ((r,0,outer),(s,delta,inner)):
            for k,val in enumerate(vals):
                theta=phi+2*math.pi*k/(2*d)
                recon=sum(coeff_at(coeff,t,m)*cmath.exp(1j*m*theta) for m in range(d+1))
                recon+=sum(coeff_at(coeff,t,m).conjugate()*cmath.exp(-1j*m*theta) for m in range(1,d+1))
                assert_near(val,recon.real)
    for k in range(4):
        delta=k*math.pi/d
        a=[0j]*(d+1);b=[0j]*(d+1)
        a[0]=b[0]=1
        a[-1]=1j;b[-1]=-1j
        for t,phi in ((.3,0),(.82,delta)):
            aa=sample(a,t,phi,d);bb=sample(b,t,phi,d)
            for u,v in zip(aa,bb):assert_near(u,v)
for d in range(1,10):
    angle=math.pi/(2*d)
    cc=abs(math.cos(d*angle))
    assert_near(math.sqrt((1+cc)/(1-cc)),1.0)
print('PASS',checks,'finite numerical assertions')
