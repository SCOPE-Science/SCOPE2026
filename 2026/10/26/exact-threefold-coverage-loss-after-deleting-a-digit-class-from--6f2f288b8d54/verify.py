#!/usr/bin/env python3
"""Finite corroboration of a threefold sumset formula for digital sets."""
from itertools import combinations_with_replacement
from math import comb


def basis(g, k):
    bound = g ** (3 * k)
    out = []
    for n in range(1, bound):
        m, ok = n, True
        position = 0
        selected = set()
        while m:
            d = m % g
            if d:
                selected.add(position % 3)
                if len(selected) > 1 or 2 in selected:
                    ok = False
                    break
            m //= g
            position += 1
        if ok:
            out.append(n)
    return out


def theoretical(g, k):
    return (2*g*g-g)**k + (3*g-2)**k - (2*g-1)**k - comb(k+2, 2)


def check(g, k):
    limit = g**(3*k)
    A = basis(g,k)
    observed = bytearray(limit)
    for a,b,c in combinations_with_replacement(A,3):
        s=a+b+c
        if s < limit:
            observed[s] = 1
    got=sum(observed)
    expect=theoretical(g,k)
    if got != expect:
        raise AssertionError((g,k,got,expect))
    print(f'base={g} blocks={k} count={got} certificate=OK')


if __name__ == '__main__':
    for g,k in ((4,1),(4,2),(4,3),(5,1),(5,2),(6,1),(6,2),(7,1),(7,2)):
        check(g,k)
    print('CERTIFICATE_OK')
