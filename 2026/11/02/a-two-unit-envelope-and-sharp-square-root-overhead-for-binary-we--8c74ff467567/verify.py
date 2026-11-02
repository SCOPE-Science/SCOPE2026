#!/usr/bin/env python3
"""Finite checks for two-marker scattered-subsequence covering bounds.

This program is supplementary: the all-length assertion follows from the
mathematical argument, not from finite enumeration.
"""
from collections import deque
from itertools import combinations
from math import isqrt


def integer_lower(k):
    assert k >= 2
    m = 8 * (k - 1)
    q = isqrt(m)
    return k - 3 + q + (q * q < m)


def build(k, d):
    assert k >= 2 and d >= 2
    K = k - 2
    Z = K + d - 1
    h = d // 2
    out = []
    for z in range(Z + 1):
        if z % d in (0, h):
            out.append('1')
        if z != Z:
            out.append('0')
    return ''.join(out)


def marks(word):
    z = 0
    ans = []
    for c in word:
        if c == '0':
            z += 1
        else:
            ans.append(z)
    return z, ans


def covers_by_pairs(word, k):
    Z, pos = marks(word)
    K = k - 2
    if Z < K:
        return False
    for a in range(K + 1):
        for b in range(K + 1 - a):
            c = K - a - b
            if not any(x >= a and y-x >= b and Z-y >= c
                       for i, x in enumerate(pos) for y in pos[i+1:]):
                return False
    return True


def greedy_subseq(target, word):
    j = 0
    for ch in word:
        if j < len(target) and target[j] == ch:
            j += 1
    return j == len(target)


def exact_shortest(k):
    targets = [tuple(int(j in ij) for j in range(k))
               for ij in combinations(range(k), 2)]
    n = len(targets)
    root = (0,) * n
    queue = deque([root])
    seen = {root: (None, -1)}
    while queue:
        state = queue.popleft()
        if all(s == k for s in state):
            length = 0
            while seen[state][0] is not None:
                state = seen[state][0]
                length += 1
            return length
        for symbol in (0, 1):
            nxt = tuple(p + (p < k and target[p] == symbol)
                        for p, target in zip(state, targets))
            if nxt not in seen:
                seen[nxt] = (state, symbol)
                queue.append(nxt)
    raise RuntimeError('finite automaton failed')


def main():
    exact = [2, 5, 7, 9, 10, 12, 14, 15, 17, 18, 20]
    for k, expected in enumerate(exact, start=2):
        assert exact_shortest(k) == expected, (k, expected)
    for k in list(range(2, 101)) + [150, 200, 300, 500]:
        lower = integer_lower(k)
        N = 2 * k + 5
        for d in range(2, min(2*k+5, 2*isqrt(2*k)+10)):
            word = build(k, d)
            assert len(word) >= lower
            if len(word) < N:
                N = len(word)
                chosen = word
        assert N <= lower + 2, (k, lower, N)
        assert covers_by_pairs(chosen, k), k
        if k <= 24:
            assert all(greedy_subseq('0'*a+'1'+'0'*b+'1'+'0'*(k-2-a-b), chosen)
                       for a in range(k-1) for b in range(k-1-a)), k
    for n in range(2, 12):
        for mask in range(1 << n):
            word = ''.join('1' if mask & (1 << j) else '0' for j in range(n))
            for k in range(2, min(n, 7) + 1):
                criterion = covers_by_pairs(word, k)
                direct = all(greedy_subseq('0'*a+'1'+'0'*b+'1'+'0'*(k-2-a-b), word)
                             for a in range(k-1) for b in range(k-1-a))
                assert criterion == direct, (n, k, word)
    print('VERIFY_OK exact BFS k=2..12; direct/mark equivalence n<=11; constructed bounds and full coverage k<=100,150,200,300,500')


if __name__ == '__main__':
    main()
