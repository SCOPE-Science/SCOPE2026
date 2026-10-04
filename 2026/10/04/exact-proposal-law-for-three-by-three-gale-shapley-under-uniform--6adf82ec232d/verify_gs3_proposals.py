#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
import hashlib

R3 = list(permutations(range(3)))

def gs_sequential(men, women):
    n = 3
    wrank = [{m:r for r,m in enumerate(pref)} for pref in women]
    next_idx = [0]*n
    held = [None]*n
    free = list(range(n))
    proposals = 0
    while free:
        m = free.pop(0)
        w = men[m][next_idx[m]]
        next_idx[m] += 1
        proposals += 1
        cur = held[w]
        if cur is None:
            held[w] = m
        elif wrank[w][m] < wrank[w][cur]:
            held[w] = m
            free.append(cur)
        else:
            free.append(m)
    match = [None]*n
    for w,m in enumerate(held):
        match[m] = w
    return tuple(match), proposals

def gs_simultaneous(men, women):
    n = 3
    wrank = [{m:r for r,m in enumerate(pref)} for pref in women]
    next_idx = [0]*n
    held_by_w = [None]*n
    engaged_m = [False]*n
    proposals = 0
    while not all(engaged_m):
        batch = {}
        proposers = [m for m in range(n) if not engaged_m[m]]
        for m in proposers:
            w = men[m][next_idx[m]]
            next_idx[m] += 1
            proposals += 1
            batch.setdefault(w, []).append(m)
        for w,ms in batch.items():
            if held_by_w[w] is not None:
                ms.append(held_by_w[w])
            best = min(ms, key=lambda m: wrank[w][m])
            for m in ms:
                engaged_m[m] = (m == best)
            held_by_w[w] = best
    match = [None]*n
    for w,m in enumerate(held_by_w):
        match[m] = w
    return tuple(match), proposals

def stable_count(men, women):
    mrank = [{w:r for r,w in enumerate(pref)} for pref in men]
    wrank = [{m:r for r,m in enumerate(pref)} for pref in women]
    out = 0
    for match in permutations(range(3)):
        inv = [None]*3
        for m,w in enumerate(match):
            inv[w] = m
        stable = True
        for m in range(3):
            for w in range(3):
                if match[m] == w:
                    continue
                if mrank[m][w] < mrank[m][match[m]] and wrank[w][m] < wrank[w][inv[w]]:
                    stable = False
                    break
            if not stable:
                break
        out += stable
    return out

proposal_hist = Counter()
rank_multiset_hist = Counter()
joint_hist = Counter()
stable_hist = Counter()
event_lines = []

for profile in product(R3, repeat=6):
    men, women = profile[:3], profile[3:]
    m1,p1 = gs_sequential(men, women)
    m2,p2 = gs_simultaneous(men, women)
    assert (m1,p1) == (m2,p2)
    ranks = tuple(sorted(men[i].index(m1[i])+1 for i in range(3)))
    assert sum(ranks) == p1
    s = stable_count(men, women)
    proposal_hist[p1] += 1
    rank_multiset_hist[ranks] += 1
    joint_hist[(p1,s)] += 1
    stable_hist[s] += 1
    event_lines.append(f"{profile}|{m1}|{p1}|{ranks}|{s}")

assert proposal_hist == Counter({3:10368,4:15552,5:14256,6:5832,7:648})
assert rank_multiset_hist == Counter({
    (1,1,1):10368,
    (1,1,2):15552,
    (1,1,3):7776,
    (1,2,2):6480,
    (1,2,3):5184,
    (2,2,2):648,
    (2,2,3):648,
})
assert stable_hist == Counter({1:34080,2:11484,3:1092})
assert joint_hist == Counter({
    (3,1):5064,(3,2):4572,(3,3):732,
    (4,1):10224,(4,2):5004,(4,3):324,
    (5,1):12420,(5,2):1800,(5,3):36,
    (6,1):5724,(6,2):108,
    (7,1):648,
})

N = 6**6
mean = Fraction(sum(p*c for p,c in proposal_hist.items()), N)
mean2 = Fraction(sum(p*p*c for p,c in proposal_hist.items()), N)
var = mean2 - mean*mean
assert mean == Fraction(35,8)
assert var == Fraction(583,576)

cond = {}
for s in (1,2,3):
    den = stable_hist[s]
    num = sum(p*c for (p,t),c in joint_hist.items() if t == s)
    cond[s] = Fraction(num, den)
assert cond == {
    1:Fraction(13089,2840),
    2:Fraction(1205,319),
    3:Fraction(306,91),
}

# A three-proposal run is exactly one proposal from every man.
assert proposal_hist[3] == 10368
# The sharp worst case is seven proposals, never eight or nine.
assert max(proposal_hist) == 7

digest = hashlib.sha256("\n".join(event_lines).encode("utf-8")).hexdigest()

print("VERIFY_OK")
print("profiles", N)
print("proposal_hist", dict(sorted(proposal_hist.items())))
print("proposal_probs", {p:str(Fraction(c,N)) for p,c in sorted(proposal_hist.items())})
print("rank_multiset_hist", {str(k):v for k,v in sorted(rank_multiset_hist.items())})
print("mean", str(mean))
print("variance", str(var))
print("stable_hist", dict(sorted(stable_hist.items())))
print("joint_hist", {str(k):v for k,v in sorted(joint_hist.items())})
print("conditional_means", {k:str(v) for k,v in cond.items()})
print("sha256", digest)
