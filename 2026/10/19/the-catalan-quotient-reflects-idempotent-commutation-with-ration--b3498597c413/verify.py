#!/usr/bin/env python3
"""Exact finite-state and small-rank checks for 0-Hecke idempotent commutation."""
from collections import defaultdict
from itertools import product


def step(state, word, r):
    pairs = [(i, j) for i in range(r) for j in range(i + 1, r)]
    out = []
    for t, (i, j) in enumerate(pairs):
        x, y = (word >> i) & 1, (word >> j) & 1
        if x == y == 0:
            out.append(0)
        elif x != y:
            side = 1 if x else 2
            if state[t] not in (0, side):
                return None
            out.append(side)
        else:
            out.append(state[t])
    return tuple(out)


def transfer(r):
    start = (0,) * (r * (r - 1) // 2)
    states = [start]
    idx = {start: 0}
    outgoing = []
    for state in states:
        out = defaultdict(int)
        for word in range(1 << r):
            nxt = step(state, word, r)
            if nxt is None:
                continue
            if nxt not in idx:
                idx[nxt] = len(states)
                states.append(nxt)
            out[idx[nxt]] += 1
        outgoing.append(dict(out))
    return states, outgoing


def counts(r, upto):
    states, trans = transfer(r)
    v = [0] * len(states)
    v[0] = 1
    output = []
    for _ in range(upto + 1):
        output.append(sum(v))
        new = [0] * len(states)
        for i, old in enumerate(v):
            for j, mult in trans[i].items():
                new[j] += old * mult
        v = new
    return states, trans, output


def parabolic_longest(mask, n):
    w = list(range(n + 1))
    i = 0
    while i < n:
        if not (mask >> i) & 1:
            i += 1
            continue
        j = i
        while j < n and (mask >> j) & 1:
            j += 1
        w[i:j + 1] = reversed(w[i:j + 1])
        i = j
    return tuple(w)


def reduced_word(w):
    a = list(w)
    seq = []
    while any(a[i] > a[i + 1] for i in range(len(a) - 1)):
        i = next(i for i in range(len(a) - 1) if a[i] > a[i + 1])
        a[i], a[i + 1] = a[i + 1], a[i]
        seq.append(i)
    return list(reversed(seq))


def demazure(x, seq):
    a = list(x)
    for i in seq:
        if a[i] < a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    return tuple(a)


def cat_idempotent(mask, n):
    # Here bits of mask index 0,...,n-1, and generators act on n+1 points.
    fixed = [0] + [i + 1 for i in range(n) if not (mask >> i) & 1]
    return tuple(max(k for k in fixed if k <= j) for j in range(n + 1))


def compose(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def test_small():
    wanted = [1, 8, 46, 254, 1390, 7592]
    for n in range(0, 7):
        mm = 1 << n
        ws = [parabolic_longest(i, n) for i in range(mm)]
        seqs = [reduced_word(w) for w in ws]
        cs = [cat_idempotent(i, n) for i in range(mm)]
        gens = []
        for a in range(n):
            g = list(range(n + 1))
            g[a + 1] = a
            gens.append(tuple(g))
        ident = tuple(range(n + 1))
        for i in range(mm):
            f = ident
            for g in seqs[i]:
                f = compose(f, gens[g])
            assert f == cs[i], (n, i, 'quotient image')
        commuting = [[False] * mm for _ in range(mm)]
        for i in range(mm):
            for j in range(mm):
                p1 = demazure(ws[i], seqs[j])
                p2 = demazure(ws[j], seqs[i])
                hecke = p1 == p2
                catalan = compose(cs[i], cs[j]) == compose(cs[j], cs[i])
                assert hecke == catalan, (n, i, j)
                if hecke:
                    assert p1 == ws[i | j]
                    assert compose(cs[i], cs[j]) == cs[i | j]
                commuting[i][j] = hecke
        if n <= 5:
            total = sum(commuting[i][j] and commuting[j][k] and commuting[i][k]
                        for i in range(mm) for j in range(mm) for k in range(mm))
            assert total == wanted[n], (n, total)


def test_matrix_certificate():
    states, trans, a = counts(3, 30)
    assert len(states) == 13
    assert a[:12] == [1, 8, 46, 254, 1390, 7592, 41452, 226316,
                      1235620, 6746144, 36832120, 201093464]
    assert a[0] == 1 and a[1] - 8*a[0] == 0
    assert a[2] - 8*a[1] + 16*a[0] == -2
    assert a[3] - 8*a[2] + 16*a[1] - 12*a[0] == 2
    # The vanishing for 13 consecutive exponents gives an exact
    # 13-dimensional Cayley-Hamilton certificate, not an extrapolation.
    for n in range(4, 17):
        assert a[n] - 8*a[n - 1] + 16*a[n - 2] - 12*a[n - 3] + 2*a[n - 4] == 0
    for n in range(17, 31):
        assert a[n] - 8*a[n - 1] + 16*a[n - 2] - 12*a[n - 3] + 2*a[n - 4] == 0
    for r in (1, 2, 4):
        st, _, values = counts(r, 7)
        assert values[0] == 1 and values[1] == 2 ** r
        assert 1 <= len(st) <= 3 ** (r * (r - 1) // 2)


if __name__ == '__main__':
    test_matrix_certificate()
    test_small()
    print('VERIFY_OK')
