#!/usr/bin/env python3
"""Reproducible checks for two short arrow-pattern avoidance classes.
Only the standard Python library is required.
"""
from itertools import permutations
from math import comb, factorial


def cycle_word(mapping):
    n = len(mapping)
    unseen = set(range(1, n + 1))
    cycles = []
    while unseen:
        start = min(unseen)
        cyc = []
        x = start
        while x in unseen:
            unseen.remove(x)
            cyc.append(x)
            x = mapping[x - 1]
        k = cyc.index(max(cyc))
        cyc = cyc[k:] + cyc[:k]
        cycles.append(cyc)
    cycles.sort(key=lambda c: c[0])
    return tuple(x for c in cycles for x in c)


def contains_arrow(word, mapping, variant):
    # Check the literal three-symbol arrow definition, not the fixed-point shortcut.
    n = len(word)
    for i in range(n):
        for j in range(i + 1, n):
            x, y = word[i], word[j]
            if variant == '12;3->3' and x < y:
                for z in range(y + 1, n + 1):
                    if mapping[z - 1] == z:
                        return True
            if variant == '23;1->1' and x < y:
                for z in range(1, x):
                    if mapping[z - 1] == z:
                        return True
    return False


def shortcut(word, mapping, variant):
    fixed = [i for i, x in enumerate(mapping, 1) if i == x]
    if not fixed:
        return True
    if variant == '12;3->3':
        seq = [x for x in word if x < max(fixed)]
    else:
        seq = [x for x in word if x > min(fixed)]
    return all(x > y for x, y in zip(seq, seq[1:]))


def derangements(maxn):
    d = [1, 0]
    for n in range(2, maxn + 1):
        d.append((n - 1) * (d[-1] + d[-2]))
    return d[:maxn + 1]


def first_formula(n, d):
    out = d[n]
    for b in range(n):
        f = n - b
        if b == 0:
            out += 1
        else:
            for r in range(f):
                for j in range(min(b, r) + 1):
                    out += comb(b, j) * d[b - j] * comb(b + r - j - 1, r - j)
    return out


def second_formula(n, d):
    out = d[n]
    for b in range(n):
        a = n - b - 1
        for r in range(a + 1):
            rising = 1
            for t in range(r):
                rising *= b + t
            out += comb(a, r) * d[a - r] * rising
    return out


def moments_formula(N, d):
    # Coefficients of D(z) + z/q(z) D(z/q(z)), q(z)=1-z-z^2.
    # First construct u(z)=z/(1-z-z^2), and powers of 1/q.
    series = [0] * (N + 1)
    for k in range(N):
        # coefficient of z^(k+1) q^-(k+1), times d_k
        # q^-m computed from (1-z-z^2) h = q^-(m-1)
        prev = [0] * (N - k)
        prev[0] = 1
        for _ in range(k + 1):
            curr = [0] * (N - k)
            for h in range(N - k):
                curr[h] = prev[h] + (curr[h - 1] if h else 0) + (curr[h - 2] if h >= 2 else 0)
            prev = curr
        for j, c in enumerate(prev):
            if k + 1 + j <= N:
                series[k + 1 + j] += d[k] * c
    return [d[n] + series[n] for n in range(N + 1)]


def main():
    D = derangements(22)
    M = moments_formula(18, D)
    for n in range(1, 19):
        x, y = first_formula(n, D), second_formula(n, D)
        assert x == y == M[n], (n, x, y, M[n])
    print('symbolic coefficient identity: PASS through n=18')
    for n in range(1, 9):
        A = B = 0
        for mapping in permutations(range(1, n + 1)):
            word = cycle_word(mapping)
            for variant in ('12;3->3', '23;1->1'):
                valid = shortcut(word, mapping, variant)
                if n <= 7:
                    assert valid == (not contains_arrow(word, mapping, variant)), (n, mapping, word, variant)
                if valid:
                    if variant == '12;3->3': A += 1
                    else: B += 1
        assert A == B == M[n], (n, A, B, M[n])
        print('n=', n, 'first=', A, 'second=', B, 'PASS')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
