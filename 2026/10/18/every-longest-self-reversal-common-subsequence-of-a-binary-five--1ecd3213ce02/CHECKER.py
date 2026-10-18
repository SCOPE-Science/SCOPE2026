#!/usr/bin/env python3
"""Reproducibility checks for a binary reversal-LCS run threshold.

This executable enumerates all distinct LCS output words, including ties in
which matching endpoint symbols can be skipped.  It does not constitute the
infinite proof, supplied separately.
"""
from functools import lru_cache
from itertools import product
from collections import Counter


def all_lcs(x, y):
    @lru_cache(None)
    def length(i, j):
        if i == len(x) or j == len(y):
            return 0
        v = max(length(i+1, j), length(i, j+1))
        if x[i] == y[j]:
            v = max(v, 1 + length(i+1, j+1))
        return v

    @lru_cache(None)
    def outputs(i, j):
        if length(i, j) == 0:
            return frozenset(('',))
        result = set()
        if x[i] == y[j] and 1 + length(i+1, j+1) == length(i, j):
            result.update(x[i] + p for p in outputs(i+1, j+1))
        if length(i+1, j) == length(i, j):
            result.update(outputs(i+1, j))
        if length(i, j+1) == length(i, j):
            result.update(outputs(i, j+1))
        return frozenset(result)
    return outputs(0, 0)


def independent_common_outputs(w):
    """Independent direct enumeration for short words, no LCS recurrence."""
    n = len(w)
    def subs(s):
        return {''.join(s[i] for i in range(n) if (mask >> i) & 1)
                for mask in range(1 << n)}
    common = subs(w) & subs(w[::-1])
    k = max(map(len, common))
    return {s for s in common if len(s) == k}


def runs(s):
    return 0 if not s else 1 + sum(a != b for a, b in zip(s, s[1:]))


def main():
    direct = 0
    for n in range(1, 10):
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            assert set(all_lcs(w, w[::-1])) == independent_common_outputs(w), w
            direct += 1

    bad_by_length = {}
    checked = 0
    for n in range(1, 13):
        bad = []
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            bad_lcs = [u for u in all_lcs(w, w[::-1]) if u != u[::-1]]
            assert not bad_lcs or runs(w) >= 6, ('5-run failure', w, bad_lcs)
            if bad_lcs:
                bad.append(w)
            checked += 1
        bad_by_length[n] = tuple(bad)
    assert all(not bad_by_length[n] for n in range(1, 7))
    assert bad_by_length[7] == ('0101001', '0110101', '1001010', '1010110')
    assert all(runs(w) == 6 for w in bad_by_length[7])
    assert {'00101', '10100'} <= set(all_lcs('0101001', '1001010'))

    params_checked = 0
    for params in product(range(1, 5), repeat=5):
        w = ''.join(('01'[i & 1])*count for i, count in enumerate(params))
        assert all(s == s[::-1] for s in all_lcs(w, w[::-1])), params
        params_checked += 1
    print('ALL_FIVE_RUN_LCS_CHECKS_PASSED',
          'direct_words', direct,
          'binary_words', checked,
          'five_run_parameter_tuples', params_checked,
          'first_exception_length', 7,
          'first_exception_count', len(bad_by_length[7]))


if __name__ == '__main__':
    main()
