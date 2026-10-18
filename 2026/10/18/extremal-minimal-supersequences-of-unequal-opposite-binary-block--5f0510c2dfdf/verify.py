#!/usr/bin/env python3
"""Finite cross-check of a four-parameter extremal-supersequence theorem.

The brute-force side evaluates subsequence containment and all single deletions
without using the closed-form construction. Standard-library Python only.
"""
from itertools import product, combinations
from math import comb


def contains(pattern, word):
    i = 0
    for letter in word:
        if i < len(pattern) and pattern[i] == letter:
            i += 1
    return i == len(pattern)


def is_minimal(word, left, right):
    if not (contains(left, word) and contains(right, word)):
        return False
    return all(not (contains(left, word[:i] + word[i+1:])
                    and contains(right, word[:i] + word[i+1:]))
               for i in range(len(word)))


def words(k):
    for digits in product('01', repeat=k):
        yield ''.join(digits)


def generated(a, b, c, d):
    out = set()
    # Shared one: X has a zeros / (c-1) ones and ends zero;
    # Y begins zero and has d zeros / (b-1) ones.
    for px in combinations(range(a+c-2), c-1):
        p = ''.join('1' if i in px else '0' for i in range(a+c-2)) + '0'
        for sy in combinations(range(b+d-2), b-1):
            q = '0' + ''.join('1' if i in sy else '0' for i in range(b+d-2))
            out.add(p + '1' + q)
    # Shared zero, with the complementary endpoint constraints.
    for px in combinations(range(a+c-2), a-1):
        p = ''.join('0' if i in px else '1' for i in range(a+c-2)) + '1'
        for sy in combinations(range(b+d-2), d-1):
            q = '1' + ''.join('0' if i in sy else '1' for i in range(b+d-2))
            out.add(p + '0' + q)
    return out


def main():
    cases = 0
    tested_words = 0
    total_extremal = 0
    for a, b, c, d in product(range(2, 5), repeat=4):
        length = a+b+c+d-1
        if length > 14:
            continue
        A = '0'*a+'1'*b
        B = '1'*c+'0'*d
        observed = set()
        for word in words(length):
            tested_words += 1
            if is_minimal(word, A, B):
                observed.add(word)
        proposed = generated(a, b, c, d)
        expected = 2*comb(a+c-2, a-1)*comb(b+d-2, b-1)
        assert observed == proposed, (a, b, c, d, observed ^ proposed)
        assert len(proposed) == expected, (a,b,c,d,len(proposed),expected)
        cases += 1
        total_extremal += len(observed)
    # Also test the sharp N upper length bound on representative parameters.
    no_long_cases = 0
    for a,b,c,d in product(range(2,4),repeat=4):
        A='0'*a+'1'*b
        B='1'*c+'0'*d
        assert not any(is_minimal(w,A,B) for w in words(a+b+c+d))
        no_long_cases += 1
    # Singleton-run boundaries are genuine (not covered by the formula).
    A, B = '01', '100'
    boundary = [w for w in words(4) if is_minimal(w,A,B)]
    assert len(boundary)==3, boundary
    print('VERIFY_OK cases=%d brute_words=%d extremal_words=%d upper_bound_cases=%d singleton_boundary=%d' %
          (cases,tested_words,total_extremal,no_long_cases,len(boundary)))

if __name__=='__main__':
    main()
