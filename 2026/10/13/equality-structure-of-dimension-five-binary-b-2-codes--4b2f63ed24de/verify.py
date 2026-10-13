#!/usr/bin/env python3
import itertools, json, hashlib, sys
from pathlib import Path

N=5
WORDS=list(range(1<<N))

def bits(x):
    return tuple((x>>i)&1 for i in range(N))

def sum_code(x,y):
    # base-3 encoding of coordinatewise ordinary sum, coordinates 0..N-1
    z=0; p=1
    for i in range(N):
        z += (((x>>i)&1)+((y>>i)&1))*p
        p*=3
    return z

def is_b2(code):
    seen=set()
    c=sorted(code)
    for j,y in enumerate(c):
        for x in c[:j+1]:
            s=sum_code(x,y)
            if s in seen:
                return False
            seen.add(s)
    return True

PAIR=[[sum_code(i,j) for j in WORDS] for i in WORDS]

# Exact normalized search: all B2 subsets containing 0, candidates increasing.
best=0
maxnorm=[]

def rec(chosen, start, seen):
    global best, maxnorm
    # Upper bound from remaining candidates.
    if len(chosen)+(32-start) < best:
        return
    if len(chosen)>best:
        best=len(chosen); maxnorm=[tuple(chosen)]
    elif len(chosen)==best:
        maxnorm.append(tuple(chosen))
    for w in range(start,32):
        # Sums w+v with v in chosen plus w+w must be pairwise new.
        ns=[]; local=set(); ok=True
        for v in chosen:
            s=PAIR[w][v]
            if s in seen or s in local:
                ok=False; break
            local.add(s); ns.append(s)
        if not ok: continue
        s=PAIR[w][w]
        if s in seen or s in local:
            continue
        ns.append(s)
        rec(chosen+[w], w+1, seen.union(ns))

rec([0],1,{PAIR[0][0]})
maxnorm=sorted(set(maxnorm))

# Complete labeled maxima obtained from normalized maxima by xor translations.
allmax=set()
for c in maxnorm:
    for a in WORDS:
        allmax.add(tuple(sorted(x^a for x in c)))
allmax=sorted(allmax)

# Full Hamming-isometry group: xor translations and coordinate permutations.
perms=list(itertools.permutations(range(N)))
def permute_word(x,p):
    y=0
    for i in range(N):
        if (x>>i)&1:
            y |= 1<<p[i]
    return y

def image_code(c,a,p):
    return tuple(sorted(permute_word(x^a,p) for x in c))

rep=allmax[0]
orbit={image_code(rep,a,p) for a in WORDS for p in perms}

# Invariants on representative.
coord_ones=[sum((x>>i)&1 for x in rep) for i in range(N)]
antipodal=sum(1 for x in rep if (x^31) in rep)//2
dist=[0]*(N+1)
for i,x in enumerate(rep):
    for y in rep[i+1:]:
        dist[(x^y).bit_count()]+=1

# Stabilizer count directly.
stab=sum(1 for a in WORDS for p in perms if image_code(rep,a,p)==rep)

payload={
    "schema_version":1,
    "dimension":5,
    "definition":"All coordinatewise ordinary sums x+y for unordered pairs with repetition are distinct.",
    "maximum_size":best,
    "normalized_maxima_containing_zero":len(maxnorm),
    "labeled_maxima":len(allmax),
    "isometry_group_order":32*120,
    "isometry_orbit_count":1 if orbit==set(allmax) else None,
    "orbit_size":len(orbit),
    "stabilizer_order":stab,
    "representative":[format(x,"05b") for x in rep],
    "coordinate_one_counts":coord_ones,
    "antipodal_pairs":antipodal,
    "pair_distance_distribution":{"1":dist[1],"2":dist[2],"3":dist[3],"4":dist[4],"5":dist[5]},
    "maxima":[[format(x,"05b") for x in c] for c in allmax],
}
canon=json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
payload_hash=hashlib.sha256(canon).hexdigest()

assert best==12
assert len(maxnorm)==72
assert len(allmax)==192
assert all(is_b2(c) and len(c)==12 for c in allmax)
assert orbit==set(allmax)
assert len(orbit)==192
assert stab==20
assert coord_ones==[6,6,6,6,6]
assert antipodal==1
assert dist[1:]==[5,20,30,10,1]
assert sum(dist)==66

census_path=Path(__file__).with_name("census.json")
if census_path.exists():
    stored=json.loads(census_path.read_text(encoding="utf-8"))
    stored_maxima=stored.get("maxima")
    assert stored_maxima==payload["maxima"]
    for key in ["maximum_size","normalized_maxima_containing_zero","labeled_maxima","isometry_group_order","orbit_size","stabilizer_order","coordinate_one_counts","antipodal_pairs","pair_distance_distribution"]:
        assert stored.get(key)==payload.get(key), (key, stored.get(key), payload.get(key))

print("VERIFY_OK maximum=12 normalized=72 labeled_maxima=192 isometry_orbits=1 orbit_size=192 stabilizer=20 balanced=6,6,6,6,6 antipodal_pairs=1 distances=5,20,30,10,1 census_sha256="+payload_hash)
