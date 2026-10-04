#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
import hashlib

def immediate_acceptance(profile):
    n = len(profile)
    assigned = [None] * n
    available = set(range(n))
    for rnd in range(n):
        applicants = {s: [] for s in available}
        for i in range(n):
            if assigned[i] is None:
                s = profile[i][rnd]
                if s in available:
                    applicants[s].append(i)
        for s in sorted(list(applicants)):
            if applicants[s]:
                # Common priority 0 > 1 > ... > n-1.
                i = min(applicants[s])
                assigned[i] = s
                available.remove(s)
    return tuple(assigned)

def immediate_acceptance_direct(profile):
    """Independent rank-by-rank replay of the same irreversible admissions."""
    n = len(profile)
    result = [None] * n
    free_students = set(range(n))
    free_schools = set(range(n))
    for rank in range(n):
        for s in tuple(sorted(free_schools)):
            cand = [i for i in free_students if profile[i][rank] == s]
            if cand:
                i = min(cand)
                result[i] = s
                free_students.remove(i)
                free_schools.remove(s)
    return tuple(result)

def deferred_acceptance(profile):
    n = len(profile)
    next_choice = [0] * n
    holder = {}
    free = set(range(n))
    while free:
        i = min(free)
        free.remove(i)
        s = profile[i][next_choice[i]]
        next_choice[i] += 1
        if s not in holder:
            holder[s] = i
        else:
            j = holder[s]
            if i < j:
                holder[s] = i
                free.add(j)
            else:
                free.add(i)
    result = [None] * n
    for s, i in holder.items():
        result[i] = s
    return tuple(result)

def serial_dictatorship(profile):
    """With one common school priority, DA equals this priority serial dictatorship."""
    n = len(profile)
    available = set(range(n))
    result = [None] * n
    for i in range(n):
        for s in profile[i]:
            if s in available:
                result[i] = s
                available.remove(s)
                break
    return tuple(result)

def relabel_schools(profile, sigma):
    return tuple(tuple(sigma[s] for s in pref) for pref in profile)

def canonical_school_orbit(profile):
    n = len(profile)
    return min(relabel_schools(profile, sigma) for sigma in permutations(range(n)))

def ranks(profile, matching):
    return tuple(profile[i].index(matching[i]) + 1 for i in range(len(profile)))

def divergence_criterion_3(profile):
    # Exact theorem criterion under common priority 0 > 1 > 2:
    # students 0 and 1 share a first choice A, and student 2's first
    # choice is student 1's second choice.
    return (
        profile[0][0] == profile[1][0]
        and profile[2][0] == profile[1][1]
    )

# Sharp 2x2 predecessor.
R2 = list(permutations(range(2)))
for P in product(R2, repeat=2):
    assert immediate_acceptance(P) == immediate_acceptance_direct(P)
    assert deferred_acceptance(P) == serial_dictatorship(P)
    assert immediate_acceptance(P) == deferred_acceptance(P)

# Complete 3x3 census.
R3 = list(permutations(range(3)))
divergent = []
criterion = []
relation_hist = Counter()
rankpair_hist = Counter()

for P in product(R3, repeat=3):
    b1 = immediate_acceptance(P)
    b2 = immediate_acceptance_direct(P)
    d1 = deferred_acceptance(P)
    d2 = serial_dictatorship(P)
    assert b1 == b2
    assert d1 == d2
    crit = divergence_criterion_3(P)
    if crit:
        criterion.append(P)
    if b1 != d1:
        divergent.append(P)
        rb = ranks(P, b1)
        rd = ranks(P, d1)
        bdom = all(x <= y for x, y in zip(rb, rd)) and any(x < y for x, y in zip(rb, rd))
        ddom = all(y <= x for x, y in zip(rb, rd)) and any(y < x for x, y in zip(rb, rd))
        relation = "BOSTON_DOMINATES" if bdom else "DA_DOMINATES" if ddom else "INCOMPARABLE"
        relation_hist[relation] += 1
        rankpair_hist[(rb, rd)] += 1

assert set(divergent) == set(criterion)
assert len(divergent) == 24
assert relation_hist == Counter({"INCOMPARABLE": 24})
assert len(set(canonical_school_orbit(P) for P in divergent)) == 4

classes = Counter(canonical_school_orbit(P) for P in divergent)
assert Counter(classes.values()) == Counter({6: 4})

expected_classes = {
    ((0,1,2),(0,1,2),(1,0,2)),
    ((0,1,2),(0,1,2),(1,2,0)),
    ((0,1,2),(0,2,1),(2,0,1)),
    ((0,1,2),(0,2,1),(2,1,0)),
}
assert set(classes) == expected_classes

# Structural consequences at every divergent profile.
for P in divergent:
    B = immediate_acceptance(P)
    D = deferred_acceptance(P)
    A = P[0][0]
    X = P[1][1]
    Y = ({0,1,2} - {A, X}).pop()
    assert P[1][0] == A
    assert P[2][0] == X
    assert B[0] == D[0] == A
    assert D[1] == X and B[1] == Y
    assert B[2] == X and D[2] == Y
    assert P[1].index(D[1]) == 1 and P[1].index(B[1]) == 2
    assert P[2].index(B[2]) == 0
    assert P[2].index(D[2]) in (1, 2)

assert rankpair_hist == Counter({
    ((1,3,1),(1,2,3)): 12,
    ((1,3,1),(1,2,2)): 12,
})

digest = hashlib.sha256(
    "\n".join(repr(P) for P in sorted(divergent)).encode("ascii")
).hexdigest()

print("VERIFY_OK")
print("n2_profiles", 4)
print("n2_divergent", 0)
print("n3_profiles", 216)
print("n3_divergent", 24)
print("n3_incidence", "1/9")
print("criterion_equivalence", True)
print("welfare_relation_hist", dict(relation_hist))
print("school_relabel_classes", 4)
print("orbit_size_hist", dict(Counter(classes.values())))
print("rankpair_hist", {str(k):v for k,v in rankpair_hist.items()})
print("canonical_classes", sorted(expected_classes))
print("divergent_set_sha256", digest)
