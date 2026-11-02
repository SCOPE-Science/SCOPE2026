#!/usr/bin/env python3
"""Finite checks for prime-power weighted Apery polynomial congruences.

This is corroboration, not a substitute for the all-prime proof.
Requires only Python 3's standard library.
"""
from math import comb


def direct_coefficients(n):
    c = [0] * n
    for k in range(n):
        for j in range(k + 1):
            c[j] += (2*k + 1) * comb(k,j)**2 * comb(k+j,j)**2
    return c


def closed_coefficients(n):
    c = []
    for j in range(n):
        num = n*n * comb(n-1,j)**2 * comb(n+j,j)**2
        assert num % (2*j+1) == 0
        c.append(num // (2*j+1))
    return c


def value_mod(c,x,m):
    y = 0
    for v in reversed(c):
        y = (y*x+v) % m
    return y


cases = [(3,1), (3,2), (3,3), (5,1), (5,2), (7,1), (7,2), (11,1)]
coeff_checks = 0
valuation_checks = 0
root_counts = 0
for p,a in cases:
    n = p**a
    c = direct_coefficients(n)
    cc = closed_coefficients(n)
    assert c == cc, (p,a,"identity")
    coeff_checks += len(c)
    q = p**(a+1)
    j0 = (n-1)//2
    assert all((v-(n if j==j0 else 0))%q==0 for j,v in enumerate(c)), (p,a,"residue polynomial")
    # Valuations are assessed by congruences rather than floating-point logs.
    for x in range(min(2*p*p,300)):
        want = a if x%p else 2*a
        if p>=5:
            assert value_mod(c,x,p**want) == 0
            assert value_mod(c,x,p**(want+1)) != 0, (p,a,x,"valuation")
        elif x%p:
            assert value_mod(c,x,p**want) == 0
            assert value_mod(c,x,p**(want+1)) != 0, (p,a,x,"unit valuation")
        valuation_checks += 1
    max_k = 6 if p == 3 else (4 if p == 5 else 3)
    if p**max_k > 2500:
        max_k = 3
    for k in range(1,max_k+1):
        modulus = p**k
        count = sum(value_mod(c,x,modulus)==0 for x in range(modulus))
        if k <= a:
            expected = modulus
        elif k<=2*a:
            expected = p**(k-1)
        elif p==3:
            expected = 3**(2*a-1)
        else:
            expected = 0
        assert count == expected, (p,a,k,count,expected)
        root_counts+=1

# The 2-adic fixed divisor comes from coefficientwise divisibility by n*n.
for a in range(1,7):
    n=2**a
    c=closed_coefficients(n)
    assert c[0]==n*n
    assert all(t%(n*n)==0 for t in c)
    coeff_checks +=len(c)

print("VERIFY_OK",f"odd_prime_cases={len(cases)}",f"coefficient_checks={coeff_checks}",f"valuation_checks={valuation_checks}",f"modular_root_counts={root_counts}","dyadic_cases=6")
