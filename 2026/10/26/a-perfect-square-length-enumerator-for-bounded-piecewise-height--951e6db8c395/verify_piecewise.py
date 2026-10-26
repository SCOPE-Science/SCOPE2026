#!/usr/bin/env python3
"""Independent finite checks for a four-run binary piecewise-height enumerator.

This checks finitely many cases; the infinite proof is in RESULT.md.
"""
from collections import Counter, deque
from itertools import product


def next_match(w, pos, symbol):
    k = w.find(symbol, pos)
    return k + 1 if k >= 0 else -1


def shortest_extra_subsequence(original, extended):
    # Greedy subsequence automata; shortest sequence recognized by 'extended'
    # but not by 'original'. States record first unused positions.
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while q:
        i, j, depth = q.popleft()
        for char in '01':
            jj = next_match(extended, j, char)
            if jj < 0:
                continue
            ii = next_match(original, i, char)
            if ii < 0:
                return depth + 1
            if (ii, jj) not in seen:
                seen.add((ii, jj))
                q.append((ii, jj, depth + 1))
    raise AssertionError('An insertion must add a distinguishable subsequence.')


def independent_height(w):
    # By the established one-insertion reduction for singleton Simon classes.
    return max(shortest_extra_subsequence(w, w[:i] + char + w[i:])
               for i in range(len(w) + 1) for char in '01')


def closed_height(a, b, c, d):
    return max(a + min(c, 2) + 1, b + 2, c + 2,
               d + min(b, 2) + 1)


def shifted_poly(H):
    if H < 3:
        return Counter()
    result = Counter()
    for a in range(1, H - 1):
        result[a + 1] += 1  # c = 1
    for a in range(1, H - 2):
        for c in range(2, H - 1):
            result[a + c] += 1
    return result


def square_poly(p):
    out = Counter()
    for n, v in p.items():
        for m, u in p.items():
            out[n+m] += v*u
    return out


def verify():
    checks = 0
    for a, b, c, d in product(range(1, 9), repeat=4):
        w = '0'*a + '1'*b + '0'*c + '1'*d
        assert independent_height(w) == closed_height(a, b, c, d), (a,b,c,d)
        checks += 1
    for H in range(3, 12):
        predicted = square_poly(shifted_poly(H))
        actual = Counter()
        # The height bound restricts every run to <= H-2 (or smaller).
        for a, b, c, d in product(range(1, H + 1), repeat=4):
            if closed_height(a,b,c,d) <= H:
                actual[a+b+c+d] += 1
        assert actual == predicted, (H, actual, predicted)
        assert sum(actual.values()) == (H*H - 5*H + 7)**2
    # The shortest possible height at length n, checked separately.
    for n in range(4, 26):
        vals = []
        for a in range(1,n-2):
            for b in range(1,n-a-1):
                for c in range(1,n-a-b):
                    d=n-a-b-c
                    vals.append(closed_height(a,b,c,d))
        expected = 3 if n==4 else 3+(n+1)//4
        assert min(vals) == expected
        assert max(vals) == n-1
    # Explicit direct subword-set check for small u and selected one-insertions.
    def subwords(w):
        acc={''}
        for char in w:
            acc |= {v+char for v in list(acc)}
        return acc
    direct_pairs=0
    for n in range(1,9):
        for tup in product('01',repeat=n):
            w=''.join(tup)
            s=subwords(w)
            for i in range(n+1):
                for c in '01':
                    v=w[:i]+c+w[i:]
                    extras=subwords(v)-s
                    assert extras
                    assert min(map(len,extras))==shortest_extra_subsequence(w,v)
                    direct_pairs+=1
    print(f'VERIFY_OK four_run_bfs={checks} height_polynomials=9 length_extrema=22 direct_subword_pairs={direct_pairs}')

if __name__=='__main__':
    verify()
