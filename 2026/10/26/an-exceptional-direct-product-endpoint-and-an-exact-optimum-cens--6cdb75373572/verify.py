"""Exact finite checks of the direct-product domination formulas.

Usage: python3 verify.py
Requires Python 3.9+ standard library only.
The general result is proved symbolically; these are finite consistency checks.
"""
from collections import Counter
from itertools import product
from math import comb


def brute_weight_distribution(r, s):
    """Independent adjacency-based enumeration; no structural assumptions."""
    neighbors = [tuple(k*s+j for k in range(r) if k != i
                       for j in range(s) if j != h)
                 for i in range(r) for h in range(s)]
    distribution = Counter()
    for lab in product(range(3), repeat=r*s):
        if any(lab[i] == lab[j] == 0
               for i in range(r*s) for j in neighbors[i] if j > i):
            continue
        if any(not any(lab[j] == 2 for j in neighbors[i])
               for i in range(r*s) if lab[i] == 0):
            continue
        if any(not any(lab[j] > 0 for j in neighbors[i])
               for i in range(r*s) if lab[i] > 0):
            continue
        distribution[sum(lab)] += 1
    return distribution


def predicted_optimum(r, s):
    assert 2 <= r <= s
    if r == 2:
        if s == 2:
            return 4, 1
        if s == 3:
            return 6, 25
        return s+3, 2*s*(s-1)
    v = r*(comb((r-1)*s, 2) - s*comb(r-1, 2) + s*(r-1))
    if r == s:
        v *= 2
    return s*(r-1)+2, v


def multiply(a, b):
    c = Counter()
    for i, x in a.items():
        for j, y in b.items():
            c[i+j] += x*y
    return +c


def power(a, k):
    z = {0: 1}
    for _ in range(k):
        z = multiply(z, a)
    return z


def predicted_crown_distribution(n):
    if n == 2:
        return power({1:1, 2:1}, 4)
    assert n >= 3
    q = Counter(power({1:1, 2:1}, 2*n))
    all_subsets = power({0:1, 1:1}, n)
    for t in range(2, n):
        defend = {j: c for j, c in all_subsets.items() if j >= 2}
        defend[1] = t
        for k, c in multiply(power({1:1, 2:1}, t), defend).items():
            q[k+n] += 2*comb(n,t)*c
    side_nonempty = Counter(power({0:1, 1:1}, n-1))
    side_nonempty[0] -= 1
    for k, c in multiply(+side_nonempty, +side_nonempty).items():
        q[k+2*n-2] += n*c
    return +q


def main():
    pairs = [(2,2), (2,3), (2,4), (2,5), (2,6), (3,3), (3,4)]
    for r,s in pairs:
        actual = brute_weight_distribution(r,s)
        best = min(actual)
        got = (best,actual[best])
        assert got == predicted_optimum(r,s), (r,s,got,predicted_optimum(r,s))
        if r == 2:
            assert actual == predicted_crown_distribution(s), (r,s)
        print('PASS',r,s, 'minimum and number',got,'all labelings',sum(actual.values()))
    for n in range(2,10):
        polynomial = predicted_crown_distribution(n)
        assert min(polynomial) == predicted_optimum(2,n)[0]
        assert polynomial[min(polynomial)] == predicted_optimum(2,n)[1]
    print('PASS symbolic coefficient check n=2,...,9')


if __name__ == '__main__':
    main()
