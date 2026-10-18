#!/usr/bin/env python3
"""Exact finite checks for the antidictionary theorem of recursively nested Zimin words.

Independent ground truth uses contextual occurrences of *every* factor,
not the recursive classification or its length formula.
"""
from collections import defaultdict


def recursively_construct(n):
    w = b''
    for j in range(1, n + 1):
        w = w + bytes([j]) + w
    return w


def valuation_construct(n):
    return bytes([1 + (j & -j).bit_length() - 1 for j in range(1, 2**n)])


def proposed_antidictionary(n):
    z = [b'']
    for j in range(1, n + 1):
        z.append(z[-1] + bytes([j]) + z[-1])
    return {
        bytes([a]) + z[j] + bytes([b])
        for j in range(n)
        for a in range(j + 1, n + 1)
        for b in range(j + 1, n + 1)
        if a == b == j + 1 or (a >= j + 2 and b >= j + 2)
    }


def brute_minimal_absent(w):
    # For every possible middle factor u, record its one-sided boundary
    # extensions and its actual two-sided extensions, including boundary-only
    # occurrences of u. The empty factor occurs in every interletter gap.
    left = defaultdict(set)
    right = defaultdict(set)
    two = defaultdict(set)
    N = len(w)
    for m in range(N):
        for i in range(N - m + 1):
            u = w[i:i+m]
            if i:
                left[u].add(w[i-1])
            if i+m<N:
                right[u].add(w[i+m])
            if i and i+m<N:
                two[u].add((w[i-1], w[i+m]))
    return {
        bytes([a]) + u + bytes([b])
        for u in left.keys() & right.keys()
        for a in left[u]
        for b in right[u]
        if (a,b) not in two[u]
    }


def main():
    for n in range(1, 10):
        W = recursively_construct(n)
        assert W == valuation_construct(n)
        actual = brute_minimal_absent(W)
        expected = proposed_antidictionary(n)
        if actual != expected:
            raise AssertionError((n, sorted(actual - expected), sorted(expected - actual)))
        spectrum = {2**j+1: (n-j-1)**2 + 1 for j in range(n)}
        from collections import Counter
        assert Counter(map(len, actual)) == spectrum, (n, Counter(map(len, actual)), spectrum)
        assert len(actual) == n + n*(n-1)*(2*n-1)//6
        for x in expected:
            assert x not in W and x[:-1] in W and x[1:] in W
        print('n=%d length=%d minimal_absent=%d agreement=yes' % (n, len(W), len(actual)))
    # A second longer-scale check of all explicitly classified forbidden words.
    for n in (10, 11):
        W = valuation_construct(n)
        for x in proposed_antidictionary(n):
            assert x not in W and x[:-1] in W and x[1:] in W
        print('n=%d length=%d all_predicted_forbidden=yes' % (n, len(W)))
    print('VERIFY_OK exhaustive_all_MAWs_levels=1..9 explicit_candidates_levels=1..11')


if __name__ == '__main__':
    main()
