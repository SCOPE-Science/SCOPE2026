#!/usr/bin/env python3
"""Independent exhaustive check of absorbing-state energy counts on circular prisms.

A configuration has two binary spins per column. A vertex flips under
minority updating precisely when at least two of its three neighbors
share its spin. Enumerates raw configurations, not symbolic encodings.
"""
from collections import Counter
from math import comb


def predicted(n):
    out = Counter()
    for k in range(n // 2 + 1):
        if (k - n) % 2 == 0:
            out[2*k] += 2*n*comb(n-k, k)//(n-k)
    if n % 2 == 0:
        out[n] += 2
    return out


def brute(n):
    out = Counter()
    for mask in range(1 << (2*n)):
        same_edges = 0
        stable = True
        for i in range(n):
            j = (i+1)%n
            for layer in (0,1):
                p = (mask >> (2*i+layer)) & 1
                near = [((mask >> (2*((i-1)%n)+layer))&1),
                        ((mask >> (2*j+layer))&1),
                        ((mask >> (2*i+1-layer))&1)]
                if sum(v == p for v in near) >= 2:
                    stable = False
                if p == ((mask >> (2*j+layer))&1):
                    same_edges += 1
            if ((mask >> (2*i))&1) == ((mask >> (2*i+1))&1):
                same_edges += 1
        if stable:
            out[same_edges] += 1
    return out


def main():
    for n in range(3, 10):
        observed = brute(n)
        expect = predicted(n)
        assert observed == expect, (n, observed, expect)
        print(f"n={n}: absorbing={sum(observed.values())}; by_monochromatic_edges={dict(sorted(observed.items()))}")
    print('ALL_EXHAUSTIVE_CHECKS_PASSED')


if __name__ == '__main__':
    main()
