#!/usr/bin/env python3
"""Exact normal-form and fixed-size checks for dicyclic product/quotient counts."""
import itertools
import math
import random
from collections import Counter


def multiply(n, x, y):
    u, e = x
    v, f = y
    return ((u + (-v if e else v) + n * e * f) % (2*n), e ^ f)


def inverse(n, x):
    u, e = x
    return (((u+n) if e else (-u)) % (2*n), e)


def counts(n, A):
    products = {multiply(n, x, y) for x in A for y in A}
    quotients = {multiply(n, x, inverse(n, y)) for x in A for y in A}
    return len(products), len(quotients)


def formal_counts(k, r):
    """Pair words as affine coefficient signatures (vector, coset bit, n parity)."""
    words = []
    for i in range(k):
        coeff = [0] * k
        coeff[i] = 1
        words.append((tuple(coeff), int(i >= r), 0))

    def fm(x, y):
        a, e, c = x
        b, f, d = y
        return (tuple(i + (-j if e else j) for i,j in zip(a,b)), e ^ f, (c + (-d if e else d) + e*f) % 2)

    def fi(x):
        a, e, c = x
        return (a, 1, (c+1)%2) if e else (tuple(-i for i in a), 0, (-c)%2)

    p = {fm(x,y) for x in words for y in words}
    q = {fm(x,fi(y)) for x in words for y in words}
    return len(p), len(q)


def generic_counts(k, r):
    s = k-r
    p = k*(k+1)//2 if s == 0 else r*(r+1)//2 + 2*r*s + s*(s-1) + 1
    q = 1 + k*(k-1)
    return p, q


def main():
    symbolic = 0
    for k in range(2, 17):
        for r in range(k+1):
            assert formal_counts(k,r) == generic_counts(k,r), (k,r)
            symbolic += 1

    # Independently reproduce published small-group counts, including k=6.
    published_n5 = {
        2: (80,0), 3: (400,200), 4: (1380,2080),
        5: (3840,7160), 6: (9520,19920),
    }
    small_cases = 0
    published_checks = 0
    for n in range(2, 6):
        G = [(i,e) for e in (0,1) for i in range(2*n)]
        for k in range(2, min(7,len(G)+1)):
            signs = Counter()
            for A in itertools.combinations(G, k):
                p, q = counts(n, A)
                signs[(p>q)-(p<q)] += 1
                small_cases += 1
            assert sum(signs.values()) == math.comb(4*n,k)
            if n == 5 and k in published_n5:
                assert (signs[1],signs[-1]) == published_n5[k], (n,k,signs)
                published_checks += 1

    # Sparse samples: actual products match predicted generic sizes except
    # when an accidental modular collision occurs (those are detected, not assumed absent).
    rng = random.Random(20261015)
    noncollision_matches = 0
    deviations = 0
    n = 300003
    for k in range(2, 11):
        for _ in range(800):
            A = [((t%(2*n)), t//(2*n)) for t in rng.sample(range(4*n),k)]
            r = sum(1 for x in A if x[1] == 0)
            actual = counts(n,A)
            expected = generic_counts(k,r)
            if actual == expected:
                noncollision_matches += 1
            else:
                deviations += 1
                assert actual[0] <= expected[0] and actual[1] <= expected[1]

    assert math.comb(6,1)+math.comb(6,2) == 21
    assert sum(math.comb(6,r) for r in range(4,7)) == 22
    for k in range(6, 40):
        positives = k + math.comb(k,2)
        negatives = sum(math.comb(k,r) for r in range(4,k+1))
        assert negatives > positives
    print('VERIFY_OK symbolic_profiles=%d exhaustive_sets=%d published_table_checks=%d sparse_exact_matches=%d collision_examples=%d' %
          (symbolic, small_cases, published_checks, noncollision_matches, deviations))


if __name__ == '__main__':
    main()
