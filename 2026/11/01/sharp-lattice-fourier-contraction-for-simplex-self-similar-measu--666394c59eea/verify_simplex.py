#!/usr/bin/env python3
"""Reproduce finite numerical tests for simplex Fourier multipliers.

All infinite-parameter and equality statements are proved in RESULT.md;
this program tests bounded examples only.
"""
import cmath
import itertools
import math


def mask(d, b, frequency, scale):
    return abs(1 + sum(cmath.exp(-2j * math.pi * n / (b ** scale))
                       for n in frequency)) / (d + 1)


def bound(d, b, scale):
    return math.sqrt(d*d + 1 + 2*d*math.cos(2*math.pi / (b**scale))) / (d+1)


def coefficient(d, b, frequency, depth=45):
    return math.prod(mask(d, b, frequency, j) for j in range(1, depth+1))


def predicted(d, b, box):
    result=set()
    scale=1
    while scale <= box:
        for sign in (-1, 1):
            for i in range(d):
                v=[0]*d
                v[i]=sign*scale
                result.add(tuple(v))
            result.add((sign*scale,)*d)
        scale*=b
    return result


def reduced(frequency, base):
    v=tuple(frequency)
    while all(x % base == 0 for x in v):
        v=tuple(x // base for x in v)
    return v


def main():
    assertions=0
    for d in (2, 3):
        for b in (2, 3, 4):
            c=math.prod(bound(d,b,j) for j in range(1,46))
            assert 0 < c < 1
            assertions+=1
            winners=[]
            for v in itertools.product(range(-5,6),repeat=d):
                if not any(v):
                    continue
                # Levelwise proof certificate tested numerically, independently
                # of the infinite-product coefficient comparison.
                for j in range(1,6):
                    assert mask(d,b,reduced(v,b),j) <= bound(d,b,j) + 1e-11
                    assertions+=1
                f=coefficient(d,b,v)
                assert f <= c + 1e-10
                assertions+=1
                if abs(f-c)<1e-10:
                    winners.append(v)
            assert set(winners)==predicted(d,b,5)
            assertions+=1
            print('dimension',d,'base',b,'constant',format(c,'.16g'),
                  'maximizers-in-box',len(winners))
    print('SIMPLEX_FOURIER_FINITE_CHECK_OK',assertions)


if __name__ == '__main__':
    main()
