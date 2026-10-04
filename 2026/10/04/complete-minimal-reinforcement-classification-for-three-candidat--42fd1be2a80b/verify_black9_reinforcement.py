#!/usr/bin/env python3
from itertools import permutations
from collections import defaultdict, Counter
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

def black_winner(profile):
    """Unique winner under Black's rule; None if Borda fallback is tied."""
    n = sum(profile)
    pair = [[0]*3 for _ in range(3)]
    borda = [0]*3
    for ranking,count in zip(RANKINGS, profile):
        pos = {a:i for i,a in enumerate(ranking)}
        borda[ranking[0]] += 2*count
        borda[ranking[1]] += count
        for a in range(3):
            for b in range(a+1,3):
                if pos[a] < pos[b]:
                    pair[a][b] += count
                else:
                    pair[b][a] += count
    cw = [a for a in range(3)
          if all(a == b or pair[a][b] > pair[b][a] for b in range(3))]
    if len(cw) == 1:
        return cw[0]
    top = max(borda)
    winners = [a for a,s in enumerate(borda) if s == top]
    return winners[0] if len(winners) == 1 else None

def black_detail(profile):
    n = sum(profile)
    pair = [[0]*3 for _ in range(3)]
    borda = [0]*3
    for ranking,count in zip(RANKINGS, profile):
        pos = {a:i for i,a in enumerate(ranking)}
        borda[ranking[0]] += 2*count
        borda[ranking[1]] += count
        for a in range(3):
            for b in range(a+1,3):
                if pos[a] < pos[b]:
                    pair[a][b] += count
                else:
                    pair[b][a] += count
    cw = [a for a in range(3)
          if all(a == b or pair[a][b] > pair[b][a] for b in range(3))]
    if len(cw) == 1:
        return cw[0], "Condorcet"
    top = max(borda)
    winners = [a for a,s in enumerate(borda) if s == top]
    if len(winners) == 1:
        return winners[0], "Borda"
    return None, "tie"

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

# Route A: pair-first, all total sizes through 9.
by_size = {}
for n in range(1,10):
    buckets = defaultdict(list)
    for p in compositions(n):
        w = black_winner(p)
        if w is not None:
            buckets[w].append(p)
    by_size[n] = buckets

counts = {}
pairs9 = []
for total in range(2,10):
    found = []
    for n1 in range(1,total):
        n2 = total-n1
        if n1 > n2:
            continue
        for w in range(3):
            for p in by_size[n1][w]:
                for q in by_size[n2][w]:
                    if n1 == n2 and p > q:
                        continue
                    u = tuple(a+b for a,b in zip(p,q))
                    wu = black_winner(u)
                    if wu is not None and wu != w:
                        key = (p,q) if p <= q else (q,p)
                        found.append((key[0],key[1],w,wu,u))
    counts[total] = len(found)
    if total == 9:
        pairs9 = found

assert all(counts[t] == 0 for t in range(2,9))
assert counts[9] == 12
assert len(pairs9) == 12
assert Counter(tuple(sorted((sum(p),sum(q)))) for p,q,_,_,_ in pairs9) == Counter({(1,8):6,(4,5):6})

classes = Counter(canonical_pair(p,q) for p,q,_,_,_ in pairs9)
assert len(classes) == 2
assert Counter(classes.values()) == Counter({6:2})
expected_classes = {
    ((0,0,0,0,0,1),(1,0,0,4,3,0)),
    ((0,0,0,2,1,1),(1,0,0,2,2,0)),
}
assert set(classes) == expected_classes

branch_hist = Counter()
transition_hist = Counter()
for p,q,w,wu,u in pairs9:
    wp,bp = black_detail(p)
    wq,bq = black_detail(q)
    ux,bu = black_detail(u)
    assert wp == wq == w and ux == wu
    branch_hist[(tuple(sorted((bp,bq))),bu)] += 1
    transition_hist[(w,wu)] += 1

# Because p,q are stored by lexicographic code, branch order can swap only for same-size;
# here both size splits are unequal, so it is stable.
assert branch_hist == Counter({
    (("Borda","Condorcet"),"Condorcet"):6,
    (("Borda","Borda"),"Condorcet"):6,
})
assert len(transition_hist) == 6 and set(transition_hist.values()) == {2}

# Every minimal pair is a partition of one candidate-relabeling orbit of union profiles.
unions = Counter(u for _,_,_,_,u in pairs9)
assert len(unions) == 6
assert set(unions.values()) == {2}
union_classes = Counter()
for u,mult in unions.items():
    cu = min(permute_profile(u,sigma) for sigma in permutations((0,1,2)))
    union_classes[cu] += mult
assert len(union_classes) == 1
assert next(iter(union_classes.keys())) == (0,1,3,1,0,4)
assert next(iter(union_classes.values())) == 12

# Route B: union-first over all 9-voter profiles and every componentwise split.
route_b = set()
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

for u in compositions(9):
    wu = black_winner(u)
    if wu is None:
        continue
    for p in subprofiles(u):
        np = sum(p)
        if np == 0 or np == 9:
            continue
        q = tuple(u[i]-p[i] for i in range(6))
        nq = 9-np
        if np > nq:
            continue
        wp = black_winner(p)
        if wp is None or wp == wu:
            continue
        wq = black_winner(q)
        if wq is None or wq != wp:
            continue
        key = (p,q) if p <= q else (q,p)
        route_b.add(key)

route_a = {(p,q) for p,q,_,_,_ in pairs9}
assert route_b == route_a
assert len(route_b) == 12

# Exact witness checks for the two canonical classes.
for key in expected_classes:
    p,q = key
    assert black_winner(p) == 2
    assert black_winner(q) == 2
    assert black_winner(tuple(a+b for a,b in zip(p,q))) == 1

digest = hashlib.sha256(
    "\n".join(f"{p}|{q}" for p,q in sorted(route_b)).encode("ascii")
).hexdigest()

print("VERIFY_OK")
print("counts_total_2_to_9", counts)
print("minimal_total", 9)
print("minimal_unordered_pairs", 12)
print("size_split_hist", {(1,8):6,(4,5):6})
print("candidate_relabel_classes", 2)
print("orbit_size_hist", dict(Counter(classes.values())))
print("branch_hist", dict(branch_hist))
print("winner_transition_hist", dict(sorted(transition_hist.items())))
print("distinct_union_profiles", len(unions))
print("partitions_per_union", dict(Counter(unions.values())))
print("candidate_relabel_union_classes", len(union_classes))
print("canonical_union", next(iter(union_classes.keys())))
print("canonical_classes", sorted(expected_classes))
print("pair_set_sha256", digest)
