#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter, defaultdict
from math import factorial
import hashlib

RANKINGS = list(permutations((0,1,2)))
INDEX = {r:i for i,r in enumerate(RANKINGS)}

def compositions(total, k=6):
    if k == 1:
        yield (total,)
        return
    for x in range(total+1):
        for tail in compositions(total-x, k-1):
            yield (x,) + tail

def multinomial(p):
    z = factorial(sum(p))
    for c in p:
        z //= factorial(c)
    return z

def baldwin_iter(profile):
    alive = [0,1,2]
    while len(alive) > 1:
        score = {a:0 for a in alive}
        for r,c in zip(RANKINGS, profile):
            if not c:
                continue
            rr = [a for a in r if a in alive]
            m = len(rr)
            for j,a in enumerate(rr):
                score[a] += c*(m-1-j)
        low = min(score.values())
        lows = [a for a in alive if score[a] == low]
        if len(lows) != 1:
            return None
        alive.remove(lows[0])
    return alive[0]

def baldwin_closed(profile):
    score = [0,0,0]
    pair = [[0]*3 for _ in range(3)]
    for r,c in zip(RANKINGS, profile):
        score[r[0]] += 2*c
        score[r[1]] += c
        pos = {a:i for i,a in enumerate(r)}
        for a in range(3):
            for b in range(a+1,3):
                if pos[a] < pos[b]:
                    pair[a][b] += c
                else:
                    pair[b][a] += c
    low = min(score)
    lows = [a for a,s in enumerate(score) if s == low]
    if len(lows) != 1:
        return None
    e = lows[0]
    a,b = [x for x in range(3) if x != e]
    if pair[a][b] == pair[b][a]:
        return None
    return a if pair[a][b] > pair[b][a] else b

def rankmap(r):
    return {a:i for i,a in enumerate(r)}

def manipulate_events(profile):
    w1 = baldwin_iter(profile)
    w2 = baldwin_closed(profile)
    assert w1 == w2
    if w1 is None:
        return []
    out = []
    for i,r in enumerate(RANKINGS):
        if profile[i] == 0:
            continue
        rr = rankmap(r)
        good = []
        for j,s in enumerate(RANKINGS):
            if j == i:
                continue
            q = list(profile)
            q[i] -= 1
            q[j] += 1
            q = tuple(q)
            z1 = baldwin_iter(q)
            z2 = baldwin_closed(q)
            assert z1 == z2
            if z1 is not None and rr[z1] < rr[w1]:
                good.append((j,z1,q))
        if good:
            out.append((i,w1,tuple(good)))
    return out

def permute_profile(profile, sigma):
    out = [0]*6
    for i,r in enumerate(RANKINGS):
        rr = tuple(sigma[a] for a in r)
        out[INDEX[rr]] = profile[i]
    return tuple(out)

def canonical_profile(profile):
    return min(permute_profile(profile,s) for s in permutations((0,1,2)))

# Route A: anonymous exhaustive census for n <= 5.
by_n = {}
all_bad = {}
unique_anon = {}
unique_labeled = {}
for n in range(1,6):
    bad = []
    uanon = 0
    ulab = 0
    for p in compositions(n):
        w1 = baldwin_iter(p)
        w2 = baldwin_closed(p)
        assert w1 == w2
        if w1 is not None:
            uanon += 1
            ulab += multinomial(p)
        ev = manipulate_events(p)
        if ev:
            bad.append((p,ev))
    by_n[n] = len(bad)
    all_bad[n] = bad
    unique_anon[n] = uanon
    unique_labeled[n] = ulab

assert [by_n[n] for n in range(1,5)] == [0,0,0,0]
assert by_n[5] == 6
bad5 = all_bad[5]
assert all(len(ev) == 1 for p,ev in bad5)
assert all(len(ev[0][2]) == 1 for p,ev in bad5)
assert all(p[ev[0][0]] == 2 for p,ev in bad5)
assert unique_anon[5] == 222
assert unique_labeled[5] == 6636
assert sum(multinomial(p) for p,ev in bad5) == 180
assert sum(multinomial(p)*p[ev[0][0]] for p,ev in bad5) == 360

# All six anonymous bad profiles form one candidate relabeling orbit.
classes = Counter(canonical_profile(p) for p,ev in bad5)
assert len(classes) == 1
assert list(classes.values()) == [6]

