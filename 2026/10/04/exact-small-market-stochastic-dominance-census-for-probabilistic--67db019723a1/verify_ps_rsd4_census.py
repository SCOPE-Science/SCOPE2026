#!/usr/bin/env python3
from itertools import permutations, combinations_with_replacement, product
from fractions import Fraction
from collections import Counter, defaultdict
import math


def rsd(profile):
    n = len(profile)
    counts = [[0] * n for _ in range(n)]
    for order in permutations(range(n)):
        available = (1 << n) - 1
        for i in order:
            for o in profile[i]:
                if (available >> o) & 1:
                    counts[i][o] += 1
                    available ^= (1 << o)
                    break
    d = math.factorial(n)
    return tuple(tuple(Fraction(x, d) for x in row) for row in counts)


def ps(profile):
    n = len(profile)
    remaining = [Fraction(1) for _ in range(n)]
    alloc = [[Fraction(0) for _ in range(n)] for __ in range(n)]
    t = Fraction(0)
    while t < 1:
        choices = []
        eaters = Counter()
        for i in range(n):
            for o in profile[i]:
                if remaining[o] > 0:
                    choices.append(o)
                    eaters[o] += 1
                    break
        dt = min(remaining[o] / k for o, k in eaters.items())
        if t + dt > 1:
            dt = 1 - t
        for i, o in enumerate(choices):
            alloc[i][o] += dt
        for o, k in eaters.items():
            remaining[o] -= k * dt
        t += dt
    assert t == 1
    assert all(sum(row) == 1 for row in alloc)
    assert all(sum(alloc[i][o] for i in range(n)) == 1 for o in range(n))
    return tuple(tuple(row) for row in alloc)


def sd_relation(A, B, profile):
    """Return (weak, strict) for A stochastically dominating B for every agent."""
    strict = False
    for i, pref in enumerate(profile):
        ca = Fraction(0)
        cb = Fraction(0)
        for o in pref[:-1]:
            ca += A[i][o]
            cb += B[i][o]
            if ca < cb:
                return False, False
            if ca > cb:
                strict = True
    return True, strict


def classify(profile):
    P = ps(profile)
    R = rsd(profile)
    if P == R:
        return "equal", P, R
    pweak, pstrict = sd_relation(P, R, profile)
    rweak, rstrict = sd_relation(R, P, profile)
    if pweak and pstrict:
        assert not (rweak and rstrict)
        return "PSdom", P, R
    if rweak and rstrict:
        return "RSDdom", P, R
    return "incomp", P, R


# Complete labeled boundary through n=3.
small = {}
for n in (1, 2, 3):
    prefs = list(permutations(range(n)))
    hist = Counter()
    for profile in product(prefs, repeat=n):
        typ, _, _ = classify(profile)
        hist[typ] += 1
    small[n] = hist
assert small[1] == Counter({"equal": 1})
assert small[2] == Counter({"equal": 4})
assert small[3] == Counter({"equal": 144, "incomp": 72})


# n=4 route A: anonymous preference multisets, then quotient by object relabeling.
n = 4
prefs = list(permutations(range(n)))
pidx = {p: i for i, p in enumerate(prefs)}
obj_perms = list(permutations(range(n)))
transform = []
for sigma in obj_perms:
    transform.append([pidx[tuple(sigma[o] for o in p)] for p in prefs])


def canonical_multiset(ms):
    return min(tuple(sorted(T[x] for x in ms)) for T in transform)


classes = {}
anon_hist = Counter()
weighted_hist = Counter()
for ms in combinations_with_replacement(range(24), 4):
    profile = tuple(prefs[x] for x in ms)
    typ, _, _ = classify(profile)
    mult = Counter(ms)
    weight = math.factorial(4)
    for v in mult.values():
        weight //= math.factorial(v)
    key = canonical_multiset(ms)
    pattern = tuple(sorted(mult.values(), reverse=True))
    if key not in classes:
        classes[key] = {"type": typ, "weight": 0, "pattern": pattern}
    else:
        assert classes[key]["type"] == typ
    classes[key]["weight"] += weight
    anon_hist[typ] += 1
    weighted_hist[typ] += weight

assert len(classes) == 762
class_hist = Counter(d["type"] for d in classes.values())
assert class_hist == Counter({"incomp": 517, "equal": 209, "PSdom": 36})
assert anon_hist == Counter({"incomp": 12204, "equal": 4716, "PSdom": 630})
assert weighted_hist == Counter({"incomp": 247824, "equal": 72288, "PSdom": 11664})
assert weighted_hist["PSdom"] == 11664
assert Fraction(weighted_hist["PSdom"], 24**4) == Fraction(9, 256)
assert Fraction(weighted_hist["equal"], 24**4) == Fraction(251, 1152)
assert Fraction(weighted_hist["incomp"], 24**4) == Fraction(1721, 2304)
assert class_hist["RSDdom"] == 0

