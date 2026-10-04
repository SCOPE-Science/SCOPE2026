#!/usr/bin/env python3
from itertools import permutations, product
from fractions import Fraction
from collections import Counter
import hashlib


def ps_event(profile):
    n = len(profile)
    rem = [Fraction(1) for _ in range(n)]
    alloc = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    t = Fraction(0)
    while t < 1:
        choice = []
        for pref in profile:
            choice.append(next(o for o in pref if rem[o] > 0))
        cnt = Counter(choice)
        dt = min(rem[o] / cnt[o] for o in cnt)
        for i,o in enumerate(choice):
            alloc[i][o] += dt
        for o,k in cnt.items():
            rem[o] -= k*dt
        t += dt
    assert all(x == 0 for x in rem)
    return tuple(tuple(r) for r in alloc)


def ps_ticks12(profile):
    """Independent finite replay for the 3x3 universe using twelve exact microticks."""
    assert len(profile) == 3
    rem = [12,12,12]
    alloc = [[0,0,0] for _ in range(3)]
    for _ in range(12):
        choice = [next(o for o in pref if rem[o] > 0) for pref in profile]
        cnt = Counter(choice)
        assert all(rem[o] >= k for o,k in cnt.items())
        for i,o in enumerate(choice):
            alloc[i][o] += 1
        for o,k in cnt.items():
            rem[o] -= k
    assert rem == [0,0,0]
    return tuple(tuple(Fraction(x,12) for x in r) for r in alloc)


def sd_ge(a,b,pref):
    """a weakly stochastically dominates b under strict ranking pref."""
    ca = cb = Fraction(0)
    for o in pref:
        ca += a[o]; cb += b[o]
        if ca < cb:
            return False
    return True


def sd_strict(a,b,pref):
    return sd_ge(a,b,pref) and a != b


def transform_pref(pref, objperm):
    return tuple(objperm[o] for o in pref)


def transform_profile(profile, agentperm, objperm):
    out = [None]*len(profile)
    for i,pref in enumerate(profile):
        out[agentperm[i]] = transform_pref(pref,objperm)
    return tuple(out)


def canonical_profile(profile):
    n = len(profile)
    return min(
        transform_profile(profile,a,o)
        for a in permutations(range(n))
        for o in permutations(range(n))
    )


def normalized_event(profile, manip, report):
    """Fix manipulator first, map true order to ABC, sort the other agents."""
    n = len(profile)
    true = profile[manip]
    objperm = [None]*n
    for new,old in enumerate(true):
        objperm[old] = new
    def tr(pref):
        return transform_pref(pref, tuple(objperm))
    others = sorted(tr(profile[j]) for j in range(n) if j != manip)
    return (tr(true), tuple(others), tr(report))


def census(n):
    prefs = list(permutations(range(n)))
    profiles = list(product(prefs, repeat=n))
    alloc = {p: ps_event(p) for p in profiles}
    if n == 3:
        for p in profiles:
            assert alloc[p] == ps_ticks12(p)
    events = []
    weak_improvements = []
    for p in profiles:
        truth = alloc[p]
        for i in range(n):
            for r in prefs:
                if r == p[i]:
                    continue
                q = list(p); q[i] = r; q = tuple(q)
                mis = alloc[q]
                # Full strategyproofness requires truth to weakly SD-dominate every report.
                if not sd_ge(truth[i], mis[i], p[i]):
                    events.append((p,i,r))
                # Weak strategyproofness rules out strict SD gains from a misreport.
                if sd_strict(mis[i], truth[i], p[i]):
                    weak_improvements.append((p,i,r))
    return prefs, profiles, alloc, events, weak_improvements

# n=2 is strategyproof: exhaustive finite confirmation.
_, profiles2, alloc2, events2, weak2 = census(2)
assert len(profiles2) == 4
assert events2 == [] and weak2 == []

prefs, profiles, alloc, events, weak = census(3)
assert len(profiles) == 216
assert len(events) == 72
assert weak == []

bad_profiles = {p for p,_,_ in events}
assert len(bad_profiles) == 54
assert Fraction(len(bad_profiles), len(profiles)) == Fraction(1,4)

agent_reports = Counter((p,i) for p,i,r in events)
assert len(agent_reports) == 72
assert Counter(agent_reports.values()) == Counter({1:72})
assert Fraction(len(agent_reports), len(profiles)*3) == Fraction(1,9)

