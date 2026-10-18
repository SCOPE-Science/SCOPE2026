#!/usr/bin/env python3
"""Reproduce the sharp fourth-moment algebra for the five-frequency cross.
Uses Python standard library and optionally sympy for exact symbolic checks.
"""
import cmath
import itertools
import random
from fractions import Fraction
from collections import defaultdict
S=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]

def energy_direct(v,N):
    twopi=2.0*cmath.pi
    return sum(abs(sum(v[s]*cmath.exp(twopi*1j*(s[0]*k+s[1]*l)/N) for s in S))**4
               for k in range(N) for l in range(N))/(N*N)

def energy_corr(v,N):
    r=defaultdict(complex)
    for a in S:
        for b in S:
            h=((a[0]-b[0])%N,(a[1]-b[1])%N)
            r[h]+=v[a]*v[b].conjugate()
    return sum(abs(w)**2 for w in r.values())

random.seed(2608)
for N in [5,6,7,8,9,11]:
    for j in range(40):
        v={s: complex(random.uniform(-2,2),random.uniform(-2,2)) for s in S}
        e1=energy_direct(v,N)
        e2=energy_corr(v,N)
        m=sum(abs(c)**2 for c in v.values())
        assert abs(e1-e2)<1e-8*max(1,e1)
        assert e1 <= (27/11)*m*m + 1e-8*max(1,e1), (N,j,e1,m)
        W=abs(v[(0,0)])**2
        U=abs(v[(1,0)])**2+abs(v[(-1,0)])**2
        V=abs(v[(0,1)])**2+abs(v[(0,-1)])**2
        rem=(27/11)*m*m-e2-(11/4)*(W-3*m/11)**2-(3/4)*(U-V)**2
        assert rem>=-1e-8*max(1,e1), (N,j,rem)
print('PASS: autocorrelation, sharp bound and quantitative two-mass deficit for 240 complex test vectors on orders 5,6,7,8,9,11.')

for N in [5,6,7,8,9,11]:
    for t in range(12):
        th=2*cmath.pi*t/12
        ph=2*cmath.pi*((7*t)%12)/12
        x=cmath.exp(1j*th);y=cmath.exp(1j*ph)
        v={(0,0):(3/2)**.5,(1,0):x,(-1,0):1/x,(0,1):y,(0,-1):1/y}
        m=sum(abs(c)**2 for c in v.values())
        q=energy_corr(v,N)/m**2
        assert abs(q-27/11)<1e-12,(N,t,q)
print('PASS: all 72 phase-modulated prescribed equality examples attain 27/11.')

for j in range(100):
    W=random.random()*3;U=random.random()*3;V=random.random()*3
    v={(0,0):W**.5,(1,0):(U/2)**.5,(-1,0):(U/2)**.5,(0,1):(V/2)**.5,(0,-1):(V/2)**.5}
    m=W+U+V
    rem=(27/11)*m*m-energy_corr(v,7)-(11/4)*(W-3*m/11)**2-(3/4)*(U-V)**2
    assert abs(rem)<1e-11*max(1,m*m),(j,rem)
print('PASS: pointwise equality in the quantitative deficit for 100 prescribed nonnegative mass triples.')


W=Fraction(3,11); U=V=Fraction(4,11); T=U+V
Q=1+4*W*T+Fraction(1,2)*(U*U+V*V)+4*U*V
assert Q==Fraction(27,11)
print('PASS: exact rational optimal mass fractions and constant: center=3/11, each arm=2/11, K=27/11.')

# Real rational brute-force coefficient vectors reproduce correct moment without floating-point error.
for N in [5,7,9]:
    for vvalues in itertools.product([-1,0,1],repeat=5):
        if not any(vvalues):continue
        v={s:complex(vvalues[i]) for i,s in enumerate(S)}
        e=energy_corr(v,N)
        m=sum(abs(c)**2 for c in v.values())
        assert e*11 <= 27*m*m+1e-10
print('PASS: full 3^5-1 signed-grid exact-support rational checks for each N=5,7,9.')

try:
    import sympy as sp
    W=sp.symbols('W',real=True)
    p=sp.expand(1+4*W*(1-W)+sp.Rational(5,4)*(1-W)**2)
    assert sp.simplify(sp.Rational(27,11)-p-sp.Rational(11,4)*(W-sp.Rational(3,11))**2)==0
    print('PASS: exact symbolic square completion using SymPy.')
except ImportError:
    print('SKIP: optional SymPy exact square-completion check, standard-library Fraction check passed.')
