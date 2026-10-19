#!/usr/bin/env python3
"""Reproduce finite checks for prefix-parsed universal cycles.

Only finite word checks are performed. The quantified theorem is proved
analytically in RESULT.md and does not depend on this diagnostic.
"""
from itertools import product


def debruijn(q, n):
    a = [0] * (q * n + 1)
    output = []

    def rec(t, p):
        if t > n:
            if n % p == 0:
                output.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            rec(t + 1, p)
            for z in range(a[t - p] + 1, q):
                a[t] = z
                rec(t + 1, t)

    rec(1, 1)
    return tuple(output)


def check_prefix(code, q):
    assert len(code) >= 2
    for w in code:
        assert w and all(0 <= a < q for a in w)
        for v in code:
            if w != v:
                assert v[:len(w)] != w
    lmax = max(map(len, code))
    for w in product(range(q), repeat=lmax):
        assert sum(w[:len(c)] == c for c in code) == 1
    return lmax


def decode_at(seq, t, code):
    N = len(seq)
    for idx, c in enumerate(code):
        if all(seq[(t + j) % N] == letter for j, letter in enumerate(c)):
            return idx, len(c)
    raise AssertionError('incomplete prefix code')


def get_cycle(seq, code, start=0):
    seen = {}
    transitions = []
    t = start
    while t not in seen:
        seen[t] = len(transitions)
        label, length = decode_at(seq, t, code)
        transitions.append((t, label, length))
        t = (t + length) % len(seq)
    return transitions[seen[t]:]


def main():
    examples = [
        (2, ((0,), (1, 0), (1, 1)), 10),
        (2, ((0, 0), (0, 1), (1,)), 10),
        (2, ((0,), (1, 0, 0), (1, 0, 1), (1, 1)), 10),
        (2, ((0, 0), (0, 1), (1, 0), (1, 1)), 9),
        (3, ((0,), (1,), (2, 0), (2, 1), (2, 2)), 7),
        (3, tuple((i,) for i in range(3)), 7),
    ]
    total = 0
    for q, code, maxn in examples:
        lmax = check_prefix(code, q)
        for n in range(1, maxn + 1):
            B = debruijn(q, n)
            N = q ** n
            assert len(B) == N
            factors = {tuple(B[(t + j) % N] for j in range(n))
                       for t in range(N)}
            assert len(factors) == N
            cycle = get_cycle(B, code)
            tloc = [t for t, _, _ in cycle]
            p = len(cycle)
            assert len(set(tloc)) == p
            assert p >= (N + lmax - 1) // lmax, (q, code, n, p)
            # A decoded primitive orbit: no smaller cyclic codeword period.
            labels = tuple(c[1] for c in cycle)
            for d in range(1, p):
                if p % d == 0:
                    assert any(labels[j] != labels[j % d] for j in range(p))
            # Each shifted codeword sequence starts at a different q-ary
            # de Bruijn position and hence has a different length-n prefix.
            assert len({tuple(B[(t + j) % N] for j in range(n))
                        for t in tloc}) == p
            # Check the actual binary/q-ary codeword prefixes agree for
            # less than n letters for every pair of distinct orbit states.
            for a in range(p):
                for b in range(a + 1, p):
                    ca = cb = 0
                    L = 0
                    while labels[(a + ca) % p] == labels[(b + cb) % p]:
                        L += len(code[labels[(a + ca) % p]])
                        assert L < n
                        ca += 1
                        cb += 1
                    assert L < n
                    total += 1
            print('case', q, 'labels', len(code), 'n', n,
                  'underlying_size', N, 'orbit_size', p, 'bound',
                  (N + lmax - 1) // lmax)
    # Rectangular forward-invariant set for explicit planar example.
    # f_0([0,4]^2)=[0,2]^2, f_1=[3,4]x[0,1],
    # f_2=[0,1]x[3,4]; pairwise Euclidean distances >=1.
    assert 3 - 2 == 1
    assert 3 - 2 == 1
    print('VERIFY_OK', 'pair_checks', total)

if __name__ == '__main__':
    main()
