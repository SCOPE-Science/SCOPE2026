#!/usr/bin/env python3
from itertools import permutations
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib, math

RANKINGS = list(permutations((0,1,2)))
RINDEX = {r:i for i,r in enumerate(RANKINGS)}


def compositions(total, k=6):
    if k == 1:
        yield (total,)
        return
    for x in range(total+1):
        for tail in compositions(total-x, k-1):
            yield (x,) + tail


def irv_unique(c):
    n = sum(c)
    if n <= 0:
        return None
    first = [0,0,0]
    for r,x in zip(RANKINGS,c):
        first[r[0]] += x
    for a in range(3):
        if 2*first[a] > n:
            return a
    mn = min(first)
    lows = [a for a in range(3) if first[a] == mn]
    if len(lows) != 1:
        return None
    elim = lows[0]
    alive = [a for a in range(3) if a != elim]
    final = {a:0 for a in alive}
    for r,x in zip(RANKINGS,c):
        if x == 0: continue
        for a in r:
            if a != elim:
                final[a] += x
                break
    if final[alive[0]] == final[alive[1]]:
        return None
    return alive[0] if final[alive[0]] > final[alive[1]] else alive[1]


def prefers(r, a, b):
    return r.index(a) < r.index(b)


def permute_profile(c, sigma):
    out=[0]*6
    for i,r in enumerate(RANKINGS):
        rr=tuple(sigma[a] for a in r)
        out[RINDEX[rr]]=c[i]
    return tuple(out)


def canonical(c):
    return min(permute_profile(c,s) for s in permutations((0,1,2)))


def normalize_event(p, ridx, k, full, post):
    """Relabel candidates so abstainer order becomes A>B>C."""
    r=RANKINGS[ridx]
    sigma=[None]*3
    sigma[r[0]]=0; sigma[r[1]]=1; sigma[r[2]]=2
    pp=permute_profile(p, tuple(sigma))
    return pp, 0, k, sigma[full], sigma[post]


def events_profile_first(n):
    events=[]
    bad_profiles=set()
    unique_full=0
    for p in compositions(n):
        w=irv_unique(p)
        if w is None:
            continue
        unique_full += 1
        pevents=[]
        for i,r in enumerate(RANKINGS):
            for k in range(1,p[i]+1):
                q=list(p); q[i]-=k; q=tuple(q)
                if sum(q)==0: continue
                wp=irv_unique(q)
                if wp is None or wp==w:
                    continue
                if prefers(r, wp, w):
                    e=(p,i,k,w,wp,q)
                    events.append(e); pevents.append(e)
        if pevents:
            bad_profiles.add(p)
    return events,bad_profiles,unique_full

# Route A, profile-first, proves minimality through n=11.
counts={}
for n in range(1,12):
    e,b,u = events_profile_first(n)
    counts[n]=(len(b),len(e),u)
    if n<11:
        assert len(b)==len(e)==0

events,bad,unique_full=events_profile_first(11)
assert len(bad)==60
assert len(events)==60
assert unique_full==4080
assert math.comb(16,5)==4368
assert Fraction(60,4368)==Fraction(5,364)
assert Fraction(60,4080)==Fraction(1,68)
assert all(k==2 for _,_,k,_,_,_ in events)
assert Counter(p for p,_,_,_,_,_ in events)==Counter({p:1 for p in bad})

# Every event moves abstainers from their last-ranked full winner to second-ranked post winner.
position_hist=Counter()
for p,i,k,w,wp,q in events:
    r=RANKINGS[i]
    position_hist[(r.index(w),r.index(wp))]+=1
assert position_hist==Counter({(2,1):60})

# Route B: event-first at n=11. Enumerate post-election profiles, a ballot type, and group size; add them.
events_b=set()
for k in range(1,12):
    for q in compositions(11-k):
        wp=irv_unique(q)
        if wp is None:
            continue
        for i,r in enumerate(RANKINGS):
            p=list(q); p[i]+=k; p=tuple(p)
            w=irv_unique(p)
            if w is None or w==wp:
                continue
            if prefers(r,wp,w):
                events_b.add((p,i,k,w,wp,q))
assert set(events)==events_b

# Candidate-relabel quotient of bad profiles.
classes=Counter(canonical(p) for p in bad)
assert len(classes)==10
assert Counter(classes.values())==Counter({6:10})

# Normalize each event by abstainer order. Exact two-family classification.
normalized=set()
for p,i,k,w,wp,q in events:
    pp,ii,kk,ww,wpp=normalize_event(p,i,k,w,wp)
    assert ii==0 and kk==2 and ww==2 and wpp==1
    normalized.add(pp)
expected=set()
for t in range(5):
    expected.add((4,0,0,3,t,4-t))
    expected.add((4,0,1,2,t,4-t))
assert normalized==expected

# Validate each normal form directly.
for p in expected:
    assert sum(p)==11
    assert irv_unique(p)==2
    q=list(p); q[0]-=2; q=tuple(q)
    assert irv_unique(q)==1

class_type_hist=Counter(sum(x>0 for x in p) for p in normalized)
assert class_type_hist==Counter({4:5,5:3,3:2})
labeled_type_hist=Counter()
for p in bad:
    labeled_type_hist[sum(x>0 for x in p)] += 1
assert labeled_type_hist==Counter({4:30,5:18,3:12})

# Extra first-choice structural identity: all normalized profiles have (4,3,4).
for p in normalized:
    first=[0,0,0]
    for r,x in zip(RANKINGS,p): first[r[0]] += x
    assert tuple(first)==(4,3,4)

# Digest exact normalized and bad sets.
bad_digest=hashlib.sha256("\n".join(map(str,sorted(bad))).encode()).hexdigest()
norm_digest=hashlib.sha256("\n".join(map(str,sorted(normalized))).encode()).hexdigest()

print("VERIFY_OK")
print("minimality_counts", counts)
print("n11_all_anonymous_profiles", 4368)
print("n11_unique_full_winner_profiles", unique_full)
print("n11_bad_profiles", len(bad))
print("n11_harmful_events", len(events))
print("all_event_group_sizes", dict(Counter(k for _,_,k,_,_,_ in events)))
print("winner_position_shift", dict(position_hist))
print("unconditional_incidence", "5/364")
print("conditional_unique_full_incidence", "1/68")
print("candidate_relabel_classes", len(classes))
print("orbit_size_hist", dict(Counter(classes.values())))
print("normalized_families", sorted(normalized))
print("class_ballot_type_hist", dict(sorted(class_type_hist.items())))
print("labeled_ballot_type_hist", dict(sorted(labeled_type_hist.items())))
print("bad_set_sha256", bad_digest)
print("normalized_set_sha256", norm_digest)
