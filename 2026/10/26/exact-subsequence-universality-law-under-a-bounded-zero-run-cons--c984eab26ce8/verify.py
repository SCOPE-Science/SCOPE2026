#!/usr/bin/env python3
"""Self-contained verification for the zero-run-limited subsequence-universality law.
Run with Python 3.10 or later; no third-party packages.
"""
from collections import defaultdict
from itertools import product


def greedy_index(word):
    seen = 0
    arches = 0
    for a in word:
        seen |= 1 << a
        if seen == 3:
            arches += 1
            seen = 0
    return arches


def direct_index(word):
    def contains(seq):
        at = 0
        for a in word:
            if at < len(seq) and a == seq[at]:
                at += 1
        return at == len(seq)
    k = 0
    while k + 1 <= len(word):
        test = k + 1
        if all(contains(seq) for seq in product(range(2), repeat=test)):
            k += 1
        else:
            break
    return k


def rational_hist(r, nmax):
    # (1-z-2uz^2+u z^(r+2)+u^2 z^(r+3))G=1+z-z^(r+1)-u z^(r+2).
    v = [defaultdict(int) for _ in range(nmax + 1)]
    for n in range(nmax + 1):
        rhs = {0: (int(n == 0) + int(n == 1) - int(n == r + 1)),
               1: -int(n == r + 2)}
        v[n].update(rhs)
        if n >= 1:
            for k, c in v[n - 1].items():
                v[n][k] += c
        if n >= 2:
            for k, c in v[n - 2].items():
                v[n][k + 1] += 2 * c
        if n >= r + 2:
            for k, c in v[n - r - 2].items():
                v[n][k + 1] -= c
        if n >= r + 3:
            for k, c in v[n - r - 3].items():
                v[n][k + 2] -= c
        v[n] = {k: c for k, c in v[n].items() if c}
        assert all(k >= 0 and c > 0 for k, c in v[n].items()), (r, n, v[n])
    return v


def automaton_hist(r, nmax):
    # DFA: (trailing 0 length, current arch mask), with a count when a second symbol appears.
    curr = {(0, 0, 0): 1}
    out = []
    for n in range(nmax + 1):
        hist = defaultdict(int)
        for (_, _, k), ways in curr.items():
            hist[k] += ways
        out.append(dict(hist))
        nxt = defaultdict(int)
        for (run, mask, k), ways in curr.items():
            for a in (0, 1):
                if a == 0 and run == r:
                    continue
                run2 = run + 1 if a == 0 else 0
                mask2 = mask | (1 << a)
                k2 = k + int(mask2 == 3)
                if mask2 == 3:
                    mask2 = 0
                nxt[(run2, mask2, k2)] += ways
        curr = nxt
    return out


def brute_hist(r, n):
    out = defaultdict(int)
    for t in product((0, 1), repeat=n):
        if '0' * (r + 1) in ''.join(map(str, t)):
            continue
        out[greedy_index(t)] += 1
    return dict(out)


def exact_totals(r, nmax):
    # Ordinary language count via forbidden 0-run DFA, independent of arches.
    curr = [1] + [0] * r
    out = [1]
    for _ in range(nmax):
        nxt = [sum(curr)] + curr[:-1]
        curr = nxt
        out.append(sum(curr))
    return out


def main():
    compared = 0
    for r in range(1, 9):
        nmax = 125
        a = rational_hist(r, nmax)
        b = automaton_hist(r, nmax)
        total = exact_totals(r, nmax)
        for n in range(nmax + 1):
            assert a[n] == b[n], ('rational v automaton', r, n, a[n], b[n])
            assert sum(a[n].values()) == total[n], ('unweighted', r, n)
            compared += 1
        for n in range(0, 15):
            assert brute_hist(r, n) == a[n], ('brute', r, n)
    for n in range(0, 11):
        for t in product((0, 1), repeat=n):
            assert greedy_index(t) == direct_index(t), ('arch identity', t)
    # The unbounded case has the independently known rational law.
    r = 160
    a = rational_hist(r, 120)
    for n in range(121):
        # For n<r+1, recurrence reduces to the unrestricted binary law.
        assert sum(a[n].values()) == 2**n
    print('RUN_LIMIT_ARCH_LAW_PASS r=1..8 lengths=0..125 direct_lengths=0..14 arch_definition=0..10 histogram_compared='+str(compared))


if __name__ == '__main__':
    main()
