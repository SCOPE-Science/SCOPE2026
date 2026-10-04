#!/usr/bin/env python3
from itertools import permutations
from collections import Counter
import hashlib

RANKINGS = list(permutations((0,1,2)))
INDEX = {r:i for i,r in enumerate(RANKINGS)}

def compositions(total, k=6):
    if k == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for tail in compositions(total - x, k - 1):
            yield (x,) + tail

def pairwise_counts(profile):
    pair = [[0]*3 for _ in range(3)]
    for ranking,count in zip(RANKINGS, profile):
        pos = {a:i for i,a in enumerate(ranking)}
        for a in range(3):
            for b in range(a+1,3):
                if pos[a] < pos[b]:
                    pair[a][b] += count
                else:
                    pair[b][a] += count
    return pair

def coombs_closed(profile):
    """Three-candidate Coombs rule, unique-outcome only."""
    n = sum(profile)
    if n == 0:
        return None
    first = [0,0,0]
    last = [0,0,0]
    for ranking,count in zip(RANKINGS, profile):
        first[ranking[0]] += count
        last[ranking[-1]] += count
    for a in range(3):
        if 2*first[a] > n:
            return a
    worst = max(last)
    eliminated = [a for a in range(3) if last[a] == worst]
    if len(eliminated) != 1:
        return None
    e = eliminated[0]
    a,b = [x for x in range(3) if x != e]
    pair = pairwise_counts(profile)
    if pair[a][b] == pair[b][a]:
        return None
    return a if pair[a][b] > pair[b][a] else b

def coombs_iterative(profile):
    """Independent literal replay of Coombs elimination."""
    n = sum(profile)
    if n == 0:
        return None
    alive = {0,1,2}
    while len(alive) > 1:
        first = {a:0 for a in alive}
        for ranking,count in zip(RANKINGS, profile):
            for a in ranking:
                if a in alive:
                    first[a] += count
                    break
        for a in alive:
            if 2*first[a] > n:
                return a
        last = {a:0 for a in alive}
        for ranking,count in zip(RANKINGS, profile):
            for a in reversed(ranking):
                if a in alive:
                    last[a] += count
                    break
        worst = max(last.values())
        eliminated = [a for a in alive if last[a] == worst]
        if len(eliminated) != 1:
            return None
        alive.remove(eliminated[0])
    return next(iter(alive))

def preference_rank(ranking):
    return {a:i for i,a in enumerate(ranking)}

def profitable_events_profile_first(limit=10):
    events = set()
    bad_by_n = Counter()
    unique_by_n = Counter()
    total_by_n = Counter()
    for n in range(1, limit+1):
        for p in compositions(n):
            total_by_n[n] += 1
            w1 = coombs_closed(p)
            w2 = coombs_iterative(p)
            assert w1 == w2
            if w1 is None:
                continue
            unique_by_n[n] += 1
            for i,ranking in enumerate(RANKINGS):
                rank = preference_rank(ranking)
                for k in range(1, p[i]+1):
                    q = list(p)
                    q[i] -= k
                    q = tuple(q)
                    if sum(q) == 0:
                        continue
                    z1 = coombs_closed(q)
                    z2 = coombs_iterative(q)
                    assert z1 == z2
                    if z1 is not None and z1 != w1 and rank[z1] < rank[w1]:
                        events.add((p,i,k,w1,z1))
                        bad_by_n[n] += 1
    return events,bad_by_n,unique_by_n,total_by_n

def profitable_events_event_first(limit=10):
    """Independently starts from the abstention profile and adds one homogeneous group."""
    events = set()
    for after_n in range(1, limit):
        for q in compositions(after_n):
            after = coombs_iterative(q)
            if after is None:
                continue
            for i,ranking in enumerate(RANKINGS):
                rank = preference_rank(ranking)
                for k in range(1, limit-after_n+1):
                    p = list(q)
                    p[i] += k
                    p = tuple(p)
                    if sum(p) > limit:
                        break
                    before = coombs_iterative(p)
                    if before is not None and before != after and rank[after] < rank[before]:
                        events.add((p,i,k,before,after))
    return events

def permute_profile(profile, sigma):
    out = [0]*6
    for i,r in enumerate(RANKINGS):
        rr = tuple(sigma[a] for a in r)
        out[INDEX[rr]] = profile[i]
    return tuple(out)

def canonical_profile(profile):
    return min(permute_profile(profile,s) for s in permutations((0,1,2)))

events_a,bad_by_n,unique_by_n,total_by_n = profitable_events_profile_first(10)
events_b = profitable_events_event_first(10)
assert events_a == events_b

assert all(bad_by_n[n] == 0 for n in range(1,10))
events10 = sorted(e for e in events_a if sum(e[0]) == 10)
assert len(events10) == 12

bad_profiles = [e[0] for e in events10]
assert len(set(bad_profiles)) == 12
assert all(e[2] == 1 for e in events10)
assert Counter(bad_profiles) == Counter({p:1 for p in bad_profiles})