bad_agents_per_profile = Counter(sum((p,i) in agent_reports for i in range(3)) for p in bad_profiles)
assert bad_agents_per_profile == Counter({1:36, 2:18})

profile_orbits = Counter(canonical_profile(p) for p in bad_profiles)
expected_profile_orbits = {
    ((0,1,2),(0,1,2),(1,2,0)): 18,
    ((0,1,2),(0,2,1),(1,0,2)): 36,
}
assert dict(profile_orbits) == expected_profile_orbits

norm = Counter(normalized_event(p,i,r) for p,i,r in events)
expected_norm = {
    ((0,1,2), ((0,1,2),(1,2,0)), (1,0,2)): 36,
    ((0,1,2), ((1,0,2),(1,2,0)), (1,0,2)): 36,
}
assert dict(norm) == expected_norm

# Every failure swaps only the top two objects, and has one universal lottery geometry.
prefix_hist = Counter()
allocation_pair_hist = Counter()
for p,i,r in events:
    assert tuple(p[i].index(o) for o in r) == (1,0,2)
    q = list(p); q[i] = r; q = tuple(q)
    truth = alloc[p][i]
    mis = alloc[q][i]
    pref = p[i]
    cum_t = cum_m = Fraction(0)
    diffs = []
    for o in pref[:-1]:
        cum_t += truth[o]; cum_m += mis[o]
        diffs.append(cum_m-cum_t)
    prefix_hist[tuple(diffs)] += 1
    rel_truth = tuple(truth[o] for o in pref)
    rel_mis = tuple(mis[o] for o in pref)
    allocation_pair_hist[(rel_truth,rel_mis)] += 1

assert prefix_hist == Counter({(Fraction(-1,4), Fraction(1,12)):72})
expected_alloc_pairs = Counter({
    ((Fraction(1,2),Fraction(1,6),Fraction(1,3)),
     (Fraction(1,4),Fraction(1,2),Fraction(1,4))):36,
    ((Fraction(3,4),Fraction(0),Fraction(1,4)),
     (Fraction(1,2),Fraction(1,3),Fraction(1,6))):36,
})
assert allocation_pair_hist == expected_alloc_pairs

# Both allocation pairs induce the same EU gain formula.
# Let utilities of top/middle/bottom be T,M,B. Gain = (-3T+4M-B)/12.
for (tr,mi),count in allocation_pair_hist.items():
    delta = tuple(mi[j]-tr[j] for j in range(3))
    assert delta == (Fraction(-1,4), Fraction(1,3), Fraction(-1,12))

# Full 3x3 profile space has ten agent/object isomorphism classes, as in the classical appendix.
all_orbits = Counter(canonical_profile(p) for p in profiles)
assert len(all_orbits) == 10
assert Counter(all_orbits.values()) == Counter({18:5,36:3,6:1,12:1})

digest = hashlib.sha256(
    "\n".join(f"{p}|{i}|{r}" for p,i,r in sorted(events)).encode("ascii")
).hexdigest()

print("VERIFY_OK")
print("n2_profiles", len(profiles2))
print("n2_strategyproofness_failures", len(events2))
print("n3_profiles", len(profiles))
print("n3_bad_profiles", len(bad_profiles))
print("n3_bad_profile_fraction", "1/4")
print("n3_bad_agent_profile_pairs", len(agent_reports))
print("n3_bad_agent_fraction", "1/9")
print("n3_failure_events", len(events))
print("n3_reports_per_bad_agent_hist", dict(sorted(Counter(agent_reports.values()).items())))
print("n3_bad_agents_per_profile_hist", dict(sorted(bad_agents_per_profile.items())))
print("n3_profile_orbits", dict(sorted((str(k),v) for k,v in profile_orbits.items())))
print("n3_normalized_event_orbits", dict(sorted((str(k),v) for k,v in norm.items())))
print("n3_prefix_difference_hist", dict((str(k),v) for k,v in prefix_hist.items()))
print("n3_weak_strategyproofness_sd_improvements", len(weak))
print("utility_gain_formula", "(-3*T+4*M-B)/12")
print("normalized_profit_condition", "M>3/4 when T=1,B=0")
print("all_profile_isomorphism_classes", len(all_orbits))
print("event_set_sha256", digest)
