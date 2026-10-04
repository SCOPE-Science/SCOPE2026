#!/usr/bin/env python3
"""Finite checks for the Choi synchronizer-map enumeration."""
from itertools import product


def elems(p, m):
    return list(product(range(p), repeat=m))


def plus_i(x, i, p):
    y = list(x)
    y[0] = (y[0] + i) % p
    return tuple(y)


def P(p, r):
    return (r - 1) ** p + ((-1) ** p) * (r - 1)


def N(p, m):
    q = p ** m
    return P(p, q - 1) ** (q // p) * P(p, q - 2) ** (q * (q - 1) // p)


def construct(p, m):
    E = elems(p, m)
    psi = {}
    for a0 in E:
        if a0[0] != 0:
            continue
        for b0 in E:
            # One representative per translation orbit has first coordinate of a0 equal to zero.
            L = [x for x in E if x != a0 and x != b0]
            if p == 2:
                if len(L) < 2:
                    raise ValueError('no two-color orbit choice')
                z = [L[0], L[1]]
            else:
                if len(L) < 3:
                    raise ValueError('no three-color orbit choice')
                z = [L[i % 2] for i in range(p - 1)] + [L[2]]
            for i in range(p):
                pair = (plus_i(a0, i, p), plus_i(b0, i, p))
                psi[pair] = plus_i(z[i], i, p)
    if len(psi) != len(E) ** 2:
        raise AssertionError('orbit partition incomplete')
    return E, psi


def check(p, m):
    E, psi = construct(p, m)
    one = (1,) + (0,) * (m - 1)
    for a in E:
        for b in E:
            y = psi[(a, b)]
            assert y != a and y != b
            ap = plus_i(a, 1, p)
            bp = plus_i(b, 1, p)
            yp = plus_i(y, 1, p)
            assert psi[(ap, bp)] != yp


def brute_small(q):
    # Prime fields q=2 or q=3 only.
    domain = [(a, b) for a in range(q) for b in range(q)]
    allowed = [tuple(x for x in range(q) if x not in (a, b)) for a, b in domain]
    if any(not x for x in allowed):
        return 0
    count = 0
    for vals in product(*allowed):
        f = dict(zip(domain, vals))
        ok = True
        for a, b in domain:
            if f[((a + 1) % q, (b + 1) % q)] == (f[(a, b)] + 1) % q:
                ok = False
                break
        count += ok
    return count


assert brute_small(2) == 0
assert brute_small(3) == 0
assert N(2, 1) == 0
assert N(3, 1) == 0
assert N(2, 2) == 2304
for p, m in [(2, 2), (5, 1), (2, 3), (3, 2), (5, 2)]:
    check(p, m)
    assert N(p, m) > 0
print('VERIFY_OK')
