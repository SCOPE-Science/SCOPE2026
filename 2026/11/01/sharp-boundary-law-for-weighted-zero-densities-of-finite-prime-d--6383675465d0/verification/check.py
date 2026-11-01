#!/usr/bin/env python3
"""Standalone checks of a finite-prime Dirichlet boundary zero-density law.
All calculations use only the Python standard library. Numerical tests complement,
not replace, the analytic Jessen/phase-cap proof in RESULT.md.
"""
from fractions import Fraction
import math


def determinant(mat):
    a = [[Fraction(t) for t in row] for row in mat]
    n = len(a)
    product = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j] != 0), None)
        assert pivot is not None
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            product = -product
        diag = a[j][j]
        product *= diag
        for i in range(j + 1, n):
            ratio = a[i][j] / diag
            for k in range(j + 1, n):
                a[i][k] -= ratio * a[j][k]
            a[i][j] = 0
    return product


def check_hessian():
    trials = [
        [1,1], [1,2,3], [Fraction(1,3),2,Fraction(4,5)],
        [1,2,3,4], [2,3,5,7,11], [Fraction(j,j+1) for j in range(1,7)],
    ]
    for b in trials:
        B = sum(b)
        hess = [[(Fraction(b[i]) if i == j else Fraction(0)) - Fraction(b[i])*Fraction(b[j])/Fraction(B)
                 for j in range(len(b)-1)] for i in range(len(b)-1)]
        actual = determinant(hess)
        wanted = math.prod(map(Fraction,b)) / Fraction(B)
        assert actual == wanted, (b,actual,wanted)
    print('PASS: six exact-rational phase-Hessian determinant identities')


def jessen_two(eps, count=180000):
    # For a=b=1, w=c-2+eps. Common-angle Jensen integration is exact.
    D = 2.0 - eps
    total = 0.0
    for k in range(count):
        angle = 2.0*math.pi*(k+0.5)/count
        R = math.sqrt(2.0+2.0*math.cos(angle))
        if R>D:
            total += math.log(R/D)
    return total/count


def jessen_three(eps, count=720):
    D = 3.0-eps
    xy = [(math.cos(2*math.pi*(j+0.5)/count),
           math.sin(2*math.pi*(j+0.5)/count)) for j in range(count)]
    total = 0.0
    for cx,sx in xy:
        for cy,sy in xy:
            R = math.hypot(1+cx+cy,sx+sy)
            if R>D:
                total += math.log(R/D)
    return total / (count*count)


def check_numeric():
    # nu=1 has M_1(w)=J(0)-log(A-eps), a consequence of known
    # mean-counting formula; the phase integrals are independent checks.
    previous = float('inf')
    for eps in (0.05,0.005,0.0005):
        exact_jensen = jessen_two(eps)
        asymptotic = 2.0/(3.0*math.pi) * eps**1.5
        ratio = exact_jensen / asymptotic
        print('two primes: eps=%g, ratio=%.8f' % (eps,ratio))
        assert abs(ratio-1) < previous
        previous = abs(ratio-1)
    assert previous < 0.005
    previous = float('inf')
    for eps in (0.10,0.05,0.02):
        exact_jensen = jessen_three(eps)
        asymptotic = math.sqrt(3)/(12*math.pi)*eps**2
        ratio = exact_jensen / asymptotic
        print('three primes: eps=%g, ratio=%.8f' % (eps,ratio))
        assert abs(ratio-1) < previous
        previous = abs(ratio-1)
    assert previous < 0.014
    print('PASS: deterministic Jensen-mean quadratures at two and three primes')

if __name__=='__main__':
    check_hessian()
    check_numeric()
