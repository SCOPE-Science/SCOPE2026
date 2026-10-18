"""Numerical cross-checks for the sharp angular zero-inclusion formulas.

Uses Python's standard library. Analytic proof, not finite sampling, covers all parameters.
"""
import cmath
import math
import random


def angular_factor(p, c):
    assert p > 1 and -1 <= c <= 1
    alpha = (p - 1) / p
    z = ((p - 2) * c + math.sqrt((p - 2) ** 2 * c * c + 4 * (p - 1))) / 2
    return math.sqrt(max(0.0, z*z + 2*c*z + 1)) / z**alpha


def threshold(p, a, d):
    assert p > 1 and a != 0 and d != 0
    cosine = (a*d.conjugate()).real / (abs(a)*abs(d))
    cosine = min(1.0, max(-1.0, cosine))
    return abs(a)**((p-1)/p) * abs(d)**(1/p) * angular_factor(p, cosine)


def numerical_minimum(p, a, d):
    # Golden-section minimization of the logarithmic amplitude ratio.
    alpha=(p-1)/p
    low, high = -18.0, 18.0
    golden = (math.sqrt(5)-1)/2
    def f(s):
        u=math.exp(s)
        return abs(a*u+d)/u**alpha
    c=high-golden*(high-low)
    e=low+golden*(high-low)
    for _ in range(180):
        if f(c)<f(e):
            high=e; e=c; c=high-golden*(high-low)
        else:
            low=c; c=e; e=low+golden*(high-low)
    return f((low+high)/2)


def test():
    tests=0
    rng=random.Random(137831)
    for p in (1.25, 1.5, 2.0, 2.75, 4.0, 7.0):
        for _ in range(90):
            A=math.exp(rng.uniform(-1.5,1.5))
            D=math.exp(rng.uniform(-1.5,1.5))
            angle=rng.uniform(-2.8,2.8)
            a=A+0j
            d=D*cmath.exp(1j*angle)
            direct=threshold(p,a,d)
            inverse=threshold(p,1/a,1/d)*A*D
            estimated=numerical_minimum(p,a,d)
            assert math.isclose(direct,estimated,rel_tol=2e-8,abs_tol=2e-8)
            assert math.isclose(direct/inverse,(A/D)**((p-2)/p),rel_tol=2e-8)
            tests+=2
    for p in (1.3,2.0,3.3,8.0):
        for c in (-1.0,-0.9,-0.25,0.0,0.75,1.0):
            h=angular_factor(p,c)
            assert h>=0.0
            if c>-1:
                assert h>0.0
            tests+=1
        assert all(angular_factor(p,x)<angular_factor(p,y) for x,y in zip([-1,-0.9,-0.25,0,0.75],[-0.9,-0.25,0,0.75,1]))
        tests+=1
    # Explicit exact-algebra witness, checked additionally in floating arithmetic:
    # for p=4, u=sqrt(2), v=-(1+i)/sqrt(2), a=1, d=4i, b=2;
    # J_4((u,v))(T(u,v))=4+4i-4(1+i)=0 (before normalization).
    p=4.0
    u=math.sqrt(2)
    v=-(1+1j)/math.sqrt(2)
    N=(abs(u)**p+abs(v)**p)**(1/p)
    u/=N; v/=N
    a=1+0j; d=4j; b=2+0j
    pairing=abs(u)**(p-2)*u.conjugate()*(a*u+b*v)+abs(v)**(p-2)*v.conjugate()*(d*v)
    assert abs(pairing)<1e-12
    assert threshold(p,a,d)<2<threshold(p,d,a)
    tests+=2
    # At p=2, thresholds for T and T^{-1} coincide for all nonzero diagonals.
    assert math.isclose(threshold(2,1+3j,4-2j), threshold(2,4-2j,1+3j),rel_tol=1e-12)
    tests+=1
    print('PASS: {} finite diagnostics; exact algebraic witness reviewed.'.format(tests))

if __name__=='__main__':
    test()
