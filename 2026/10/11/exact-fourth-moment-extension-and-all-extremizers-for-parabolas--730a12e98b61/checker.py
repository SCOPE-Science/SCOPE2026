#!/usr/bin/env python3
"""Finite exact-integer checks for quadratic-graph fourth moments over odd prime powers.

No external dependencies. The checks are not an exhaustive test over all signals,
nor do they replace the general proof.
"""
from collections import defaultdict
from fractions import Fraction
from math import cos, pi, sin
from cmath import exp
import random


def predicted_constant(p, k):
    if k % 2 == 0:
        return Fraction(p ** (k // 2))
    if k == 1:
        return Fraction(2 * p - 1, p)
    return Fraction((2 * p - 1) * p ** ((k - 3) // 2))


def predicted_roots(t, p, k):
    r = 0
    while r < k and t % p == 0:
        t //= p
        r += 1
    return p ** (k // 2) if 2 * r >= k else 2 * p ** r


def fibres(q):
    classes = defaultdict(list)
    for x in range(q):
        for y in range(q):
            classes[((x + y) % q, (x * x + y * y) % q)].append((x, y))
    return classes


def gaussian_moment(f, classes):
    # Each f entry is a Gaussian integer represented by (real, imaginary).
    numerator = 0
    for pairs in classes.values():
        real = imag = 0
        for x, y in pairs:
            a, b = f[x]
            c, d = f[y]
            real += a*c - b*d
            imag += a*d + b*c
        numerator += real*real + imag*imag
    norm = sum(a*a + b*b for a, b in f)
    return Fraction(numerator, norm*norm)


def complex_moment(f, classes):
    energy = 0.0
    for pairs in classes.values():
        z = sum(f[x]*f[y] for x, y in pairs)
        energy += abs(z)**2
    norm = sum(abs(z)**2 for z in f)
    return energy/(norm*norm)


def complex_extremizer(p,k):
    q = p**k
    m = k//2
    C = p**m
    a = 1 % C
    f = [0j]*q
    for x in range(q):
        if (x-a)%C:
            continue
        r = ((x-a)//C)%p
        theta = 0 if k%2==0 else 2*pi*(r*r+2*r)/(p+1)
        theta += 2*pi*7*(x-a)/q
        f[x] = complex(cos(theta),sin(theta))
    return f


def direct_fourier_fourth_power(f, q):
    # The normalization is q^-1 on the curve and counting measure on the plane.
    w = [exp(2j*pi*t/q) for t in range(q)]
    ans = 0.0
    for u in range(q):
        for v in range(q):
            z = sum(f[x]*w[(u*x+v*x*x)%q] for x in range(q))/q
            ans += abs(z)**4
    return ans


def test():
    rng = random.Random(20180109)
    cases = [(3,1),(5,1),(7,1),(11,1),(3,2),(5,2),(7,2),
             (3,3),(5,3),(3,4),(3,5)]
    checks = 0
    for p,k in cases:
        q = p**k
        classes = fibres(q)
        assert sum(len(g) for g in classes.values()) == q*q
        half = pow(2,-1,q)
        # Independently enumerate each actual two-sum fibre and compare
        # its size with the p-adic root-multiplicity formula.
        for x in range(q):
            for y in range(q):
                group = classes[((x+y)%q,(x*x+y*y)%q)]
                assert len(group) == predicted_roots(((x-y)*half)%q,p,k)
                checks += 1
        # Integer-valued coset witness attains the theorem's exact rational bound.
        h = p**(k//2)
        f = [(int(x%h==0),0) for x in range(q)]
        assert gaussian_moment(f,classes) == predicted_constant(p,k)
        checks += 1
        # Nontrivial phases from the proposed complete equality family.
        z = complex_extremizer(p,k)
        assert abs(complex_moment(z,classes)-float(predicted_constant(p,k)))<1e-10
        checks += 1
        # 8 integer-complex stress tests for each order; no rounding.
        for _ in range(8):
            f = [(rng.randint(-3,3),rng.randint(-3,3)) for x in range(q)]
            assert gaussian_moment(f,classes) <= predicted_constant(p,k)
            checks += 1
        if q in (3,9,27):
            f = [complex(rng.randint(-2,2),rng.randint(-2,2)) for x in range(q)]
            norm = sum(abs(v)**2 for v in f)
            via_fibres = complex_moment(f,classes)*norm**2/q**2
            direct = direct_fourier_fourth_power(f,q)
            assert abs(direct-via_fibres) < 1e-10*max(1,abs(via_fibres))
            checks += 1
        print('p=%d k=%d |R|=%d sharp_fourth_power_ratio=%s fibres=%d' %
              (p,k,q,predicted_constant(p,k),len(classes)))
    print('EXACT_CHECKS_PASSED',checks)


if __name__ == '__main__':
    test()
