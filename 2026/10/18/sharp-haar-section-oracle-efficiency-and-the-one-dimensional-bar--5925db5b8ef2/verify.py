#!/usr/bin/env python3
"""Reproduce finite checks for the sharp Haar-section efficiency theorem.

Only the Python standard library is needed. Finite tests corroborate the
analytic proof; they are not certificates for universal quantifiers.
"""
from __future__ import annotations
import math
import random
from fractions import Fraction

SEED = 260524
rng = random.Random(SEED)
COUNTS = {"rational_identities":0,"line_quadratures":0,
          "random_projector_checks":0,"fourier_shift_checks":0}

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def gaussian_frame(n,d):
    """Uniform d-frame by rotationally invariant Gaussian Gram-Schmidt."""
    cols=[]
    for j in range(d):
        for attempt in range(50):
            z=[rng.gauss(0.0,1.0) for _ in range(n)]
            for q in cols:
                s=dot(z,q)
                z=[a-s*b for a,b in zip(z,q)]
            length=math.sqrt(dot(z,z))
            if length > 1.e-10:
                cols.append([v/length for v in z]);break
        else:
            raise ArithmeticError('degenerate Gaussian vector')
    return cols

def projected_norm(cols,x):
    return math.sqrt(sum(dot(c,x)**2 for c in cols))

def gamma_from_two_rows(a,b,theta):
    na=math.sqrt(dot(a,a)); nb=math.sqrt(dot(b,b))
    # rationalized representation is stable for theta moderately small
    numer=na*nb-dot(a,b)
    return numer/(1-math.cos(theta))

def line_exact_ratio(n,theta):
    return (2/(math.pi*n))*(math.sin(theta)-theta*math.cos(theta))/(1-math.cos(theta))

def check_rational():
    for n in range(2,30):
        for d in range(1,n+1):
            a=Fraction(d,n)-Fraction(n-d,n*(n-1))
            assert a==Fraction(d-1,n-1)
            assert a>=0 and a<=Fraction(d,n)
            COUNTS['rational_identities']+=3

def check_rank_one_angular_quadrature():
    # For n=2, uniform p is (cos alpha,sin alpha). For n>2,
    # the independent expected squared radial projection is exactly 2/n.
    N=24000
    for n in [2,3,5,9,17]:
        for theta in [0.04,0.19,0.63,1.1,math.pi/2,2.17,2.8,math.pi]:
            vals=[max(0.,-math.cos(2*math.pi*(j+.5)/N)
                   *math.cos(2*math.pi*(j+.5)/N-theta))
                   for j in range(N)]
            avg=(4/n)*(sum(vals)/N)/(1-math.cos(theta))
            formula=line_exact_ratio(n,theta)
            assert abs(avg-formula)<4.e-6,(n,theta,avg,formula)
            COUNTS['line_quadratures']+=1

def check_random_projectors():
    cases=[(2,1),(3,1),(3,2),(4,2),(4,3),(6,1),(6,2),
           (6,4),(8,3),(8,6)]
    angles=[0.12,0.39,0.9,1.6,2.4,math.pi]
    N=7200
    for n,d in cases:
        accum=[0.]*len(angles)
        for k in range(N):
            cols=gaussian_frame(n,d)
            row0=[c[0] for c in cols]
            row1=[c[1] for c in cols]
            norm0=math.sqrt(dot(row0,row0))
            for j,theta in enumerate(angles):
                ct,st=math.cos(theta),math.sin(theta)
                v=[ct*a+st*b for a,b in zip(row0,row1)]
                normv=math.sqrt(dot(v,v))
                numer=normv*norm0-dot(row0,v)
                g=numer/(1-ct)
                assert g>=-2.e-10 and g<=1+2.e-10
                accum[j]+=g
                COUNTS['random_projector_checks']+=1
        for j,theta in enumerate(angles):
            mean=accum[j]/N
            sharp=(d-1)/(n-1)
            upper=d/n
            assert mean >= sharp-0.03,(n,d,theta,mean,sharp)
            assert mean <=upper+0.03,(n,d,theta,mean,upper)
            if d==1:
                expected=line_exact_ratio(n,theta)
                assert abs(mean-expected)<0.025,(n,d,theta,mean,expected)

def check_fixed_frame_fourier_energy():
    # At each fixed frame, the averaged circle finite-difference energy
    # is bounded by chord-length squared times its circular Dirichlet energy.
    N=2048
    for n,d in [(3,1),(4,2),(6,3),(8,6)]:
        for rep in range(12):
            cols=gaussian_frame(n,d)
            samples=[projected_norm(cols,[math.cos(2*math.pi*j/N),
                                        math.sin(2*math.pi*j/N)] + [0.]*(n-2))
                     for j in range(N)]
            h=2*math.pi/N
            # centered numerical derivatives over periodic grid
            deriv=[(samples[(j+1)%N]-samples[(j-1)%N])/(2*h)
                   for j in range(N)]
            energy=sum(z*z for z in deriv)/N
            for shift in [3,26,111,437,1024]:
                phi=2*math.pi*shift/N
                lhs=sum((samples[(j+shift)%N]-samples[j])**2 for j in range(N))/N
                rhs=2*(1-math.cos(phi))*energy
                assert lhs<=rhs+0.003,(n,d,shift,lhs,rhs)
                COUNTS['fourier_shift_checks']+=1

if __name__=='__main__':
    check_rational()
    check_rank_one_angular_quadrature()
    check_random_projectors()
    check_fixed_frame_fourier_energy()
    print('Finite checks passed:', COUNTS)
    print('Total checks:',sum(COUNTS.values()))
    print('Seed:',SEED)
