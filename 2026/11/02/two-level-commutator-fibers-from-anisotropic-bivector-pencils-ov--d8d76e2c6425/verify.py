#!/usr/bin/env python3
"""Reproduce finite-field tests for the four-generator commutator construction.

Requires Python standard library only. This checks finite instances, not the
all-prime lower-bound proof supplied separately in RESULT.md.
"""
from itertools import product
from collections import Counter

PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def nonsquare(p):
    squares = {x*x % p for x in range(p)}
    return next(d for d in range(2, p) if d not in squares)


def wedge(v, w, p):
    return tuple((v[i]*w[j] - v[j]*w[i]) % p for i, j in PAIRS)


def beta(v, w, p, delta):
    x = wedge(v, w, p)
    return ((x[5]-x[0]) % p, (x[4]-delta*x[1]) % p, x[2], x[3])


def rank(rows, p):
    a = [list(map(lambda t: t % p, row)) for row in rows]
    r = 0
    for j in range(len(a[0])):
        k = next((i for i in range(r, len(a)) if a[i][j] % p), None)
        if k is None:
            continue
        a[k], a[r] = a[r], a[k]
        inv = pow(a[r][j], -1, p)
        a[r] = [(inv*x) % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j] % p:
                f = a[i][j]
                a[i] = [(x-f*y) % p for x, y in zip(a[i], a[r])]
        r += 1
    return r


def q_of_bivector(x, p):
    return (x[0]*x[5]-x[1]*x[4]+x[2]*x[3]) % p


def check(p):
    delta = nonsquare(p)
    assert all(q_of_bivector((a,b,0,0,delta*b,a),p) != 0
               for a in range(p) for b in range(p) if (a,b)!=(0,0))
    V = list(product(range(p), repeat=4))
    basis = tuple(tuple(int(i==j) for i in range(4)) for j in range(4))
    assert rank([beta(e, f, p, delta) for e in basis for f in basis], p) == 4
    for v in V[1:]:
        assert rank([beta(v, e, p, delta) for e in basis], p) == 3, (p, v)
    if p <= 5:
        fibers = Counter(beta(v, w, p, delta) for v in V for w in V)
        assert len(fibers) == p**4
        inv4 = pow(4, -1, p)
        idelta = pow(delta, -1, p)
        null, nonnull = 0, 0
        for t in product(range(p), repeat=4):
            t1,t2,c,d = t
            qbar = ((-t1*t1 + idelta*t2*t2)*inv4+c*d) % p
            if not any(t):
                target = p**5+p**4-p
            elif qbar == 0:
                null += 1
                target = p*(p*p-1)
            else:
                nonnull += 1
                target = p*(p*p-1)*(p+1)
            assert fibers[t] == target, (p,t,fibers[t],target)
        assert null == p**3-p*p+p-1
        assert nonnull == p**4-p**3+p*p-p
        print(f'p={p}: full commutator-fiber distribution verified, null_nonzero={null}, anisotropic={nonnull}; PASS')
    else:
        print(f'p={p}: nonzero contractions rank 3 and no decomposable kernel; PASS')


if __name__ == '__main__':
    for prime in (3, 5, 7, 11):
        check(prime)
    print('VERIFY_OK')
