"""Exact enumerative checks of cyclic/terminal-point formulas for uniform mappings.

Run: python3 verify.py
Uses only the Python standard library; no external source material.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def falling(n, k):
    a = 1
    for j in range(k):
        a *= n - j
    return a


def cycle_count(f):
    n = len(f)
    done = [False] * n
    total = 0
    for v in range(n):
        if done[v]:
            continue
        seen = {}
        trail = []
        x = v
        while not done[x] and x not in seen:
            seen[x] = len(trail)
            trail.append(x)
            x = f[x]
        if x in seen:
            total += len(trail) - seen[x]
        for x in trail:
            done[x] = True
    return total


def conditional_numerator(n, k, z):
    m = n - k
    if m == 0:
        return (1, 1) if z == 0 else (0, 1)
    if not 0 <= z <= m:
        return (0, 1)
    numerator = comb(m, z) * sum(
        (-1) ** j * comb(m-z, j) * (n-z-j) ** (m-1)
        for j in range(m-z+1)
    )
    return numerator, n ** (m-1)


def cmean(n):
    return sum((Fraction(falling(n, j), n ** j) for j in range(1,n+1)),Fraction(0))


def model_prob(n, k, z):
    if k == n:
        return Fraction(factorial(n), n**n) if z == 0 else Fraction(0)
    a, b = conditional_numerator(n, k, z)
    return Fraction(k * falling(n, k), n ** (k+1)) * Fraction(a,b)


def check():
    assertions = 0
    count_maps = 0
    for n in range(2, 8):
        seen = Counter()
        for f in product(range(n), repeat=n):
            seen[(cycle_count(f), n-len(set(f)))] += 1
            count_maps += 1
        assert sum(seen.values()) == n ** n
        assertions += 1
        eC = sum(Fraction(c * count, n ** n) for (c,z),count in seen.items())
        eZ = sum(Fraction(z * count, n ** n) for (c,z),count in seen.items())
        eCZ = sum(Fraction(c * z * count, n ** n) for (c,z),count in seen.items())
        p0 = Fraction((n-1)**n, n**n)
        assert eC == cmean(n)
        assert eZ == n*p0
        assert eCZ-eC*eZ == n*p0*(cmean(n-1)-cmean(n))
        assert eCZ-eC*eZ < 0
        assertions += 4
        for k in range(1,n+1):
            count_k = sum(seen[(k,z)] for z in range(n+1))
            expected_k = Fraction(k*falling(n,k), n**(k+1))
            assert Fraction(count_k,n**n)==expected_k
            assertions += 1
            mass = 0
            for z in range(n+1):
                expected = model_prob(n,k,z)
                assert Fraction(seen[(k,z)],n**n)==expected, (n,k,z,seen[(k,z)],expected)
                mass += expected
                assertions += 1
            assert mass==expected_k
            assertions += 1
            m=n-k
            if m:
                for r in range(m+1):
                    ef=Fraction(sum(falling(z,r)*seen[(k,z)] for z in range(n+1)),count_k)
                    predicted=Fraction(falling(m,r)*(n-r)**(m-1),n**(m-1))
                    assert ef==predicted,(n,k,r,ef,predicted)
                    assertions += 1
        assert cmean(n)>cmean(n-1)
        assertions+=1
    print(f'PASS: {count_maps:,} uniformly weighted mappings exhaustively inspected; {assertions:,} exact assertions')

if __name__=='__main__':
    check()
