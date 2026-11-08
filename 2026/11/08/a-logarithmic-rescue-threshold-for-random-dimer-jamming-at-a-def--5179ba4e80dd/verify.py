#!/usr/bin/env python3
"""Finite-state checks for uniform-edge irreversible dimer adsorption."""
from fractions import Fraction
from functools import lru_cache
from math import comb, exp, log
import random


def lumped_failure(n, m):
    assert n >= 4 and n % 2 == 0 and 0 <= m <= n - 1
    @lru_cache(None)
    def f(k, a):
        if k == 1:
            return Fraction(int(a == 0))
        denom = comb(k, 2) + a
        return sum((Fraction(comb(a, j) * comb(k - a, 2 - j), denom) * f(k - 2, a - j)
                    for j in range(3) if j <= a and 2-j <= k-a), Fraction(0))
    return f(n - 1, m)


def labeled_failure(n, m):
    assert n >= 4 and n % 2 == 0
    all_mask = (1 << n) - 1
    edges = [(u, v) for u in range(1, n) for v in range(u + 1, n)]
    edges += [(0, j) for j in range(1, m + 1)]
    @lru_cache(None)
    def go(mask):
        available = [(u, v) for u, v in edges if (mask >> u & 1) and (mask >> v & 1)]
        if not available:
            return Fraction(int(mask.bit_count() == 2))
        return sum((go(mask ^ (1 << u) ^ (1 << v)) for u,v in available), Fraction(0)) / len(available)
    return go(all_mask)


def sampled_survival(n, m, reps, seed):
    rng = random.Random(seed)
    vals = []
    for _ in range(reps):
        specials = set(rng.sample(range(1, n), m))
        a = m
        weight = 1.0
        # Uniform deletion order of core vertices; positions are the fixed sequence.
        order = rng.sample(range(1, n), n-1)
        k = n-1
        j = 0
        while k > 1:
            weight *= comb(k,2) / (comb(k,2) + a)
            a -= int(order[j] in specials) + int(order[j+1] in specials)
            j += 2
            k -= 2
        vals.append(weight if a == 0 else 0.0)
    return sum(vals)/reps


def main():
    checks=0
    for n in range(4, 13, 2):
        for m in range(n):
            a=lumped_failure(n,m)
            b=labeled_failure(n,m)
            assert a == b, (n,m,a,b)
            checks += 1
        assert lumped_failure(n,0) == 1
        assert lumped_failure(n,n-1) == 0
        checks += 2
    for n in (200, 1000, 4000):
        m=round(n/log(n))
        est=sampled_survival(n,m,2000 if n<4000 else 800,20261105+n)
        target=exp(-m*log(n)/n)
        # broad probabilistic sanity tolerance, not an infinite-size proof
        assert abs(est-target)<0.12, (n,m,est,target)
        print('sample',n,m,round(est,6),round(target,6))
        checks += 1
    print('PASS',checks,'independent exact and numerical assertions')


if __name__=='__main__':
    main()
