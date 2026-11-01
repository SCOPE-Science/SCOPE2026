#!/usr/bin/env python3
"""Reproducible finite and stochastic checks for the exact acute-triangle variance law.
Pure Python 3 standard library; its numerical diagnostics are not infinite proofs.
"""
from fractions import Fraction as F
from itertools import combinations
from math import acos, comb, cos, pi, sin, sqrt
from random import Random

# Exact algebra of the coefficients of 1 and pi in relevant moments.
# E[sin(theta/2)]=E[cos(theta/2)]=2/3;
# E[sin^2(theta/2)]=E[cos^2(theta/2)]=1/2;
# E[sin(theta/2)*cos(theta/2)]=pi/8.
E_q_rational = F(2,3)-F(1,2)+F(1,3)
E_q2_rational = F(1,2) + (F(1)-2*F(2,3)+F(1,2))/4 - F(2,3)
E_q2_pi = F(1,8)
assert E_q_rational == F(1,2)
assert E_q2_rational == -F(1,8) and E_q2_pi == F(1,8)
assert E_q2_rational-E_q_rational**2 == -F(3,8)
print('EXACT_MOMENT_COEFFICIENTS_PASSED')

# Check the claimed combinatorial overlap counts by exhaustive finite enumeration.
for n in range(3,10):
    triples=list(combinations(range(n),3))
    overlap_two=sum(1 for i,a in enumerate(triples) for b in triples[i+1:] if len(set(a)&set(b))==2)
    assert overlap_two==comb(n,2)*comb(n-2,2)
    assert len(triples)==comb(n,3)
print('EXHAUSTIVE_PAIR_OVERLAP_COUNTS_PASSED')

# Independent one-dimensional midpoint-cap probability check by numerical quadrature.
# The integral 1/4 * int_{-1}^1 sqrt(1-t*t) dt = pi/8 is
# established analytically in RESULT.md; quadrature checks arithmetic only.
def q_t(t):
    return sqrt((1-t)/2) - (1-sqrt((1+t)/2))/2
Ngrid=100000
dt=2/Ngrid
mq=sum(q_t(-1+(i+.5)*dt) for i in range(Ngrid))*dt/2
mq2=sum(q_t(-1+(i+.5)*dt)**2 for i in range(Ngrid))*dt/2
assert abs(mq-.5)<2e-7
assert abs(mq2-(pi-1)/8)<2e-7
print('INDEPENDENT_NUMERICAL_INTEGRATION_PASSED')

rng=Random(20261030)
def sample_sphere():
    z=2*rng.random()-1
    phi=2*pi*rng.random()
    r=sqrt(1-z*z)
    return (r*cos(phi),r*sin(phi),z)
def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def subtract(a,b):
    return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def acute(a,b,c):
    ab=subtract(b,a);ac=subtract(c,a);bc=subtract(c,b)
    return dot(ab,ac)>0 and dot(ab,bc)<0 and dot(ac,bc)>0

for n, reps, tol in [(4,90000,.09),(5,90000,.16),(6,90000,.28)]:
    indices=list(combinations(range(n),3))
    sum_n=0.;sum_n2=0.;sum_pair=0
    for _ in range(reps):
        samples=[sample_sphere() for k in range(n)]
        hits=[acute(samples[a],samples[b],samples[c]) for a,b,c in indices]
        total=sum(hits)
        sum_n+=total;sum_n2+=total*total
        if n==4: sum_pair+=int(acute(samples[0],samples[1],samples[2]) and acute(samples[0],samples[1],samples[3]))
    observed_mean=sum_n/reps
    observed_variance=sum_n2/reps-observed_mean**2
    expected_mean=comb(n,3)/2
    expected_variance=comb(n,3)/4+(pi-3)*comb(n,2)*comb(n-2,2)/4
    print(f'n={n} sample_mean={observed_mean:.6f} exact_mean={expected_mean:.6f} sample_var={observed_variance:.6f} exact_var={expected_variance:.6f}')
    assert abs(observed_mean-expected_mean)<.055
    assert abs(observed_variance-expected_variance)<tol
    if n==4:
        pair_probability=sum_pair/reps
        print(f'pair_joint_sample={pair_probability:.6f} pair_joint_exact={(pi-1)/8:.6f}')
        assert abs(pair_probability-(pi-1)/8)<.009
print('INDEPENDENT_MONTE_CARLO_DIAGNOSTICS_PASSED')
print('ALL_CHECKS_PASSED')
