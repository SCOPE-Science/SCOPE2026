#!/usr/bin/env python3
from itertools import permutations
from fractions import Fraction
from collections import Counter


def antichains(n):
    """All nonempty antichains of nonempty subsets of [n]."""
    subs = list(range(1, 1 << n))
    comp = {
        s: {t for t in subs if t != s and (((s & t) == s) or ((s & t) == t))}
        for s in subs
    }
    out = []
    def rec(cands, chosen):
        if not cands:
            if chosen:
                out.append(tuple(sorted(chosen)))
            return
        s = min(cands)
        rec(cands - {s}, chosen)
        rec((cands - {s}) - comp[s], chosen + (s,))
    rec(set(subs), ())
    return tuple(out)


def value(fam, S):
    return int(any((m & S) == m for m in fam))


def proper(n, fam):
    N = (1 << n) - 1
    return all(not (value(fam, S) and value(fam, N ^ S)) for S in range(1 << n))


def banzhaf_losing(n, fam):
    swings = [0] * n
    for S in range(1 << n):
        if value(fam, S):
            continue
        for i in range(n):
            if not ((S >> i) & 1) and value(fam, S | (1 << i)):
                swings[i] += 1
    total = sum(swings)
    return tuple(Fraction(x, total) for x in swings), tuple(swings)


def banzhaf_winning(n, fam):
    swings = [0] * n
    for S in range(1, 1 << n):
        if not value(fam, S):
            continue
        for i in range(n):
            if ((S >> i) & 1) and not value(fam, S & ~(1 << i)):
                swings[i] += 1
    total = sum(swings)
    return tuple(Fraction(x, total) for x in swings), tuple(swings)


def johnston_by_coalition(n, fam):
    raw = [Fraction(0) for _ in range(n)]
    for S in range(1, 1 << n):
        if not value(fam, S):
            continue
        crit = [i for i in range(n) if ((S >> i) & 1) and not value(fam, S & ~(1 << i))]
        if crit:
            share = Fraction(1, len(crit))
            for i in crit:
                raw[i] += share
    total = sum(raw)
    return tuple(x / total for x in raw), tuple(raw)


def johnston_by_player(n, fam):
    raw = [Fraction(0) for _ in range(n)]
    for i in range(n):
        for S in range(1, 1 << n):
            if not ((S >> i) & 1) or not value(fam, S) or value(fam, S & ~(1 << i)):
                continue
            k = sum(
                1 for j in range(n)
                if ((S >> j) & 1) and not value(fam, S & ~(1 << j))
            )
            raw[i] += Fraction(1, k)
    total = sum(raw)
    return tuple(x / total for x in raw), tuple(raw)


def weak_order(v):
    return tuple(
        (v[i] > v[j]) - (v[i] < v[j])
        for i in range(len(v)) for j in range(i + 1, len(v))
    )


def relabel_family(fam, p, n):
    out = []
    for S in fam:
        T = 0
        for i in range(n):
            if (S >> i) & 1:
                T |= 1 << p[i]
        out.append(T)
    return tuple(sorted(out))


def canonical_family(fam, n):
    return min(relabel_family(fam, p, n) for p in permutations(range(n)))


def refinement_check(b, j):
    changes = []
    for i in range(len(b)):
        for k in range(i + 1, len(b)):
            sb = (b[i] > b[k]) - (b[i] < b[k])
            sj = (j[i] > j[k]) - (j[i] < j[k])
            if sb != sj:
                changes.append((i, k, sb, sj))
            if sb != 0:
                assert sj == sb
            if sb == 0 and sj != 0:
                assert sj in (-1, 1)
    return tuple(changes)


proper_counts = {}
iso_counts = {}
divergence_counts = {}
div_orbits = Counter()
orbit_data = {}
change_hist = Counter()

for n in range(1, 6):
    games = antichains(n)
    # Standard small Dedekind numbers after deleting the two constant games.
    expected_simple = {1: 1, 2: 4, 3: 18, 4: 166, 5: 7579}
    assert len(games) == expected_simple[n]

    pc = 0
    dc = 0
    classes = set()
    for fam in games:
        if not proper(n, fam):
            continue
        pc += 1
        classes.add(canonical_family(fam, n))

        b1, bs1 = banzhaf_losing(n, fam)
        b2, bs2 = banzhaf_winning(n, fam)
        assert b1 == b2 and bs1 == bs2

        j1, jr1 = johnston_by_coalition(n, fam)
        j2, jr2 = johnston_by_player(n, fam)
        assert j1 == j2 and jr1 == jr2
        assert sum(b1) == 1 and sum(j1) == 1

        if weak_order(b1) != weak_order(j1):
            dc += 1
            changes = refinement_check(b1, j1)
            assert changes
            change_hist[len(changes)] += 1
            if n == 5:
                c = canonical_family(fam, n)
                div_orbits[c] += 1
                orbit_data.setdefault(c, (banzhaf_losing(n, c)[0], johnston_by_coalition(n, c)[0]))

    proper_counts[n] = pc
    iso_counts[n] = len(classes)
    divergence_counts[n] = dc

