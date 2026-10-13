#!/usr/bin/env python3
from itertools import permutations, product
from fractions import Fraction
from collections import Counter

def antichains(n):
    subs = list(range(1, 1 << n))
    for mask in range(1, 1 << len(subs)):
        fam = [subs[i] for i in range(len(subs)) if (mask >> i) & 1]
        ok = True
        for i, a in enumerate(fam):
            for b in fam[i+1:]:
                if (a & b) == a or (a & b) == b:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            yield tuple(sorted(fam))

def value(fam, S):
    return int(any((m & S) == m for m in fam))

def proper(n, fam):
    N = (1 << n) - 1
    return all(not (value(fam,S) and value(fam,N ^ S)) for S in range(1 << n))

def dp_formula(n, fam):
    m = len(fam)
    return tuple(
        sum((Fraction(1, S.bit_count()) for S in fam if (S >> i) & 1), Fraction(0)) / m
        for i in range(n)
    )

def dp_coalition_split(n, fam):
    # Independently build each minimal coalition's unit payoff vector and average.
    acc = [Fraction(0) for _ in range(n)]
    for S in fam:
        share = Fraction(1, S.bit_count())
        for i in range(n):
            if (S >> i) & 1:
                acc[i] += share
    return tuple(x / len(fam) for x in acc)

def pg_formula(n, fam):
    counts = [sum(1 for S in fam if (S >> i) & 1) for i in range(n)]
    total = sum(counts)
    return tuple(Fraction(c,total) for c in counts)

def pg_incidence(n, fam):
    # Independently count the player-coalition incidences and normalize.
    inc = []
    for S in fam:
        inc.extend(i for i in range(n) if (S >> i) & 1)
    return tuple(Fraction(inc.count(i), len(inc)) for i in range(n))

def weak_order(v):
    return tuple(
        (v[i] > v[j]) - (v[i] < v[j])
        for i in range(len(v))
        for j in range(i+1, len(v))
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
    return min(relabel_family(fam,p,n) for p in permutations(range(n)))

def weighted_rep(n, fam, maxw=6):
    truth = [value(fam,S) for S in range(1 << n)]
    for w in product(range(maxw+1), repeat=n):
        if not any(w):
            continue
        total = sum(w)
        for q in range(1,total+1):
            ok = True
            for S in range(1 << n):
                sw = sum(w[i] for i in range(n) if (S >> i) & 1)
                if int(sw >= q) != truth[S]:
                    ok = False
                    break
            if ok:
                return (q,w)
    return None

proper_counts = {}
div_counts = {}
class_counts = {}
div_orbits = Counter()
orbit_data = {}

for n in range(1,5):
    pc = 0
    dc = 0
    classes = Counter()
    for fam in antichains(n):
        if not proper(n,fam):
            continue
        pc += 1
        d1 = dp_formula(n,fam)
        d2 = dp_coalition_split(n,fam)
        p1 = pg_formula(n,fam)
        p2 = pg_incidence(n,fam)
        assert d1 == d2
        assert p1 == p2
        assert sum(d1) == 1
        assert sum(p1) == 1
        c = canonical_family(fam,n)
        classes[c] += 1
        if weak_order(d1) != weak_order(p1):
            dc += 1
            if n == 4:
                div_orbits[c] += 1
                orbit_data.setdefault(c,(dp_formula(n,c),pg_formula(n,c)))
    proper_counts[n] = pc
    div_counts[n] = dc
    class_counts[n] = len(classes)

assert proper_counts == {1:1,2:3,3:11,4:80}
assert class_counts == {1:1,2:2,3:5,4:14}
assert div_counts == {1:0,2:0,3:0,4:30}

expected = {
    (3,13): {
        "orbit":12,
        "dp":(Fraction(5,12),Fraction(1,4),Fraction(1,6),Fraction(1,6)),
        "pg":(Fraction(2,5),Fraction(1,5),Fraction(1,5),Fraction(1,5)),
        "weighted":(5,(3,2,1,1)),
    },
    (3,5,14): {
        "orbit":12,
        "dp":(Fraction(1,3),Fraction(5,18),Fraction(5,18),Fraction(1,9)),
        "pg":(Fraction(2,7),Fraction(2,7),Fraction(2,7),Fraction(1,7)),
        "weighted":(5,(3,2,2,1)),
    },
    (3,13,14): {
        "orbit":6,
        "dp":(Fraction(5,18),Fraction(5,18),Fraction(2,9),Fraction(2,9)),
        "pg":(Fraction(1,4),Fraction(1,4),Fraction(1,4),Fraction(1,4)),
        "weighted":(4,(2,2,1,1)),
    },
}
assert set(div_orbits) == set(expected)
assert div_orbits == Counter({(3,13):12,(3,5,14):12,(3,13,14):6})
for c,e in expected.items():
    assert orbit_data[c] == (e["dp"], e["pg"])
    assert weighted_rep(4,c) == e["weighted"]

# Properness really matters: without it, ordinal divergence appears already at 3 players.
all_div3 = [
    fam for fam in antichains(3)
    if weak_order(dp_formula(3,fam)) != weak_order(pg_formula(3,fam))
]
assert len(all_div3) == 3
assert len({canonical_family(f,3) for f in all_div3}) == 1
assert all(not proper(3,f) for f in all_div3)

print("VERIFY_OK")
print("proper_counts", proper_counts)
print("proper_isomorphism_classes", class_counts)
print("divergence_counts", div_counts)
print("four_player_divergent_orbits", dict(div_orbits))
for c,e in expected.items():
    print("orbit",c,"count",e["orbit"],"DP",e["dp"],"PG",e["pg"],"weighted",e["weighted"])
print("nonproper_three_player_divergences",len(all_div3))
