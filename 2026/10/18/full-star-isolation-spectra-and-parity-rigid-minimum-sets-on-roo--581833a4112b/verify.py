#!/usr/bin/env python3
"""Independent graph-based replay for star-isolation counts in Cartesian rook graphs."""
from math import comb, factorial, ceil
from random import Random


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted(m, n, ell):
    coeff = [0] * (m*n+1)
    for a in range(m+1):
        for b in range(n+1):
            if not (a == m or b == n or m+n-a-b <= ell+1):
                continue
            multiplier = comb(m, a)*comb(n, b)
            for t in range(m*n+1):
                spanning = sum(
                    (-1)**(a+b-i-j)*comb(a, i)*comb(b, j)*choose(i*j, t)
                    for i in range(a+1) for j in range(b+1)
                )
                coeff[t] += multiplier*spanning
    return coeff


def optimum_count(m, n, ell):
    assert 2 <= m <= n and ell >= 1
    L = m+n-ell-1
    t = min(m, max(0, ceil(L/2)))
    if t == 0:
        return t, 1
    if t == m:
        v = n**m
        if ell == n-m:
            v += m*comb(n, m)*factorial(m-1)*comb(m, 2)
        return t, v
    v = comb(m, t)*comb(n, t)*factorial(t)
    if L % 2:
        v += comb(t, 2)*factorial(t-1)*(
            comb(m, t)*comb(n, t-1)+comb(m, t-1)*comb(n, t)
        )
    return t, v


def graph_neighbors(m, n):
    out = []
    for x in range(m*n):
        i, j = divmod(x, n)
        mask = 0
        for y in range(m*n):
            if y != x and (y//n == i or y%n == j):
                mask |= 1 << y
        out.append(mask)
    return out


def direct_test(subset, mask, neighbors, ell):
    closed = subset
    for i in range(len(neighbors)):
        if subset & (1 << i):
            closed |= neighbors[i]
    residual = mask & ~closed
    return all((neighbors[i] & residual).bit_count() < ell
               for i in range(len(neighbors)) if residual & (1 << i))


def exhaust(m, n, ell, neighbors):
    N = m*n
    all_mask = (1 << N)-1
    counts = [0]*(N+1)
    for subset in range(1 << N):
        if direct_test(subset, all_mask, neighbors, ell):
            counts[subset.bit_count()] += 1
    return counts


def main():
    triples = 0
    subset_checks = 0
    for m in range(2, 5):
        for n in range(m, 5):
            neighbor = graph_neighbors(m, n)
            for ell in range(1, m+n):
                p = predicted(m, n, ell)
                b = exhaust(m, n, ell, neighbor)
                assert p == b, (m, n, ell, p, b)
                t, c = optimum_count(m, n, ell)
                assert t == next(i for i, x in enumerate(b) if x)
                assert c == b[t], (m, n, ell, c, b[t])
                triples += 1
                subset_checks += 1 << (m*n)
    assert (triples, subset_checks) == (30, 487472)

    rng = Random(517037)
    samples = 0
    for m, n in [(3, 7), (4, 8), (5, 7), (6, 6), (7, 9)]:
        neighbors = graph_neighbors(m, n)
        mask = (1 << (m*n))-1
        for ell in range(1, m+n+2):
            t, c = optimum_count(m, n, ell)
            full = predicted(m, n, ell)
            assert min(i for i, x in enumerate(full) if x) == t
            assert full[t] == c
            for _ in range(200):
                subset = rng.getrandbits(m*n)
                rows = {v//n for v in range(m*n) if subset & (1 << v)}
                cols = {v%n for v in range(m*n) if subset & (1 << v)}
                by_structure = (len(rows) == m or len(cols) == n or
                                m+n-len(rows)-len(cols) <= ell+1)
                assert direct_test(subset, mask, neighbors, ell) == by_structure
                samples += 1
    print('VERIFICATION_OK', triples, subset_checks, samples)


if __name__ == '__main__':
    main()
