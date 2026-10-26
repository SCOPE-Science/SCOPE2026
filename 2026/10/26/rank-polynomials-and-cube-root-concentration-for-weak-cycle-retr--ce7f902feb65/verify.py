#!/usr/bin/env python3
"""Finite enumeration checks for weak-cycle retraction rank polynomials."""
from collections import Counter
from itertools import product

def via_direct_maps(n):
    out = Counter()
    for first in range(n):
        for increments in product((-1, 0, 1), repeat=n-1):
            f = [first]
            for d in increments:
                f.append((f[-1] + d) % n)
            if (f[-1]-first) % n not in (0, 1, n-1):
                continue
            if any(f[f[i]] != f[i] for i in range(n)):
                continue
            out[len(set(f))] += 1
    return out

def via_arc_walks(n):
    out = Counter({1:n, n:1})
    for ell in range(1,n//2 + 1):
        w = [0]*(ell+1)
        w[ell] = 1
        for _ in range(n-ell):
            w = [w[i] + (w[i-1] if i else 0) +
                 (w[i+1] if i < ell else 0) for i in range(ell+1)]
        out[ell+1] = n*w[0]
    return out

def main():
    for n in range(3,10):
        a = via_direct_maps(n)
        b = via_arc_walks(n)
        assert a == b, (n,a,b)
        assert b[2] == n*2**(n-2)
        ell = n//2
        assert b[ell+1] == (n if n%2 == 0 else n*(n+1)//2), n
    for n in range(10,61):
        b = via_arc_walks(n)
        assert b[2] == n*2**(n-2)
        ell = n//2
        assert b[ell+1] == (n if n%2 == 0 else n*(n+1)//2), n
        assert b[n] == 1 and b[1] == n
    print('VERIFY_OK: weak-cycle idempotent ranks n=3..9 exhaustive, boundaries n=3..60')

if __name__ == '__main__':
    main()