# Normalize the sincere ranking of the manipulator to A>B>C.
normalized = set()
for p,ev in bad5:
    i,w,good = ev[0]
    j,z,q = good[0]
    true_r = RANKINGS[i]
    sigma = [None]*3
    for new,old in enumerate(true_r):
        sigma[old] = new
    sigma = tuple(sigma)
    pp = permute_profile(p,sigma)
    report = tuple(sigma[a] for a in RANKINGS[j])
    normalized.add((pp,report,sigma[w],sigma[z],p[i]))

expected = {
    ((2,0,0,1,2,0),(1,2,0),2,1,2),
}
assert normalized == expected

# Direct mechanism check for the normalized representative.
p = (2,0,0,1,2,0)
q = (1,0,0,2,2,0)
assert baldwin_iter(p) == 2 and baldwin_iter(q) == 1

def round_scores(profile, alive):
    score = {a:0 for a in alive}
    for r,c in zip(RANKINGS, profile):
        rr = [a for a in r if a in alive]
        m = len(rr)
        for j,a in enumerate(rr):
            score[a] += c*(m-1-j)
    return score
assert round_scores(p,[0,1,2]) == {0:6,1:4,2:5}
assert round_scores(p,[0,2]) == {0:2,2:3}
assert round_scores(q,[0,1,2]) == {0:4,1:5,2:6}
assert round_scores(q,[1,2]) == {1:3,2:2}

# Route B: enumerate all labeled profiles independently and compare the bad anonymous set.
labeled_bad_counts = Counter()
labeled_vulnerable_pairs = 0
labeled_events = 0
for prof in product(range(6), repeat=5):
    p = [0]*6
    for x in prof:
        p[x] += 1
    p = tuple(p)
    w = baldwin_closed(p)
    if w is None:
        continue
    bad_agents = []
    for aidx,true_i in enumerate(prof):
        r = RANKINGS[true_i]
        rr = rankmap(r)
        goods = []
        for j in range(6):
            if j == true_i:
                continue
            q = list(p)
            q[true_i] -= 1
            q[j] += 1
            z = baldwin_closed(tuple(q))
            if z is not None and rr[z] < rr[w]:
                goods.append((j,z))
        if goods:
            bad_agents.append((aidx,true_i,tuple(goods)))
            labeled_vulnerable_pairs += 1
            labeled_events += len(goods)
    if bad_agents:
        labeled_bad_counts[p] += 1

assert set(labeled_bad_counts) == {p for p,ev in bad5}
for p,count in labeled_bad_counts.items():
    assert count == multinomial(p)
assert sum(labeled_bad_counts.values()) == 180
assert labeled_vulnerable_pairs == 360
assert labeled_events == 360

# Every bad labeled profile has exactly the two voters of the vulnerable type as manipulators,
# each with the same unique false report.
for p,ev in bad5:
    i,w,good = ev[0]
    assert p[i] == 2 and len(good) == 1

# Hash the exact anonymous event set.
records=[]
for p,ev in sorted(bad5):
    i,w,good=ev[0]
    j,z,q=good[0]
    records.append(f"{p}|{i}|{j}|{w}|{z}|{q}")
digest=hashlib.sha256("\n".join(records).encode('ascii')).hexdigest()

print('VERIFY_OK')
print('bad_anonymous_by_n',by_n)
print('n5_total_anonymous',252)
print('n5_unique_outcome_anonymous',unique_anon[5])
print('n5_bad_anonymous',6)
print('n5_bad_anonymous_incidence_all','1/42')
print('n5_bad_labeled_profiles',180)
print('n5_total_labeled_profiles',6**5)
print('n5_bad_labeled_incidence_all','5/216')
print('n5_unique_outcome_labeled',unique_labeled[5])
print('n5_bad_labeled_incidence_unique','15/553')
print('n5_vulnerable_agent_profile_pairs',360)
print('n5_vulnerable_agent_profile_incidence_all','1/108')
print('n5_vulnerable_agent_profile_incidence_unique','6/553')
print('n5_profitable_report_events',360)
print('n5_candidate_relabel_classes',1)
print('normalized_representative',next(iter(expected)))
print('event_set_sha256',digest)
