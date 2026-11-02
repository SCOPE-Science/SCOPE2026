#!/usr/bin/env python3
"""Independent exact incidence enumeration, mode tests, and numerical asymptotic checks."""
from math import comb, log, exp, sqrt, pi
from itertools import combinations


def count_transversal(n, r):
    total = 0
    for cuts in combinations(range(1, n), r-1):
        bounds = (0,) + cuts + (n,)
        for images in combinations(range(1, n+1), r):
            if all(bounds[i] < images[i] <= bounds[i+1] for i in range(r)):
                total += 1
    return total


def main():
    for n in range(1, 12):
        for r in range(1, n+1):
            actual = count_transversal(n,r)
            expected = comb(n+r-1, 2*r-1)
            assert actual == expected, (n,r,actual,expected)
    print('INCIDENCE_OK n<=11')
    for n in range(1, 151):
        weights=[comb(n+r-1, 2*r-1)**2 for r in range(1,n+1)]
        maxima=[r for r,w in enumerate(weights,1) if w==max(weights)]
        peak=(sqrt(1+5*n*n)-1)/5
        # Integer comparisons avoid floating-point tie mistakes.
        modes=[r for r in range(1,n+1) if all(weights[r-1]>=q for q in weights)]
        if n==72:
            assert modes==[32,33]
        else:
            assert len(modes)==1
    print('MODES_OK n<=150; unique tie n=72 at ranks 32,33')
    phi=(1+sqrt(5))/2
    for n in (50,100,200,400):
        total=sum(comb(n+r-1, 2*r-1)**2 for r in range(1,n+1))
        log_approx=4*n*log(phi)-log(2*sqrt(2*pi)*5**.25)-0.5*log(n)
        ratio=exp(log(total)-log_approx)
        assert abs(ratio-1)<0.02, (n,ratio)
        print(f'n={n} total_over_asymptotic={ratio:.9f}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
