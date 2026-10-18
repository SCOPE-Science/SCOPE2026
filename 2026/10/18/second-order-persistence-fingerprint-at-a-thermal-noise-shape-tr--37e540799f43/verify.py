"""Numerical cross-checks of the stationary mode expansion.

Requires numpy and scipy. Run: python verify.py
The analytical proof does not depend on numerical verification.
"""
import math
import numpy as np
from scipy.special import roots_jacobi
from scipy.optimize import brentq


def tilted_moments(ell, t, order=3):
    u, w = roots_jacobi(480, ell-1, -0.5)
    u=(u+1)/2
    a=w*np.exp(-t*u)
    a=a/a.sum()
    return [sum(a*u**n) for n in range(order+1)]


def critical(ell):
    def func(t):
        return 2*t*tilted_moments(ell,t,1)[1]-1
    t=brentq(func,0.1,1000,xtol=1e-12)
    return 1/(2*t)


def density_derivative(x, variance, nodes, weights):
    return float(np.dot(weights,(nodes-x)*np.exp(-(x-nodes)**2/(2*variance)))/variance)


def check():
    assertions=0
    data=[]
    for ell in (0.1,0.25,0.5,0.75,0.85,0.9,0.95):
        nu=critical(ell)
        mom=tilted_moments(ell,1/(2*nu),3)
        assert abs(mom[1]-nu)<1e-11;assertions+=1
        assert abs(mom[2]-(2*ell+1)*nu**2)<1e-9;assertions+=1
        expected_m3=2*(ell-1)*nu**2+(4*ell**2+8*ell+3)*nu**3
        assert abs(mom[3]-expected_m3)<2e-9;assertions+=1
        k=.3*(1+(2*ell-9)*nu)/nu**2
        data.append((ell,nu,k))
    assert data[2][2]<0 and data[5][2]>0;assertions+=1
    for ell in (0.5,0.9):
        nu=critical(ell)
        k=.3*(1+(2*ell-9)*nu)/nu**2
        y,w=roots_jacobi(650,ell-1,ell-1)
        w/=w.sum()
        def curvature(variance):
            return np.dot(w,(y*y-variance)*np.exp(-y*y/(2*variance)))/variance**2
        nu_independent=brentq(curvature,0.03,1.0,xtol=5e-14)
        assert abs(nu-nu_independent)<4e-10;assertions+=1
        for delta in (.01,.003,.001,.0003):
            variance=nu-delta
            def derivative(x):
                return density_derivative(x,variance,y,w)
            root=brentq(derivative,1.e-5,1.0,xtol=2e-14)
            approx=3*delta+k*delta**2
            assert abs(root**2-approx)<0.02*delta;assertions+=1
            if delta==0.0003:
                assert abs((root**2-3*delta)/delta**2-k)<0.05;assertions+=1
        print(f'ell={ell}: nu_c={nu:.12f}; K={k:.9f}; last observed K={(root**2-3*delta)/delta**2:.9f}')
    print(f'PASS: {assertions} independent assertions; qualitative K sign reversal verified')


if __name__=='__main__':
    check()
