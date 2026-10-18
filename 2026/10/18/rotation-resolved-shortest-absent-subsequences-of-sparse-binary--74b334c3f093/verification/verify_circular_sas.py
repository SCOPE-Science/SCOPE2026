#!/usr/bin/env python3
"""Independent exact checks of circular short-gap SAS profiles."""
from collections import Counter
from itertools import product

def is_subseq(u, w):
    j = 0
    for a in w:
        if j < len(u) and a == u[j]:
            j += 1
    return j == len(u)

def direct_absent(w, length):
    return {''.join(v) for v in product('01', repeat=length)
            if not is_subseq(v, w)}

def dp_shortest(w):
    """Independent next-occurrence/word-count DP, not target enumeration."""
    n = len(w)
    nxt = [[n + 1, n + 1] for _ in range(n + 2)]
    for i in range(n - 1, -1, -1):
        nxt[i] = nxt[i + 1].copy()
        nxt[i][int(w[i])] = i + 1
    counts = {0: 1}
    for length in range(1, n + 2):
        out = {}
        for p, cnt in counts.items():
            for symbol in (0, 1):
                q = nxt[p][symbol]
                if q <= n:
                    out[q] = out.get(q, 0) + cnt
        counts = out
        missed = (1 << length) - sum(counts.values())
        if missed:
            return length, missed
    raise AssertionError('no shortest absent word')

def predicted(gaps):
    k = len(gaps)
    out = Counter({1: gaps.count(2)})
    for p in range(k):
        r = 0
        j = (p - 1) % k
        while gaps[j] == 1 and r < k:
            r += 1
            j = (j - 1) % k
        out[2 + r] += 2
    return +out

def gapword(gaps):
    return ''.join('1' + '0' * g for g in gaps)

def check_all_small():
    cases = cuts = 0
    for k in range(2, 9):
        for gaps in product((1, 2), repeat=k):
            if 2 not in gaps:
                continue
            w = gapword(gaps)
            expected = predicted(gaps)
            observed = Counter()
            for i in range(len(w)):
                rot = w[i:] + w[:i]
                absent = direct_absent(rot, k + 1)
                assert all(is_subseq(''.join(p), rot)
                           for p in product('01', repeat=k)), (gaps, i)
                observed[len(absent)] += 1
                if k <= 5:
                    assert dp_shortest(rot) == (k + 1, len(absent))
            assert observed == expected, (gaps, observed, expected)
            cases += 1
            cuts += len(w)
    return cases, cuts

def fibword(m):
    w = '0'
    for _ in range(m):
        w = ''.join('01' if x == '0' else '0' for x in w)
    return w

def check_fib():
    a, b = '0', '01'
    tests = 0
    for m in range(2, 12):
        a, b = b, b + a
        if m < 3:
            continue
        w = fibword(m)
        assert b == w
        k = w.count('1')
        assert k >= 2
        gaps = []
        pos = [i for i, x in enumerate(w) if x == '1']
        for i in range(k):
            gaps.append((pos[(i + 1) % k] - pos[i] - 1) % len(w))
        assert set(gaps).issubset({1, 2})
        assert all(not (gaps[i] == gaps[(i + 1) % k] == 1) for i in range(k))
        expected = predicted(gaps)
        got = Counter()
        for i in range(len(w)):
            rot = w[i:] + w[:i]
            L, num = dp_shortest(rot)
            assert L == k + 1
            got[num] += 1
        assert got == expected, (m,got,expected)
        t = gaps.count(1)
        assert got == Counter({1: k-t, 2: 2*(k-t), 3: 2*t})
        tests += 1
    return tests

if __name__ == '__main__':
    cases, cuts = check_all_small()
    tests = check_fib()
    print('VERIFY_OK binary_gap_necklaces=' + str(cases) +
          ' rooted_cuts=' + str(cuts) + ' fibonacci_m3_to11=' + str(tests))
