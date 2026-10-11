#!/usr/bin/env python3
"""Exact finite-moment identity tests and independent three-dimensional slice check.

Python 3.10+ standard library only. Tests are diagnostics, not an infinite proof.
"""
from fractions import Fraction
from itertools import product
from math import factorial, sqrt, pi, prod


def rising(x, k):
    out = Fraction(1)
    for j in range(k):
        out *= x + j
    return out


def moment(b, k):
    d = len(b)
    ans = Fraction(0)
    for alpha in product(range(k + 1), repeat=d):
        if sum(alpha) != k:
            continue
        term = Fraction(factorial(k))
        for bi, ai in zip(b, alpha):
            term *= rising(Fraction(1, 2), ai) * bi**ai / factorial(ai)
        ans += term
    return ans / rising(Fraction(d, 2), k)


def moment_reconstruction(b):
    d = len(b)
    mm = [moment(b, j) for j in range(d + 1)]
    g = [rising(Fraction(d, 2), j) * mm[j] / factorial(j)
         for j in range(d + 1)]
    g2 = [sum(g[i] * g[k - i] for i in range(k + 1))
          for k in range(d + 1)]
    h = [Fraction(1)]
    for k in range(1, d + 1):
        h.append(-sum(h[k-j] * g2[j] for j in range(1, k + 1)))
    exact = [Fraction(1)]
    for bi in b:
        out = [Fraction(0)] * (len(exact) + 1)
        for j, c in enumerate(exact):
            out[j] += c
            out[j+1] -= bi*c
        exact = out
    assert h == exact, (b, h, exact)
    return mm


def dot(u, v):
    return sum(x*y for x, y in zip(u, v))


def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1],
            u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])


def unit(u):
    norm=sqrt(dot(u,u))
    return tuple(x/norm for x in u)


def independent_slice_area(a, normal):
    u=unit(normal)
    v=unit(cross(u,(1.,0.,0.)))
    w=cross(u,v)
    qvv=sum((x/y)**2 for x,y in zip(v,a))
    qww=sum((x/y)**2 for x,y in zip(w,a))
    qvw=sum(v[i]*w[i]/a[i]**2 for i in range(3))
    return pi/sqrt(qvv*qww-qvw*qvw)


def checks():
    for b in [
        [Fraction(2), Fraction(5)],
        [Fraction(2), Fraction(3), Fraction(7)],
        [Fraction(1), Fraction(2), Fraction(3), Fraction(4)],
        [Fraction(1), Fraction(3), Fraction(4), Fraction(5), Fraction(8)],
    ]:
        mm=moment_reconstruction(b)
        assert len(mm) == len(b)+1
        assert mm[1] == sum(b)/len(b)
    # For two dimensions, (2,4) and (1,5) share the first moment,
    # yet correspond to different axis multisets.
    assert moment([Fraction(2), Fraction(4)],1) == moment(
        [Fraction(1), Fraction(5)],1)
    a=(1.5, 2.0, 3.5)
    for normal in [(1.,2.,3.),(2.,-3.,1.),(1.,1.,1.),(-1.,2.,4.)]:
        u=unit(normal)
        via_jacobian=pi*prod(a)/sqrt(sum((ai*ui)**2
                                               for ai,ui in zip(a,u)))
        via_restricted_quadratic=independent_slice_area(a,normal)
        assert abs(via_jacobian/via_restricted_quadratic-1)<2e-14
    print('VERIFY_OK: exact moments in dimensions 2-5, sharp 2D ambiguity, four independent 3D section-area checks')


if __name__=='__main__':
    checks()
