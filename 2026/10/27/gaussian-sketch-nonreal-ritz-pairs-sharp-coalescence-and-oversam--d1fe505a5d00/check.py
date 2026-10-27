#!/usr/bin/env python3
"""Independent finite checks of Gaussian-sketch complex-pair formula.

The universal statements in the accompanying analysis are proved analytically;
these computations test implementation and selected cases, not infinity.
Dependencies: numpy, scipy, sympy. Run: python check.py
"""
import math
import numpy as np
import sympy as sp
from scipy import integrate, special, stats


def probability(s, tau):
    if not (s >= 2 and tau > 0):
        raise ValueError("require s>=2, tau>0")
    def f(y):
        b = (tau * tau + y * y) / (2.0 * tau)
        sigma = math.sqrt((1.0 + y * y) / s)
        return 2.0 * stats.t.pdf(y, s - 1, scale=1.0/math.sqrt(s - 1)) * stats.t.sf(b / sigma, s)
    return integrate.quad(f, 0, np.inf, epsabs=3e-12, epsrel=1e-10, limit=300)[0]


def low_constant(s):
    return (s-1)/(math.sqrt(2)*math.pi)*special.beta(.75,(2*s-1)/4)


def high_constant(s):
    def f(theta):
        cs=math.cos(theta)
        rt=math.sqrt(max(0,math.cos(2*theta)))
        return ((cs+rt)**(s-1)-(cs-rt)**(s-1))/(2*math.pi)
    return integrate.quad(f,-math.pi/4,math.pi/4,epsabs=1e-13)[0]


def check():
    a, delta, g, p, q = sp.symbols('a delta g p q', real=True)
    M=sp.Matrix([[a+g*p,g*p],[g*q,a+delta+g*q]])
    discriminant=sp.factor(sp.trace(M)**2-4*M.det())
    expected=delta**2-2*delta*g*(p-q)+g**2*(p+q)**2
    assert sp.expand(discriminant-expected)==0
    tau, X, Y=sp.symbols('tau X Y', real=True)
    reduced=sp.simplify(expected.subs({delta:sp.sqrt(2)*g*tau,p:(X+Y)/sp.sqrt(2),q:(Y-X)/sp.sqrt(2)})/(2*g*g))
    assert sp.simplify(reduced-(tau**2-2*tau*X+Y**2))==0

    for s in (2,3,5,8):
        # Full radial integration of the bivariate Student density.
        normal=(s-1)*integrate.quad(lambda r:r/(1+r*r)**((s+1)/2),0,np.inf)[0]
        assert abs(normal-1)<1e-10
        assert low_constant(s)>0 and high_constant(s)>0
    assert abs(low_constant(2)-high_constant(2))<1e-12
    assert abs(low_constant(3)-0.5)<1e-12
    assert abs(high_constant(3)-1/math.sqrt(2))<1e-12

    for s in (2,3,5):
        small=probability(s,1e-4)
        assert abs(small/math.sqrt(1e-4)/low_constant(s)-1)<0.025
        atone=probability(s,1.0)
        assert 0<atone<.5
        print(f's={s}: P(1)={atone:.12f}; C={low_constant(s):.10f}; K={high_constant(s):.10f}')

    rng=np.random.default_rng(20261019)
    for s in (2,3,5):
        count=60000
        S=rng.normal(size=(count,s,3))
        B=S[:,:,:2]
        gram=np.einsum('nsi,nsj->nij', B,B)
        rhs=np.einsum('nsi,ns->ni',B,S[:,:,2])
        coeff=np.linalg.solve(gram,rhs[...,None])[...,0]
        x=(coeff[:,0]-coeff[:,1])/math.sqrt(2)
        y=(coeff[:,0]+coeff[:,1])/math.sqrt(2)
        observed=np.mean(1-2*x+y*y<0)
        target=probability(s,1.0)
        sigma=math.sqrt(target*(1-target)/count)
        assert abs(observed-target)<5*sigma+0.002
        print(f's={s}: empirical={observed:.6f}, exact={target:.6f}, tolerance={5*sigma+0.002:.6f}')

    # Explicit SPD witness producing complex sRR eigenvalues.
    a=2.; delta=math.sqrt(2); g=1.; d=3.;
    A=np.array([[a,0,g],[0,a+delta,g],[g,g,d]])
    assert np.linalg.eigvalsh(A)[0]>0
    sketch=np.array([[1.,0.,1/math.sqrt(2)],[0.,1.,-1/math.sqrt(2)]])
    Q=np.eye(3)[:,:2]
    estimated=np.linalg.pinv(sketch@Q)@sketch@A@Q
    assert np.max(abs(np.imag(np.linalg.eigvals(estimated))))>0.1
    print('Symbolic, normalization, asymptotic, Monte Carlo and SPD witness checks passed.')

if __name__=='__main__':
    check()
