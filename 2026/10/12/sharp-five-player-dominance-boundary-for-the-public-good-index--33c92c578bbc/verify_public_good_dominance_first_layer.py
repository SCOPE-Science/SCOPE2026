#!/usr/bin/env python3
from itertools import permutations, product
from fractions import Fraction
from collections import Counter


def antichains(n):
    """All nonempty antichains of nonempty subsets of [n]."""
    subs = list(range(1, 1 << n))
    comparable = {
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
        rec((cands - {s}) - comparable[s], chosen + (s,))
    rec(set(subs), ())
    return tuple(out)


def value(fam, S):
    return int(any((m & S) == m for m in fam))


def proper(n, fam):
    N = (1 << n) - 1
    return all(not (value(fam, S) and value(fam, N ^ S)) for S in range(1 << n))


def public_good_counts(n, fam):
    counts = [sum(1 for S in fam if (S >> i) & 1) for i in range(n)]
    total = sum(counts)
    return tuple(Fraction(c, total) for c in counts)


def public_good_incidence(n, fam):
    inc = []
    for S in fam:
        inc.extend(i for i in range(n) if (S >> i) & 1)
    return tuple(Fraction(inc.count(i), len(inc)) for i in range(n))


def dominates_addition(n, fam, i, j):
    """Isbell desirability: replacing j by i never turns a win into a loss."""
    if i == j:
        return True
    for S in range(1 << n):
        if (S >> i) & 1 or (S >> j) & 1:
            continue
        if value(fam, S | (1 << j)) and not value(fam, S | (1 << i)):
            return False
    return True


def dominates_swap(n, fam, i, j):
    """Equivalent direct swap test on all winning coalitions."""
    if i == j:
        return True
    for W in range(1 << n):
        if not value(fam, W):
            continue
        if ((W >> j) & 1) and not ((W >> i) & 1):
            W2 = (W & ~(1 << j)) | (1 << i)
            if not value(fam, W2):
                return False
    return True


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


def weighted_rep(n, fam, maxw=9):
    truth = [value(fam, S) for S in range(1 << n)]
    for w in product(range(maxw + 1), repeat=n):
        if not any(w):
            continue
        for q in range(1, sum(w) + 1):
            if all(
                int(sum(w[i] for i in range(n) if (S >> i) & 1) >= q) == truth[S]
                for S in range(1 << n)
            ):
                return q, w
    return None


def violations(n, fam):
    pg1 = public_good_counts(n, fam)
    pg2 = public_good_incidence(n, fam)
    assert pg1 == pg2
    assert sum(pg1) == 1
    out = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d1 = dominates_addition(n, fam, i, j)
            d2 = dominates_swap(n, fam, i, j)
            assert d1 == d2
            if d1 and pg1[i] < pg1[j]:
                out.append((i, j, pg1[i], pg1[j]))
    return pg1, tuple(out)

proper_counts = {}
class_counts = {}
violation_counts = {}
bad5 = {}
violation_pair_hist = Counter()
violation_pair_class_hist = Counter()

for n in range(1, 6):
    classes = Counter(canonical_family(f, n) for f in antichains(n) if proper(n, f))
    proper_counts[n] = sum(classes.values())
    class_counts[n] = len(classes)
    bad = 0
    for c, orbit in classes.items():
        pg, viol = violations(n, c)
        if viol:
            bad += orbit
            if n == 5:
                bad5[c] = (orbit, pg, viol)
                violation_pair_hist[len(viol)] += orbit
                violation_pair_class_hist[len(viol)] += 1
    violation_counts[n] = bad

assert proper_counts == {1:1, 2:3, 3:11, 4:80, 5:2645}
assert class_counts == {1:1, 2:2, 3:5, 4:14, 5:86}
assert violation_counts == {1:0, 2:0, 3:0, 4:0, 5:460}
assert len(bad5) == 9
assert sum(x[0] for x in bad5.values()) == 460
assert violation_pair_hist == Counter({1:300, 2:120, 3:40})
assert violation_pair_class_hist == Counter({1:4, 2:3, 3:2})

expected = {
    (3,13,21): (60, (8,(5,3,2,1,1))),
    (3,13,21,25): (20, (6,(4,2,1,1,1))),
    (3,13,21,30): (60, (7,(4,3,2,1,1))),
    (3,13,21,25,30): (20, (5,(3,2,1,1,1))),
    (3,13,14,21): (120, (9,(5,4,3,2,1))),
    (3,13,14,21,25): (60, (7,(4,3,2,2,1))),
    (3,13,14,21,22): (30, (6,(3,3,2,1,1))),
    (3,5,14,22): (30, (7,(4,3,3,1,1))),
    (3,13,14,21,22,25): (60, (9,(5,4,3,2,2))),
}
assert set(bad5) == set(expected)

for c, (orbit, rep) in expected.items():
    assert bad5[c][0] == orbit
    found = weighted_rep(5, c)
    assert found == rep
    q, w = rep
    # Every dominance violation is also a strict local-monotonicity failure
    # in the displayed weighted representation.
    for i, j, pgi, pgj in bad5[c][2]:
        assert w[i] > w[j]
        assert pgi < pgj

# Compact first-layer witness: [8;5,3,2,1,1], minimal winners {AB,ACD,ACE}.
w = (3,13,21)
assert bad5[w][1] == (
    Fraction(3,8), Fraction(1,8), Fraction(1,4), Fraction(1,8), Fraction(1,8)
)
assert bad5[w][2] == ((1,2,Fraction(1,8),Fraction(1,4)),)
assert expected[w][1] == (8,(5,3,2,1,1))

print('VERIFY_OK')
print('proper_counts', proper_counts)
print('proper_isomorphism_classes', class_counts)
print('dominance_violation_counts', violation_counts)
print('five_player_bad_labeled', 460, 'of', 2645, '=', '92/529')
print('five_player_bad_classes', len(bad5))
print('violation_pair_hist', dict(violation_pair_hist))
print('violation_pair_class_hist', dict(violation_pair_class_hist))
for c in sorted(bad5):
    orbit, pg, viol = bad5[c]
    print('class', c, 'orbit', orbit, 'PG', pg, 'violations', viol, 'weighted', expected[c][1])