orbit_hist = defaultdict(Counter)
pattern_hist = defaultdict(Counter)
for d in classes.values():
    orbit_hist[d["type"]][d["weight"]] += 1
    pattern_hist[d["type"]][d["pattern"]] += 1
assert orbit_hist["PSdom"] == Counter({288: 20, 576: 9, 72: 4, 144: 3})
assert pattern_hist["PSdom"] == Counter({(1,1,1,1): 23, (2,1,1): 9, (2,2): 4})

min_distinct = min(len(set(k)) for k, d in classes.items() if d["type"] == "PSdom")
min_keys = sorted(k for k, d in classes.items() if d["type"] == "PSdom" and len(set(k)) == min_distinct)
assert min_distinct == 2
assert min_keys == [(0,0,1,1), (0,0,2,2), (0,0,6,6), (0,0,7,7)]
assert all(classes[k]["weight"] == 72 for k in min_keys)

# n=4 route B: independently recover the symmetry-class counts by Burnside
# over object relabelings acting on anonymous agent multisets.
# The mechanism type is already known for every anonymous multiset from route A.
type_by_ms = {}
for ms in combinations_with_replacement(range(24), 4):
    profile = tuple(prefs[x] for x in ms)
    typ, _, _ = classify(profile)
    type_by_ms[ms] = typ

burnside_sums = Counter()
for T in transform:
    fixed = Counter()
    for ms, typ in type_by_ms.items():
        if tuple(sorted(T[x] for x in ms)) == ms:
            fixed[typ] += 1
    burnside_sums.update(fixed)
burnside_classes = Counter({typ: val // 24 for typ, val in burnside_sums.items()})
assert all(val % 24 == 0 for val in burnside_sums.values())
assert burnside_classes == class_hist

# Independently reconstruct the labeled count by walking all labeled index tuples
# and looking up the already-exhaustive anonymous classification.
direct_hist = Counter()
for idxs in product(range(24), repeat=4):
    direct_hist[type_by_ms[tuple(sorted(idxs))]] += 1
assert direct_hist == weighted_hist

# n=3 quotient cross-check: 8 equality classes and 2 incomparable classes.
n3prefs = list(permutations(range(3)))
n3idx = {p:i for i,p in enumerate(n3prefs)}
n3trans = []
for sigma in permutations(range(3)):
    n3trans.append([n3idx[tuple(sigma[o] for o in p)] for p in n3prefs])

def can3(ms):
    return min(tuple(sorted(T[x] for x in ms)) for T in n3trans)

n3classes = {}
for ms in combinations_with_replacement(range(6),3):
    profile = tuple(n3prefs[x] for x in ms)
    typ, _, _ = classify(profile)
    k = can3(ms)
    if k in n3classes:
        assert n3classes[k] == typ
    else:
        n3classes[k] = typ
assert Counter(n3classes.values()) == Counter({"equal": 8, "incomp": 2})

# Published four-agent Bogomolnaia-Moulin/Hosseini-Larson-Cohen witness.
a,b,c,d = range(4)
witness = (
    (a,b,c,d),
    (a,b,c,d),
    (b,a,d,c),
    (b,a,d,c),
)
typ, P, R = classify(witness)
assert typ == "PSdom"
expected_P = (
    (Fraction(1,2),0,Fraction(1,2),0),
    (Fraction(1,2),0,Fraction(1,2),0),
    (0,Fraction(1,2),0,Fraction(1,2)),
    (0,Fraction(1,2),0,Fraction(1,2)),
)
expected_R = (
    (Fraction(5,12),Fraction(1,12),Fraction(5,12),Fraction(1,12)),
    (Fraction(5,12),Fraction(1,12),Fraction(5,12),Fraction(1,12)),
    (Fraction(1,12),Fraction(5,12),Fraction(1,12),Fraction(5,12)),
    (Fraction(1,12),Fraction(5,12),Fraction(1,12),Fraction(5,12)),
)
assert P == expected_P
assert R == expected_R

print("VERIFY_OK")
print("n1", dict(small[1]))
print("n2", dict(small[2]))
print("n3", dict(small[3]))
print("n3_symmetry_classes", dict(Counter(n3classes.values())))
print("n4_labeled", dict(direct_hist))
print("n4_probability_PSdom", "9/256")
print("n4_probability_equal", "251/1152")
print("n4_probability_incomp", "1721/2304")
print("n4_symmetry_classes", dict(class_hist))
print("n4_PSdom_orbit_hist", dict(sorted(orbit_hist["PSdom"].items())))
print("n4_PSdom_pattern_hist", {str(k):v for k,v in pattern_hist["PSdom"].items()})
print("n4_min_distinct_orders", min_distinct)
print("n4_min_PSdom_classes", min_keys)
print("published_witness_replayed", True)
