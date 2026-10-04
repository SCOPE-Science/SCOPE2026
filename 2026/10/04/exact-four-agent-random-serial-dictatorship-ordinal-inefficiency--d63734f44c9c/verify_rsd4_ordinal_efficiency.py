#!/usr/bin/env python3
from itertools import permutations, combinations_with_replacement, product
from collections import Counter, defaultdict
from fractions import Fraction
import math

def ranks_of(profile):
    n = len(profile)
    ranks = [[0] * n for _ in range(n)]
    for i, pref in enumerate(profile):
        for r, o in enumerate(pref):
            ranks[i][o] = r
    return ranks

def rsd_support(profile):
    n = len(profile)
    support = [[False] * n for _ in range(n)]
    for order in permutations(range(n)):
        available = (1 << n) - 1
        for i in order:
            for o in profile[i]:
                if (available >> o) & 1:
                    support[i][o] = True
                    available ^= (1 << o)
                    break
    return support

def ordinal_relation(profile):
    n = len(profile)
    ranks = ranks_of(profile)
    support = rsd_support(profile)
    adj = [[False] * n for _ in range(n)]
    for i in range(n):
        for worse in range(n):
            if support[i][worse]:
                for better in range(n):
                    if ranks[i][better] < ranks[i][worse]:
                        adj[better][worse] = True
    return adj, support

def cyclic(adj):
    n = len(adj)
    reach = [row[:] for row in adj]
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]:
                        reach[i][j] = True
    return any(reach[i][i] for i in range(n))

def reciprocal_pair(adj):
    n = len(adj)
    return any(adj[i][j] and adj[j][i] for i in range(n) for j in range(i + 1, n))

def rsd_matrix(profile):
    n = len(profile)
    counts = [[0] * n for _ in range(n)]
    orders = list(permutations(range(n)))
    for order in orders:
        available = (1 << n) - 1
        for i in order:
            for o in profile[i]:
                if (available >> o) & 1:
                    counts[i][o] += 1
                    available ^= (1 << o)
                    break
    d = math.factorial(n)
    return [[Fraction(x, d) for x in row] for row in counts]

# Minimal-size check by direct labeled enumeration.
for n in (1, 2, 3):
    prefs = list(permutations(range(n)))
    bad = 0
    for profile in product(prefs, repeat=n):
        adj, _ = ordinal_relation(profile)
        bad += cyclic(adj)
    assert bad == 0

n = 4
prefs = list(permutations(range(n)))
pref_index = {p:i for i,p in enumerate(prefs)}
obj_perms = list(permutations(range(n)))

# Object-relabel action on individual preference orders.
transform = [[0] * len(prefs) for _ in obj_perms]
for si, sigma in enumerate(obj_perms):
    for pi, pref in enumerate(prefs):
        transform[si][pi] = pref_index[tuple(sigma[o] for o in pref)]

def canonical_anonymous(ms):
    best = None
    for si in range(len(obj_perms)):
        image = tuple(sorted(transform[si][p] for p in ms))
        if best is None or image < best:
            best = image
    return best

# Route A: enumerate all anonymous multisets, quotient by object relabeling,
# and restore agent-label multiplicities exactly.
classes = defaultdict(lambda: {
    "weight": 0, "inefficient": None, "members": 0,
    "pattern": None, "reciprocal": None
})
anonymous_inefficient = 0
labeled_weight_inefficient = 0
for ms in combinations_with_replacement(range(len(prefs)), n):
    profile = tuple(prefs[p] for p in ms)
    adj, _ = ordinal_relation(profile)
    bad = cyclic(adj)
    rec = reciprocal_pair(adj)
    assert bad == rec  # finite structural claim at n=4

    mult = Counter(ms)
    weight = math.factorial(n)
    for v in mult.values():
        weight //= math.factorial(v)

    key = canonical_anonymous(ms)
    d = classes[key]
    pat = tuple(sorted(mult.values(), reverse=True))
    if d["inefficient"] is None:
        d["inefficient"] = bad
        d["reciprocal"] = rec
        d["pattern"] = pat
    else:
        assert d["inefficient"] == bad
        assert d["reciprocal"] == rec
    d["weight"] += weight
    d["members"] += 1

    anonymous_inefficient += int(bad)
    labeled_weight_inefficient += weight * int(bad)

