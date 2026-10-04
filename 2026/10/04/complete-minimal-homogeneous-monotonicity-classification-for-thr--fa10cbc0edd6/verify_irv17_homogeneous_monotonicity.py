#!/usr/bin/env python3
from itertools import permutations
from collections import Counter
from fractions import Fraction
import math, hashlib

RANKINGS = list(permutations((0,1,2)))
INDEX = {r:i for i,r in enumerate(RANKINGS)}

def compositions(total, k=6):
    if k == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for tail in compositions(total-x, k-1):
            yield (x,) + tail

def irv_unique(counts):
    """Three-candidate IRV, returning None whenever a decisive tie occurs."""
    n = sum(counts)
    first = [0,0,0]
    for r,c in zip(RANKINGS, counts):
        first[r[0]] += c
    for a in range(3):
        if 2*first[a] > n:
            return a
    low = min(first)
    losers = [a for a in range(3) if first[a] == low]
    if len(losers) != 1:
        return None
    elim = losers[0]
    alive = [a for a in range(3) if a != elim]
    final = {a:0 for a in alive}
    for r,c in zip(RANKINGS, counts):
        for a in r:
            if a != elim:
                final[a] += c
                break
    if final[alive[0]] == final[alive[1]]:
        return None
    return alive[0] if final[alive[0]] > final[alive[1]] else alive[1]

def raise_moves():
    """All strict moves that raise one candidate and preserve the order of the other two."""
    out = []
    for i,r in enumerate(RANKINGS):
        for oldpos,w in enumerate(r):
            if oldpos == 0:
                continue
            for newpos in range(oldpos):
                rr = list(r)
                rr.pop(oldpos)
                rr.insert(newpos,w)
                rr = tuple(rr)
                out.append((w,i,INDEX[rr],r,rr,oldpos-newpos))
    return out

MOVES = raise_moves()

def harmful_homogeneous_events(n):
    """All events: a nonempty same-ballot group raises the current winner identically and makes that winner lose."""
    events = []
    for c in compositions(n):
        w = irv_unique(c)
        if w is None:
            continue
        for mw,i,j,r,rr,dist in MOVES:
            if mw != w or c[i] == 0:
                continue
            for k in range(1,c[i]+1):
                cc = list(c)
                cc[i] -= k
                cc[j] += k
                cc = tuple(cc)
                w2 = irv_unique(cc)
                if w2 is not None and w2 != w:
                    events.append((c,w,i,j,k,w2,dist))
    return events

def permute_counts(c, sigma):
    out = [0]*6
    for i,r in enumerate(RANKINGS):
        rr = tuple(sigma[a] for a in r)
        out[INDEX[rr]] = c[i]
    return tuple(out)

def canon(c):
    return min(permute_counts(c,s) for s in permutations((0,1,2)))

# Route A: exhaustive profile-and-change search through the boundary.
count_by_n = {}
events17 = None
for n in range(1,18):
    e = harmful_homogeneous_events(n)
    count_by_n[n] = len(e)
    if n == 17:
        events17 = e
    else:
        assert len(e) == 0
assert len(events17) == 252
assert len({e[0] for e in events17}) == 252
assert Counter(e[4] for e in events17) == Counter({2:252})
assert Counter(e[6] for e in events17) == Counter({1:126,2:126})

# Exact incidence denominators.
all17 = math.comb(22,5)
unique17 = sum(irv_unique(c) is not None for c in compositions(17))
assert all17 == 26334
assert unique17 == 25470
assert Fraction(252, all17) == Fraction(2,209)
assert Fraction(252, unique17) == Fraction(14,1415)

# Candidate-relabeling quotient.
orbits = Counter(canon(e[0]) for e in events17)
assert len(orbits) == 42
assert Counter(orbits.values()) == Counter({6:42})

# Normalize each event so old winner=A=0, new winner=B=1, remaining candidate=C=2.
def normalize_event(e):
    c,w,i,j,k,w2,dist = e
    rem = ({0,1,2}-{w,w2}).pop()
    sigma = [None]*3
    sigma[w] = 0
    sigma[w2] = 1
    sigma[rem] = 2
    sigma = tuple(sigma)
    cc = permute_counts(c,sigma)
    oldr = tuple(sigma[a] for a in RANKINGS[i])
    newr = tuple(sigma[a] for a in RANKINGS[j])
    return cc,oldr,newr,k,dist

norm = [normalize_event(e) for e in events17]
norm_unique = {(cc,oldr,newr,k) for cc,oldr,newr,k,_ in norm}
assert len(norm_unique) == 42

# Route B: symbolic normal-form generation.
fam1 = set()
fam2 = set()
for x in range(7):
    for y in range(3,6):
        # Ballot order ABC, ACB, BAC, BCA, CAB, CBA.
        c1 = (x,6-x,y,5-y,2,4)
        c2 = (x,6-x,y,5-y,0,6)
        fam1.add((c1,(2,0,1),(0,2,1),2))  # two CAB -> ACB
        fam2.add((c2,(2,1,0),(0,2,1),2))  # two CBA -> ACB
        assert irv_unique(c1) == 0
        d1 = list(c1); d1[4] -= 2; d1[1] += 2
        assert irv_unique(tuple(d1)) == 1
        assert irv_unique(c2) == 0
        d2 = list(c2); d2[5] -= 2; d2[1] += 2
        assert irv_unique(tuple(d2)) == 1
expected = fam1 | fam2
assert len(fam1) == len(fam2) == 21
assert norm_unique == expected

# Verify each bad profile has exactly one harmful homogeneous raise event.
profile_event_count = Counter(e[0] for e in events17)
assert set(profile_event_count.values()) == {1}

# Each ordered old/new winner transition occurs equally often.
transition_hist = Counter((e[1],e[5]) for e in events17)
assert len(transition_hist) == 6
assert set(transition_hist.values()) == {42}

# Independent arithmetic lower-bound check encoded from the proof:
# Let b be the old plurality-loser first count and delta=c-b>=1.
# If k donor voters move from C-first to A-first, then k>=delta+1.
# For B to beat A after C is eliminated, even the most favorable transfers require
# b+c-k > a+k. With a>=b+1, this forces b>=delta+4, hence n>=4*delta+13>=17.
for delta in range(1,20):
    for b in range(1,30):
        a_min = b+1
        k_min = delta+1
        feasible_necessary = (b + (b+delta) - k_min > a_min + k_min)
        if feasible_necessary:
            assert b >= delta+4
            n_lower = a_min + b + (b+delta)
            assert n_lower >= 4*delta + 13 >= 17

digest = hashlib.sha256(
    "\n".join(repr(z) for z in sorted(norm_unique)).encode("ascii")
).hexdigest()

print("VERIFY_OK")
print("counts_n_1_to_17", count_by_n)
print("n17_all_anonymous_profiles", all17)
print("n17_unique_irv_profiles", unique17)
print("n17_harmful_profiles", 252)
print("all_profile_incidence", "2/209")
print("unique_profile_incidence", "14/1415")
print("changed_group_size_hist", {2:252})
print("raise_distance_hist", dict(sorted(Counter(e[6] for e in events17).items())))
print("candidate_relabel_classes", 42)
print("orbit_size_hist", dict(sorted(Counter(orbits.values()).items())))
print("family_sizes", (len(fam1),len(fam2)))
print("transition_hist", dict(sorted(transition_hist.items())))
print("normal_form_digest_sha256", digest)
