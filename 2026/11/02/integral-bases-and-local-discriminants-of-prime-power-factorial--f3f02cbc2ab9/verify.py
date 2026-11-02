#!/usr/bin/env python3
"""Reproduce finite exact checks for factorial-Hadamard polynomial local invariants."""
from math import factorial, gcd


def vp(n, p):
    if n == 0:
        return float('inf')
    n = abs(n)
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def digit_sum(n, p):
    result = 0
    while n:
        result += n % p
        n //= p
    return result


def det_bareiss(matrix):
    a = [list(row) for row in matrix]
    d = len(a)
    sign = 1
    prev = 1
    for i in range(d-1):
        if a[i][i] == 0:
            j = next((j for j in range(i+1, d) if a[j][i]), None)
            if j is None:
                return 0
            a[i], a[j] = a[j], a[i]
            sign *= -1
        pivot = a[i][i]
        for j in range(i+1, d):
            for k in range(i+1, d):
                num = a[j][k]*pivot - a[j][i]*a[i][k]
                assert num % prev == 0
                a[j][k] = num // prev
            a[j][i] = 0
        prev = pivot
    return sign*a[-1][-1]


def polynomial_discriminant(coeff):
    # Coefficients ascending, monic and degree n.
    n = len(coeff)-1
    f = list(reversed(coeff))
    deriv = [j*coeff[j] for j in range(n, 0, -1)]
    mat = []
    size = 2*n-1
    for shift in range(n-1):
        mat.append([0]*shift + f + [0]*(n-2-shift))
    for shift in range(n):
        mat.append([0]*shift + deriv + [0]*(n-1-shift))
    assert len(mat) == size and all(len(row) == size for row in mat)
    resultant = det_bareiss(mat)
    assert resultant != 0
    return (-1)**(n*(n-1)//2)*resultant


def run():
    cases = [(3,1,2), (3,2,2), (5,1,2), (5,1,3), (5,1,4),
             (7,1,2), (7,1,3), (7,1,4)]
    coeff_checks = 0
    derivative_checks = 0
    for p,a,r in cases:
        n = p**a
        h = (n-1)//(p-1)
        s = r*h
        assert gcd(n,s) == 1
        fac = factorial(n)
        coeff = [(fac//factorial(k))**r for k in range(n+1)]
        assert coeff[n] == 1
        for k,c in enumerate(coeff):
            value = vp(c,p)
            assert value == r*(h-vp(factorial(k),p))
            if 0<k<n:
                assert value*n>(n-k)*s
                assert digit_sum(k,p)*n>k
            if k>=2:
                # Comparison to derivative term at k=1, with valuation in units of 1/n.
                assert n*(vp(k,p)+value)+ (k-1)*s > n*s
                derivative_checks += 1
            coeff_checks += 1
        direct_disc = polynomial_discriminant(coeff)
        assert vp(direct_disc,p) == n*s
        integral_index = sum(j*s//n for j in range(n))
        assert integral_index == (n-1)*(s-1)//2
        field_disc = vp(direct_disc,p)-2*integral_index
        assert field_disc == n+s-1
    print(f'VERIFY_OK cases={len(cases)} exact_resultant_discriminants={len(cases)} coefficient_checks={coeff_checks} derivative_competitor_checks={derivative_checks}')

if __name__ == '__main__':
    run()
