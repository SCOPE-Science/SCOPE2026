#!/usr/bin/env python3
"""Standalone exhaustive verification of the Desargues anti-forcing classification.

Run: python3 verify.py
Only the Python standard library is used.
"""
from collections import Counter
from itertools import combinations, permutations

PAIRS = tuple(combinations(range(5), 2))
INDEX = {p: i for i, p in enumerate(PAIRS)}
ADJ = tuple(tuple(j for j, b in enumerate(PAIRS)
                  if set(a).isdisjoint(b)) for a in PAIRS)
EDGES = tuple((i, j) for i in range(10) for j in ADJ[i])
assert len(EDGES) == 30 and all(len(q) == 3 for q in ADJ)


def enumerate_matchings():
    """All bijections f(i)=j allowed by the incidence condition."""
    out = []
    def walk(i, used, a):
        if i == 10:
            out.append(tuple(a))
            return
        for j in ADJ[i]:
            if not used & (1 << j):
                a.append(j)
                walk(i + 1, used | (1 << j), a)
                a.pop()
    walk(0, 0, [])
    return tuple(out)


def assignment_count():
    """Independent subset recurrence for the bipartite permanent."""
    counts = [0] * (1 << 10)
    counts[0] = 1
    for mask in range(1 << 10):
        row = mask.bit_count()
        if row == 10:
            continue
        for col in ADJ[row]:
            if not mask & (1 << col):
                counts[mask | (1 << col)] += counts[mask]
    return counts[-1]


def complementary_lengths(f):
    """Cycle lengths of the 2-factor left after removing the matching."""
    residual = [[] for _ in range(20)]
    for i, j in EDGES:
        if f[i] != j:
            residual[i].append(10 + j)
            residual[10 + j].append(i)
    assert all(len(q) == 2 for q in residual)
    visited = set()
    lengths = []
    for s in range(20):
        if s in visited:
            continue
        stack = [s]
        visited.add(s)
        for a in stack:
            for b in residual[a]:
                if b not in visited:
                    visited.add(b)
                    stack.append(b)
        lengths.append(len(stack))
    return tuple(sorted(lengths))


def anti_forcing_dp(f):
    """Exact minimum feedback-arc deletion after contracting f."""
    inverse = [0] * 10
    for i, j in enumerate(f):
        inverse[j] = i
    incoming = [0] * 10
    total_arcs = 0
    for i, j in EDGES:
        if f[i] != j:
            source, target = inverse[j], i
            assert source != target
            incoming[target] |= 1 << source
            total_arcs += 1
    assert total_arcs == 20
    dp = [-1] * (1 << 10)
    dp[0] = 0
    for mask in range(1, 1 << 10):
        vertices = mask
        optimum = -1
        while vertices:
            bit = vertices & -vertices
            v = bit.bit_length() - 1
            before = mask ^ bit
            optimum = max(optimum, dp[before] + (incoming[v] & before).bit_count())
            vertices ^= bit
        dp[mask] = optimum
    return 20 - dp[-1]


def anti_forcing_hitting(f, matchings):
    """Independent complete transversal search among all alternative matchings."""
    base = set((i, f[i]) for i in range(10))
    candidates = [edge for edge in EDGES if edge not in base]
    changes = []
    for g in matchings:
        if g == f:
            continue
        gset = set((i, g[i]) for i in range(10))
        difference = gset - base
        changes.append(sum(1 << j for j, e in enumerate(candidates)
                           if e in difference))
    assert len(changes) == len(matchings) - 1
    assert all(mask for mask in changes)
    # Exact search, not a greedy hitting-set approximation.
    for k in range(21):
        for chosen in combinations(range(20), k):
            mask = sum(1 << j for j in chosen)
            if all(mask & cycle for cycle in changes):
                return k, tuple(candidates[j] for j in chosen)
    raise AssertionError('No anti-forcing set found')


def permutation_actions():
    """The explicit faithful action of S_5 times the layer swap."""
    for sigma in permutations(range(5)):
        p = tuple(INDEX[tuple(sorted(sigma[k] for k in a))] for a in PAIRS)
        for swap in (False, True):
            yield p, swap


def transform(f, p, swap):
    out = [-1] * 10
    for i, j in enumerate(f):
        if swap:
            out[p[j]] = p[i]
        else:
            out[p[i]] = p[j]
    return tuple(out)


def cycle_type_on_petersen(f):
    seen = set()
    lengths = []
    for i in range(10):
        if i in seen:
            continue
        j = i
        count = 0
        while j not in seen:
            seen.add(j)
            count += 1
            j = f[j]
        lengths.append(count)
    return tuple(sorted(lengths))


def main():
    matchings = enumerate_matchings()
    assert len(matchings) == 60 == assignment_count()
    unique = set(matchings)
    assert len(unique) == 60
    actions = tuple(permutation_actions())
    assert len(actions) == 240
    for p, swap in actions:
        assert all(p[j] in ADJ[p[i]] for i, j in EDGES)
        assert set(transform(f, p, swap) for f in matchings) == unique
    unseen = set(matchings)
    profile = Counter()
    detailed = []
    while unseen:
        rep = min(unseen)
        orbit = {transform(rep, p, swap) for p, swap in actions}
        assert orbit <= unseen
        unseen -= orbit
        size = len(orbit)
        lengths = complementary_lengths(rep)
        ftype = cycle_type_on_petersen(rep)
        af_dp = anti_forcing_dp(rep)
        af_brute, witness = anti_forcing_hitting(rep, matchings)
        assert af_dp == af_brute
        assert all(anti_forcing_dp(f) == af_dp for f in orbit)
        assert all(complementary_lengths(f) == lengths for f in orbit)
        assert all(cycle_type_on_petersen(f) == ftype for f in orbit)
        profile[(size, lengths, ftype, af_dp)] += 1
        detailed.append((size, lengths, ftype, af_dp, rep, witness))
    expected = Counter({
        (6, (10, 10), (2, 2, 2, 2, 2), 5): 1,
        (24, (20,), (5, 5), 6): 1,
        (30, (10, 10), (2, 8), 6): 1,
    })
    assert profile == expected, (profile, expected)
    assert sum(s for s, *_ in detailed) == 60
    # Exceptional orbit comprises precisely the layer-symmetric matchings;
    # these are bijective with the six perfect matchings of the Petersen graph.
    symmetric = {f for f in matchings if all(f[f[i]] == i for i in range(10))}
    assert len(symmetric) == 6
    assert symmetric == {f for f in matchings if anti_forcing_dp(f) == 5}
    for size, cycles, ftype, af, rep, witness in sorted(detailed):
        print(f'ORBIT size={size} complement={cycles} permutation_cycles={ftype} '
              f'anti_forcing={af} representative={rep} witness={witness}')
    print('PROFILE 6*z^5 + 54*z^6; perfect_matchings=60; automorphism_actions=240')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
