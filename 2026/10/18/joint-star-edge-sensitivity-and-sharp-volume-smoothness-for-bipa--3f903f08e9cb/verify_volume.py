#!/usr/bin/env python3
"""Exact independent lattice-count/Ehrhart verification of star-edge volume formula.

No dependencies other than Python standard library. The leading Ehrhart coefficient
is recovered from lattice counts for dilations 0,...,d of the anchored polytope.
"""
from fractions import Fraction
from itertools import product
from math import factorial, comb


def formula(p,q,k,h):
    h=Fraction(h);s=h-1;delta=3-h
    assert p>=2 and q>=3 and 2<=k<=q-1 and 1<=h<=3
    r=q-k;d=p+q-1
    baseline=Fraction(2**d*factorial(p)*factorial(q),factorial(d))
    deleted=baseline*(1+Fraction(2*k,p*(r+1)))
    deficit=sum((Fraction(2*factorial(p-1)*comb(k,j)*j*factorial(r+j),(r+1)*factorial(p+r+j-1))*s**(k-j)*delta**(p+r+j-1) for j in range(1,k+1)),Fraction(0))
    return deleted-deficit


def count_dilate(p,q,k,h,n):
    h=Fraction(h);scale=h.denominator
    basic=scale*n;special=h.numerator*n
    choices=range(-basic,basic+1)
    total=0
    for Bs in product(choices,repeat=q):
        lo_A=max(Bs)-basic;hi_A=min(Bs)+basic
        if hi_A<lo_A:continue
        lo=max(max(Bs[k:])-basic,max(Bs[:k])-special)
        hi=min(min(Bs[k:])+basic,min(Bs[:k])+special)
        if hi<lo:continue
        total+=(hi-lo+1)*(hi_A-lo_A+1)**(p-2)
    return total


def ehrhart_volume(p,q,k,h):
    h=Fraction(h);d=p+q-1
    counts=[count_dilate(p,q,k,h,n) for n in range(d+1)]
    # Exact forward differences. For a d-dimensional integral polytope under
    # scaling by denominator h.denominator, difference^d equals d! times volume.
    differences=counts[:]
    while len(differences)>1:
        differences=[differences[j+1]-differences[j] for j in range(len(differences)-1)]
    assert differences[0]>0
    return Fraction(differences[0],factorial(d)*h.denominator**d),counts


def main():
    cases=[(2,3,2,Fraction(1)),(2,3,2,Fraction(3,2)),(2,3,2,Fraction(2)),
           (2,3,2,Fraction(3)),(3,3,2,Fraction(2)),
           (3,4,2,Fraction(2)),(3,4,3,Fraction(3)),(4,3,2,Fraction(2))]
    for p,q,k,h in cases:
        expected=formula(p,q,k,h)
        observed,counts=ehrhart_volume(p,q,k,h)
        assert observed==expected,(p,q,k,h,observed,expected)
        print(f"PASS p={p} q={q} k={k} h={h} volume={observed} Ehrhart_counts={counts}")
    print(f"PASS: {len(cases)} independent exact Ehrhart-lattice checks")

if __name__=='__main__':main()
