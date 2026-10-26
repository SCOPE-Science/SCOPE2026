#!/usr/bin/env python3
"""Exact reproducibility checks for a binary observation of a cubic toral skew map.

The unrestricted Haar result is proved in RESULT.md by Fourier approximation
and a coefficient-parity argument. This script checks the identities used in
that argument and gives an independent finite-grid illustration.
"""
from math import comb


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def poly_for(a, b, c):
    return multiply([1,-4,6,-4,1], [a,b,c])


def verify_polynomial_lemma():
    # Symbolic coefficient vectors of (z-1)^4(a+bz+cz^2).
    e_a = poly_for(1,0,0)
    e_b = poly_for(0,1,0)
    e_c = poly_for(0,0,1)
    assert (e_a,e_b,e_c) == (
        [1,-4,6,-4,1,0,0],
        [0,1,-4,6,-4,1,0],
        [0,0,1,-4,6,-4,1]
    )
    # If all coefficients are zero or odd, coefficient 3 is even => zero:
    # -4a+6b-4c=0, hence 3b=2(a+c), so b is even.
    # Coefficients 1 and 5 are then even, hence zero:
    # b-4a=b-4c=0; thus a=c and b=4a.
    # Substitution into coefficient 3 gives 16a=0, hence a=b=c=0.
    for a in range(-8,9):
        for b in range(-8,9):
            for c in range(-8,9):
                v = poly_for(a,b,c)
                if all(x == 0 or x % 2 for x in v):
                    assert a == b == c == 0
    # The first degree-7 odd-support relation is a separate boundary
    # illustration; it does NOT assert a nonzero eighth sign moment.
    degree_seven = multiply([1,-4,6,-4,1],[1,1,1,1])
    assert degree_seven == [1,-3,3,-1,-1,3,-3,1]
    for k in range(4):
        assert sum(degree_seven[j]*comb(j,k) for j in range(8)) == 0
    return degree_seven


def grid_check():
    q = 32
    # On this particular rational grid the 128 patterns happen to be exactly
    # equinumerous. This finite computation is not the Haar-space proof.
    hist = [0]*128
    rows = [[comb(j,k) for k in range(4)] for j in range(7)]
    for x0 in range(q):
        for x1 in range(q):
            for x2 in range(q):
                base = [r[0]*x0+r[1]*x1+r[2]*x2 for r in rows]
                for x3 in range(q):
                    pattern = 0
                    for j in range(7):
                        val = (base[j]+rows[j][3]*x3) % q
                        pattern |= (val >= q//2) << j
                    hist[pattern] += 1
    assert sum(hist) == q**4
    assert min(hist)==max(hist)==q**4//128
    return min(hist)


if __name__ == '__main__':
    relation = verify_polynomial_lemma()
    per_pattern = grid_check()
    print('VERIFY_OK: exact cubic binomial coefficient identities;')
    print('no degree-at-most-six fourth-order zero with odd-or-zero coefficients;')
    print('degree-seven odd-coefficient relation:', relation)
    print('finite q=32 illustration: all 128 seven-bit patterns occur',per_pattern,'times;')
    print('unrestricted 7-block independence follows from the separate Fourier proof.')
