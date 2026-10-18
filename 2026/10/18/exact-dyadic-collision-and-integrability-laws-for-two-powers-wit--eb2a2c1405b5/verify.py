#!/usr/bin/env python3
"""Reproduce exact dyadic two-power representation and collision checks.

The finite computations test the theorem; the infinite conclusion uses the proof.
"""
from collections import Counter
from fractions import Fraction


def predicted_fibre(d, n, a):
    assert d >= 6 and d % 4 == 2 and 0 <= a < (1 << n)
    if n == 1:
        return 1
    if n == 2:
        return (1, 2, 1, 0)[a]
    if a % 8 == 1:
        return 4
    if a % 8 == 2:
        return 2
    if n <= d:
        return 1 << (n - 2) if a == 0 else 0
    if a % (1 << d):
        return 0
    return (1 << (d - 2)) * predicted_fibre(d, n-d, a >> d)


def brute_fibres(d, n):
    modulus = 1 << n
    powers = Counter(pow(x, d, modulus) for x in range(modulus))
    fibres = [0] * modulus
    for u, cu in powers.items():
        for v, cv in powers.items():
            fibres[(u+v) % modulus] += cu * cv
    return fibres


def second_moment_formula(d, n):
    if n == 1:
        return Fraction(1)
    if n == 2:
        return Fraction(3,2)
    if n <= d:
        return Fraction(5,2) + Fraction(1 << (n-4)) if n >= 4 else Fraction(3)
    return Fraction(5,2) + (1 << (d-4))*second_moment_formula(d,n-d)


def main():
    cases = {6: range(1,14), 10: range(1,12), 14: range(1,11), 18: range(1,10)}
    checks = 0
    for d, exponents in cases.items():
        for n in exponents:
            fibres=brute_fibres(d,n)
            modulus=1 << n
            assert sum(fibres)==modulus*modulus
            predicted=[predicted_fibre(d,n,a) for a in range(modulus)]
            observed=[k//modulus for k in fibres]
            assert all(k%modulus==0 for k in fibres), (d,n,'nonintegral')
            assert observed==predicted, (d,n,next(i for i in range(modulus) if observed[i]!=predicted[i]))
            moment=Fraction(sum(k*k for k in observed), modulus)
            assert moment == second_moment_formula(d,n), (d,n,moment,second_moment_formula(d,n))
            checks += modulus + 2
        # Odd units map with equal fibres onto 1 modulo 8 for every level.
        for n in range(3,14):
            m=1<<n
            image=Counter(pow(u,d,m) for u in range(1,m,2))
            assert set(image)==set(range(1,m,8))
            assert set(image.values())=={4}
            checks+=len(image)
    print('PASS: dyadic fibre counts, exact energy, and odd-unit image laws')
    print('Exponents and level counts:', {d:len(list(ns)) for d,ns in cases.items()})
    print('Comparisons:',checks)
    print('In particular for sixth powers C(6,6)=',second_moment_formula(6,6),', C(6,12)=',second_moment_formula(6,12))

if __name__=='__main__':
    main()
