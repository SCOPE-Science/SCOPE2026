#!/usr/bin/env python3
"""Independent finite-field checks of the stated reduced p-nullcone components and point counts."""
from itertools import product
from random import Random


def add(x, y, p):
    return x ^ y if p == 2 else (x + y) % p


def mul(x, y, p):
    if p == 2:
        # GF(4) represented with root t of t^2+t+1.
        z = 0
        for i in range(2):
            if (x >> i) & 1:
                for j in range(2):
                    if (y >> j) & 1:
                        z ^= 1 << (i+j)
        if z & 8:
            z ^= (1 << 3) | (1 << 2) | (1 << 1)
        if z & 4:
            z ^= 7
        return z
    return (x * y) % p


def pow_matrix(a, b, p, q, extras=None):
    n = p + 2
    mat = [[0] * n for _ in range(n)]
    for i in range(n-1):
        mat[i][i+1] = a[i]
    for i in range(n-2):
        mat[i][i+2] = b[i]
    if extras is not None:
        for i in range(n):
            for j in range(i+3, n):
                mat[i][j] = next(extras)
    power = [row[:] for row in mat]
    for _ in range(1, p):
        nex = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                v = 0
                for k in range(i+1, j):
                    v = add(v, mul(power[i][k], mat[k][j], p), p)
                nex[i][j] = v
        power = nex
    return all(v == 0 for row in power for v in row)


def union_components(a, b, p):
    for i in range(p+1):
        if a[i]:
            continue
        for j in range(i+2, p+1):
            if a[j] == 0:
                return True
    for k in range(1, p):
        if a[k] == 0 and add(mul(a[k+1],b[k-1],p),mul(a[k-1],b[k],p),p) == 0:
            return True
    return False


def expected(p,q):
    n=p+2
    return q**(n*(n-1)//2-n) * (q**n - (q-1)**p * (q*q+p*q+1))


def verify(p,q):
    assert (p,q) in [(2,2),(2,4),(3,3)]
    good = 0
    for a in product(range(q), repeat=p+1):
        for b in product(range(q), repeat=p):
            f = pow_matrix(a,b,p,q)
            g = union_components(a,b,p)
            if f != g:
                raise AssertionError((p,q,a,b,f,g))
            good += f
    n=p+2
    other=n*(n-1)//2-(2*p+1)
    total=good*q**other
    assert total == expected(p,q), (p,q,total,expected(p,q))
    print(f'p={p}, q={q}, total={total}, components={(p-1)*(p+2)//2}, VERIFIED')

if __name__=='__main__':
    for p,q in [(2,2),(2,4),(3,3)]:
        verify(p,q)
    rng=Random(27411)
    for p,q in [(2,2),(2,4),(3,3),(5,5)]:
        n=p+2
        for _ in range(400):
            a=[rng.randrange(q) for _ in range(n-1)]
            b=[rng.randrange(q) for _ in range(n-2)]
            extras=iter(rng.randrange(q) for i in range(n) for j in range(i+3,n))
            assert pow_matrix(a,b,p,q,extras)==union_components(a,b,p), (p,q,a,b)
        print(f'p={p}, q={q}, 400 randomized full-matrix checks VERIFIED')
    print('VERIFY_OK')
