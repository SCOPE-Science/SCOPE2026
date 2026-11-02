#!/usr/bin/env python3
"""Direct finite checks of the stated prime-support valuation formula."""
from math import gcd
from itertools import combinations


def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def val(n, p):
    if n == 0:
        raise ValueError('valuation of zero')
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def phi(m):
    v = m
    for p in factor(m):
        v = v // p * (p - 1)
    return v


def order(m):
    t = phi(m)
    for p in factor(t):
        while t % p == 0 and pow(2, t//p, m) == 1:
            t //= p
    assert pow(2, t, m) == 1
    return t


def local(p):
    t = order(p)
    h = 1
    while pow(2, t, p**(h+1)) == 1:
        h += 1
    return t, h


def predicted(n):
    f = factor(n)
    L = {p: local(p) for p in f}
    g = 1
    thresholds = {}
    for p,e in f.items():
        H = max([0] + [val(L[q][0],p) for q in f if q != p])
        threshold = L[p][1] + H
        thresholds[p] = threshold
        g *= p**min(e, max(0, threshold-e))
    return g, thresholds


def direct_gcd(n):
    ell = order(n)
    residue = pow(2, ell, n*n)
    assert residue % n == 1
    return gcd(n, (residue-1)//n)


def run():
    tested = 0
    bad = 0
    for n in range(3, 15002, 2):
        predicted_gcd, thresholds = predicted(n)
        actual = direct_gcd(n)
        assert predicted_gcd == actual, (n, predicted_gcd, actual)
        ell = order(n)
        for p, e in factor(n).items():
            expected_v = max(e, thresholds[p])
            assert pow(2, ell, p**expected_v) == 1
            assert pow(2, ell, p**(expected_v+1)) != 1, (n, p, expected_v)
        tested += 1
        if actual > 1:
            bad += 1
    example_supports = [(3,7),(3,13),(3,7,1093),(1093,), (3511,), (5,11,13)]
    for P in example_supports:
        f = {}
        for p in P:
            t,h = local(p)
            f[p] = h+max([0] + [val(local(q)[0],p) for q in P if q != p])
        n = 1
        for p,e in f.items():
            n *= p**e
        assert predicted(n)[0] == direct_gcd(n) == 1, (P,n)
        for p in P:
            if f[p]>1:
                m=n//p
                assert predicted(m)[0] == direct_gcd(m)>1,(P,m)
    assert predicted(21)[0] == 3 and predicted(63)[0]==1
    assert predicted(1093)[0] == 1093 and predicted(1093**2)[0] == 1
    print(f'VERIFY_OK odd_n={tested} wieferich_cases={bad} supports={len(example_supports)}')
    print('EXAMPLES 21=defect3 63=non-Wieferich 1093=defect1093 1093^2=non-Wieferich')


if __name__ == '__main__':
    run()
