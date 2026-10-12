#!/usr/bin/env python3
"""Independent exact enumeration for random-recursive-tree leaf/profile covariance."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from cmath import exp, pi


def multiply(a, b):
    c = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def from_enumeration(n):
    pair = defaultdict(int)
    totals = defaultdict(int)
    leaf_sum = 0
    count = 0
    residue_moments = {q: [Fraction(0)] * q for q in range(2, 10)}
    for parents in product(*(range(1, j) for j in range(2, n+1))):
        children = [0] * (n+1)
        depth = [0] * (n+1)
        for j, parent in enumerate(parents, 2):
            children[parent] += 1
            depth[j] = depth[parent] + 1
        leaves = sum(children[j] == 0 for j in range(1, n+1))
        leaf_sum += leaves
        count += 1
        for j in range(1, n+1):
            d = depth[j]
            totals[d] += 1
            pair[d] += leaves
    return [Fraction(pair[d], count)-Fraction(leaf_sum*totals[d], count*count)
            for d in range(n)]


def from_formula(n):
    if n == 2:
        return [Fraction(0)]*n
    a = [Fraction(1)]
    for j in range(3, n):
        a = multiply(a, [Fraction(j-1,j), Fraction(1,j)])
    a = multiply(a, [Fraction(0), Fraction(n-2,4), Fraction(-(n-2),4)])
    return a + [Fraction(0)]*(n-len(a))


def evaluate(coefficients, z):
    return sum(complex(float(x))*z**k for k, x in enumerate(coefficients))


def run():
    case_count=0
    fourier_count=0
    for n in range(2,10):
        enumerated = from_enumeration(n)
        predicted = from_formula(n)
        assert enumerated == predicted, (n, enumerated, predicted)
        case_count += n
        if n >= 3:
            alt = sum(c*(-1)**k for k,c in enumerate(predicted))
            assert alt == -Fraction(1,n-1), (n,alt)
            slope=sum(k*c for k,c in enumerate(predicted))
            assert slope == -Fraction(n-2,4), (n,slope)
            case_count += 2
        for q in range(2,10):
            w=exp(2j*pi/q)
            for r in range(q):
                direct=sum(float(c) for k,c in enumerate(enumerated) if k%q == r)
                fourier=sum((w**(-r*ell))*evaluate(predicted,w**ell)
                             for ell in range(q))/q
                assert abs(fourier.real-direct)<1e-9 and abs(fourier.imag)<1e-9, (n,q,r)
                fourier_count+=1
    print('PASS exact coefficient cases:',case_count)
    print('PASS finite Fourier coefficient checks:',fourier_count)
    print('No finite enumeration is used to establish the asymptotic theorem.')

if __name__=='__main__':run()
