#!/usr/bin/env python3
"""Finite checks for power domination on tensor products of complete graphs.

Run with: python3 verify_power_direct_product.py
Only finite cases are tested; the theorem requires its separate proof.
"""
from collections import Counter
from itertools import combinations
from math import comb
from random import Random


def neighbors(m, n):
    return [sum(1 << (k*n+l) for k in range(m) for l in range(n)
                if k != i and l != j)
            for i in range(m) for j in range(n)]


def power_dominates(mask, adj, full):
    observed = mask
    for v, nb in enumerate(adj):
        if (mask >> v) & 1:
            observed |= nb
    while observed != full:
        new = observed
        x = observed
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            unknown = adj[v] & ~observed
            if unknown and not (unknown & (unknown - 1)):
                new |= unknown
            x ^= bit
        if new == observed:
            return False
        observed = new
    return True


def predicted(mask, m, n):
    if not mask:
        return False
    rows, cols = set(), set()
    t = mask
    while t:
        bit = t & -t
        i = bit.bit_length() - 1
        rows.add(i // n)
        cols.add(i % n)
        t ^= bit
    if len(rows) >= 2 and len(cols) >= 2:
        return True
    if len(rows) == 1:
        return mask.bit_count() >= n-2
    return mask.bit_count() >= m-2


def predicted_counts(m, n):
    N = m*n
    ans = [comb(N,k) for k in range(N+1)]
    ans[0] = 0
    ans[1] = 0
    for k in range(2,n-2):
        ans[k] -= m * comb(n,k)
    for k in range(2,m-2):
        ans[k] -= n * comb(m,k)
    return ans


def run():
    exhaustive_profiles = [(4,4), (4,5), (5,4)]
    for m,n in exhaustive_profiles:
        adj = neighbors(m,n)
        full = (1<<(m*n))-1
        counts = [0]*(m*n+1)
        for mask in range(1 << (m*n)):
            actual = power_dominates(mask, adj, full)
            expected = predicted(mask,m,n)
            assert actual == expected, (m,n,mask,actual,expected)
            if actual:
                counts[mask.bit_count()] += 1
        assert counts == predicted_counts(m,n), (m,n,counts,predicted_counts(m,n))
        print('EXHAUSTIVE_OK',m,n,'subsets',1<<(m*n),'PDS',sum(counts),'minimum_count',counts[2])

    rng = Random(1729)
    total = 0
    for m,n in [(4,6),(4,7),(5,5),(5,6),(6,6),(6,8),(7,9),(9,7),(10,10)]:
        adj = neighbors(m,n)
        full = (1<<(m*n))-1
        for i in range(2500):
            # Mix sparse, intermediate, and dense sets.
            k = [rng.randrange(m*n+1),rng.randrange(min(m*n,8)+1),
                 rng.randrange(max(1,m*n-12),m*n+1)][i%3]
            selected = rng.sample(range(m*n), k)
            mask = sum(1<<v for v in selected)
            actual = power_dominates(mask,adj,full)
            assert actual == predicted(mask,m,n), (m,n,mask)
            total += 1
        # Check every 2-vertex selection independently.
        for i,j in combinations(range(m*n),2):
            mask=(1<<i)|(1<<j)
            assert power_dominates(mask,adj,full)==predicted(mask,m,n), (m,n,i,j)
            total += 1
        coeff = predicted_counts(m,n)
        assert coeff[2] == (2*comb(m,2)*comb(n,2) +
                            (m*comb(n,2) if n==4 else 0)+
                            (n*comb(m,2) if m==4 else 0))
        last_fail = max(i for i,c in enumerate(coeff) if c < comb(m*n,i))
        assert last_fail == max(m,n)-3
        print('SAMPLED_AND_PAIRS_OK',m,n,'last_nonuniversal_degree',last_fail,
              'minimum_count',coeff[2])
    print('VERIFICATION_OK','additional_cases',total)

if __name__ == '__main__':
    run()
