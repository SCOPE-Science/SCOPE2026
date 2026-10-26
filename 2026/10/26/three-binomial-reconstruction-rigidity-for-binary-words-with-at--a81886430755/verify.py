"""Reproducible checks of the 3-binomial low-run reconstruction theorem.

Python >=3.9; standard library only.  The infinite theorem has a written
algebraic proof: these finite checks independently test its identities and
its finite sharp counterexample length.
"""
from collections import defaultdict
from itertools import combinations, product
from math import gcd

PATTERNS = tuple(''.join(x) for k in (1, 2, 3) for x in product('01', repeat=k))


def counts_dp(w):
    """Streaming subsequence counter, counting paths by their target strings."""
    dp = {'': 1}
    for letter in w:
        for x, times in list(dp.items()):
            if len(x) < 3:
                dp[x + letter] = dp.get(x + letter, 0) + times
    return tuple(dp.get(s, 0) for s in PATTERNS)


def counts_combinatorial(w):
    """Independent direct enumeration of all index tuples."""
    buckets = defaultdict(int)
    for k in (1, 2, 3):
        for indices in combinations(range(len(w)), k):
            buckets[''.join(w[i] for i in indices)] += 1
    return tuple(buckets[x] for x in PATTERNS)


def runs(w):
    return 1 + sum(x != y for x, y in zip(w, w[1:]))


def word4(a, b, c, d):
    return '0' * a + '1' * b + '0' * c + '1' * d


def check():
    direct_checks = 0
    for n in range(1, 10):
        for x in range(1 << n):
            w = format(x, f'0{n}b')
            assert counts_dp(w) == counts_combinatorial(w), w
            direct_checks += 1

    # Compare the full decks of every run <=4 word up to length 19.
    # Each class with an unequal member must have exactly two reversals.
    restricted_words = 0
    reversal_classes = 0
    for n in range(1, 20):
        classes = defaultdict(set)
        for a in range(1 << n):
            w = format(a, f'0{n}b')
            if runs(w) <= 4:
                restricted_words += 1
                classes[counts_dp(w)].add(w)
        for group in classes.values():
            assert len(group) <= 2
            assert all(w[::-1] in group or len(group) == 1 for w in group)
            if len(group) == 2:
                reversal_classes += 1

    # All four-run parameter quadruples in the discrete box, with both
    # orientations; test analytical formulas and reversal criterion.
    param_checks = 0
    for a, b, c, d in product(range(1, 9), repeat=4):
        w = word4(a, b, c, d)
        dck = dict(zip(PATTERNS, counts_dp(w)))
        assert dck['10'] == b * c
        assert dck['010'] == a * b * c
        assert dck['101'] == b * c * d
        assert dck['01'] == (a + c) * (b + d) - b * c
        assert (counts_dp(w) == counts_dp(w[::-1])) == (2 * b * c == (a+c)*(b+d))
        z, o = a+c, b+d
        assert 2*(dck['001']-dck['100']) == (z-1)*(dck['01']-dck['10'])
        assert 2*(dck['011']-dck['110']) == (o-1)*(dck['01']-dck['10'])
        param_checks += 1

    # Exact arithmetic parameterization of every positive reversal collision.
    parametrized = 0
    for a in range(1, 10):
        for c in range(a+1, 13):
            g = gcd(c-a, c+a)
            for t in range(1, 8):
                b = (a+c)//g*t
                d = (c-a)//g*t
                assert counts_dp(word4(a,b,c,d)) == counts_dp(word4(a,b,c,d)[::-1])
                parametrized += 1

    # Global onset of any non-reversal collision in length <=8.
    first_nonreversal = None
    for n in range(1, 9):
        groups = defaultdict(list)
        for x in range(1 << n):
            w = format(x, f'0{n}b')
            groups[counts_dp(w)].append(w)
        bad = [(u,v) for group in groups.values() for i,u in enumerate(group) for v in group[i+1:] if v != u[::-1]]
        if bad:
            first_nonreversal = n
            break
    assert first_nonreversal == 8
    u,v = '00110001','01000110'
    assert runs(u) == 4 and runs(v) == 5 and u != v[::-1]
    assert counts_dp(u) == counts_dp(v) == (5,3,10,9,6,3,10,12,12,6,6,6,3,1)
    assert counts_combinatorial(u) == counts_combinatorial(v)
    print('VERIFY_OK brute_independent_decks=%d low_run_words=%d reversal_classes=%d four_run_parameters=%d parametrized_reversals=%d first_nonreversal_length=%d' % (direct_checks,restricted_words,reversal_classes,param_checks,parametrized,first_nonreversal))


if __name__ == '__main__':
    check()
