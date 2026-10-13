#!/usr/bin/env python3
from itertools import combinations, combinations_with_replacement, permutations, product
from collections import Counter, defaultdict
import hashlib, json

N=4
WORDS=tuple(range(1<<N))

def bits(x): return tuple((x>>i)&1 for i in range(N))
B={x:bits(x) for x in WORDS}

def sumkey_triple(a,b,c):
    return tuple(B[a][i]+B[b][i]+B[c][i] for i in range(N))

def is_b3_v1(C):
    seen=set()
    for a,b,c in combinations_with_replacement(C,3):
        k=sumkey_triple(a,b,c)
        if k in seen: return False
        seen.add(k)
    return True

def is_b3_v2(C):
    # independent encoding: coordinate sums as base-4 digits; loop multiplicities i<=j<=k manually.
    seen=bytearray(4**N)
    L=list(C); m=len(L)
    for i in range(m):
        ai=B[L[i]]
        for j in range(i,m):
            bj=B[L[j]]
            for k in range(j,m):
                ck=B[L[k]]
                z=0; p=1
                for r in range(N):
                    z += (ai[r]+bj[r]+ck[r])*p
                    p *= 4
                if seen[z]: return False
                seen[z]=1
    return True

maxima=[]
for C in combinations(WORDS,6):
    a=is_b3_v1(C); b=is_b3_v2(C)
    assert a==b
    if a: maxima.append(C)
# hereditary upper-bound certificate: every 7-set fails both implementations
assert all(not is_b3_v1(C) and not is_b3_v2(C) for C in combinations(WORDS,7))
assert maxima and len(maxima)==656
M=set(maxima)

PERMS=tuple(permutations(range(N)))
def transform_word(x,perm,mask):
    out=0
    for i in range(N):
        bit=((x>>perm[i])&1)^((mask>>i)&1)
        out |= bit<<i
    return out

def transform_code(C,perm,mask):
    return tuple(sorted(transform_word(x,perm,mask) for x in C))

def orbit(C):
    return {transform_code(C,p,m) for p in PERMS for m in WORDS}

unseen=set(maxima); orbits=[]
while unseen:
    C=min(unseen); O=orbit(C)&M
    assert len(O)==len(orbit(C))
    orbits.append((C,O)); unseen-=O
assert sum(len(O) for _,O in orbits)==656
assert sorted(len(O) for _,O in orbits)==[16,64,96,96,192,192]

def dist(a,b): return (a^b).bit_count()
def dist_profile(C):
    c=Counter(dist(a,b) for a,b in combinations(C,2))
    return [c[d] for d in range(1,N+1)]
def weights(C): return sorted(x.bit_count() for x in C)

rows=[]
for C,O in sorted(orbits,key=lambda z:(len(z[1]),z[0])):
    rows.append({
        'representative_ints':list(C),
        'representative_bits':[''.join(map(str,reversed(B[x]))) for x in C],
        'orbit_size':len(O),
        'stabilizer_order':384//len(O),
        'distance_distribution_d1_to_d4':dist_profile(C),
        'weight_multiset':weights(C),
    })

# check invariants and B3 for every maximum
assert all(is_b3_v2(C) for C in maxima)
# canonical orbit IDs via minimum transform to prove exact partition independently
canon_counts=Counter(min(orbit(C)) for C in maxima)
assert sorted(canon_counts.values())==[16,64,96,96,192,192]

census={
  'schema_version':1,
  'object':'binary B_3 codes in {0,1}^4 under coordinatewise integer addition',
  'maximum_size':6,
  'number_labeled_maxima':len(maxima),
  'number_hamming_isometry_orbits':len(orbits),
  'group_order':384,
  'orbit_size_multiset':sorted(len(O) for _,O in orbits),
  'orbits':rows,
  'checked_6_subsets':8008,
  'checked_7_subsets':11440,
  'triple_multisets_per_maximum':56,
}
raw=json.dumps(census,sort_keys=True,separators=(',',':')).encode()
print(json.dumps(census,indent=2,sort_keys=True))
print('CENSUS_SHA256',hashlib.sha256(raw).hexdigest())
print('VERIFY_OK maximum=6 labeled_maxima=656 orbits=6 orbit_sizes=16,64,96,96,192,192')
