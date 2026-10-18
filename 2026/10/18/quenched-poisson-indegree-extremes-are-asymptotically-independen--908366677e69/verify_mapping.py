"""Finite exact checks for a random-mapping orbit and high-indegree counts.

Run: python verify_mapping.py
No third-party modules or external data are required.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def orbit_history(f):
    visited = [0]
    seen = {0: 0}
    x = 0
    while True:
        y = f[x]
        if y in seen:
            return len(visited), seen[y]
        seen[y] = len(visited)
        visited.append(y)
        x = y


def high_indegree_count(f, k):
    counts = [0] * len(f)
    for y in f:
        counts[y] += 1
    return sum(z >= k for z in counts)


def canonical_completion_distribution(n, m, j, k):
    prefix = list(range(1, m)) + [j]
    out = Counter()
    for free in product(range(n), repeat=n-m):
        out[high_indegree_count(prefix + list(free), k)] += 1
    return out


def binomial_tail(n, k):
    if k <= 0:
        return Fraction(1)
    if k > n:
        return Fraction(0)
    return Fraction(sum(comb(n, z)*(n-1)**(n-z)
                        for z in range(k, n+1)), n**n)


def tv(a, a_total, b, b_total):
    return sum((abs(Fraction(a.get(i,0),a_total) -
                    Fraction(b.get(i,0),b_total))
                for i in (a.keys() | b.keys())), Fraction(0))/2


def check():
    assertions = 0
    mapping_total = 0
    conditional_cases = 0
    for n in range(2, 7):
        histories = Counter()
        joint = {k: Counter() for k in range(2,n+1)}
        unconditional = {k: Counter() for k in range(2,n+1)}
        for f in product(range(n), repeat=n):
            m,j = orbit_history(f)
            histories[m,j] += 1
            for k in range(2,n+1):
                y = high_indegree_count(f,k)
                joint[k][m,j,y] += 1
                unconditional[k][y] += 1
        mapping_total += n**n
        assert sum(histories.values()) == n**n
        assertions += 1
        for m in range(1,n+1):
            path_count = factorial(n-1)//factorial(n-m)
            for j in range(m):
                assert histories[m,j] == path_count * n**(n-m)
                assertions += 1
                for k in range(2,n+1):
                    prescribed = canonical_completion_distribution(n,m,j,k)
                    assert sum(prescribed.values()) == n**(n-m)
                    assertions += 1
                    for value, count in prescribed.items():
                        assert joint[k][m,j,value] == path_count * count
                        assertions += 1
                    q1 = binomial_tail(n, k-1)
                    q2 = binomial_tail(n, k-2)
                    bound = 2*m*q1 + q2
                    assert tv(prescribed,n**(n-m),unconditional[k],n**n) <= bound
                    assertions += 1
                    conditional_cases += 1
    print('VERIFY_OK', 'mappings', mapping_total,
          'conditionals', conditional_cases, 'assertions', assertions)


if __name__ == '__main__':
    check()
