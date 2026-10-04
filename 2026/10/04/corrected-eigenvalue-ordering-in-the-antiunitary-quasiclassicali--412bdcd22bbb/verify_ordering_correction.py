#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement

def corrected_bell(p):
    a=(1-p)/4
    b=(1+3*p)/4
    return max(Fraction(0), b-3*a)

def literal_bell(p):
    a=(1-p)/4
    b=(1+3*p)/4
    vals=sorted([a,a,a,b])
    return max(Fraction(0), vals[0]-sum(vals[1:], Fraction(0)))

def main():
    collapse_checks=0
    # Exhaustive nondecreasing nonnegative integer spectra of lengths 2..6.
    for r in range(2,7):
        for vals in combinations_with_replacement(range(7), r):
            lhs=vals[0]-sum(vals[1:])
            assert lhs <= vals[0]-vals[1] <= 0
            assert max(0,lhs)==0
            collapse_checks += 1

    bell_checks=0
    for q in range(0,21):
        p=Fraction(q,20)
        got=corrected_bell(p)
        expected=max(Fraction(0),(3*p-1)/2)
        assert got==expected
        assert literal_bell(p)==0
        bell_checks += 1

    p=Fraction(1,2)
    assert corrected_bell(p)==Fraction(1,4)
    assert literal_bell(p)==0

    # Corrected ordering must put the Bell eigenvalue first for p>=0.
    order_checks=0
    for q in range(0,21):
        p=Fraction(q,20)
        a=(1-p)/4
        b=(1+3*p)/4
        assert b>=a>=0
        vals=sorted([a,a,a,b], reverse=True)
        assert vals[0]==b
        order_checks += 1

    print('VERIFY_OK')
    print('ascending_collapse_checks =', collapse_checks)
    print('bell_white_noise_checks =', bell_checks)
    print('descending_order_checks =', order_checks)
    print('p_half_corrected = 1/4')
    print('p_half_literal = 0')

if __name__=='__main__':
    main()
