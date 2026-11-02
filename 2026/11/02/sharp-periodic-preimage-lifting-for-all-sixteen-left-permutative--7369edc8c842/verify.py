#!/usr/bin/env python3
"""Exact finite-semigroup certificate for spatial preimage multipliers.

Runs with the Python 3 standard library. Its closure tests quantify over all
finite target words, not merely words up to a chosen length.
"""
from collections import deque, defaultdict
from itertools import product

STATES = tuple(range(4))
IDENTITY = STATES
# The generators g are indexed by g(b,c), with index 2*b+c.
EXPECTED = {
    0: (240, 7, {1: 7}),
    1: (225, 41, {1: 30, 2: 9, 3: 2}),
    2: (210, 21, {1: 18, 2: 3}),
    3: (195, 5, {1: 3, 2: 2}),
    4: (180, 21, {1: 18, 2: 3}),
    5: (165, 8, {1: 3, 2: 3, 4: 2}),
    6: (150, 12, {1: 9, 2: 3}),
    7: (135, 41, {1: 30, 2: 9, 3: 2}),
    8: (120, 41, {1: 30, 2: 9, 3: 2}),
    9: (105, 12, {1: 9, 2: 3}),
    10: (90, 8, {1: 3, 2: 3, 4: 2}),
    11: (75, 21, {1: 18, 2: 3}),
    12: (60, 5, {1: 3, 2: 2}),
    13: (45, 21, {1: 18, 2: 3}),
    14: (30, 41, {1: 30, 2: 9, 3: 2}),
    15: (15, 7, {1: 7}),
}


def compose(f, h):
    return tuple(f[h[s]] for s in STATES)


def generator(g, y):
    return tuple(2 * (y ^ ((g >> s) & 1)) + s // 2 for s in STATES)


def wolfram_code(g):
    return sum((a ^ ((g >> (2*b+c)) & 1)) << (4*a+2*b+c)
               for a in (0, 1) for b in (0, 1) for c in (0, 1))


def cycle_lengths(f):
    marked = set()
    lengths = []
    for u in STATES:
        if u in marked:
            continue
        path, where = [], {}
        while u not in marked and u not in where:
            where[u] = len(path)
            path.append(u)
            u = f[u]
        if u in where:
            lengths.append(len(path) - where[u])
        marked.update(path)
    return tuple(sorted(lengths))


def minimum_multiplier(f):
    return min(cycle_lengths(f))


def semigroup(g):
    T = [generator(g, y) for y in (0, 1)]
    queue = deque([IDENTITY])
    shortest = {IDENTITY: ''}
    while queue:
        f = queue.popleft()
        for y in (0, 1):
            nxt = compose(f, T[y])
            if nxt not in shortest:
                shortest[nxt] = shortest[f] + str(y)
                queue.append(nxt)
    assert all(compose(f, t) in shortest for f in shortest for t in T)
    return shortest


def exceptional(g, n_mod6, parity, all_zero, all_one):
    if g in (1, 7):
        return 3 if all_zero and n_mod6 % 3 else 0
    if g in (8, 14):
        return 3 if all_one and n_mod6 % 3 else 0
    if g == 5:
        return 4 if n_mod6 % 2 and parity == 0 else 0
    if g == 10:
        return 4 if n_mod6 % 2 and parity == 1 else 0
    return 0


def all_lengths_certificate(g):
    T = [generator(g, y) for y in (0, 1)]
    # (transformation, length mod 6, ones parity, all-zero, all-one, nonempty)
    origin = (IDENTITY, 0, 0, True, True, False)
    queue, seen = deque([origin]), {origin}
    while queue:
        state = queue.popleft()
        f, n6, parity, az, ao, nonempty = state
        if nonempty:
            m = minimum_multiplier(f)
            high = exceptional(g, n6, parity, az, ao)
            if high:
                assert m == high, (g, state, m, high)
            else:
                assert m in (1, 2), (g, state, m)
            if g in (0, 15):
                assert m == 1
        for y in (0, 1):
            nxt = (compose(f, T[y]), (n6 + 1) % 6, parity ^ y,
                   az and y == 0, ao and y == 1, True)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return len(seen)


def forward(rule, bits):
    n = len(bits)
    return tuple((rule >> (4 * bits[(i-1) % n] +
                           2 * bits[i] + bits[(i+1) % n])) & 1
                 for i in range(n))


def shortest_nonempty_witnesses(g):
    T = [generator(g, y) for y in (0, 1)]
    queue = deque([(IDENTITY, '')])
    discovered = {IDENTITY: ''}
    witness = {}
    # Avoid treating the empty word as an admissible output.
    for y in (0, 1):
        f = T[y]
        m = minimum_multiplier(f)
        witness.setdefault(m, str(y))
    while queue:
        f, w = queue.popleft()
        for y in (0, 1):
            nxt = compose(f, T[y]); nw = w + str(y)
            m = minimum_multiplier(nxt)
            if m not in witness:
                witness[m] = nw
            if nxt not in discovered:
                discovered[nxt] = nw; queue.append((nxt, nw))
    return witness


def direct_small_ring_check():
    # A separate, forward-image exhaustive check; 2^N inputs for each N<=12.
    # In particular this does not use the four-state inverse recurrence.
    counts = 0
    for g, (rule, _, _) in EXPECTED.items():
        images = {}
        for N in range(1, 13):
            images[N] = {forward(rule, x) for x in product((0, 1), repeat=N)}
        for n in range(1, 7):
            for y in product((0, 1), repeat=n):
                phi = IDENTITY
                for c in y:
                    phi = compose(phi, generator(g, c))
                for m in range(1, 12 // n + 1):
                    by_cycles = any(length <= m and m % length == 0
                                    for length in cycle_lengths(phi))
                    by_direct = y * m in images[n * m]
                    assert by_cycles == by_direct, (g, n, y, m)
                    counts += 1
    return counts


def main():
    witnesses = {}
    assert len(set(v[0] for v in EXPECTED.values())) == 16
    for g, (rule, size, expected_counts) in EXPECTED.items():
        assert wolfram_code(g) == rule
        sg = semigroup(g)
        assert len(sg) == size, (g, len(sg), size)
        counts = defaultdict(int)
        witnesses[rule] = shortest_nonempty_witnesses(g)
        assert set(witnesses[rule]) == set(expected_counts)
        for f, word in sg.items():
            m = minimum_multiplier(f)
            counts[m] += 1
        assert dict(counts) == expected_counts, (g, dict(counts))
        reached = all_lengths_certificate(g)
        print(f'rule={rule:3} transformations={len(sg):2} '
              f'minimum-multiplier-counts={dict(sorted(counts.items()))} '
              f'augmented-states={reached}')
    checks = direct_small_ring_check()
    print(f'direct-forward-comparisons={checks}')
    print('sharp-example-words:', witnesses)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
