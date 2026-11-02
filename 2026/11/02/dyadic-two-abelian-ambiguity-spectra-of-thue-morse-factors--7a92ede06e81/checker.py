#!/usr/bin/env python3
"""Exact finite checks of dyadic two-Abelian class-size formulas.

Usage: python checker.py [max_k]
Only the Python standard library is needed. This is finite corroboration,
not a replacement for the proof for all dyadic lengths.
"""
import sys
from collections import Counter


def morphism(s):
    return ''.join('01' if c == '0' else '10' for c in s)


def iterate(k):
    s = '0'
    for _ in range(k):
        s = morphism(s)
    return s


def signature(w):
    return (w[0], w[-1], sum(w[i:i+2] == '00' for i in range(len(w)-1)),
            sum(w[i:i+2] == '11' for i in range(len(w)-1)))


def expected(k):
    N = 1 << k
    d = {}
    if k % 2 == 0:
        H = (N + 2) // 6
        J = (N - 1) // 3
        for ep in ('00', '11'):
            d[(ep[0], ep[1], H-1, H)] = N//2 if ep == '11' else J
            d[(ep[0], ep[1], H, H-1)] = N//2 if ep == '00' else J
        for ep in ('01', '10'):
            d[(ep[0], ep[1], H, H)] = J
            d[(ep[0], ep[1], H-1, H-1)] = J
    else:
        H = (N - 2) // 6
        for ep in ('00', '11'):
            a, b = ep
            d[(a, b, H-1, H) if ep == '00' else (a, b, H, H-1)] = H
            d[(a, b, H, H+1) if ep == '00' else (a, b, H+1, H)] = H
            d[(a, b, H+1, H) if ep == '00' else (a, b, H, H+1)] = N//2
        for ep in ('01', '10'):
            d[(ep[0], ep[1], H, H)] = N//2 + H
    assert len(d) == 8 and sum(d.values()) == 3*N-2
    return d


def test(k):
    N = 1 << k
    # The first eight level-k substitution blocks already include all four
    # two-letter adjacent block types; this segment therefore contains every
    # length-N factor and is an exact finite input, not a sampling heuristic.
    full = iterate(k+3)
    assert len(full) == 8*N
    factors = {full[i:i+N] for i in range(len(full)-N+1)}
    assert all(len(f) == N for f in factors)
    direct = Counter(map(signature, factors))
    desired = Counter(expected(k))
    assert direct == desired, (k, direct, desired)
    # Independent generative description of all factors using block cuts.
    P = iterate(k)
    Q = ''.join('1' if x == '0' else '0' for x in P)
    generated = {u[r:]+v[:r] for u in (P, Q) for v in (P, Q)
                 for r in range(N)}
    assert factors == generated
    same = {P[r:]+P[:r] for r in range(N)}
    mixed = {u[r:]+v[:r] for u,v in ((P,Q),(Q,P))
             for r in range(1,N)}
    assert len(same) == N and len(mixed) == 2*(N-1)
    assert same.isdisjoint(mixed)
    assert same | mixed == factors
    return N, len(factors), sorted(Counter(direct.values()).items())


def main():
    limit = int(sys.argv[1]) if len(sys.argv)>1 else 10
    assert 2 <= limit <= 12
    for k in range(2, limit+1):
        print('k=%d N=%d factors=%d size_frequencies=%s PASS' %
              ((k,) + test(k)))
    print('All direct checks passed through k=%d.' % limit)

if __name__ == '__main__':
    main()
