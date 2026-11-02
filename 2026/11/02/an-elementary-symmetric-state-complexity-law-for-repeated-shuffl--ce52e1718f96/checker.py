#!/usr/bin/env python3
"""Independent finite tests for the state complexity of ordered-block shuffle powers.

Uses direct interleaving enumeration and right-quotient minimization; no third-party modules.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import comb


def formula(p, k):
    e = [1] + [0] * len(p)
    for j, value in enumerate(p, 1):
        for r in range(j, 0, -1):
            e[r] += value * e[r-1]
    return 1 + sum(e[r] * comb(k, r) for r in range(min(k, len(p)) + 1))


def shuffle_words(p, k):
    w = ''.join(chr(ord('a') + i) * length for i, length in enumerate(p))
    n = len(w)
    @lru_cache(None)
    def rec(state):
        if state == (n,) * k:
            return frozenset({''})
        ans = set()
        for i, pos in enumerate(state):
            if pos == n:
                continue
            t = list(state)
            t[i] += 1
            for suffix in rec(tuple(t)):
                ans.add(w[pos] + suffix)
        return frozenset(ans)
    return rec((0,) * k)


def prefix_test(w, p, k):
    count = [0] * len(p)
    for x in w:
        j = ord(x) - ord('a')
        count[j] += 1
        if count[j] > k * p[j]:
            return False
        if j and count[j] > p[j] * (count[j-1] // p[j-1]):
            return False
    return count == [k * x for x in p]


def all_fixed_content(p, k):
    counts = tuple(k * x for x in p)
    @lru_cache(None)
    def rec(cnt):
        if all(x == 0 for x in cnt):
            return frozenset({''})
        out = set()
        for i, x in enumerate(cnt):
            if x:
                next_count = list(cnt)
                next_count[i] -= 1
                out.update(chr(ord('a')+i)+z for z in rec(tuple(next_count)))
        return frozenset(out)
    return rec(counts)


def distinct_right_quotients(language):
    # The accepted language is finite and contains no epsilon in these tests.
    quotients = defaultdict(set)
    for w in language:
        for i in range(len(w)+1):
            quotients[w[:i]].add(w[i:])
    # Nonempty quotients correspond to viable prefixes; empty one is the sink.
    return len({frozenset(v) for v in quotients.values()}) + 1


def enumerated_feasible_vectors(p, k):
    count = 0
    for c in product(*(range(k*x+1) for x in p)):
        if all(c[j] <= p[j] * (c[j-1] // p[j-1]) for j in range(1, len(p))):
            count += 1
    return count


def main():
    cases = [((1,1),2), ((2,3),2), ((1,2,3),2), ((2,1,2),2),
             ((1,1,1),3), ((1,1,1,1),2), ((1,2,1,2),2),
             ((2,2,2),2), ((1,3),3), ((2,1,1),3)]
    for p,k in cases:
        words = shuffle_words(p,k)
        expected = formula(p,k)
        direct = distinct_right_quotients(words)
        actual_language = frozenset(w for w in all_fixed_content(p,k) if prefix_test(w,p,k))
        assert words == actual_language, ('language classification',p,k)
        assert direct == expected, ('minimum DFA',p,k,direct,expected)
        print('DIRECT', p, k, 'words',len(words),'min_states',direct)
    comparisons = 0
    for d in range(1,5):
        for p in product((1,2,3), repeat=d):
            for k in range(0,5):
                f=formula(p,k)
                direct=enumerated_feasible_vectors(p,k)+1
                assert f == direct, (p,k,f,direct)
                comparisons+=1
    print('LATTICE', comparisons, 'exact finite comparisons passed')
    print('ALL CHECKS PASSED')

if __name__ == '__main__':main()
