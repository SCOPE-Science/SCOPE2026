#!/usr/bin/env python3
"""Reproduce exact Fourier-moment and geometric identities for circular number variance.

Requires only the Python standard library. All algebraic moment checks use
fractions; the pi-valued factor is kept outside the rational calculations.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import cos, sin, pi, isclose
from random import Random

ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

def polyprod(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = ka + kb
            out[k] = add(out.get(k, ZERO), mul(va, vb))
    return out

def coefficients(epsilon, kind):
    half = epsilon / 2
    out = {0: ONE, 1: (half, Q(0)), -1: (half, Q(0))}
    if kind == 1:
        out.update({2: (half, Q(0)), -2: (half, Q(0))})
    else:
        out.update({2: (Q(0), -half), -2: (Q(0), half)})
    return out

def value_of_phi_moments(f):
    # On the half-circle scale, the convolution kernel has pi^2 * c_1 = 1,
    # and even Fourier frequencies have coefficient zero. Write
    # pi^2 * phi(x)=sum_{k=+-1} fhat(k) exp(2*pi*i*k*x).
    phi = {k: f[k] for k in (-1, 1)}
    mean = polyprod(f, phi).get(0, ZERO)
    triple = polyprod(f, polyprod(phi, phi)).get(0, ZERO)
    return mean, triple

def circular_half_variance_direct(points):
    n = len(points)
    s = Q(1, 2)
    knots = {Q(0), Q(1)}
    for x in points:
        knots.add(x % 1)
        knots.add((x - s) % 1)
    intervals = sorted(knots)
    total = Q(0)
    for left, right in zip(intervals, intervals[1:]):
        midpoint = (left + right) / 2
        count = sum(Q(0) < (x - midpoint) % 1 <= s for x in points)
        total += (right-left) * (count - n*s)**2
    return total

def circular_half_variance_pairs(points):
    n = len(points)
    result = Q(n, 4)
    for x, y in combinations(points, 2):
        delta = abs(x-y)
        delta = min(delta, 1-delta)
        result += 2 * (Q(1, 4)-delta)
    return result

def run():
    trials = 0
    for denominator in [5, 8, 13, 19, 31]:
        for numerator in range(1, denominator // 2 + 1):
            eps = Q(numerator, denominator)
            if not eps < Q(1, 2):
                continue
            f1, f2 = coefficients(eps, 1), coefficients(eps, 2)
            # Same circular power spectrum at every Fourier mode.
            assert {k: mul(v, (v[0], -v[1]))[0] for k, v in f1.items()} == {
                k: mul(v, (v[0], -v[1]))[0] for k, v in f2.items()}
            m1, t1 = value_of_phi_moments(f1)
            m2, t2 = value_of_phi_moments(f2)
            assert m1 == m2 == (eps**2 / 2, Q(0))
            assert t1 == (eps**2 / 2 + eps**3 / 4, Q(0))
            assert t2 == (eps**2 / 2, Q(0))
            for n in range(1, 23):
                # Multiply covariance difference by pi^4; same-pair terms
                # cancel, whereas adjacent-pair terms produce this exact gap.
                normalized_gap = 4*n*(n-1)*(n-2)*(t1[0]-t2[0])
                assert normalized_gap == n*(n-1)*(n-2)*eps**3
                trials += 1
    rng = Random(74103)
    geometric_tests = 0
    for n in range(1, 11):
        for _ in range(25):
            sample = [Q(rng.randrange(10007), 10007) for _ in range(n)]
            assert circular_half_variance_direct(sample) == circular_half_variance_pairs(sample)
            geometric_tests += 1
    # A separate finite-grid enumeration integrates the complete third-sample
    # law for two noncongruent densities and checks its limiting variance gap.
    eps = 0.25
    numeric_tests = []
    for m in [24, 48, 96]:
        f1 = [1 + eps*(cos(2*pi*j/m) + cos(4*pi*j/m)) for j in range(m)]
        f2 = [1 + eps*(cos(2*pi*j/m) + sin(4*pi*j/m)) for j in range(m)]
        weights1 = [v/m for v in f1]
        weights2 = [v/m for v in f2]
        def kval(j, k):
            d = abs(j-k)/m
            return .25-min(d,1-d)
        ktab = [[kval(i,j) for j in range(m)] for i in range(m)]
        first = [0.0, 0.0]
        second = [0.0, 0.0]
        for a in range(m):
            for b in range(m):
                kab = ktab[a][b]
                for c in range(m):
                    v = .75+2*(kab+ktab[a][c]+ktab[b][c])
                    wa = weights1[a]*weights1[b]*weights1[c]
                    wb = weights2[a]*weights2[b]*weights2[c]
                    first[0] += wa*v
                    first[1] += wb*v
                    second[0] += wa*v*v
                    second[1] += wb*v*v
        gap = second[0]-first[0]**2-second[1]+first[1]**2
        predicted = 6*eps**3/pi**4
        assert isclose(gap, predicted, rel_tol=.015), (m,gap,predicted)
        numeric_tests.append((m,gap,predicted))
    print(f'PASS {trials} exact-rational Fourier/covariance checks')
    print(f'PASS {geometric_tests} exact-rational direct integration checks')
    for m,gap,predicted in numeric_tests:
        print(f'PASS grid={m}: variance gap={gap:.12g}, continuum={predicted:.12g}')

if __name__ == '__main__':
    run()
