#!/usr/bin/env python3
"""Independent finite exact-arithmetic checks for delayed-tent phase permutation.

Mathematical statements about infinitely many dimensions/slope parameters
are proved analytically in RESULT.md; this program checks selected finite cases.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd


def R(a, p):
    return a[1:] + ((a[0] + 1) % p,)


def expected_fixed(k, d, p):
    g = gcd(k, d)
    return p ** g if (k // g) % p == 0 else 0


def mobius(n):
    if n == 1:
        return 1
    primes = 0
    t = n
    p = 2
    while p*p <= t:
        if t % p == 0:
            primes += 1
            t //= p
            if t % p == 0:
                return 0
            while t % p == 0:
                t //= p
        p += 1
    if t > 1:
        primes += 1
    return -1 if primes % 2 else 1


def divisors(n):
    return [k for k in range(1, n + 1) if n % k == 0]


def check_case(d, p):
    states = list(product(range(p), repeat=d))
    expected = {a: R(a, p) for a in states}
    assert set(expected.values()) == set(states)
    fixed_comparisons = 0
    for k in range(d * p + 1):
        count = 0
        for a in states:
            b = a
            for _ in range(k):
                b = expected[b]
            count += int(b == a)
        assert count == expected_fixed(k, d, p), (d,p,k,count,expected_fixed(k,d,p))
        fixed_comparisons += 1
    unvisited = set(states)
    cycle_hist = Counter()
    while unvisited:
        a = next(iter(unvisited))
        b = a
        length = 0
        while True:
            assert b in unvisited
            unvisited.remove(b)
            b = expected[b]
            length += 1
            if b == a:
                break
        assert d * p % length == 0
        cycle_hist[length] += 1
    burnside = sum(expected_fixed(k, d, p) for k in range(d*p))
    assert burnside % (d*p) == 0
    assert burnside // (d*p) == sum(cycle_hist.values())
    for ell in divisors(d*p):
        total = sum(mobius(ell // m) * expected_fixed(m,d,p) for m in divisors(ell))
        assert total % ell == 0
        assert total // ell == cycle_hist[ell], (d,p,ell,total,cycle_hist[ell])
    assert sum(ell*n for ell,n in cycle_hist.items()) == p**d
    return fixed_comparisons, dict(sorted(cycle_hist.items()))


def tent(x, beta):
    return 1 - beta*abs(x)


def interval_image(interval, beta):
    lo, hi = interval
    vals = [tent(lo,beta),tent(hi,beta)]
    if lo <= 0 <= hi:
        vals.append(Fraction(1))
    return min(vals), max(vals)


def check_bands_11_10():
    beta = Fraction(11,10)
    r = [Fraction(0)]
    for _ in range(8):
        r.append(tent(r[-1],beta))
    intervals = [tuple(sorted((r[2],r[6]))),
                 tuple(sorted((r[8],r[4]))),
                 tuple(sorted((r[3],r[7]))),
                 tuple(sorted((r[5],r[1])))]
    assert all(a<b for a,b in intervals)
    assert all(intervals[i][1]<intervals[j][0] or intervals[j][1]<intervals[i][0]
               for i in range(4) for j in range(i+1,4))
    for source, target in ((0,2),(2,1),(1,3),(3,0)):
        assert interval_image(intervals[source],beta) == intervals[target]
    return r, intervals


def main():
    cases = [(d,p) for d in range(2,7) for p in (1,2,4,8)
             if p**d <= 4096]
    aggregate = 0
    for d,p in cases:
        checks,hist = check_case(d,p)
        aggregate += checks
        print(f'd={d} p={p}: cyclic sectors by exact length = {hist}; fixed-count tests = {checks}')
    r, intervals = check_bands_11_10()
    print('beta=11/10: exact critical-orbit rational points r[1] through r[8] =')
    print(' ',[str(x) for x in r[1:]])
    print('beta=11/10: exact four disjoint intervals =')
    for i,ab in enumerate(intervals):
        print(f'  I{i} = {ab}')
    print('PASS: exact affine fixed counts, Burnside, Möbius cycle histogram and beta=11/10 band images')
    print(f'{len(cases)} exhaustive parameter pairs; {aggregate} distinct power/fixed-count comparisons')


if __name__ == '__main__':
    main()
