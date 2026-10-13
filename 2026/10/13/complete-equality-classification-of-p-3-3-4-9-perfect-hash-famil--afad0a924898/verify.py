#!/usr/bin/env python3
import hashlib
import itertools
from collections import Counter

Q=4
N=3
WORDS=list(itertools.product(range(Q), repeat=N))
INDEX={w:i for i,w in enumerate(WORDS)}
V=len(WORDS)
ZERO=INDEX[(0,0,0)]


def separates3(a,b,c):
    return any(len({a[j],b[j],c[j]})==3 for j in range(N))

# Direct forbidden-triple table and future masks for strictly increasing searches.
bad_future=[[0]*V for _ in range(V)]
bad_triples=0
for i,j,k in itertools.combinations(range(V),3):
    if not separates3(WORDS[i],WORDS[j],WORDS[k]):
        bad_future[i][j] |= 1<<k
        bad_triples += 1


def enumerate_with_zero(target, stop_after_one=False):
    out=[]
    # chosen is strictly increasing and always starts with ZERO=0.
    def rec(chosen, cand_mask):
        need=target-len(chosen)
        if need==0:
            out.append(tuple(chosen))
            return stop_after_one
        if cand_mask.bit_count() < need:
            return False
        # Simple but exhaustive lexicographic branching.
        m=cand_mask
        while m:
            lsb=m & -m
            v=lsb.bit_length()-1
            m ^= lsb
            # Remaining candidates must exceed v; m already has only later bits.
            newmask=m
            for u in chosen:
                newmask &= ~bad_future[u][v]
            if rec(chosen+[v], newmask):
                return True
            # Excluding v is handled by continuing with m.
            if m.bit_count() < need:
                break
        return False
    initial=((1<<V)-1) & ~((1<<(ZERO+1))-1)
    rec([ZERO], initial)
    return out


def valid_code(code):
    return all(separates3(WORDS[i],WORDS[j],WORDS[k])
               for i,j,k in itertools.combinations(code,3))

# Exclude size 10 after normalization; enumerate every size-9 normalized maximum.
ten=enumerate_with_zero(10, stop_after_one=True)
assert not ten
normalized=enumerate_with_zero(9, stop_after_one=False)
assert len(normalized)==648
assert len(set(normalized))==648
assert all(valid_code(c) for c in normalized)


def translate_word(w,t):
    return tuple((w[j]+t[j])%Q for j in range(N))

def translate_code(code,t):
    return tuple(sorted(INDEX[translate_word(WORDS[i],t)] for i in code))

translations=list(itertools.product(range(Q), repeat=N))
all_codes=set()
for c in normalized:
    for t in translations:
        all_codes.add(translate_code(c,t))
assert len(all_codes)==4608
assert all(valid_code(c) for c in all_codes)

# Incidence check: the translation group is transitive on ambient words.
assert len(all_codes)*9 == len(normalized)*64

# Natural equivalence group: coordinate permutations and independent alphabet permutations.
coord_perms=list(itertools.permutations(range(N)))
sym_perms=list(itertools.permutations(range(Q)))
rep=min(all_codes)

def transform_word(w,cp,sps):
    # First reorder coordinates, then relabel symbols independently in output coordinates.
    return tuple(sps[j][w[cp[j]]] for j in range(N))

def transform_code(code,cp,sps):
    return tuple(sorted(INDEX[transform_word(WORDS[i],cp,sps)] for i in code))

orbit=set()
for cp in coord_perms:
    for s0 in sym_perms:
        for s1 in sym_perms:
            for s2 in sym_perms:
                orbit.add(transform_code(rep,cp,(s0,s1,s2)))
assert orbit==all_codes
GROUP=6*(24**3)
assert GROUP==82944
assert GROUP//len(orbit)==18

# Structural profiles, checked directly for every maximum.
def coord_profile(code):
    profiles=[]
    for j in range(N):
        cnt=Counter(WORDS[i][j] for i in code)
        profiles.append(tuple(sorted(cnt.values(), reverse=True)))
    return tuple(profiles)

def hamming(a,b):
    return sum(x!=y for x,y in zip(a,b))

def distance_profile(code):
    cnt=Counter(hamming(WORDS[i],WORDS[j]) for i,j in itertools.combinations(code,2))
    return tuple(sorted(cnt.items()))

profiles={coord_profile(c) for c in all_codes}
dprofiles={distance_profile(c) for c in all_codes}
assert profiles=={((3,2,2,2),(3,2,2,2),(3,2,2,2))}
assert dprofiles=={((2,18),(3,18))}

# Canonical digests for exact replay.
def digest_codes(codes):
    lines=[]
    for c in sorted(codes):
        lines.append(' '.join(''.join(map(str,WORDS[i])) for i in c))
    data=('\n'.join(lines)+'\n').encode('ascii')
    return hashlib.sha256(data).hexdigest()

nsha=digest_codes(normalized)
asha=digest_codes(all_codes)
rep_words=','.join(''.join(map(str,WORDS[i])) for i in rep)
print(
    'VERIFY_OK '
    f'vertices={V} bad_triples={bad_triples} maximum=9 '
    f'normalized_maxima={len(normalized)} labeled_maxima={len(all_codes)} '
    f'natural_group={GROUP} orbits=1 orbit_size={len(orbit)} stabilizer=18 '
    'coordinate_profile=3,2,2,2x3 hamming_profile=2x18,3x18 '
    f'representative={rep_words} '
    f'normalized_sha256={nsha} labeled_sha256={asha}'
)
