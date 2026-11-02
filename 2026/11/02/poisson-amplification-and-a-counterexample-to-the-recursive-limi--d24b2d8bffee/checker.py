#!/usr/bin/env python3
"""Exact finite checks for balanced-successor counts on complete n-ary trees.

Requires only Python 3 standard library. This finite checker is not an
infinite-limit proof; the latter uses Stirling and the binomial Poisson limit.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def direct_one_pair(n):
    # Four equally likely truth states for (p,q) at each leaf.
    frequencies = Counter()
    for leaves in product(range(4), repeat=n):
        np = sum((v >> 1) & 1 for v in leaves)
        nq = sum(v & 1 for v in leaves)
        frequencies[np - nq] += 1
    return frequencies[0], 4 ** n


def direct_k_pairs(n, k):
    # Independently enumerate each of the k pairs, without using the formula.
    good, total = 0, 0
    for leaves in product(range(4), repeat=n*k):
        total += 1
        ok = True
        for i in range(k):
            segment = leaves[n*i:n*(i+1)]
            np = sum((v >> 1) & 1 for v in segment)
            nq = sum(v & 1 for v in segment)
            if np != nq:
                ok = False
                break
        good += ok
    return good, total


def count_root_from_local(good, total, n):
    # DP over n disjoint child subtrees for the number of balanced children.
    distribution = [1] + [0] * n
    for i in range(n):
        nxt = [0] * (n+1)
        for j in range(i+1):
            nxt[j] += distribution[j] * (total-good)
            nxt[j+1] += distribution[j] * good
        distribution = nxt
    assert sum(distribution) == total**n
    return distribution


def claimed_probability(n, k, t):
    r = Fraction(comb(2*n,n),4**n)**k
    return sum((Fraction(comb(n,j),1)*r**j*(1-r)**(n-j)
                for j in range(t,n+1)), Fraction(0))


def test():
    for n in range(1,9):
        good,total = direct_one_pair(n)
        assert total == 4**n and good == comb(2*n,n),(n,good,total)
    for k,n in [(1,1),(1,2),(1,3),(1,4),
                (2,1),(2,2),(2,3),(2,4),
                (3,1),(3,2),(3,3)]:
        good,total = direct_k_pairs(n,k)
        expected_good = comb(2*n,n)**k
        assert total == 4**(n*k) and good == expected_good,(k,n,good)
        counts = count_root_from_local(good,total,n)
        for t in range(1,n+2):
            observed = Fraction(sum(counts[t:]), total**n)
            expected = claimed_probability(n,k,t)
            assert observed == expected, (k,n,t,observed,expected)
    # Independently brute-force entire relevant depth-2 leaf patterns in the
    # manageable (n,k) cases; parent/root truth values are irrelevant.
    for n,k in [(1,1),(2,1),(3,1),(1,2),(2,2)]:
        successes = 0
        total = 0
        for full_leaves in product(range(4), repeat=n*n*k):
            total += 1
            hit = False
            for c in range(n):
                good_child = True
                for j in range(k):
                    offs = (c*k+j)*n
                    segment = full_leaves[offs:offs+n]
                    if sum((v>>1)&1 for v in segment) != sum(v&1 for v in segment):
                        good_child = False
                        break
                if good_child:
                    hit = True
                    break
            successes += hit
        assert Fraction(successes,total) == claimed_probability(n,k,1)
    # Verify the binomial-pmf coefficient normalization and the root law.
    for n in [1,2,3,4,5,10,20,40]:
        r = Fraction(comb(2*n,n),4**n)
        assert 0 < r < 1
        for k in [1,2,3]:
            q = r**k
            assert 0 < q < 1
            assert claimed_probability(n,k,1) == 1-(1-q)**n
    print('ALL_CHECKS_OK: single-pair n<=8; k-pair exact n<=4; full-tree brute force; root threshold law')
    print('n   depth1_probability   root_k1   root_k2   root_k3')
    for n in [1,2,3,4,8,16,32,64,256,1024]:
        r=float(Fraction(comb(2*n,n),4**n))
        ps=[1-(1-r**k)**n for k in [1,2,3]]
        print(f'{n:<4d} {r:20.12g} ' + ' '.join(f'{p:.12g}' for p in ps))

if __name__ == '__main__':
    test()
