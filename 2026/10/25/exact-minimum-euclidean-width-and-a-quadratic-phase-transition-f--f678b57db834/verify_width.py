#!/usr/bin/env python3
"""Finite regression tests for a proved exact minimum-width formula.

Requires only the Python standard library. Infinite-dimensional-family
correctness rests on the analytic argument in RESULT.md, not these tests.
"""
import math
import random
from fractions import Fraction


def width_of_vector(v, rank):
    w = sorted(v)
    return math.fsum(w[-rank:]) - math.fsum(w[:rank])


def ray(n, j):
    return [-(n-j)/n]*j + [j/n]*(n-j)


def candidates(n, k):
    r = min(k, n-k)
    a = math.sqrt(n/(n-1))
    h = n//2
    b = r*math.sqrt(n/(h*(n-h)))
    return a, b


def check():
    # Integer-arithmetic verification of the exact candidate minimum
    # and the quadratic transition, for a wide finite range.
    n_cases = 0
    for n in range(5, 225):
        for r in range(2, n//2+1):
            ratios_squared = [Fraction(n*min(r,j,n-j)**2, j*(n-j))
                              for j in range(1, n)]
            target = min(Fraction(n,n-1),
                         Fraction(n*r*r,(n//2)*((n+1)//2)))
            assert min(ratios_squared) == target, (n,r)
            A = Fraction(n,n-1)
            B = Fraction(n*r*r,(n//2)*((n+1)//2))
            pivot = 4*r*r-1
            if n<pivot: assert A<B,(n,r)
            if n==pivot: assert A==B,(n,r)
            if n>pivot: assert B<A,(n,r)
            n_cases += 1

    # Check exact ray normalization and support width directly.
    ray_cases = 0
    for n in range(5,45):
        for rank in range(2,n-1):
            for j in range(1,n):
                v=ray(n,j)
                actual=width_of_vector(v, rank)
                expected=min(rank,n-rank,j,n-j)
                assert abs(actual-expected)<1e-11,(n,rank,j,actual,expected)
                assert abs(math.fsum(v))<1e-11
                assert abs(math.fsum(x*x for x in v)-j*(n-j)/n)<1e-10
                ray_cases+=1

    # Test the universal inequality for random centered directions,
    # including dimensions on both sides of the transition.
    rng=random.Random(20231022)
    random_cases=0
    for n in [5,6,7,8,10,14,15,16,17,25,34,35,36,40,49,60]:
        for k in range(2,n-1):
            a,b=candidates(n,k)
            floor_width=min(a,b)
            for _ in range(200):
                raw=[rng.gauss(0,1) for _ in range(n)]
                avg=math.fsum(raw)/n
                v=[x-avg for x in raw]
                norm=math.sqrt(math.fsum(x*x for x in v))
                actual=width_of_vector(v,k)/norm
                assert actual+3e-12>=floor_width,(n,k,actual,floor_width)
                random_cases+=1
    print('OK: %d exact rational candidate/phase cases, %d explicit two-level rays, %d random directions' % (n_cases, ray_cases, random_cases))
    print('Threshold examples:')
    for r in [2,3,4]:
        for n in [4*r*r-2, 4*r*r-1, 4*r*r]:
            a,b=candidates(n,r)
            print('r=%d, n=%d, facet=%.12f, balanced=%.12f, optimum=%.12f' % (r,n,a,b,min(a,b)))

if __name__=='__main__':
    check()
