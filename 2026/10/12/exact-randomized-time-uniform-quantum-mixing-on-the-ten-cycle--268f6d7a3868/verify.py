#!/usr/bin/env python3
"""Reproduce exact Fourier-coherence cancellation for the ten-cycle.
Public scientific verifier; standard-library Python 3.10+ only.
"""
from collections import Counter
from cmath import exp
from math import cos, pi, sqrt

N = 10
# Exact coefficient pairs: lambda_j = a_j + phi*b_j, phi=(1+sqrt(5))/2.
C = ((2,0),(0,1),(-1,1),(1,-1),(0,-1),(-2,0),
     (0,-1),(1,-1),(-1,1),(0,1))
TARGET = (1,-2)

# Verify actual adjacency eigenvalues against the algebraic representation.
phi = (1+sqrt(5))/2
for j, (a,b) in enumerate(C):
    assert abs(2*cos(2*pi*j/N) - (a+b*phi)) < 2e-14

# The two-torus density f(x,y)=(1-cos(x-2y))/(4*pi*pi)
# has character moments 1 at (0,0), -1/2 at +/- TARGET, 0 otherwise.
def moment(v):
    if v == (0,0): return 1
    if v == TARGET or v == (-TARGET[0],-TARGET[1]): return -0.5
    return 0

rows=[]
for k in range(1,N):
    frequencies=Counter((C[j][0]-C[(j-k)%N][0],
                         C[j][1]-C[(j-k)%N][1]) for j in range(N))
    zero=frequencies[(0,0)]
    plus=frequencies[TARGET]
    minus=frequencies[(-TARGET[0],-TARGET[1])]
    value=sum(count*moment(v) for v,count in frequencies.items())
    assert value == 0, (k,value)
    assert (zero,plus,minus) == ((2,2,2) if k%2==0 else (0,0,0))
    rows.append((k,zero,plus,minus))

# Independently compute the weighted torus averages from the original
# complex amplitudes. Periodic trapezoidal quadrature on a 16x16 grid
# integrates the trigonometric polynomial exactly in exact arithmetic;
# floating point is a numerical cross-check, not part of the proof.
R=32
means=[0.0]*N
mass=0.0
for r in range(R):
    x=2*pi*r/R
    for s in range(R):
        y=2*pi*s/R
        weight=(1-cos(x-2*y))/(R*R)
        assert weight >= -1e-15
        mass+=weight
        phases=[exp(1j*(a*x+b*y)) for a,b in C]
        for d in range(N):
            amp=sum(phases[j]*exp(2j*pi*j*d/N) for j in range(N))/N
            means[d]+=weight*abs(amp)**2
assert abs(mass-1)<3e-14
assert max(abs(x-.1) for x in means)<3e-14, means

# Standard Cesaro / Haar-torus average is not uniform: 0.18 for
# 0 and 5 and 0.08 for the other eight offsets.
cesaro=[]
for d in range(N):
    c=Counter(C)
    # group amplitudes by distinct torus frequencies
    group={pair:sum(exp(2j*pi*j*d/N) for j in range(N) if C[j]==pair)/N
           for pair in c}
    cesaro.append(sum(abs(z)**2 for z in group.values()).real)
for d,v in enumerate(cesaro):
    assert abs(v-(.18 if d in (0,5) else .08)) < 1e-13

print('VERIFY_OK algebraic_spectrum=10 nontrivial_Fourier_modes=9 '
      'torus_points=1024 offsets=10 cesaro_profiles=10')
for k,z,p,m in rows:
    print(f'k={k} zero={z} positive_target={p} negative_target={m}')
