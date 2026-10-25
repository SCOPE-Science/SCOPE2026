#!/usr/bin/env python3
"""Stand-alone checks of a binary circular-subsequence universality enumeration."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def is_subseq(pattern, word):
    it = iter(word)
    return all(any(c == target for c in it) for target in pattern)


def direct_index(word):
    for k in range(len(word) // 2 + 1):
        if any(not is_subseq(p, word) for p in product('01', repeat=k)):
            return k - 1
    return len(word)//2


def greedy_index(word):
    seen = set(); count = 0
    for x in word:
        seen.add(x)
        if len(seen) == 2:
            seen.clear(); count += 1
    return count


def circular_index(word):
    return max(greedy_index(word[i:] + word[:i]) for i in range(len(word)))


def circular_matching(word):
    n = len(word)
    edge_list = [(i, (i + 1) % n) for i in range(n) if word[i] != word[(i + 1) % n]]
    best = 0
    for mask in range(1 << len(edge_list)):
        taken = set(); valid = True
        for j, (a, b) in enumerate(edge_list):
            if mask >> j & 1:
                if a in taken or b in taken:
                    valid = False; break
                taken.add(a); taken.add(b)
        if valid:
            best = max(best, mask.bit_count())
    return best


def predicted(n, k):
    if k == 0:
        return 2
    if not (1 <= k <= n//2):
        return 0
    return (1 << k) * n * comb(n-k, k) // (n-k) - (2 if n == 2*k else 0)


def verify():
    direct_checked = 0; match_checked = 0; total_checked = 0
    for n in range(1, 17):
        hist = Counter()
        for tup in product('01', repeat=n):
            w = ''.join(tup)
            zeta = circular_index(w)
            hist[zeta] += 1; total_checked += 1
            if n <= 10:
                assert all(greedy_index(w[i:] + w[:i]) == direct_index(w[i:] + w[:i]) for i in range(n))
                direct_checked += n
            if n <= 10:
                assert circular_matching(w) == zeta
                match_checked += 1
        for k in range(n//2 + 1):
            assert hist[k] == predicted(n, k), (n, k, hist[k], predicted(n,k))
        assert sum(hist.values()) == (1 << n)
        exact_mean = Fraction(sum(k*count for k,count in hist.items()), 1 << n)
        t = (-1)**n
        closed_mean = Fraction(n, 3) + Fraction(n*(t-3), 6*(1 << n))
        assert exact_mean == closed_mean, (n, exact_mean, closed_mean)
        exact_var = Fraction(sum(k*k*count for k,count in hist.items()),1 << n) - exact_mean**2
        closed_var = Fraction(2*n,27) + Fraction(n*((9*n-8)*t + 9*n), 108*(1<<n)) - Fraction(n*n*(t-3)**2, 36*(1<<(2*n)))
        assert exact_var == closed_var, (n, exact_var, closed_var)
    # Independent polynomial recurrence for the trace/eigenvalue expression.
    a=[2]; b=[1]
    for n in range(2, 81):
        x = [0] * (max(len(b),len(a)+1))
        for k,c in enumerate(b):x[k]+=c
        for k,c in enumerate(a):x[k+1]+=2*c
        a,b=b,x
        poly=b[:]
        poly[0] += 1
        if n%2==0:poly[n//2]-=2
        assert all(poly[k] == predicted(n,k) for k in range(n//2+1))
    print(f'VERIFY_OK words={total_checked} direct_rotations={direct_checked} cyclic_matchings={match_checked} trace_recurrence_n<=80')


if __name__=='__main__':verify()
