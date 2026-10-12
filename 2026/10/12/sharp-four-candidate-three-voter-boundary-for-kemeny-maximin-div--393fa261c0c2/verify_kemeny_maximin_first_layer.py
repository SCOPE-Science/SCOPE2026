#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from math import factorial

def pairwise_support(profile, m):
    s = [[0]*m for _ in range(m)]
    for ballot in profile:
        pos = {c:i for i,c in enumerate(ballot)}
        for a in range(m):
            for b in range(m):
                if a != b and pos[a] < pos[b]:
                    s[a][b] += 1
    return s

def kemeny_pairwise(profile, m):
    s = pairwise_support(profile, m)
    scores = {}
    best = None
    for order in permutations(range(m)):
        val = sum(s[order[i]][order[j]] for i in range(m) for j in range(i+1,m))
        scores[order] = val
        if best is None or val > best:
            best = val
    winners = frozenset(order[0] for order,val in scores.items() if val == best)
    return winners, best, scores

def kendall_distance(a, b):
    pos = {x:i for i,x in enumerate(b)}
    d = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if pos[a[i]] > pos[a[j]]:
                d += 1
    return d

def kemeny_distance(profile, m):
    totals = {}
    best = None
    for order in permutations(range(m)):
        d = sum(kendall_distance(order, ballot) for ballot in profile)
        totals[order] = d
        if best is None or d < best:
            best = d
    winners = frozenset(order[0] for order,d in totals.items() if d == best)
    return winners, best, totals

def maximin_support(profile, m):
    s = pairwise_support(profile, m)
    vals = tuple(min(s[c][d] for d in range(m) if d != c) for c in range(m))
    best = max(vals)
    return frozenset(c for c,v in enumerate(vals) if v == best), vals

def maximin_opposition(profile, m):
    s = pairwise_support(profile, m)
    n = len(profile)
    worst_opp = tuple(max(s[d][c] for d in range(m) if d != c) for c in range(m))
    # Since s[c][d] + s[d][c] = n for every pair, minimizing worst opposition
    # is equivalent to maximizing the minimum support.
    best = min(worst_opp)
    return frozenset(c for c,v in enumerate(worst_opp) if v == best), worst_opp

def relabel_profile(profile, p):
    return tuple(sorted(tuple(p[x] for x in ballot) for ballot in profile))

def canonical(profile, m):
    return min(relabel_profile(profile, p) for p in permutations(range(m)))


def labeled_orbit(profile, m):
    out=set()
    nv=len(profile)
    for p in permutations(range(m)):
        renamed=tuple(tuple(p[x] for x in ballot) for ballot in profile)
        for q in permutations(range(nv)):
            out.add(tuple(renamed[q[i]] for i in range(nv)))
    return out

def relation(k, x):
    if k == x:
        return "equal"
    if k < x:
        return "kemeny_subset_maximin"
    if x < k:
        return "maximin_subset_kemeny"
    if k & x:
        return "overlap_nonnested"
    return "disjoint"

# Exhaust the four-candidate domains with one, two, and three labeled voters.
orders4 = tuple(permutations(range(4)))
relation_hist = {}
size_hist = {}
classes = Counter()
details = {}

for nv in (1,2,3):
    rh = Counter()
    sh = Counter()
    for profile in product(orders4, repeat=nv):
        k1, kb, kscore = kemeny_pairwise(profile, 4)
        k2, kd, kdist = kemeny_distance(profile, 4)
        assert k1 == k2
        # Every ranking has six candidate pairs, so pairwise Kemeny score
        # plus total Kendall distance equals 6*nv.
        assert all(kscore[o] + kdist[o] == 6*nv for o in orders4)

        m1, ms = maximin_support(profile, 4)
        m2, mo = maximin_opposition(profile, 4)
        assert m1 == m2
        assert all(ms[c] + mo[c] == nv for c in range(4))

        r = relation(k1,m1)
        rh[r] += 1
        sh[(len(k1),len(m1),r)] += 1

        if nv == 3 and r != "equal":
            c = canonical(profile,4)
            classes[c] += 1
            if c not in details:
                ck, cb, _ = kemeny_pairwise(c,4)
                cm, cv = maximin_support(c,4)
                details[c] = (ck,cm,cb,cv)

    relation_hist[nv] = rh
    size_hist[nv] = sh

assert relation_hist[1] == Counter({"equal":24})
assert relation_hist[2] == Counter({"equal":576})
assert relation_hist[3] == Counter({
    "equal":12768,
    "kemeny_subset_maximin":1056,
})
assert size_hist[3] == Counter({
    (1,1,"equal"):12288,
    (3,3,"equal"):480,
    (1,3,"kemeny_subset_maximin"):144,
    (1,4,"kemeny_subset_maximin"):576,
    (3,4,"kemeny_subset_maximin"):336,
})

# The divergent layer has eight candidate/voter-isomorphism classes.
assert len(classes) == 8
assert Counter(classes.values()) == Counter({144:7,48:1})
assert sum(classes.values()) == 1056

expected = {
((0,1,2,3),(1,2,0,3),(3,2,0,1)):
    (frozenset({0,1,2}),frozenset({0,1,2,3}),11,(1,1,1,1),144),
((0,1,2,3),(1,2,3,0),(2,3,0,1)):
    (frozenset({1}),frozenset({0,1,2}),12,(1,1,1,0),144),
((0,1,2,3),(1,2,3,0),(3,0,2,1)):
    (frozenset({0}),frozenset({0,1,2,3}),11,(1,1,1,1),144),
((0,1,2,3),(1,2,3,0),(3,2,0,1)):
    (frozenset({1}),frozenset({0,1,2,3}),11,(1,1,1,1),144),
((0,1,2,3),(1,3,0,2),(2,3,0,1)):
    (frozenset({0}),frozenset({0,1,2,3}),11,(1,1,1,1),144),
((0,1,2,3),(1,3,0,2),(3,2,0,1)):
    (frozenset({0,1,3}),frozenset({0,1,2,3}),11,(1,1,1,1),144),
((0,1,2,3),(1,3,2,0),(2,3,0,1)):
    (frozenset({1}),frozenset({0,1,2,3}),11,(1,1,1,1),144),
((0,1,2,3),(1,3,2,0),(3,0,2,1)):
    (frozenset({0,1,3}),frozenset({0,1,2,3}),11,(1,1,1,1),48),
}
assert set(classes) == set(expected)
for c, (ek, em, eb, ev, orbit) in expected.items():
    k,m,b,v = details[c]
    assert (k,m,b,v) == (ek,em,eb,ev)
    assert classes[c] == orbit
    actual_orbit = labeled_orbit(c,4)
    assert len(actual_orbit) == orbit
    assert (factorial(4)*factorial(3)) % orbit == 0

# Seven classes are asymmetric under the joint candidate/voter action;
# the exceptional 48-profile class has stabilizer order three.
stabilizers = sorted((factorial(4)*factorial(3)) // len(labeled_orbit(c,4)) for c in expected)
assert stabilizers == [1,1,1,1,1,1,1,3]

# The exceptional class contributes 48 labeled voter profiles;
# the direct full-domain enumeration above establishes this orbit size.

print("VERIFY_OK")
for nv in (1,2,3):
    print("voters",nv,"relation_hist",dict(relation_hist[nv]))
    print("voters",nv,"size_hist",dict(size_hist[nv]))
print("divergence",1056,"of",24**3,"=","11/144")
print("classes",len(classes),"orbit_sizes",sorted(classes.values()))
for c in sorted(expected):
    print("class",c,"data",expected[c])
