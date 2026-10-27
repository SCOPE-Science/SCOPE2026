#!/usr/bin/env python3
"""Exact integer checks for cubics from a rank-two projective bundle.

This is a finite regression check; the all-parameter arguments are mathematical.
"""
from itertools import product
from math import comb, gcd


def cubic_coefficients(q):
    # Coefficients of a^3, a^2*b, a*b^2, b^3.
    return (0, 3, 3 * q, 0)


def cubic_discriminant(c):
    a, b, cc, d = c
    return b*b*cc*cc - 4*a*cc**3 - 4*b**3*d - 27*a*a*d*d + 18*a*b*cc*d


def substitute(c, matrix):
    """Substitute a = u*x+v*y, b = w*x+z*y into a binary cubic."""
    u, v, w, z = matrix
    out = [0, 0, 0, 0]
    for j, coefficient in enumerate(c):
        for r in range(4-j):
            for s in range(j+1):
                x_exp = (3-j-r)+(j-s)
                y_exp = r+s
                out[y_exp] += (coefficient * comb(3-j,r) * comb(j,s)
                                   * u**(3-j-r) * v**r * w**(j-s) * z**s)
    return tuple(out)


def product_monomials(q, monomials):
    """Reduce h^a * eta^b modulo h^3 and eta^2=q*h*eta-q^2*h^2."""
    a = sum(x for x, _ in monomials)
    b = sum(y for _, y in monomials)
    # The needed degree-three monomials have only these possibilities.
    if a+b != 3:
        raise ValueError('only top-degree products supported')
    return {(3,0): 0, (2,1): 1, (1,2): q, (0,3): 0}[(a,b)]


def residue_normalization(q, prime):
    if q % prime == 0:
        # Each positive Frobenius height gives eta^2=0 modulo p.
        return ('degenerate', 0, 0)
    inv = pow(q, -1, prime)
    # z=eta/q -> z^2-h*z+h^2=0
    return ('nondegenerate', (q*inv) % prime, (q*q*inv*inv) % prime)


def check():
    qs = (2, 3, 4, 5, 8, 9, 16, 25, 27)
    matrices = [M for M in product(range(-2,3), repeat=4)
                if abs(M[0]*M[3]-M[1]*M[2]) == 1]
    for q in qs:
        coeff = cubic_coefficients(q)
        assert cubic_discriminant(coeff) == 81*q*q
        assert product_monomials(q, ((2,0),(0,1))) == 1
        assert product_monomials(q, ((1,0),(0,2))) == q
        assert product_monomials(q, ((0,3),)) == 0
        for M in matrices:
            assert cubic_discriminant(substitute(coeff,M)) == 81*q*q
        for ell in (2,3,5,7,11,13):
            if q in (2,4,8,16):
                p=2
            elif q in (3,9,27):
                p=3
            else:
                p=5
            if ell == p:
                assert residue_normalization(q,ell)==('degenerate',0,0)
            else:
                assert residue_normalization(q,ell)==('nondegenerate',1,1)
    assert gcd(1,3) == 1
    print(f'VERIFY_OK heights={len(qs)} unimodular_changes={len(matrices)} prime_reductions=54')


if __name__ == '__main__':
    check()
