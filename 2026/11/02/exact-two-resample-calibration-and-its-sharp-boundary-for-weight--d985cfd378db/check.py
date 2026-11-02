#!/usr/bin/env python3
"""Exact arithmetic enumeration of an iid-transformation rank calibration identity.

Usage: python3 check.py
All calculations use integers or fractions; no external packages are required.
"""
from fractions import Fraction
from itertools import permutations, product
from math import factorial

G = tuple(range(4))  # XOR group: two commuting, disjoint transpositions

def law(weights, ordering, M):
    """P-value numerator distribution for a uniform group orbit.

    Each input weight is an integer; no normalization until the end.
    ordering enumerates transformed states in decreasing score order.
    """
    score = {a: len(G) - i for i, a in enumerate(ordering)}
    ans = [0] * (M + 1)
    den = len(G) * sum(weights) ** (M + 1)
    for x in G:
        sx = score[x]
        for draws in product(G, repeat=M + 1):
            w = 1
            for a in draws:
                w *= weights[a]
            if not w:
                continue
            a0 = draws[0]
            hit = sum(score[x ^ am ^ a0] >= sx for am in draws[1:])
            ans[hit] += w
    return tuple(Fraction(a, den) for a in ans)

def moment_law(weights):
    total = sum(weights)
    s2 = sum(Fraction(a, total) ** 2 for a in weights)
    s3 = sum(Fraction(a, total) ** 3 for a in weights)
    return (Fraction(1,3) - s2/2 + s3/6,
            Fraction(1,3) - s3/3,
            Fraction(1,3) + s2/2 + s3/6)

def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for first in range(n+1):
            for tail in compositions(n-first,k-1):
                yield (first,) + tail

def main():
    checks = 0
    orders = tuple(permutations(G))
    for weights in compositions(8, 4):
        expect = moment_law(weights)
        for order in orders:
            assert law(weights, order, 2) == expect, (weights, order)
            checks += 1
    # This M=3 witness has the identical nonuniform q for both score maps.
    weights=(4,2,1,1)
    a=law(weights,(0,1,2,3),3)
    b=law(weights,(0,2,1,3),3)
    assert a == (Fraction(63,512),Fraction(3,16),Fraction(123,512),Fraction(115,256)), a
    assert b == (Fraction(981,8192),Fraction(1617,8192),Fraction(1887,8192),Fraction(3707,8192)), b
    assert a != b
    checks += 3
    # Balancing a pair cannot decrease either rejection CDF.
    for weights in compositions(8,4):
        old=moment_law(weights)
        for i in G:
            for j in G:
                if weights[i]-weights[j]>=2:
                    new=list(weights)
                    new[i]-=1;new[j]+=1
                    fresh=moment_law(new)
                    assert fresh[0]>=old[0]
                    assert sum(fresh[:2])>=sum(old[:2])
                    checks+=2
    print(f'PASS: {checks} exact rational assertions; M=3 contrasting laws:',a,b)

if __name__ == '__main__':
    main()
