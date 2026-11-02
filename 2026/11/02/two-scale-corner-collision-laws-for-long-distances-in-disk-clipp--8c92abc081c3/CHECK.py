"""Reproducible geometric and symbolic checks for the square-disk intersection distance-tail theorem.
Dependencies: Python 3, numpy, scipy, sympy.
Runs local deterministic quadrature and symbolic checks; universal results use the proof in RESULT.md.
"""
from math import acos, pi, sqrt
import numpy as np
from scipy.special import roots_legendre
import sympy as sp


def area(r):
    return pi*r*r - 4*(r*r*acos(1/r)-sqrt(r*r-1))


def smooth_coefficient(r):
    return 16*r**1.5*(2*pi-8*acos(1/r))/(15*area(r)**2)


def crossover_H(z):
    if z <= 1/sqrt(2):
        return 8*2**.25*z**2.5/15 - sqrt(2)*z**3/6
    return (30*z*z-5*sqrt(2)*z+1)/60


def corner_J(t):
    return 1/24 + t/3 + t*t/2


def local_quadrature(r, eps, n=550):
    """Integrate the exact opposite-corner distance inequality over local (S,T) coordinates.
    Applicable in the near-diameter regime, where no other corner pair contributes.
    The q upper boundary is inactive for the values tested.
    """
    Tmax = 1-sqrt(r*r-1)
    width = min(1.9, Tmax + 4*eps + 4*sqrt(eps)*eps)
    nodes, weights = roots_legendre(n)
    T = width*nodes
    w = width*weights
    Smin = np.maximum(np.abs(T), 2-np.sqrt(np.maximum(2*r*r-T*T, 0)))
    TP = T[:,None]+T[None,:]
    slack = (4 - Smin[:,None]-Smin[None,:]
             - sqrt(2)*np.sqrt(np.maximum((2*r-eps)**2-TP**2/2, 0)))
    return .5*np.sum(np.outer(w,w)*np.maximum(slack,0)**2)/area(r)**2


def run():
    tests=0
    z=sp.symbols('z',positive=True)
    u=sp.symbols('u',nonnegative=True)
    f=(2*sp.sqrt(2)-u)*(sp.sqrt(2)*z-u*u/8)**2/16
    cutoff=2**sp.Rational(7,4)*sp.sqrt(z)
    first=sp.simplify(sp.integrate(f,(u,0,cutoff)))
    second=sp.simplify(sp.integrate(f,(u,0,2*sp.sqrt(2))))
    assert sp.simplify(first-(8*2**sp.Rational(1,4)*z**sp.Rational(5,2)/15 -sp.sqrt(2)*z**3/6))==0
    assert sp.simplify(second-((30*z*z-5*sp.sqrt(2)*z+1)/60))==0
    tests+=2
    t=sp.symbols('t',nonnegative=True)
    X,Y=sp.symbols('X Y',nonnegative=True)
    W=sp.sqrt(2)
    eq=sp.integrate(sp.integrate((X+W*t)*(Y+W*t),(Y,0,W-X)),(X,0,W))/4
    assert sp.simplify(eq-(sp.Rational(1,24)+t/3+t*t/2))==0
    tests+=1
    assert abs(crossover_H(1/sqrt(2)) - 11/60)<1e-12
    assert abs(area(sqrt(2))-4)<1e-12
    assert abs(area(1)-pi)<1e-12
    tests+=3
    for r in [1.03, 1.15, 1.3]:
        val=local_quadrature(r,0.00025)/(.00025**2.5)
        coeff=smooth_coefficient(r)
        assert 0.92 < val/coeff < 1.02, (r,val,coeff)
        tests+=1
    for lam in [0.03,0.015]:
        for z0 in [.15,.5,1.,2.]:
            val=local_quadrature(sqrt(2)-lam,z0*lam*lam)/lam**6
            assert abs(val/crossover_H(z0)-1)<.065,(lam,z0,val,crossover_H(z0))
            tests+=1
    for eps in [.002,.0005]:
        for t0 in [0.,.5,1.,2.]:
            val=local_quadrature(sqrt(2)-t0*eps,eps)/eps**4
            assert abs(val/corner_J(t0)-1)<.003,(eps,t0,val,corner_J(t0))
            tests+=1
    print(f'PASS: {tests} symbolic, endpoint, and deterministic quadrature assertions.')
    print('Quadrature checks finite-parameter agreement with asymptotic limits; it does not prove them.')

if __name__=='__main__':run()
