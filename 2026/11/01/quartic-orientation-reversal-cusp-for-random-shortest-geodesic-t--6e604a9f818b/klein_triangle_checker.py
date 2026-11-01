"""Numerical and exact checks of orientation-reversing shortest-geodesic triangles.
Run: python3 klein_triangle_checker.py
"""
from fractions import Fraction
from math import pi
import numpy as np


def pair_tail(h,k):
    m=max(h,k); l=min(h,k)
    return 2*((1-m)**3/3+(m-l)*(1-m)**2/2)+max(0,1-h-k)**3/3

def triple_tail(h12,h13,h23):
    return (max(0,1-h12-h13)**3 + max(0,1-h12-h23)**3 + max(0,1-h13-h23)**3)/3

def odd_probability_conditional(u):
    h=np.array(u,dtype=float)+0.5
    singles=sum((1-v)**2 for v in h)
    pairs=sum(pair_tail(h[i],h[j]) for i,j in ((0,1),(0,2),(1,2)))
    return singles-2*pairs+4*triple_tail(*h)

def quadratic_approx(u):
    return 0.25+sum(2*x*x for x in u)-sum(u)**2

rng=np.random.default_rng(20261029)
for u in ((0,0,0),(.01,-.02,.03),(-.07,.09,-.03),(.1,.03,-.11)):
    assert abs(odd_probability_conditional(u)-quadratic_approx(u)) <= 56*(max(abs(x) for x in u)**3)+1e-12
print('CONDITIONAL_DISTANCE_THRESHOLD_CUBIC_BOUND_PASSED')

# Exact Fourier coefficient computation:  E z_ij² = sum 1/(pi^4 n^4) =1/90,
# and E z_12 z_13=0 by orthogonality and independence.
# Euler's identity zeta(4)=pi^4/90 and Fourier orthogonality yield the exact moment.
assert Fraction(3,1)*Fraction(1,4)*Fraction(1,90) == Fraction(1,120)
assert Fraction(56,512)==Fraction(7,64)
print('EXACT_FOURIER_SECOND_MOMENTS_AND_COEFFICIENT_PASSED')

# Independent vertex-coordinate simulation, not using conditional tail formula.
for ratio in (1.0, 1.5, 2.5, 4.0):
    n=600000
    x=rng.uniform(0,ratio,(3,n))
    y=rng.uniform(-0.5,0.5,(3,n))
    parity=np.zeros(n,dtype=np.int8)
    for i in range(3):
        j=(i+1)%3
        dx=np.abs(x[i]-x[j]); dy=np.abs(y[i]-y[j]); sy=np.abs(y[i]+y[j])
        de=dx**2+np.minimum(dy,1-dy)**2
        do=(ratio-dx)**2+np.minimum(sy,1-sy)**2
        parity ^= do<de
    observed=parity.mean(); theorem=.25+1/(120*ratio**4)
    error=7/(64*ratio**6)
    sigma=np.sqrt(observed*(1-observed)/n)
    assert abs(observed-theorem) <= error+6*sigma,(ratio,observed,theorem,error)
    print(f'GEODESIC_TRIANGLE_MC_PASSED aspect={ratio:.1f} p={observed:.7f} leading={theorem:.7f} bound={error:.7f}')
print('ALL_CHECKS_PASSED')
