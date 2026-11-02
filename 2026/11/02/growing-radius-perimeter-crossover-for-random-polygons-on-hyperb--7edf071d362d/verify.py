#!/usr/bin/env python3
"""Numerical crosschecks for the hyperbolic random-polygon crossover.
No external packages or network are required; checks are not infinite proofs.
"""
import math
import random

PI=math.pi
EULER=0.5772156649015328606065

def simpson(f,a,b,N=12000):
    assert N%2==0
    h=(b-a)/N
    v=f(a)+f(b)
    for k in range(1,N):
        v+=(4 if k%2 else 2)*f(a+k*h)
    return v*h/3

def crossover(s):
    if s==0:return 1.0
    z=PI*s
    return simpson(lambda y: math.exp(-y)*math.asinh(z*y),0,42)/z

def finite_mean_ratio(n,s):
    z=PI*s
    # Y=n Delta/(2pi) has beta-rescaled density.
    f=lambda y: ((n-1)/n)*math.exp((n-2)*math.log1p(-y/n))*math.asinh(n*s*math.sin(PI*y/n)) if y<n else 0.0
    return simpson(f,0,min(42.,float(n)),12000)/z

def critical_variance(s):
    z=PI*s
    mu=simpson(lambda y:math.exp(-y)*math.asinh(z*y),0,42)
    beta=simpson(lambda y:math.exp(-y)*z*y/math.sqrt(1+(z*y)**2),0,42)
    v=simpson(lambda y:math.exp(-y)*(math.asinh(z*y)-mu-beta*(y-1))**2,0,42)
    return v/z**2

for s in (.04,.2,1.,3.,12.):
    assert 0 < crossover(s) < 1
assert all(crossover(a)>crossover(b) for a,b in zip((.04,.2,1.,3.),(.2,1.,3.,12.)))
print('STRICT_CROSSOVER_AND_RANGE_NUMERICS_PASSED')

for n,s in ((80,.15),(200,.15),(120,1.),(400,1.),(200,4.)):
    assert abs(finite_mean_ratio(n,s)-crossover(s))<.003
print('INDEPENDENT_BETA_SPACING_QUADRATURE_PASSED 5')

# Separate direct intrinsic-distance sampler: hyperbolic cosine law.
rng=random.Random(2950331)
for n,s,N in ((60,.2,4500),(160,1.0,4500),(160,3.0,4500)):
    S=n*s
    total=total2=0.
    for _ in range(N):
        angles=sorted(2*PI*rng.random() for _ in range(n))
        gaps=[(angles[(i+1)%n]-angles[i])%(2*PI) for i in range(n)]
        L=math.fsum(math.acosh(1+2*S*S*math.sin(g/2)**2) for g in gaps)
        val=L/(2*PI*S)
        total+=val;total2+=val*val
        assert val<=math.asinh(PI*s)/(PI*s)+1e-11
    avg=total/N
    target=finite_mean_ratio(n,s)
    variance=max(0.,total2/N-avg*avg)
    assert abs(avg-target)<max(.003,6*math.sqrt(variance/N)) ,(n,s,avg,target)
    sdlimit=math.sqrt(critical_variance(s)/n)
    assert abs(math.sqrt(variance)-sdlimit)<.013,(n,s,math.sqrt(variance),sdlimit)
    print('DIRECT_HYPERBOLIC_COSINE_LAW_MONTE_CARLO_PASSED',n,s,N)

# Small-crossover expansion, and far-crossover logarithmic asymptotics.
for s in (.003,.006):
    approx=1-PI**2*s*s+9*PI**4*s**4
    assert abs(crossover(s)-approx)<2e-7
for s in (80.,160.):
    approx=(math.log(2*PI*s)-EULER)/(PI*s)
    assert 0<crossover(s)-approx<0.00003
print('SMALL_AND_LARGE_SCALE_ASYMPTOTIC_DIAGNOSTICS_PASSED')

# Fixed-radius cubic-chord correction using exact finite integral.
R=1.1;S=math.sinh(R)
for n in (240,480,960):
    actual=finite_mean_ratio(n,S/n)
    approx=1-PI**2*(1+S*S)/((n+1)*(n+2))
    assert abs(actual-approx)<2e-6,(n,actual,approx)
print('FIXED_RADIUS_SHARP_N_INVERSE_SQUARE_COEFFICIENT_PASSED')
print('ALL_CHECKS_PASSED')
