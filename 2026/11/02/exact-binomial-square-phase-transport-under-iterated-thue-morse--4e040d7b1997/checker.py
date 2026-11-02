#!/usr/bin/env python3
"""Standalone exact-integer checks of finite cases for the dyadic binomial-square theorem.
No external packages, documents or network access required.
"""
from itertools import combinations


def thue(n):
    return [i.bit_count() & 1 for i in range(n)]


def basis(r):
    words = [""] + [format(x, "0%db" % h) for h in range(1, r+1)
                    for x in range(1 << h)]
    return words, {w: i for i, w in enumerate(words)}


def all_prefix_counts(text, words, ix):
    data = [[1] + [0] * (len(words)-1)]
    indices = sorted(range(1, len(words)), key=lambda j: len(words[j]), reverse=True)
    for a in text:
        before = data[-1]
        after = before.copy()
        for j in indices:
            pat = words[j]
            if pat[-1] == str(a):
                after[j] += before[ix[pat[:-1]]]
        data.append(after)
    return data


def factor_counts(data, a, b, words, ix):
    result = [0] * len(words)
    result[0] = 1
    for j in range(1, len(words)):
        w = words[j]
        v = data[b][j] - data[a][j]
        for cut in range(1, len(w)):
            v -= data[a][ix[w[:cut]]] * result[ix[w[cut:]]]
        result[j] = v
    return tuple(result)


def direct_counts(text, r, words):
    return tuple(1 if not w else sum(
        all(str(text[i]) == w[z] for z, i in enumerate(c))
        for c in combinations(range(len(text)), len(w))) for w in words)


def substituted(source, depth):
    w = list(source)
    for _ in range(depth):
        w = [digit for a in w for digit in (a, 1-a)]
    return w


def arbitrary_source_checks():
    for size in range(3, 8):
        for mask in range(1 << size):
            source = [(mask >> i) & 1 for i in range(size)]
            for r in range(1, 5):
                w = substituted(source, r)
                words, ix = basis(r)
                data = all_prefix_counts(w, words, ix)
                scale = 1 << r
                for m in range(1, min(3, (size-1)//2)+1):
                    for q in range(size-2*m):
                        triple = source[q] == source[q+m] == source[q+2*m]
                        for d in range(scale):
                            s = q*scale+d
                            if s+2*m*scale > len(w):
                                continue
                            equal = factor_counts(data,s,s+m*scale,words,ix) == factor_counts(data,s+m*scale,s+2*m*scale,words,ix)
                            assert equal == (d == 0 or triple), (source,r,m,q,d)


def run():
    arbitrary_source_checks()
    starts = 256
    largest_k = 8
    text = thue(starts + 2*(1 << largest_k))
    for r in range(1, 6):
        words, ix = basis(r)
        pref = all_prefix_counts(text, words, ix)
        for k in range(r, largest_k + 1):
            half = 1 << k
            for s in range(starts):
                first = factor_counts(pref, s, s+half, words, ix)
                second = factor_counts(pref, s+half, s+2*half, words, ix)
                assert (first == second) == (s % (1 << r) == 0), (r,k,s)
    for r in range(1, 4):
        words, ix = basis(r)
        tiny = thue(96)
        pref = all_prefix_counts(tiny, words, ix)
        for s in range(0, 12):
            for n in range(0, 11):
                assert factor_counts(pref, s, s+n, words, ix) == direct_counts(tiny[s:s+n], r, words)
    print('VERIFY_OK: arbitrary binary-source transport checks and exact dyadic occurrence criterion at all starts 0..255, orders 1..5, k<=8; direct count cross-checks')

if __name__ == '__main__':
    run()
