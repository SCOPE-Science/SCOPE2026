#!/usr/bin/env python3
"""Standalone arithmetic and quadrature checks for cuboctahedral lattice Fourier coefficients.
Uses only the Python standard library. Run: python verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import cos, pi, isclose


def in_root_polytope(x):
    """Coordinate form x_4=-x_1-x_2-x_3, in the type-A3 root polytope."""
    z = -sum(x)
    return sum(max(Fraction(0), v) for v in (*x, z)) <= 1


def periodization_at_rational(y):
    return sum(in_root_polytope(tuple(y[i]-b[i] for i in range(3)))
               for b in product((0,1), repeat=3))


def predicted_coefficient(k):
    """Return rational R such that C(k)=R/pi**2, or ('volume',10/3) at 0."""
    if k == (0,0,0):
        return ('volume', Fraction(10,3))
    c = Counter((0, *k))
    pattern = sorted(c.values(), reverse=True)
    if pattern == [1,1,1,1]:
        return Fraction(0)
    if pattern == [2,1,1]:
        r = next(v for v,m in c.items() if m == 2)
        s,t = (v for v,m in c.items() if m == 1)
        return Fraction(-1, 2*(s-r)*(t-r))
    if pattern == [2,2]:
        r,s = tuple(c.keys())
        return Fraction(-1, (s-r)**2)
    if pattern == [3,1]:
        r = next(v for v,m in c.items() if m == 3)
        s = next(v for v,m in c.items() if m == 1)
        return Fraction(1, 2*(s-r)**2)
    raise AssertionError((k, pattern))


def gl_nodes_weights(n):
    """Gauss–Legendre quadrature in [0,1], computed by Newton iteration."""
    out=[]
    for j in range(1,n+1):
        z=cos(pi*(j-0.25)/(n+0.5))
        for _ in range(25):
            a,b=1.0,z
            for d in range(2,n+1):
                a,b=b,((2*d-1)*z*b-(d-1)*a)/d
            dp=n*(z*b-a)/(z*z-1)
            nz=z-b/dp
            if abs(nz-z)<1e-15:
                z=nz
                break
            z=nz
        a,b=1.0,z
        for d in range(2,n+1):
            a,b=b,((2*d-1)*z*b-(d-1)*a)/d
        dp=n*(z*b-a)/(z*z-1)
        out.append(((z+1)/2, 1/((1-z*z)*dp*dp)))
    return out


def simplex_real_fourier(k, order=32):
    """Independent 3-dimensional integration over the standard simplex."""
    q=gl_nodes_weights(order)
    result=0.0
    for u,wu in q:
        for v,wv in q:
            for w,ww in q:
                x=u
                y=(1-u)*v
                z=(1-u)*(1-v)*w
                jac=(1-u)**2*(1-v)
                result+=wu*wv*ww*jac*cos(2*pi*(k[0]*x+k[1]*y+k[2]*z))
    return 2*result+(3 if k == (0,0,0) else 0)


def main():
    tested=0
    # Rational points strictly inside the unit cube and away from dividing planes.
    for digits in product(range(1,10),repeat=3):
        y=tuple(Fraction(d,11) for d in digits)
        t=sum(y)
        if t in (1,2) or any(yi == t-1 for yi in y):
            continue
        observed=periodization_at_rational(y)
        target=4 if t<1 or t>2 else 3
        assert observed==target,(y,observed,target)
        tested+=1
    print('exact rational periodizations:',tested)

    cases=((0,0,0),(1,2,3),(1,1,2),(1,2,1),(1,2,0),
           (1,0,0),(1,1,1),(1,1,0),(2,-1,-1),
           (3,-2,1),(2,2,0),(0,0,1),(-1,-1,2))
    for k in cases:
        z=predicted_coefficient(k)
        target=float(z[1]) if isinstance(z,tuple) else float(z)/pi**2
        measured=simplex_real_fourier(k)
        assert abs(measured-target)<1e-8,(k,target,measured)
    print('independent simplex quadratures:',len(cases))

    for N in range(0,7):
        count=sum(predicted_coefficient(k) != 0 for k in product(range(-N,N+1),repeat=3))
        target=24*N*N+2*N+1
        assert count==target,(N,count,target)
    print('exhaustive Fourier support counts: N=0..6')
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    main()
