#!/usr/bin/env python3
from itertools import permutations
from collections import defaultdict, Counter
import hashlib

RANKINGS = list(permutations((0,1,2)))
INDEX = {r:i for i,r in enumerate(RANKINGS)}

# Pairwise margin coordinates (0>1, 0>2, 1>2).
CONTRIB = []
for r in RANKINGS:
    pos = {a:i for i,a in enumerate(r)}
    CONTRIB.append((
        1 if pos[0] < pos[1] else -1,
        1 if pos[0] < pos[2] else -1,
        1 if pos[1] < pos[2] else -1,
    ))

def compositions(total, k=6):
    if k == 1:
        yield (total,)
        return
    for x in range(total+1):
        for tail in compositions(total-x, k-1):
            yield (x,) + tail

def margins(profile):
    m01=m02=m12=0
    for c,v in zip(profile, CONTRIB):
        m01 += c*v[0]
        m02 += c*v[1]
        m12 += c*v[2]
    return (m01,m02,m12)

def winner_from_margins(m):
    m01,m02,m12 = m
    scores = (
        min(m01,m02),
        min(-m01,m12),
        min(-m02,-m12),
    )
    best = max(scores)
    ws = [a for a,s in enumerate(scores) if s == best]
    return ws[0] if len(ws)==1 else None

def maximin(profile):
    return winner_from_margins(margins(profile))

def permute_profile(profile, sigma):
    out = [0]*6
    for i,r in enumerate(RANKINGS):
        rr = tuple(sigma[a] for a in r)
        out[INDEX[rr]] = profile[i]
    return tuple(out)

def canonical_pair(p,q):
    best = None
    for sigma in permutations((0,1,2)):
        pp = permute_profile(p,sigma)
        qq = permute_profile(q,sigma)
        key = tuple(sorted((pp,qq)))
        if best is None or key < best:
            best = key
    return best

def canonical_union(u):
    return min(permute_profile(u,s) for s in permutations((0,1,2)))

# Precompute profiles by size, unique maximin winner, and margins.
by_size = {}
winner_cache = {}
for n in range(1,16):
    buckets = defaultdict(list)
    for p in compositions(n):
        m = margins(p)
        w = winner_from_margins(m)
        winner_cache[p] = w
        if w is not None:
            buckets[w].append((p,m))
    by_size[n] = buckets

# Route A: pair-first exhaustive census for every total through 15.
counts_by_total = {}
pairs15 = []
for total in range(2,16):
    found = []
    for n1 in range(1,total):
        n2 = total-n1
        if n1 > n2:
            continue
        for w in range(3):
            A = by_size[n1][w]
            B = by_size[n2][w]
            for p,mp in A:
                for q,mq in B:
                    if n1 == n2 and p > q:
                        continue
                    mu = tuple(mp[i]+mq[i] for i in range(3))
                    wu = winner_from_margins(mu)
                    if wu is not None and wu != w:
                        key = (p,q) if p <= q else (q,p)
                        found.append((key[0],key[1],w,wu,tuple(a+b for a,b in zip(p,q))))
    counts_by_total[total] = len(found)
    if total == 15:
        pairs15 = found

assert all(counts_by_total[t] == 0 for t in range(2,15))
assert counts_by_total[15] == 18
assert len(pairs15) == 18
assert Counter(tuple(sorted((sum(p),sum(q)))) for p,q,_,_,_ in pairs15) == Counter({(5,10):18})

pair_classes = Counter(canonical_pair(p,q) for p,q,_,_,_ in pairs15)
assert len(pair_classes) == 3
assert Counter(pair_classes.values()) == Counter({6:3})

transition_hist = Counter((w,wu) for _,_,w,wu,_ in pairs15)
assert len(transition_hist) == 6 and set(transition_hist.values()) == {3}

# Distinct unions and their multiplicity among paradox-producing partitions.
union_mult = Counter(u for _,_,_,_,u in pairs15)
union_classes = Counter(canonical_union(u) for u in union_mult)

# Route B: union-first enumeration of every 15-voter union and every componentwise split.
def subprofiles(u):
    cur = [0]*6
    def rec(i):
        if i == 6:
            yield tuple(cur)
            return
        for x in range(u[i]+1):
            cur[i] = x
            yield from rec(i+1)
    yield from rec(0)

route_b_pairs = set()
route_b_unions = Counter()
for u in compositions(15):
    wu = winner_cache.get(u)
    if wu is None:
        wu = maximin(u)
        winner_cache[u] = wu
    if wu is None:
        continue
    local = 0
    for p in subprofiles(u):
        np = sum(p)
        if np == 0 or np == 15:
            continue
        q = tuple(u[i]-p[i] for i in range(6))
        nq = 15-np
        if np > nq:
            continue
        wp = winner_cache.get(p)
        if p not in winner_cache:
            wp = maximin(p); winner_cache[p]=wp
        if wp is None or wp == wu:
            continue
        wq = winner_cache.get(q)
        if q not in winner_cache:
            wq = maximin(q); winner_cache[q]=wq
        if wq is None or wq != wp:
            continue
        key=(p,q) if p<=q else (q,p)
        route_b_pairs.add(key)
        local += 1
    if local:
        route_b_unions[u]=local

route_a_pairs = {(p,q) for p,q,_,_,_ in pairs15}
assert route_b_pairs == route_a_pairs
assert route_b_unions == union_mult

# Structural refinements discovered from the exact set.
assert len(union_mult) == 18
assert set(union_mult.values()) == {1}
assert len(union_classes) == 3
assert Counter(union_classes.values()) == Counter({6:3})

# At the minimal boundary the five-voter side has the shared winner as Condorcet winner,
# the ten-voter side is cyclic, and the union has the new winner as Condorcet winner.
def condorcet(profile):
    m01,m02,m12 = margins(profile)
    wins=[]
    if m01>0 and m02>0: wins.append(0)
    if m01<0 and m12>0: wins.append(1)
    if m02<0 and m12<0: wins.append(2)
    return wins[0] if len(wins)==1 else None

branch_hist = Counter()
for p,q,w,wu,u in pairs15:
    small,big = (p,q) if sum(p) < sum(q) else (q,p)
    cs,cb,cu = condorcet(small),condorcet(big),condorcet(u)
    branch_hist[(cs==w, cb is None, cu==wu)] += 1
assert branch_hist == Counter({(True,True,True):18})

canon_list = sorted(pair_classes)
digest = hashlib.sha256("\n".join(f"{p}|{q}" for p,q in sorted(route_b_pairs)).encode("ascii")).hexdigest()

print("VERIFY_OK")
print("counts_total_2_to_15", counts_by_total)
print("minimal_total", 15)
print("minimal_unordered_pairs", 18)
print("size_split", "5+10")
print("candidate_relabel_pair_classes", len(pair_classes))
print("pair_orbit_hist", dict(sorted(Counter(pair_classes.values()).items())))
print("distinct_union_profiles", len(union_mult))
print("union_partition_multiplicity_hist", dict(sorted(Counter(union_mult.values()).items())))
print("candidate_relabel_union_classes", len(union_classes))
print("winner_transition_hist", dict(sorted(transition_hist.items())))
print("five_side_shared_winner_condorcet_ten_side_cyclic_union_new_winner_condorcet", True)
print("canonical_pairs", canon_list)
print("pair_set_sha256", digest)
