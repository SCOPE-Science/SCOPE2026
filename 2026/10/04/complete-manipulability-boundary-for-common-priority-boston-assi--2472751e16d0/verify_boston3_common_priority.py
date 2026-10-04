#!/usr/bin/env python3
from itertools import permutations, product
from collections import defaultdict, Counter
import hashlib


def boston_rounds(profile):
    """Immediate acceptance with unit capacities and common priority 0>1>..."""
    n = len(profile)
    m = len(profile[0])
    assigned = [None] * n
    filled = [False] * m
    for r in range(m):
        apps = defaultdict(list)
        for i in range(n):
            if assigned[i] is None:
                s = profile[i][r]
                if not filled[s]:
                    apps[s].append(i)
        for s, applicants in apps.items():
            winner = min(applicants)
            assigned[winner] = s
            filled[s] = True
    return tuple(assigned)


def boston_scan(profile):
    """Independent replay: process rank levels and schools explicitly."""
    n = len(profile)
    m = len(profile[0])
    assigned = [None] * n
    occupied = set()
    for rank in range(m):
        for s in range(m):
            if s in occupied:
                continue
            eligible = [i for i in range(n) if assigned[i] is None and profile[i][rank] == s]
            if eligible:
                winner = min(eligible)
                assigned[winner] = s
                occupied.add(s)
    return tuple(assigned)


def all_events(n):
    prefs = list(permutations(range(n)))
    events = []
    for profile in product(prefs, repeat=n):
        truthful = boston_rounds(profile)
        assert truthful == boston_scan(profile)
        for i in range(n):
            rank = {s:r for r,s in enumerate(profile[i])}
            for report in prefs:
                if report == profile[i]:
                    continue
                q = list(profile)
                q[i] = report
                q = tuple(q)
                alt1 = boston_rounds(q)
                alt2 = boston_scan(q)
                assert alt1 == alt2
                if rank[alt1[i]] < rank[truthful[i]]:
                    events.append((profile, i, report, truthful, alt1))
    return events

# Two-agent square market is strategy-proof under a common priority.
ev2 = all_events(2)
assert ev2 == []

# Complete three-agent square market.
ev3 = all_events(3)
assert len(ev3) == 72
bad_profiles = {p for p,_,_,_,_ in ev3}
bad_pairs = {(p,i) for p,i,_,_,_ in ev3}
assert len(bad_profiles) == 36
assert len(bad_pairs) == 36
assert Counter(Counter((p,i) for p,i,_,_,_ in ev3).values()) == Counter({2:36})
assert Counter(i for p,i in bad_pairs) == Counter({1:24, 2:12})
assert all(i != 0 for _,i in bad_pairs)

# Every manipulation improves third choice to second choice.
assert Counter(
    (p[i].index(t[i]), p[i].index(a[i]))
    for p,i,r,t,a in ev3
) == Counter({(2,1):72})

# Structural iff criterion.
prefs3 = list(permutations(range(3)))
def structural_bad(p):
    r1,r2,r3 = p
    A = r1[0]
    if r2[0] != A:
        return False
    X = r2[1]
    return (r3[0] == A and r3[1] == X) or (r3[0] == X)

universe = list(product(prefs3, repeat=3))
assert {p for p in universe if structural_bad(p)} == bad_profiles
assert sum(structural_bad(p) for p in universe) == 36

# Structural identity of the vulnerable agent and reports.
for p in bad_profiles:
    r1,r2,r3 = p
    A = r1[0]
    X = r2[1]
    pair_events = [(i,r,t,a) for pp,i,r,t,a in ev3 if pp == p]
    assert len(pair_events) == 2
    vuln = {i for i,_,_,_ in pair_events}
    if r3[0] == X:
        assert vuln == {1}
        sincere = r2
    else:
        assert r3[0] == A and r3[1] == X
        assert vuln == {2}
        sincere = r3
    for i,r,t,a in pair_events:
        assert r[0] == X
        assert set(r[1:]) == ({0,1,2} - {X})
        assert sincere.index(t[i]) == 2
        assert sincere.index(a[i]) == 1

# Object-relabeling quotient, keeping priority positions fixed.
def relabel_profile(profile, sigma):
    return tuple(tuple(sigma[x] for x in order) for order in profile)

def canon_obj(profile):
    return min(relabel_profile(profile, s) for s in permutations(range(3)))

classes = Counter(canon_obj(p) for p in bad_profiles)
assert len(classes) == 6
assert Counter(classes.values()) == Counter({6:6})
expected = {
    ((0,1,2),(0,1,2),(0,1,2)),
    ((0,1,2),(0,1,2),(1,0,2)),
    ((0,1,2),(0,1,2),(1,2,0)),
    ((0,1,2),(0,2,1),(0,2,1)),
    ((0,1,2),(0,2,1),(2,0,1)),
    ((0,1,2),(0,2,1),(2,1,0)),
}
assert set(classes) == expected

# Direct count consequences.
assert 36 * 6 == 216
assert 36 * 18 == 648
assert 72 * 45 == 216 * 3 * 5

digest = hashlib.sha256(
    "\n".join(f"{p}|{i}|{r}|{t}|{a}" for p,i,r,t,a in sorted(ev3)).encode("ascii")
).hexdigest()

print("VERIFY_OK")
print("two_agent_events", len(ev2))
print("three_agent_profiles", 216)
print("bad_profiles", len(bad_profiles))
print("profile_incidence", "1/6")
print("vulnerable_agent_profile_pairs", len(bad_pairs))
print("distinguished_agent_incidence", "1/18")
print("profitable_reports", len(ev3))
print("report_triple_incidence", "1/45")
print("vulnerable_priority_rank_hist", {2:24, 3:12})
print("profit_reports_per_vulnerable_pair", {2:36})
print("improvement_rank", "third_to_second")
print("object_relabel_classes", len(classes))
print("orbit_size_hist", {6:6})
print("canonical_classes", sorted(expected))
print("event_set_sha256", digest)
