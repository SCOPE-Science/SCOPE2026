#!/usr/bin/env python3
"""Checks exact Fourier invariants and each ambiguity type for quadratic phaseless sampling.
No external dependencies. All numerical assertions use fixed examples or seeded tests.
"""
import cmath
import math
import random

GRID = (1, 1j, -1, -1j)

def measure(coeff):
    a,b,c=coeff
    return tuple((abs(a+b*z+c*z*z)**2, abs(b+2*c*z)**2) for z in GRID)

def signatures(coeff):
    a,b,c=coeff
    y=measure(coeff)
    yf=[sum(y[j][0] * GRID[j]**(-k) for j in range(4))/4 for k in range(3)]
    yd=[sum(y[j][1] * GRID[j]**(-k) for j in range(4))/4 for k in range(2)]
    return yf,yd

def predicted(coeff):
    a,b,c=coeff
    return ((abs(a)**2+abs(b)**2+abs(c)**2,
             b*a.conjugate()+c*b.conjugate(),
             2*(c*a.conjugate()).real),
             (abs(b)**2+4*abs(c)**2,2*c*b.conjugate()))

def close(x,y, tol=5e-10):
    assert abs(x-y)<=tol*(1+max(abs(x),abs(y))), (x,y)

def same_measure(p,q):
    A=measure(p); B=measure(q)
    for (a,b),(c,d) in zip(A,B): close(a,c);close(b,d)

def distinct_mod_phase(p,q):
    # two vectors globally phase-equivalent iff all pairwise coordinate ratios are equal
    for i in range(3):
        for j in range(i+1,3):
            if abs(p[i]*q[j]-p[j]*q[i])>1e-8:
                return True
    return abs(sum(abs(x)**2 for x in p)-sum(abs(x)**2 for x in q))>1e-8

rng=random.Random(7102026)
for trial in range(5000):
    p=tuple(complex(rng.randrange(-5,6), rng.randrange(-5,6)) for _ in range(3))
    (af,bf,cf),(df,ef)=signatures(p)
    (ap,bp,cp),(dp,ep)=predicted(p)
    for a,b in zip((af,bf,cf,df,ef),(ap,bp,cp,dp,ep)):close(a,b)
    close(signatures(p)[0][2],cp)

# A full-support two-class fiber: |a|^2=3|c|^2, Re(a*conj(c))=0.
s3=math.sqrt(3)
p=(1j*s3,1+0j,1+0j)
q=(1j*s3/2,2+0j,.5+0j)
same_measure(p,q);assert distinct_mod_phase(p,q)

# Singular collapse of the quadratic two-branch reconstruction at |b|=2|c|.
r=(1j*s3,2+0j,1+0j)
close(abs(r[1]), 2*abs(r[2]))

# On b=0, complex conjugation of the relative phase gives the second class.
p=(1+2j,0j,2-1j)
# Normalize a to a positive real; mirror the relative phase of c about a.
a,b,c=p
q=(a,0j, (a/abs(a))**2*c.conjugate())
same_measure(p,q);assert distinct_mod_phase(p,q)

# Three-class fiber. It includes the 2022 example of two collisions.
p=(0j,1+0j,0j)
q=(.5j*s3,0j,.5+0j)
r=(-.5j*s3,0j,.5+0j)
for v in (q,r):same_measure(p,v);assert distinct_mod_phase(p,v)
assert distinct_mod_phase(q,r)

# A generic fiber is uniquely reconstructed from the moment difference.
for trial in range(500):
    a=complex(rng.randrange(-8,9),rng.randrange(-8,9))
    b=complex(rng.randrange(1,9),rng.randrange(-8,9))
    c=complex(rng.randrange(-8,9),rng.randrange(-8,9))
    if not c or abs(a)**2 == 3*abs(c)**2:continue
    p=(a,b,c)
    (S,U,T),(H,V)=predicted(p)
    C=V/2;A=U-C
    x=(abs(A)**2-3*abs(C)**2)/(S-H)
    close(x,abs(b)**2)
    bn=math.sqrt(x)
    reconstructed=(A.conjugate()/bn,bn,C/bn)
    same_measure(p,reconstructed)
print('PASS: 5,000 random Fourier-invariant checks; 500 generic inverse checks; two- and three-class witnesses.')
