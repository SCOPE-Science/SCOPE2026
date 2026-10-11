#!/usr/bin/env python3
"""Numerical and exact-arithmetic checks for the sharp Lp rotundity coefficient.

The infinite-dimensional theorem requires the analytic proof in RESULT.md;
finite computations check only identities and its explicit extremizing family.
"""
import math
from fractions import Fraction


def phi(p, t):
    return (abs(t + 1) ** p - abs(t) ** p - p * abs(t) ** (p - 2) * t) / p


def scalar_bregman(p, a, b):
    return (abs(a + b) ** p - abs(a) ** p - p * abs(a) ** (p - 2) * a * b) / p


def argmin_phi(p):
    # The global minimum lies in (-1,0): if t>=0, phi>=1/p;
    # if t<=-1, symmetry and elementary convexity bound from the proof apply.
    a, b = -1., 0.
    for _ in range(170):
        l = a + (b-a)*0.3819660112501051
        r = b - (b-a)*0.3819660112501051
        if phi(p, l) <= phi(p, r):
            b = r
        else:
            a = l
    t = (a+b)/2
    return t, phi(p, t)


def sharp_pair(p, t, h):
    a = (1 - abs(t) ** p * h ** p) ** (1 / p)
    b = (1 - abs(t+1) ** p * h ** p) ** (1 / p)
    x = (a, t*h)
    y = (b, (t+1)*h)
    norm = lambda u: (sum(abs(v)**p for v in u)) ** (1/p)
    Jxy = abs(a)**(p-2)*a*b + abs(t*h)**(p-2)*t*h*(t+1)*h
    return norm(x), norm(y), norm((x[0]-y[0], x[1]-y[1])), (1-Jxy)


def test():
    checks=0
    for a_n in range(-10,11):
        for b_n in range(-10,11):
            a = Fraction(a_n, 3)
            b = Fraction(b_n, 4)
            actual = ((a+b)**4-a**4-4*a**3*b)/4
            identity = Fraction(3,2)*b*b*(a+b/Fraction(3))**2 + b**4/Fraction(12)
            assert actual==identity, (a,b,actual,identity)
            checks+=1
    assert phi(4., -1/3) > 0
    assert abs(phi(4., -1/3)-1/12)<1e-14
    for p in (2.2, 2.5, 3., 4., 5., 6., 8.):
        t, c = argmin_phi(p)
        assert -1 < t < 0
        assert 0<c<1/p
        for z_i in range(-1400,1401):
            z=z_i/140
            # Numerical roundoff is allowed only near minimizers and for large p.
            assert phi(p,z) >= c - 1e-9*max(1.,abs(phi(p,z))), (p,z,c)
            checks+=1
        vals=[]
        for h in (0.08,0.04,0.02,0.01,0.005):
            nx,ny,d,deficit=sharp_pair(p,t,h)
            assert abs(nx-1)<5e-13 and abs(ny-1)<5e-13
            assert d>=h*(1-1e-12)
            assert deficit>=0
            vals.append(deficit/h**p)
            checks+=1
        # p=8 has catastrophic cancellation at h<.01, so use h=.08, .04
        for v in vals[:2]:
            assert abs(v-c)<0.02, (p,c,v)
        print(f'p={p:g} t={t:.9f} c={c:.12g} ratios_at_h=.08,.04: {vals[0]:.12g}, {vals[1]:.12g}')
    print('VERIFY_OK exact_quartic_pairs=441 numeric_scalars=19607 two_atom_sphere_tests=35 analytic_infinite_proof_required=True')

if __name__=='__main__':
    test()
