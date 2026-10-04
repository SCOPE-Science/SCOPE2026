#!/usr/bin/env python3
from itertools import permutations
from collections import Counter, defaultdict
import math, hashlib

RANKINGS = list(permutations((0,1,2)))

def compositions(total, k=6):
    if k == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for tail in compositions(total - x, k - 1):
            yield (x,) + tail

def irv_unique(counts):
    """Three-candidate IRV winner, requiring unique elimination and final winner."""
    first = [0,0,0]
    for r,c in zip(RANKINGS, counts):
        first[r[0]] += c
    n = sum(counts)
    if n == 0:
        return None
    # A strict majority wins immediately.
    for a in range(3):
        if 2 * first[a] > n:
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

def permute_counts(counts, sigma):
    out = [0]*6
    index = {r:i for i,r in enumerate(RANKINGS)}
    for i,r in enumerate(RANKINGS):
        rr = tuple(sigma[a] for a in r)
        out[index[rr]] = counts[i]
    return tuple(out)

def canon_pair(p,q):
    best = None
    for s in permutations((0,1,2)):
        pp = permute_counts(p,s)
        qq = permute_counts(q,s)
        key = tuple(sorted((pp,qq)))
        if best is None or key < best:
            best = key
    return best

def canon_union(u):
    return min(permute_counts(u,s) for s in permutations((0,1,2)))

# Route A: enumerate profile pairs by electorate-size split.
profiles = {}
for n in range(1,14):
    buckets = defaultdict(list)
    for p in compositions(n):
        w = irv_unique(p)
        if w is not None:
            buckets[w].append(p)
    profiles[n] = buckets

counts_by_total = {}
pairs13 = []
for total in range(2,14):
    count = 0
    for n1 in range(1, total):
        n2 = total - n1
        if n1 > n2:
            continue
        for w in range(3):
            for p in profiles[n1][w]:
                for q in profiles[n2][w]:
                    if n1 == n2 and p > q:
                        continue
                    u = tuple(a+b for a,b in zip(p,q))
                    wu = irv_unique(u)
                    if wu is not None and wu != w:
                        count += 1
                        if total == 13:
                            pairs13.append((p,q,w,wu,u))
    counts_by_total[total] = count

assert all(counts_by_total[t] == 0 for t in range(2,13))
assert counts_by_total[13] == 288
assert len(pairs13) == 288
assert {tuple(sorted((sum(p),sum(q)))) for p,q,_,_,_ in pairs13} == {(5,8)}

pair_classes = Counter(canon_pair(p,q) for p,q,_,_,_ in pairs13)
assert len(pair_classes) == 48
assert Counter(pair_classes.values()) == Counter({6:48})

union_mult = Counter(u for _,_,_,_,u in pairs13)
assert len(union_mult) == 126
assert Counter(union_mult.values()) == Counter({1:36,2:36,3:36,4:18})
union_classes = Counter(canon_union(u) for u in union_mult)
assert len(union_classes) == 21
assert Counter(union_classes.values()) == Counter({6:21})

transition_hist = Counter((w,wu) for _,_,w,wu,_ in pairs13)
assert len(transition_hist) == 6
assert set(transition_hist.values()) == {48}

# Route B: independently enumerate each 13-voter union and all componentwise splits.
route_b_pairs = set()
route_b_union_mult = Counter()

def subprofiles_of_union(u):
    cur = [0]*6
    def rec(i):
        if i == 6:
            yield tuple(cur)
            return
        for x in range(u[i]+1):
            cur[i] = x
            yield from rec(i+1)
    yield from rec(0)

for u in compositions(13):
    wu = irv_unique(u)
    if wu is None:
        continue
    local = 0
    for p in subprofiles_of_union(u):
        np = sum(p)
        if np == 0 or np >= 13:
            continue
        q = tuple(u[i]-p[i] for i in range(6))
        nq = 13 - np
        # total is odd, so one side is strictly smaller; count unordered pair once.
        if np > nq:
            continue
        wp = irv_unique(p)
        if wp is None or wp == wu:
            continue
        wq = irv_unique(q)
        if wq is None or wq != wp:
            continue
        key = (p,q) if p <= q else (q,p)
        route_b_pairs.add(key)
        local += 1
    if local:
        route_b_union_mult[u] = local

assert len(route_b_pairs) == 288
route_a_set = {((p,q) if p <= q else (q,p)) for p,q,_,_,_ in pairs13}
assert route_b_pairs == route_a_set
assert route_b_union_mult == union_mult

# Concrete canonical witness.
P = (0,0,0,2,0,3)
Q = (3,0,0,2,0,3)
U = tuple(P[i]+Q[i] for i in range(6))
assert sum(P) == 5 and sum(Q) == 8 and sum(U) == 13
assert irv_unique(P) == 2
assert irv_unique(Q) == 2
assert irv_unique(U) == 1

digest = hashlib.sha256(
    "\n".join(
        f"{p}|{q}" for p,q in sorted(route_b_pairs)
    ).encode("ascii")
).hexdigest()

print("VERIFY_OK")
print("counts_total_2_to_13", {t:counts_by_total[t] for t in range(2,14)})
print("minimal_total", 13)
print("minimal_unordered_pairs", 288)
print("size_split", "5+8")
print("candidate_relabel_pair_classes", 48)
print("pair_orbit_hist", dict(sorted(Counter(pair_classes.values()).items())))
print("distinct_union_profiles", 126)
print("union_partition_multiplicity_hist", dict(sorted(Counter(union_mult.values()).items())))
print("candidate_relabel_union_classes", 21)
print("winner_transition_hist", dict(sorted(transition_hist.items())))
print("canonical_witness_P", P)
print("canonical_witness_Q", Q)
print("canonical_witness_union", U)
print("pair_set_sha256", digest)
