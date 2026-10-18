#!/usr/bin/env python3
"""Finite diagnostics for complex mean-field polygon linearization.
This tests calculations; the theorem's all-size proof is analytical.
Requires numpy.
"""
import cmath
from fractions import Fraction
import math
import numpy as np


def coefficients(x, y, d):
    v = x*x + y*y
    return np.array([1., 4.-2.*x, 4.-6.*x+v,
                     2.*(v-2.*x), (1.-d*d)*v])


def H(x, u, d2):
    a = 2.-x
    return (u+a*a)*((1.-x)*u-x*a*a)+d2*a*a*(x*x+u)


def jacobian(theta, a, q):
    n = len(theta)
    c = q/n
    coupling = np.array([[c.real,-c.imag],[c.imag,c.real]])
    J = np.zeros((2*n,2*n))
    for j,angle in enumerate(theta):
        v = np.array([math.cos(angle),math.sin(angle)])
        J[2*j:2*j+2,2*j:2*j+2] -= 2*a*np.outer(v,v)
        for k in range(n):
            J[2*j:2*j+2,2*k:2*k+2] += coupling
    return J


def test_one(theta, x, y):
    n = len(theta)
    assert abs(sum(cmath.exp(1j*t) for t in theta)) < 2e-12
    d = abs(sum(cmath.exp(2j*t) for t in theta)/n)
    assert d < 1-1e-8
    a = 1.3
    J = jacobian(theta,a,a*complex(x,y))
    eig = np.linalg.eigvals(J/a)
    c = coefficients(x,y,d)
    # Characteristic identity: lambda^(n-2)(lambda+2)^(n-2) Q(lambda)
    poly = np.poly(eig)
    expected = np.polymul(np.polymul(np.poly1d([1.,0.])**(n-2),
                         np.poly1d([1.,2.])**(n-2)),np.poly1d(c))
    assert np.max(np.abs(poly-expected.coeffs)) < 3e-6, (n,x,y,d,np.max(abs(poly-expected.coeffs)))
    nonneutral=np.sort(np.real(eig[np.abs(eig)>1e-6]))
    roots=np.roots(c)
    predicted=np.sort(np.r_[np.real(roots),np.repeat(-2.,n-2)])
    assert np.max(abs(nonneutral-predicted))<1e-6
    if abs(H(x,y*y,d*d))>1e-7:
        # Classification only of the four collective roots (n-2 exact radial modes are stable).
        stable=max(roots.real)<-1e-7
        criterion=(x<1 and H(x,y*y,d*d)>0)
        assert stable==criterion,(x,y,d,roots,criterion)
    return 1


def rational_identity():
    count = 0
    for xi in range(1,9):
        x=Fraction(xi,10)
        for yi in range(0,12):
            y=Fraction(yi,4)
            for di in range(0,10):
                d2=Fraction(di,10)
                v=x*x+y*y
                b1=4-2*x;b2=4-6*x+v;b3=2*(v-2*x);b4=(1-d2)*v
                hh=(b1*b2*b3-b3*b3-b1*b1*b4)/4
                rhs=(y*y+(2-x)**2)*((1-x)*y*y-x*(2-x)**2) + d2*(2-x)**2*(x*x+y*y)
                assert hh==rhs
                count+=1
    return count


def main():
    checks=rational_identity()
    for n in [3,4,5,6,7,8,9,10]:
        regular=[2*math.pi*j/n for j in range(n)]
        for x in [.07,.4,.5,.83,.97,1.0,1.2,1.8,2.1]:
            for y in [0,.2,.8,1,1.5,2,3,7,15]:
                checks+=test_one(regular,x,y)
    # Four-point non-regular balanced shapes; near-collinear angles are excluded.
    for ph in [.02,.04,.1,.2,.3,math.pi/6,math.pi/4,1.,math.pi/2,2.,2.7,3.]:
        t=[0.,math.pi,ph,ph+math.pi]
        for x in [.1,.35,.5,.75,.95,1.,1.25]:
            for y in [0,.2,.8,1.,1.3,2.,3.,8.]:
                checks+=test_one(t,x,y)
    # Exact four-agent boundary (x=1/2, y=1): d^2 = 13/18.
    x=Fraction(1,2);u=Fraction(1);d2=Fraction(13,18)
    H_exact=(u+(2-x)**2)*((1-x)*u-x*(2-x)**2)+d2*(2-x)**2*(x*x+u)
    assert H_exact==0
    assert H(float(x),float(u),3/4)>0
    assert H(float(x),float(u),0)<0
    checks+=3
    print('PASS',checks,'finite computations, exact rational Hurwitz identity and numeric full Jacobian characteristic checks')
    print('Four-site example d^2=0 instability; d^2=3/4 stability; threshold exactly 13/18')

if __name__=='__main__': main()
