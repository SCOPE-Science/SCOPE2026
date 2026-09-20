#!/usr/bin/env python3
"""Finite coefficient checks for the two-call additive-polynomial theorem.

The general result is proved algebraically in RESULT.md.  This script checks,
for small prime characteristics, the formal binomial criterion
(X+Y)^d-X^d-Y^d=0 and the two-access Frobenius transcript.
"""
from math import comb

def is_additive_monomial(d, p):
    return all(comb(d, k) % p == 0 for k in range(1, d))

def p_powers_up_to(p, D):
    out = []
    e = 0
    v = 1
    while v <= D:
        out.append(v)
        e += 1
        v *= p
    return out

def frobenius_difference_coeffs(p, exponents, coeffs):
    # For A(Z)=sum c_e Z^(p^e), return mixed binomial coefficients
    # in A(T+X)-A(T)-A(X), indexed by (total_degree,k).
    mixed = {}
    for e, c in zip(exponents, coeffs):
        d = p ** e
        for k in range(1, d):
            val = (c * comb(d, k)) % p
            if val:
                mixed[(d, k)] = val
    return mixed

def main():
    for p, D in [(2, 32), (3, 32), (5, 30), (7, 30)]:
        observed = [d for d in range(1, D + 1) if is_additive_monomial(d, p)]
        expected = p_powers_up_to(p, D)
        assert observed == expected, (p, observed, expected)
        print(f"p={p}, additive monomial degrees through {D}: {observed}")

    tests = [
        (2, [0,1,2,4], [1,1,1,1]),
        (3, [0,1,2], [2,1,2]),
        (5, [0,1,2], [3,4,2]),
        (7, [0,1], [6,5]),
    ]
    for p, exps, coeffs in tests:
        mixed = frobenius_difference_coeffs(p, exps, coeffs)
        assert mixed == {}, (p, mixed)
        degree = p ** max(exps)
        print(f"p={p}, verified A(T+X)-A(T)-A(X)=0 through degree {degree}")

    # Non-Frobenius controls: at least one mixed term must survive.
    controls = [(2,3), (3,2), (3,4), (5,2), (5,6), (7,3)]
    for p, d in controls:
        assert not is_additive_monomial(d, p), (p, d)
    print("non-Frobenius controls: PASS")
    print("PASS")

if __name__ == "__main__":
    main()
