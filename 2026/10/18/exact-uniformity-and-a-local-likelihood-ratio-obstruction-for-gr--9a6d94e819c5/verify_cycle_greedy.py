"""Exact finite checks for the random-order greedy law on cycle graphs.

Requires Python >=3.9; no third-party libraries or external data.
The finite checks corroborate but do not replace the general analytic proof.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations


def greedy(n, order):
    picked = 0
    for v in order:
        if not (picked >> ((v-1)%n) & 1) and not (picked >> ((v+1)%n) & 1):
            picked |= 1 << v
    return picked


def exact_law(n):
    closed = [(1 << i) | (1 << ((i-1)%n)) | (1 << ((i+1)%n))
              for i in range(n)]
    @lru_cache(maxsize=None)
    def solve(mask):
        if not mask:
            return {0: Fraction(1)}
        vertices = [i for i in range(n) if mask & (1 << i)]
        out = {}
        for v in vertices:
            for target, p in solve(mask & ~closed[v]).items():
                key = target | (1 << v)
                out[key] = out.get(key, Fraction(0)) + p / len(vertices)
        return out
    return solve((1 << n)-1)


def independent_and_maximal(n, mask):
    for v in range(n):
        if mask >> v & 1:
            if mask >> ((v+1)%n) & 1:
                return False
        elif not ((mask >> ((v-1)%n) & 1) or (mask >> ((v+1)%n) & 1)):
            return False
    return True


def target_from_gaps(gaps):
    n = sum(gaps)
    vertices = [0]
    v = 0
    for d in gaps[:-1]:
        v += d
        vertices.append(v)
    return sum(1 << v for v in vertices)


def complement_gaps(m):
    if m == 0:
        return []
    if m < 2:
        raise ValueError('unrepresentable remainder')
    out = []
    while m:
        d = 2 if m % 2 == 0 else 3
        out.append(d)
        m -= d
    return out


def main():
    small = {3,4,5,7}
    exhaustive_orders = 0
    dp_cases = 0
    for n in range(3,16):
        law = exact_law(n)
        assert sum(law.values()) == 1
        truth = {m for m in range(1 << n) if independent_and_maximal(n, m)}
        assert set(law) == truth
        assert (len(set(law.values())) == 1) == (n in small)
        dp_cases += 1
        if n <= 8:
            counts = Counter(greedy(n, order) for order in permutations(range(n)))
            from math import factorial
            assert {m: Fraction(c, factorial(n)) for m,c in counts.items()} == law
            exhaustive_orders += factorial(n)
        if n == 6 or n >= 8:
            rem = complement_gaps(n-6)
            a = target_from_gaps([2,2,2] + rem)
            b = target_from_gaps([3,3] + rem)
            assert a in law and b in law
            assert law[a] >= 2*law[b] and law[b] > 0
            print('n=%d; P(222)=%s; P(33)=%s; ratio=%s' %
                  (n, law[a], law[b], law[a]/law[b]))
    assert exhaustive_orders == sum(__import__('math').factorial(k) for k in range(3,9))
    print('PASS: %d exact DP cycle laws, %d explicit orderings, support and uniformity through n=15' %
          (dp_cases, exhaustive_orders))


if __name__ == '__main__':
    main()
