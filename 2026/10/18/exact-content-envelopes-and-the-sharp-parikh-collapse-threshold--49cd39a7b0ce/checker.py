#!/usr/bin/env python3
"""Finite, independently enumerated tests for the sharp Parikh-collapse threshold.

Run: python3 checker.py. Uses only the Python standard library.
The infinite theorem requires the separate combinatorial proof.
"""
from itertools import product
from math import ceil
from collections import Counter


def lcs(a, b):
    d = [0] * (len(b) + 1)
    for x in a:
        prev = 0
        for j, y in enumerate(b, 1):
            old = d[j]
            d[j] = prev + 1 if x == y else max(d[j], d[j - 1])
            prev = old
    return d[-1]


def contained(a, b, q):
    ca, cb = Counter(a), Counter(b)
    return all(ca[i] <= cb[i] for i in range(q))


def sharp_pair(q, k):
    r = min(q, k)
    counts = [k // r + (i < k % r) for i in range(r)]
    a = tuple(x for i in range(r) for x in [i] * counts[i])
    b = tuple(x for i in range(r - 1, -1, -1) for x in [i] * counts[i])
    assert contained(a, b, q) and contained(b, a, q)
    assert lcs(a, b) == ceil(k / q)
    return a, b


def brute_plateau(q, k, max_host):
    threshold = k - ceil(k / q)
    targets = [s for length in range(k + 1) for s in product(range(q), repeat=length)]
    num_pairs = 0
    for n in range(max_host + 1):
        for w in product(range(q), repeat=n):
            for u in targets:
                is_possible = contained(u, w, q)
                is_jumbled = is_possible and len(u) - lcs(u, w) <= threshold
                if is_possible != is_jumbled:
                    raise AssertionError((q, k, threshold, u, w))
                num_pairs += 1
    a, b = sharp_pair(q, k)
    if threshold > 0:
        assert k - lcs(a, b) == threshold
        assert k - lcs(a, b) > threshold - 1
    return num_pairs, threshold


def content_envelope(counts, k):
    from math import inf
    hcap = min(k, max(counts, default=0))
    return max([0] + [min(k, sum(min(c, h) for c in counts)) - h
                      for h in range(1, hcap + 1)])


def verify_content_envelope(q, max_length):
    patterns = [u for m in range(max_length + 1) for u in product(range(q), repeat=m)]
    by_content = {}
    tested = 0
    for n in range(max_length + 1):
        for w in product(range(q), repeat=n):
            counts = tuple(w.count(i) for i in range(q))
            key = counts
            best = -1
            for u in patterns:
                if len(u) > n or not contained(u, w, q):
                    continue
                deficit = len(u) - lcs(u, w)
                if deficit > best:
                    best = deficit
                tested += 1
            if key not in by_content:
                by_content[key] = best
            else:
                by_content[key] = max(by_content[key], best)
            assert best <= content_envelope(counts, max_length), (w, best)
            if w == tuple(i for i,c in enumerate(counts) for _ in range(c)):
                assert best == content_envelope(counts, max_length), (w,best,content_envelope(counts, max_length))
    for counts, val in by_content.items():
        assert val == content_envelope(counts, max_length), (counts,val)
    return tested, len(by_content)


def main():
    checked = 0
    for q in (2, 3):
        for k in range(1, 7 if q == 2 else 6):
            max_host = (k + 1) if q == 2 else k
            pairs, t = brute_plateau(q, k, max_host)
            checked += pairs
            print(f'q={q}, k={k}, threshold={t}, host-length<= {max_host}, checked={pairs}')
    # More symbols than target positions: the first stage below k-1 still
    # genuinely retains order information.
    for q, k in ((4, 3), (5, 4), (7, 5)):
        a, b = sharp_pair(q, k)
        assert lcs(a, b) == 1
        assert k - lcs(a, b) == k - 1
        print(f'q={q}, k={k}, reverse-block gap={k - lcs(a, b)}')
    c2, t2 = verify_content_envelope(2, 7)
    c3, t3 = verify_content_envelope(3, 5)
    print(f'content envelopes: q=2, compositions={t2}, pairs={c2}; q=3, compositions={t3}, pairs={c3}')
    print(f'PASS: {checked} plateau tests and {c2 + c3} content-envelope pairs')

if __name__ == '__main__':
    main()
