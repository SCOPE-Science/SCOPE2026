#!/usr/bin/env python3
"""Finite sanity checks for the exact endpoint identity and spectral boundary.
The all-dimensional results require the mathematical proof, not these tests.
"""
import math
import random

A=(1.0,0.5)
K=((2.0,-1.0),(-1.0,2.0))
lam=(3.0+math.sqrt(3.0))/2.0
h=2.0/lam


def mv(u):
    return (2.0*u[0]-u[1], -u[0]+2.0*u[1])


def simpson(f, subdivisions=1024):
    assert subdivisions%2==0
    step=1/subdivisions
    return step/3*(f(0)+f(1)+4*sum(f(j*step) for j in range(1,subdivisions,2))+2*sum(f(j*step) for j in range(2,subdivisions,2)))


def verify(z):
    u=(A[0]*math.sin(z[0]), A[1]*math.sin(z[1]))
    w=mv(u)
    q=u[0]*w[0]+u[1]*w[1]
    wa=A[0]*w[0]**2+A[1]*w[1]**2
    v=lambda x:sum(A[i]*math.cos(x[i]) for i in range(2))
    next_z=tuple(z[i]+h*w[i] for i in range(2))
    decrement=v(z)-v(next_z)
    rem=h*h*sum(A[i]*w[i]**2*simpson(lambda t,i=i:(1-t)*(1+math.cos(z[i]+t*h*w[i]))) for i in range(2))
    formula=h*(1-h*lam/2)*q+h*h/2*(lam*q-wa)+rem
    assert abs(decrement-formula)<2e-12,(z,decrement,formula)
    if max(abs(t) for t in u)>1e-5:
        assert decrement>0,(z,decrement)
    assert lam*q-wa>=-1e-11

rng=random.Random(810025)
for _ in range(500):
    z=tuple(rng.uniform(-math.pi,math.pi) for _ in range(2))
    verify(z)
for z in ((math.pi,math.pi),(0.0,math.pi),(0.0,0.0),(math.pi,-math.pi)):
    verify(z)
print('ENDPOINT_EXACT_REMAINDER_IDENTITY_QUADRATURE_PASS',504)
print('ENDPOINT_STRICT_LOSS_PASS',500)
print('WEIGHTED_SPECTRAL_BOUND_PASS',504)
print('ENDPOINT_TOP_MULTIPLIER',round(1-h*lam,12))
print('SUPERCRITICAL_TOP_MULTIPLIER',round(1-(h+0.01)*lam,12))
print('MEASURE_ZERO_BASINS_AND_GLOBAL_CONVERGENCE_USE_ANALYTIC_PROOF')