# Every bad profile has exactly one profitable homogeneous abstention event.
assert len({p for p,_,_,_,_ in events10}) == 12
assert Counter(p for p,_,_,_,_ in events10) == Counter({p:1 for p in bad_profiles})

# Candidate-relabeling quotient.
classes = Counter(canonical_profile(p) for p in bad_profiles)
assert len(classes) == 2
assert Counter(classes.values()) == Counter({6:2})

# Normalize the abstainer's ranking to A>B>C.
normalized = set()
for p,i,k,before,after in events10:
    ranking = RANKINGS[i]
    sigma = [None]*3
    for new,old in enumerate(ranking):
        sigma[old] = new
    sigma = tuple(sigma)
    pp = permute_profile(p,sigma)
    normalized.add((pp,k,sigma[before],sigma[after]))

expected = {
    ((1,0,2,3,4,0),1,2,1),
    ((1,1,2,3,3,0),1,2,1),
}
assert normalized == expected

# Direct mechanism checks for the two normalized forms.
for p,_,before,after in expected:
    assert before == 2 and after == 1
    assert coombs_closed(p) == 2
    q = list(p)
    q[0] -= 1  # one A>B>C voter abstains
    q = tuple(q)
    assert coombs_closed(q) == 1
    first = [0,0,0]
    last = [0,0,0]
    for r,c in zip(RANKINGS,p):
        first[r[0]] += c
        last[r[-1]] += c
    assert first[1] == 5 and sum(p) == 10 and 2*first[1] == 10
    assert last[1] == 4 and sorted(last) == [3,3,4]
    qfirst = [0,0,0]
    for r,c in zip(RANKINGS,q):
        qfirst[r[0]] += c
    assert qfirst[1] == 5 and sum(q) == 9 and 2*qfirst[1] > 9

assert total_by_n[10] == 3003
assert unique_by_n[10] == 2412
assert (12,3003) == (12,total_by_n[10])
assert (12,2412) == (12,unique_by_n[10])

digest = hashlib.sha256(
    "\n".join(
        f"{p}|{i}|{k}|{w}|{z}" for p,i,k,w,z in events10
    ).encode("ascii")
).hexdigest()

# Exact two-identical-voter variant used in some tie-independent presentations.
two_events = set()
for n in range(1,14):
    for p in compositions(n):
        before = coombs_closed(p)
        assert before == coombs_iterative(p)
        if before is None:
            continue
        for i,ranking in enumerate(RANKINGS):
            if p[i] < 2:
                continue
            q = list(p)
            q[i] -= 2
            q = tuple(q)
            if sum(q) == 0:
                continue
            after = coombs_closed(q)
            assert after == coombs_iterative(q)
            if after is None or after == before:
                continue
            rank = preference_rank(ranking)
            if rank[after] < rank[before]:
                two_events.add((p,i,2,before,after))

assert all(sum(p) >= 13 for p,_,_,_,_ in two_events)
events13 = sorted(e for e in two_events if sum(e[0]) == 13)
assert len(events13) == 18
assert len({p for p,_,_,_,_ in events13}) == 18
classes13 = Counter(canonical_profile(p) for p,_,_,_,_ in events13)
assert len(classes13) == 3
assert Counter(classes13.values()) == Counter({6:3})

normalized13 = set()
for p,i,k,before,after in events13:
    ranking = RANKINGS[i]
    sigma = [None]*3
    for new,old in enumerate(ranking):
        sigma[old] = new
    sigma = tuple(sigma)
    normalized13.add((permute_profile(p,sigma),k,sigma[before],sigma[after]))

expected13 = {
    ((2,0,2,4,5,0),2,2,1),
    ((2,1,2,4,4,0),2,2,1),
    ((2,2,2,4,3,0),2,2,1),
}
assert normalized13 == expected13

digest13 = hashlib.sha256(
    "\n".join(
        f"{p}|{i}|{k}|{w}|{z}" for p,i,k,w,z in events13
    ).encode("ascii")
).hexdigest()

print("VERIFY_OK")
print("no_show_events_by_n", {n:bad_by_n[n] for n in range(1,11)})
print("standard_minimal_total", 10)
print("n10_total_profiles", total_by_n[10])
print("n10_unique_outcome_profiles", unique_by_n[10])
print("n10_bad_profiles", 12)
print("n10_incidence_all_profiles", "4/1001")
print("n10_incidence_unique_profiles", "1/201")
print("n10_profitable_group_size_hist", {1:12})
print("n10_candidate_relabel_classes", 2)
print("n10_orbit_size_hist", {6:2})
print("n10_normalized_classes", sorted(expected))
print("n10_event_set_sha256", digest)
print("two_voter_variant_minimal_total", 13)
print("n13_two_voter_bad_profiles", 18)
print("n13_two_voter_candidate_relabel_classes", 3)
print("n13_two_voter_orbit_size_hist", {6:3})
print("n13_two_voter_normalized_classes", sorted(expected13))
print("n13_two_voter_event_set_sha256", digest13)
