#!/usr/bin/env python3
"""Independent geometry and importance-sampling checks for diameter-endpoint tails."""
from math import factorial, comb, sqrt, pi
from fractions import Fraction
import numpy as np

def simplex_constant(d):
    return Fraction(d*(d+1)*4**(d-1),comb(2*d,d))

def cube_constant(d):
    return Fraction(2**d*d**(2*d),factorial(2*d))

def ratio(d):
    return simplex_constant(d)/cube_constant(d)

assert simplex_constant(3)==Fraction(48,5)
assert cube_constant(3)==Fraction(81,10)
assert simplex_constant(4)==Fraction(128,7)
assert cube_constant(4)==Fraction(8192,315)
assert ratio(3)==Fraction(32,27)
assert ratio(4)==Fraction(45,64)
for d in range(2,61):
    assert ratio(d+1)<ratio(d)
    assert (1+1/d)**(2*d) > 2+4/d
print('EXACT_SIMPLEX_CUBE_COEFFICIENTS_AND_DIMENSION_FOUR_CROSSOVER_OK')

rng=np.random.default_rng(20261019)
N=220_000
for d in (3,4):
    # Random differences: |Xi-Yi|=1-delta_i with density 2 delta_i on [0,1].
    DD=sqrt(d)
    for eps in (0.10,0.04,0.015):
        T=DD*eps*(1+3*eps)
        ga=rng.gamma(shape=2,scale=1,size=(N,d))
        gs=rng.gamma(shape=1,scale=1,size=N)
        z=T*ga/(ga.sum(axis=1)+gs)[:,None]
        indicator=(np.linalg.norm(1-z,axis=1)>DD-eps)
        coef=float(Fraction(2**d,factorial(2*d)))*(T/eps)**(2*d)*indicator.mean()
        truth=float(Fraction(2**d*d**d,factorial(2*d)))
        # Predicted finite-epsilon downward/small excess effects are O(eps).
        assert abs(coef/truth-1)<0.23, (d,eps,coef,truth)
        print(f'CUBE_DIFFERENCE_DENSITY_IMPORTANCE_OK d={d} eps={eps} coeff={coef:.10f} target={truth:.10f}')

root3=sqrt(3)
vertices=np.array([[0.,0.,0.],[1.,0.,0.],[.5,root3/2,0.],[.5,root3/6,sqrt(2/3)]])
V=np.linalg.det((vertices[1:]-vertices[0]).T)/6
assert abs(V-sqrt(2)/12)<1e-12
edge_a=(vertices[[1,2,3]]-vertices[0]).T
edge_b=(vertices[[0,2,3]]-vertices[1]).T
unit=(vertices[0]-vertices[1])
a=-unit@edge_a
b=unit@edge_b
assert np.allclose(a,[1,.5,.5]) and np.allclose(b,[1,.5,.5])
assert abs(np.linalg.det(edge_a))==abs(np.linalg.det(edge_b))
print('REGULAR_TETRAHEDRON_DIRECT_VERTEX_GRAM_AND_CAP_VOLUMES_OK')
for eps in (0.08,0.04,0.02):
    T=eps*(1+3*eps)
    g=rng.gamma(shape=1,scale=1,size=(N,7))
    samp=T*g[:,:6]/g.sum(axis=1)[:,None]
    lam=samp[:,:3]/a
    mu=samp[:,3:]/b
    x=vertices[0]+lam@edge_a.T
    y=vertices[1]+mu@edge_b.T
    assert np.max(lam.sum(axis=1))<1 and np.max(mu.sum(axis=1))<1
    truth=float(simplex_constant(3))
    # each ordered diametral pair, all 12 equivalent by symmetry.
    coef=(12*36/(factorial(6)*np.prod(a)*np.prod(b)))*(T/eps)**6*np.mean(np.linalg.norm(x-y,axis=1)>1-eps)
    assert abs(coef/truth-1)<0.26,(eps,coef,truth)
    print(f'TETRAHEDRON_DIRECT_VERTEX_CONES_IMPORTANCE_OK eps={eps} coeff={coef:.10f} target={truth:.10f}')
print('ALL_DIAMETER_TAIL_GEOMETRY_CHECKS_OK')
