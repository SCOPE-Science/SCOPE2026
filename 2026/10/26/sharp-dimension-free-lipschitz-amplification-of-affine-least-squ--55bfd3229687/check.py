#!/usr/bin/env python3
"""Exact rational checks for the continuous-cube affine projection bounds."""
from fractions import Fraction
from math import comb

def integral_minimum_square(d):
    # Integrate 2*t*(1-t)**d by expanding the binomial polynomial.
    return sum((2 * Fraction((-1)**j * comb(d,j), j+2)
                for j in range(d+1)), Fraction(0))

def median_second_moment(k):
    assert k%2==1 and k>=1
    # If B ~ Beta(a,a), Var(B)=1/[4*(2*a+1)]; M=2B-1.
    a=(k+1)//2
    return Fraction(1,2*a+1)

def bounds(d):
    assert d>=1
    upper=Fraction(3,2)*(1-integral_minimum_square(d))
    k=d if d%2 else d-1
    lower=Fraction(3,2)*(1-median_second_moment(k))
    return lower,upper

def main():
    for d in range(1,19):
        assert integral_minimum_square(d)==Fraction(2,(d+1)*(d+2))
        low,high=bounds(d)
        assert Fraction(0)<low<=high<Fraction(3,2)
        if d==1: assert low==high==1
        if d==3: assert low==Fraction(6,5)
        print(f'd={d:2d}: lower={low}, upper={high}')
    assert bounds(101)[0]>Fraction(14,10)
    print('PASS: exact finite-dimensional sample identities and bounds')
if __name__=='__main__': main()
