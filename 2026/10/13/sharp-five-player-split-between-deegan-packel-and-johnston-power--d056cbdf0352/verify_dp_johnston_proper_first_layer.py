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


def deegan_packel_direct(n, fam):
    m = len(fam)
    return tuple(
        sum((Fraction(1, S.bit_count()) for S in fam if (S >> i) & 1), Fraction(0)) / m
        for i in range(n)
    )


def deegan_packel_split(n, fam):
    acc = [Fraction(0) for _ in range(n)]
    for S in fam:
        share = Fraction(1, S.bit_count())
        for i in range(n):
            if (S >> i) & 1:
                acc[i] += share
    return tuple(x / len(fam) for x in acc)


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


def pair_relation_types(a, b):
    reversals = a_refines = b_refines = changed = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            ca = (a[i] > a[j]) - (a[i] < a[j])
            cb = (b[i] > b[j]) - (b[i] < b[j])
            if ca == cb:
                continue
            changed += 1
            if ca * cb == -1:
                reversals += 1
            elif cb == 0:
                a_refines += 1
            elif ca == 0:
                b_refines += 1
    return reversals, a_refines, b_refines, changed


proper_counts = {}
class_counts = {}
divergence_counts = {}
relation_hist = Counter()
relation_class_hist = Counter()
all_divergent_orbits = Counter()
all_divergent_data = {}
dummy_free_total = 0
dummy_free_divergent = 0

for n in range(1, 6):
    classes = Counter(canonical_family(f, n) for f in antichains(n) if proper(n, f))
    proper_counts[n] = sum(classes.values())
    class_counts[n] = len(classes)
    div = 0
    for c, orbit in classes.items():
        dp1 = deegan_packel_direct(n, c)
        dp2 = deegan_packel_split(n, c)
        assert dp1 == dp2
        assert sum(dp1) == 1

        j1, raw1 = johnston_by_coalition(n, c)
        j2, raw2 = johnston_by_player(n, c)
        assert j1 == j2 and raw1 == raw2
        assert sum(j1) == 1

        if n == 5 and all(x > 0 for x in dp1):
            dummy_free_total += orbit

        if weak_order(dp1) != weak_order(j1):
            div += orbit
            if n == 5:
                typ = pair_relation_types(dp1, j1)
                relation_hist[typ] += orbit
                relation_class_hist[typ] += 1
                all_divergent_orbits[c] = orbit
                all_divergent_data[c] = (dp1, j1, typ)
                if all(x > 0 for x in dp1):
                    dummy_free_divergent += orbit
    divergence_counts[n] = div

assert proper_counts == {1: 1, 2: 3, 3: 11, 4: 80, 5: 2645}
assert class_counts == {1: 1, 2: 2, 3: 5, 4: 14, 5: 86}
assert divergence_counts == {1: 0, 2: 0, 3: 0, 4: 0, 5: 940}
assert len(all_divergent_orbits) == 18
assert sum(all_divergent_orbits.values()) == 940
assert dummy_free_total == 2330
assert dummy_free_divergent == 940

# Types are (strict reversals, DP-refines-Johnston-tie, Johnston-refines-DP-tie, changed pairs).
assert relation_hist == Counter({
    (0, 0, 2, 2): 420,
    (1, 0, 0, 1): 300,
    (2, 0, 0, 2): 120,
    (0, 0, 4, 4): 60,
    (3, 0, 0, 3): 40,
})
assert relation_class_hist == Counter({
    (0, 0, 2, 2): 7,
    (1, 0, 0, 1): 4,
    (2, 0, 0, 2): 3,
    (0, 0, 4, 4): 2,
    (3, 0, 0, 3): 2,
})

# Therefore 480 labeled games (nine classes) are pure Johnston refinements of DP ties,
# while 460 labeled games (nine classes) contain only genuine strict reversals.
assert relation_hist[(0,0,2,2)] + relation_hist[(0,0,4,4)] == 480
assert relation_class_hist[(0,0,2,2)] + relation_class_hist[(0,0,4,4)] == 9
assert sum(v for k,v in relation_hist.items() if k[0] > 0) == 460
assert sum(v for k,v in relation_class_hist.items() if k[0] > 0) == 9
assert all(k[1] == 0 for k in relation_hist)  # DP never refines a Johnston tie at first layer.

# Clean strict-reversal witness: {AB, ACD, ACE}.
strict = (3, 13, 21)
assert all_divergent_orbits[strict] == 60
assert all_divergent_data[strict] == (
    (Fraction(7,18), Fraction(1,6), Fraction(2,9), Fraction(1,9), Fraction(1,9)),
    (Fraction(20,33), Fraction(5,22), Fraction(7,66), Fraction(1,33), Fraction(1,33)),
    (1,0,0,1),
)
# Here DP ranks C>B, while Johnston ranks B>C.

# Clean tie-refinement witness: {ABC, ABD, ACD, BCE}.
tie = (7, 11, 13, 22)
assert all_divergent_orbits[tie] == 60
assert all_divergent_data[tie] == (
    (Fraction(1,4), Fraction(1,4), Fraction(1,4), Fraction(1,6), Fraction(1,12)),
    (Fraction(8,27), Fraction(13,54), Fraction(13,54), Fraction(4,27), Fraction(2,27)),
    (0,0,2,2),
)
# Here DP ties A=B=C, while Johnston ranks A>B=C.

print("VERIFY_OK")
print("proper_counts", proper_counts)
print("proper_isomorphism_classes", class_counts)
print("divergence_counts", divergence_counts)
print("five_player_divergent_labeled", 940, "of", 2645, "=", "188/529")
print("five_player_divergent_classes", len(all_divergent_orbits))
print("relation_hist", dict(relation_hist))
print("relation_class_hist", dict(relation_class_hist))
print("pure_tie_refinements", 480, "in", 9, "classes")
print("strict_reversal_games", 460, "in", 9, "classes")
print("dummy_free_proper", dummy_free_total, "divergent", dummy_free_divergent)
print("strict_witness", strict, all_divergent_data[strict])
print("tie_witness", tie, all_divergent_data[tie])
