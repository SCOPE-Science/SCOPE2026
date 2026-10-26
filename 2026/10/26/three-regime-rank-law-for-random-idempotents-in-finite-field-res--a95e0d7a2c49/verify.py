#!/usr/bin/env python3
"""Independent finite-field checks of restricted-range idempotent ranks.
Run: python3 verify.py (standard library only).
"""
from itertools import product
from math import prod


def gaussian(n, r, q):
    if not (0 <= r <= n):
        return 0
    num, den = 1, 1
    for i in range(r):
        num *= q ** (n - i) - 1
        den *= q ** (r - i) - 1
    assert num % den == 0
    return num // den


def expected(k, m, q):
    return [gaussian(k, r, q) * q ** (r * (k + m - r))
            for r in range(k + 1)]


def rank(rows, p):
    if not rows:
        return 0
    a = [list(row) for row in rows]
    nrows, ncols = len(a), len(a[0])
    piv = 0
    for col in range(ncols):
        select = next((i for i in range(piv, nrows) if a[i][col] % p), None)
        if select is None:
            continue
        a[piv], a[select] = a[select], a[piv]
        inv = pow(a[piv][col], -1, p)
        a[piv] = [(x * inv) % p for x in a[piv]]
        for i in range(nrows):
            if i != piv and a[i][col]:
                factor = a[i][col]
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[piv])]
        piv += 1
        if piv == nrows:
            break
    return piv


def brute(k, m, p):
    n = k + m
    got = [0] * (k + 1)
    for entries in product(range(p), repeat=k * n):
        top = [entries[i*n:(i+1)*n] for i in range(k)]
        # The bottom m rows of the full endomorphism matrix vanish.
        # Test E^2=E by multiplying its top k rows with its k top columns.
        ok = True
        for i in range(k):
            for j in range(n):
                if sum(top[i][h] * top[h][j] for h in range(k)) % p != top[i][j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            got[rank(top, p)] += 1
    return got


def main():
    cases = [(2,0,2), (2,1,2), (2,2,2), (2,3,2), (3,0,2),
             (3,1,2), (3,2,2), (2,0,3), (2,1,3), (2,2,3),
             (1,3,3), (2,0,5), (2,1,5)]
    for k, m, p in cases:
        ex = expected(k, m, p)
        got = brute(k, m, p)
        assert ex == got, (k, m, p, got, ex)
        print('PASS', (k,m,p), tuple(got), 'total', sum(got))
    # Normalizations of the exact Gaussian formula for prime powers,
    # independent of enumeration over extension-field elements.
    for q in (2, 3, 4, 5, 7, 8, 9, 11):
        for k in range(1, 15):
            for m in (0, 1, 2*k-1, 2*k, 2*k+1, 3*k):
                e = expected(k,m,q)
                assert all(isinstance(z,int) and z>0 for z in e)
                assert e[-1] == q ** (k*m)
                assert e[0] == 1
    # Quantitative agreement with the critical-window limiting law.
    import math
    for q in (2,3,4,5):
        for t in (-5,-2,0,1,4):
            k = 55
            m = 2*k+t
            e = expected(k,m,q)
            weights = [x/e[-1] for x in reversed(e)]
            total = sum(weights)
            critical = [q**(-2*j*j-t*j) / math.prod(1-q**(-h) for h in range(1,j+1))
                        for j in range(20)]
            z = sum(critical)
            assert abs(weights[0]/total - critical[0]/z) < 1e-10
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
