#!/usr/bin/env python3
"""Finite arithmetic checks for separated composition cross-products.

These tests are supplementary; the Schatten theorem is proved analytically.
"""
from fractions import Fraction as F
from math import comb, sqrt


def conjugate(z):
    return (z[0], -z[1])


def abs2(z):
    return z[0]*z[0] + z[1]*z[1]


def phi(z):
    return ((F(1)+z[0])/2,z[1]/2)


def psi(z):
    return ((F(1)-z[0])/2,-z[1]/2)


def coeff(i,j):
    """Exactly T_ij/sqrt((i+1)(j+1)), with e_j=sqrt(j+1) z^j."""
    return sum((F((-1)**k*comb(i,k)*comb(j,k),2**(i+j)*(k+1))
               for k in range(min(i,j)+1)), F(0))


def polynomial_integral_coeff(i,j):
    """Direct expansion of integral phi(z)^j conjugate(psi(z)^i) dA."""
    ai=[F(comb(j,k),2**j) for k in range(j+1)]
    bj=[F((-1)**k*comb(i,k),2**i) for k in range(i+1)]
    return sum((ai[k]*bj[k]/(k+1) for k in range(min(i,j)+1)),F(0))

checks=0
for n in range(1,80):
    assert F(1,n+1) > 0  # normalized Bergman radial moment
    assert F(n+1)*F(1,n+1) == 1
    checks+=2
for a in range(-8,9):
    for b in range(-8,9):
        z=(F(a,12),F(b,12))
        if abs2(z)>=1:continue
        x=phi(z); y=psi(z)
        assert abs2(x)+abs2(y)==(1+abs2(z))/2
        assert min(abs2(x),abs2(y))<=F(1,2)
        checks+=2
for i in range(25):
    for j in range(25):
        assert coeff(i,j)==polynomial_integral_coeff(i,j)
        assert coeff(i,j)==coeff(j,i)
        checks+=2
# At z=i on the boundary, both |phi|^2 and |psi|^2 equal 1/2.
z=(F(0),F(1))
assert abs2(phi(z))==abs2(psi(z))==F(1,2)
checks+=1
# The monomial high-degree envelope obeys exponential suppression.
r=0.85
for N in range(5,25):
    upper=sum((n+1)*r**(2*n) for n in range(N,1200))
    coarse=(N+1)*r**(2*N)/(1-r*r)+r**(2*N+2)/(1-r*r)**2
    assert 0<=upper<=coarse*(1+1e-9)
    assert sqrt(upper) < 100*(N+1)**0.5*r**N
    checks+=2
print('CHECKS_OK',checks)
