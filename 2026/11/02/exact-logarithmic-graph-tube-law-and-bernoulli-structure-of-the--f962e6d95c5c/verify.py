#!/usr/bin/env python3
"""Exact branch/cylinder tests and finite-scale checks for a geometric full-branch map.

The infinite Minkowski-tube asymptotic is proved analytically in RESULT.md;
finite computation does not certify an infinite limit.
"""
from fractions import Fraction as Q
from itertools import product
from math import log


def inverse(t, side, i, k):
    d=(1-k)/2
    s=(1-k**i)/2
    length=d*k**i
    return s+length*t if side == 'L' else 1-s-length*t


def forward(x,k):
    d=(1-k)/2
    s=Q(0)
    for i in range(160):
        ell=d*k**i
        if s < x < s+ell:
            return (x-s)/ell,('L',i)
        if 1-s-ell < x < 1-s:
            return (1-s-x)/ell,('R',i)
        s+=ell
    raise AssertionError('A tested cylinder midpoint should lie in a finite open branch')


def test_exact():
    count=0
    for k in (Q(1,2),Q(1,3),Q(2,3),Q(3,4)):
        d=(1-k)/2
        assert 2*d/(1-k)==1
        count+=1
        for i in range(10):
            s=(1-k**i)/2
            ell=d*k**i
            assert (1-k**(i+1))/2-s==ell
            for side in ('L','R'):
                for t in (Q(1,7), Q(1,2), Q(5,7)):
                    x=inverse(t,side,i,k)
                    y,symbol=forward(x,k)
                    assert y==t and symbol==(side,i)
                    count+=1
        # Codes are i.i.d.: nested inverse branch images have product lengths.
        alphabet=[('L',0),('R',0),('L',1),('R',1),('L',2),('R',2)]
        for depth in (1,2,3):
            for code in product(alphabet,repeat=depth):
                y=Q(1,2)
                for side,i in reversed(code):
                    y=inverse(y,side,i,k)
                x=y
                for symbol in code:
                    y,got=forward(y,k)
                    assert got==symbol
                count+=1
    return count


def probe_horizontal(eps,k,samples=801):
    # A horizontal slice of the Euclidean epsilon-neighborhood contains the
    # horizontal epsilon intervals around graph points at precisely that height.
    d=(1-k)/2
    n=max(16,int(log(eps*1e-7/d)/log(k))+2)
    area=0.
    for j in range(samples):
        y=(j+.5)/samples
        s=0.; pts=[.5]
        for i in range(n):
            ell=d*k**i
            pts.extend([s+ell*y,1-s-ell*y])
            s+=ell
        pts.sort()
        a=pts[0]-eps;b=pts[0]+eps
        width=0.
        for p in pts[1:]:
            if p-eps>b:
                width+=b-a
                a=p-eps;b=p+eps
            else:
                b=max(b,p+eps)
        width+=b-a
        area+=width
    return area/samples


if __name__ == '__main__':
    print('Exact branch and inverse-cylinder comparisons:',test_exact())
    for k in (1/2,1/3):
        target=4/log(1/k)
        print('k',k,'predicted logarithmic coefficient',target)
        values=[]
        for e in (1e-4,1e-5,1e-6):
            a=probe_horizontal(e,k,301)
            ratio=a/(e*log(1/e))
            values.append(ratio)
            print('  scale',e,'horizontal-width ratio',ratio)
        # A finite-scale diagnostic, not a proof of convergence.
        assert all(0<r<target for r in values)
        assert values[0]<values[1]<values[2]
    print('CHECKS PASSED')
