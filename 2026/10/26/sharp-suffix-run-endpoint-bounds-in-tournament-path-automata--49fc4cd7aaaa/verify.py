"""Finite verification for tournament remanent-language run theorem.

Enumerates every labeled tournament through six vertices, and searches the
product of its NFA subset transition and the run-avoiding DFA for an
arbitrarily long counterexample. Also independently minimizes the DFA.
"""
from itertools import combinations
from collections import deque


def dfa(n):
    # Initial 0, followed by (last letter, run length) states, then sink.
    states = [(None, 0)] + [(b, r) for b in (0, 1) for r in range(1, n)] + [('sink', 0)]
    index = {s: i for i, s in enumerate(states)}
    sink = index[('sink', 0)]
    delta = []
    for last, run in states:
        if last == 'sink':
            delta.append((sink, sink))
        else:
            row = []
            for b in (0, 1):
                nr = run + 1 if last == b else 1
                row.append(sink if nr == n else index[(b, nr)])
            delta.append(tuple(row))
    return states, delta, sink


def minimize_count(n):
    states, trans, sink = dfa(n)
    block = [int(i == sink) for i in range(len(states))]
    while True:
        keys = [(block[i], block[trans[i][0]], block[trans[i][1]]) for i in range(len(states))]
        ids = {key: i for i, key in enumerate(sorted(set(keys)))}
        update = [ids[key] for key in keys]
        if len(set(update)) == len(set(block)):
            return len(set(update))
        block = update


def verify_tournament(n, bits):
    edges = list(combinations(range(n), 2))
    f = [0] * n
    b = [0] * n
    for j, (i, k) in enumerate(edges):
        u, v = (i, k) if not ((bits >> j) & 1) else (k, i)
        f[u] |= 1 << v
        b[v] |= 1 << u
    trans = [[0] * (1 << n) for _ in range(2)]
    for mask in range(1, 1 << n):
        bit = mask & -mask
        i = bit.bit_length() - 1
        smaller = mask ^ bit
        trans[0][mask] = trans[0][smaller] | f[i]
        trans[1][mask] = trans[1][smaller] | b[i]
    initial = ((1 << n) - 1, 2, 0)
    todo = deque([initial])
    seen = {initial}
    while todo:
        S, last, r = todo.popleft()
        for c in (0, 1):
            nr = r + 1 if last == c else 1
            if nr >= n:
                continue  # outside claimed remanent language
            new_S = trans[c][S]
            assert new_S, (n, bits, S, last, r, c)
            # Stronger predicted size bound.
            assert new_S.bit_count() >= n - nr, (n, bits, S, last, r, c)
            state = (new_S, c, nr)
            if state not in seen:
                seen.add(state)
                todo.append(state)


def coefficient_counts(n, limit):
    words = [('', 0, 0)]
    actual = [1]
    for m in range(1, limit+1):
        nxt = []
        for w, last, r in words:
            for c in (0, 1):
                nr = r + 1 if w and last == c else 1
                if nr < n:
                    nxt.append((w + str(c), c, nr))
        words = nxt
        actual.append(len(words))
    # From (1-2z+z^n)F = 1-z^n.
    predicted = [0] * (limit + 1)
    for m in range(limit + 1):
        predicted[m] = (1 if m == 0 else 0) - (1 if m == n else 0)
        if m >= 1:
            predicted[m] += 2 * predicted[m-1]
        if m >= n:
            predicted[m] -= predicted[m-n]
    assert actual == predicted, (n, actual, predicted)
    return actual


def main():
    for n in range(2, 7):
        for bits in range(1 << (n * (n-1) // 2)):
            verify_tournament(n, bits)
        assert minimize_count(n) == 2*n
        cnt = coefficient_counts(n, 12)
        print('n=%d tournaments=%d minimal_states=%d counts_first_8=%s' % (
            n, 1 << (n*(n-1)//2), 2*n, cnt[:8]))
    for n in (7, 8):
        assert minimize_count(n) == 2*n
        coefficient_counts(n, 12)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