assert len(classes) == 762
assert sum(d["weight"] for d in classes.values()) == 24**4
assert anonymous_inefficient == 3270
assert labeled_weight_inefficient == 68976
assert sum(d["inefficient"] for d in classes.values()) == 153

all_orbit_hist = Counter(d["weight"] for d in classes.values())
bad_orbit_hist = Counter(d["weight"] for d in classes.values() if d["inefficient"])
bad_pattern_hist = Counter(d["pattern"] for d in classes.values() if d["inefficient"])
assert all_orbit_hist == Counter({576:420, 288:295, 96:23, 144:14, 72:9, 24:1})
assert bad_orbit_hist == Counter({576:91, 288:55, 72:4, 144:3})
assert bad_pattern_hist == Counter({(1,1,1,1):119, (2,1,1):30, (2,2):4})

two_type = sorted(key for key,d in classes.items() if d["inefficient"] and len(set(key)) == 2)
expected_two_type = [
    (0,0,1,1),
    (0,0,2,2),
    (0,0,6,6),
    (0,0,7,7),
]
# Under lexicographic permutation indexing:
# 0=0123, 1=0132, 2=0213, 6=1023, 7=1032.
assert two_type == expected_two_type
assert all(classes[k]["weight"] == 72 for k in two_type)

# Route B: independently enumerate every labeled profile directly.
direct_bad = 0
direct_reciprocal_equiv = 0
for profile in product(prefs, repeat=n):
    adj, _ = ordinal_relation(profile)
    bad = cyclic(adj)
    rec = reciprocal_pair(adj)
    direct_bad += int(bad)
    direct_reciprocal_equiv += int(bad == rec)
assert direct_bad == 68976
assert direct_reciprocal_equiv == 24**4

# Published Bogomolnaia-Moulin/Manea four-agent witness:
# two agents rank a>b>c>d; two rank b>a>c>d.
a,b,c,d = range(4)
witness = (
    (a,b,c,d),(a,b,c,d),
    (b,a,c,d),(b,a,c,d),
)
matrix = rsd_matrix(witness)
expected = [
    [Fraction(5,12), Fraction(1,12), Fraction(1,4), Fraction(1,4)],
    [Fraction(5,12), Fraction(1,12), Fraction(1,4), Fraction(1,4)],
    [Fraction(1,12), Fraction(5,12), Fraction(1,4), Fraction(1,4)],
    [Fraction(1,12), Fraction(5,12), Fraction(1,4), Fraction(1,4)],
]
assert matrix == expected
adj, support = ordinal_relation(witness)
assert adj[a][b] and adj[b][a]
assert all(all(row) for row in support)

p = Fraction(68976, 24**4)
assert p == Fraction(479,2304)

print("VERIFY_OK")
print("n<=3_labeled_inefficient", 0)
print("n4_labeled_profiles", 24**4)
print("n4_labeled_inefficient", 68976)
print("n4_inefficiency_probability", "479/2304")
print("n4_anonymous_multisets", math.comb(27,4))
print("n4_anonymous_inefficient", 3270)
print("n4_symmetry_classes", 762)
print("n4_inefficient_symmetry_classes", 153)
print("inefficient_orbit_sizes", dict(sorted(bad_orbit_hist.items())))
print("inefficient_multiplicity_patterns", dict(sorted(bad_pattern_hist.items())))
print("all_inefficiency_has_reciprocal_pair", True)
print("minimum_distinct_preference_orders", 2)
print("minimum_classes", 4)