assert proper_counts == {1: 1, 2: 3, 3: 11, 4: 80, 5: 2645}
assert iso_counts == {1: 1, 2: 2, 3: 5, 4: 14, 5: 86}
assert divergence_counts == {1: 0, 2: 0, 3: 0, 4: 0, 5: 480}
assert div_orbits == Counter({
    (3, 13, 21, 26): 60,
    (7, 11, 13, 19, 21, 26): 60,
    (7, 11, 13, 19, 21, 26, 28): 30,
    (7, 11, 13, 19, 22, 28): 60,
    (7, 11, 13, 19, 28): 60,
    (7, 11, 13, 22): 60,
    (7, 11, 13, 22, 26): 60,
    (7, 11, 21, 26): 60,
    (7, 11, 28): 30,
})
assert sum(div_orbits.values()) == 480
assert change_hist == Counter({2: 420, 4: 60})

expected_vectors = {
    (3, 13, 21, 26): (
        (Fraction(9,25),Fraction(7,25),Fraction(3,25),Fraction(3,25),Fraction(3,25)),
        (Fraction(31,72),Fraction(11,36),Fraction(7,72),Fraction(1,12),Fraction(1,12))),
    (7, 11, 13, 19, 21, 26): (
        (Fraction(4,13),Fraction(3,13),Fraction(2,13),Fraction(2,13),Fraction(2,13)),
        (Fraction(25,66),Fraction(8,33),Fraction(3,22),Fraction(4,33),Fraction(4,33))),
    (7, 11, 13, 19, 21, 26, 28): (
        (Fraction(7,27),Fraction(5,27),Fraction(5,27),Fraction(5,27),Fraction(5,27)),
        (Fraction(11,36),Fraction(7,36),Fraction(7,36),Fraction(11,72),Fraction(11,72))),
    (7, 11, 13, 19, 22, 28): (
        (Fraction(3,13),Fraction(3,13),Fraction(3,13),Fraction(2,13),Fraction(2,13)),
        (Fraction(17,66),Fraction(17,66),Fraction(7,33),Fraction(3,22),Fraction(3,22))),
    (7, 11, 13, 19, 28): (
        (Fraction(7,25),Fraction(1,5),Fraction(1,5),Fraction(1,5),Fraction(3,25)),
        (Fraction(1,3),Fraction(1,5),Fraction(11,60),Fraction(11,60),Fraction(1,10))),
    (7, 11, 13, 22): (
        (Fraction(1,4),Fraction(1,4),Fraction(1,4),Fraction(1,6),Fraction(1,12)),
        (Fraction(8,27),Fraction(13,54),Fraction(13,54),Fraction(4,27),Fraction(2,27))),
    (7, 11, 13, 22, 26): (
        (Fraction(1,5),Fraction(7,25),Fraction(1,5),Fraction(1,5),Fraction(3,25)),
        (Fraction(7,30),Fraction(17,60),Fraction(11,60),Fraction(11,60),Fraction(7,60))),
    (7, 11, 21, 26): (
        (Fraction(1,4),Fraction(1,4),Fraction(1,6),Fraction(1,6),Fraction(1,6)),
        (Fraction(7,27),Fraction(7,27),Fraction(1,6),Fraction(1,6),Fraction(4,27))),
    (7, 11, 28): (
        (Fraction(5,23),Fraction(5,23),Fraction(5,23),Fraction(5,23),Fraction(3,23)),
        (Fraction(11,48),Fraction(11,48),Fraction(5,24),Fraction(5,24),Fraction(1,8))),
}
assert orbit_data == expected_vectors

print("VERIFY_OK")
print("proper_counts", proper_counts)
print("proper_isomorphism_counts", iso_counts)
print("divergence_counts", divergence_counts)
print("first_layer_fraction", "480/2645=96/529")
print("divergent_orbits", dict(div_orbits))
print("changed_pair_hist", dict(change_hist))
for c in sorted(expected_vectors):
    print("class", c, "orbit", div_orbits[c], "B", expected_vectors[c][0], "J", expected_vectors[c][1])
