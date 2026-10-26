#!/usr/bin/env python3
"""Direct finite verification of the three-marker cyclic Abelian-cube phase census.
Standard-library-only; indexed phase positions, not distinct rotated strings.
"""
from collections import Counter
from itertools import combinations
from math import comb


def observed(p, positions):
    n = 3 * p
    ones = set(positions)
    good = 0
    for s in range(n):
        counts = [0, 0, 0]
        for pos in ones:
            counts[((pos - s) % n) // p] += 1
        if counts == [1, 1, 1]:
            good += 1
    return good


def claimed(p, gaps):
    return 3 * max(0, min(min(gaps), 2 * p - max(gaps)))


def necklace_key(gaps):
    a, b, c = gaps
    return min((a, b, c), (b, c, a), (c, a, b))


def distribution(p):
    n = 3 * p
    classes = {}
    for a in range(1, n-1):
        for b in range(1, n-a):
            c = n-a-b
            key = necklace_key((a,b,c))
            classes[key] = claimed(p, (a,b,c)) // 3
    return Counter(classes.values())


def expected(p):
    d = {0: p * (p-1)//2}
    d.update({k: 2*(p-k) for k in range(1,p)})
    d[p] = 1
    return Counter({k:v for k,v in d.items() if v})


def run():
    checked = 0
    for p in range(1, 13):
        n=3*p
        for i,j,k in combinations(range(n),3):
            gaps=(j-i,k-j,n-k+i)
            o=observed(p,(i,j,k))
            t=claimed(p,gaps)
            assert o==t, (p, (i,j,k), gaps, o, t)
            checked+=1
        assert distribution(p) == expected(p), (p,distribution(p),expected(p))
        print('p=',p,'n=',n,'direct supports=',comb(n,3),'necklaces=',sum(expected(p).values()))
    for p in range(13, 121):
        d=distribution(p)
        assert d==expected(p),(p,d,expected(p))
        assert sum(d.values()) == (3*p*p-3*p+2)//2
    print('VERIFIED',checked,'direct labeled weight-three supports, 120 entire necklace distributions')

if __name__ == '__main__':
    run()
