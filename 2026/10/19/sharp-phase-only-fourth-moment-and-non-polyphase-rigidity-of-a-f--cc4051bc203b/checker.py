#!/usr/bin/env python3
"""Independent finite Fourier and difference-correlation checks for a five-site cross.
Standard library only. Computational checks corroborate the analytic proof.
"""
import cmath
import itertools
import math
import random

S=((0,0),(1,0),(-1,0),(0,1),(0,-1))

def direct_corr_energy(a):
    C={}
    for i,x in enumerate(S):
        for j,y in enumerate(S):
            d=(x[0]-y[0],x[1]-y[1])
            C[d]=C.get(d,0j)+a[i]*a[j].conjugate()
    return sum(abs(z)**2 for z in C.values())

def claimed_energy(a):
    c,ax,am,by,bm=a
    U=ax*am/(c*c)
    V=by*bm/(c*c)
    return 45+4*(U.real+V.real)+8*(U*V.conjugate()).real

def discrete_Fourier_energy(a,m,n):
    return sum(abs(sum(a[j]*cmath.exp(2j*math.pi*(s[0]*h/m+s[1]*k/n))
                   for j,s in enumerate(S)))**4
               for h in range(m) for k in range(n))/(m*n)

def check():
    rng=random.Random(20261014)
    tested=0
    for _ in range(300):
        a=[cmath.exp(2j*math.pi*rng.random()) for _ in range(5)]
        exact=direct_corr_energy(a)
        rhs=claimed_energy(a)
        assert abs(exact-rhs)<2e-10,(exact,rhs,a)
        assert rhs>=36-1e-10 and rhs<=61+1e-10
        tested+=1
    for m,n in ((5,5),(5,6),(6,7),(8,5),(7,9),(10,10)):
        for _ in range(10):
            a=[cmath.exp(2j*math.pi*rng.random()) for _ in range(5)]
            discrete=discrete_Fourier_energy(a,m,n)
            exact=direct_corr_energy(a)
            assert abs(discrete-exact)<2e-9,(m,n,discrete,exact)
            tested+=1
    U=(-1+1j*math.sqrt(15))/4
    V=U.conjugate()
    a=[1+0j,1+0j,U,1+0j,V]
    for e in (direct_corr_energy(a),claimed_energy(a),discrete_Fourier_energy(a,5,7)):
        assert abs(e-36)<1e-9,e
        tested+=1
    for q,expected in ((1,61),(2,37),(3,37),(4,37),(6,37)):
        roots=[cmath.exp(2j*math.pi*k/q) for k in range(q)]
        best=min(45+4*(u.real+v.real)+8*(u*v.conjugate()).real
                 for u,v in itertools.product(roots,repeat=2))
        assert abs(best-expected)<1e-9,(q,best)
        tested+=1
    print('PASS:',tested,'independent autocorrelation, discrete Fourier, optimizer, and phase-alphabet checks')

if __name__=='__main__':check()
