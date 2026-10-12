#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter, defaultdict
from functools import lru_cache

WORDS=[''.join(p) for p in product('01', repeat=5)]
IDX={w:i for i,w in enumerate(WORDS)}

def edit_dp(a,b):
    prev=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        cur=[i]+[0]*len(b)
        for j,cb in enumerate(b,1):
            cur[j]=min(prev[j]+1,cur[j-1]+1,prev[j-1]+(ca!=cb))
        prev=cur
    return prev[-1]

@lru_cache(None)
def edit_rec(a,b):
    if not a: return len(b)
    if not b: return len(a)
    return min(edit_rec(a[1:],b)+1,
               edit_rec(a,b[1:])+1,
               edit_rec(a[1:],b[1:])+(a[0]!=b[0]))

def complement(w): return ''.join('1' if c=='0' else '0' for c in w)
def reverse(w): return w[::-1]
def xor_word(a,b): return format(int(a,2)^int(b,2),'05b')

# Pairwise metric agreement.
D={}
for a,b in combinations(WORDS,2):
    x=edit_dp(a,b); y=edit_rec(a,b)
    assert x==y
    D[a,b]=D[b,a]=x
for w in WORDS: D[w,w]=0

ADJ={w:set() for w in WORDS}
for a,b in combinations(WORDS,2):
    if D[a,b]>=3:
        ADJ[a].add(b); ADJ[b].add(a)

max4=[]
for C in combinations(WORDS,4):
    if all(b in ADJ[a] for a,b in combinations(C,2)):
        max4.append(tuple(C))
assert not any(all(b in ADJ[a] for a,b in combinations(C,2)) for C in combinations(WORDS,5))
assert len(max4)==28

# Every maximum is an affine 2-flat over F_2^5.
def affine_direction(C):
    a=C[0]
    H=tuple(sorted(xor_word(x,a) for x in C))
    S=set(H)
    assert '00000' in S and len(S)==4
    assert all(xor_word(x,y) in S for x in S for y in S)
    return H

dirs=defaultdict(list)
for C in max4:
    H=affine_direction(C)
    dirs[H].append(C)
assert len(dirs)==14
assert all(len(v)==2 for v in dirs.values())
for H,Cs in dirs.items():
    assert tuple(sorted(complement(x) for x in Cs[0]))==tuple(sorted(Cs[1])) or tuple(sorted(complement(x) for x in Cs[1]))==tuple(sorted(Cs[0]))

# Full automorphism group of the compatibility graph by exact backtracking.
def signature(w):
    return (len(ADJ[w]), tuple(sorted(Counter(len(ADJ[x]) for x in ADJ[w]).items())))
SIG={w:signature(w) for w in WORDS}
CANDS={w:[v for v in WORDS if SIG[v]==SIG[w]] for w in WORDS}
order=sorted(WORDS,key=lambda w:(len(CANDS[w]),-len(ADJ[w]),w))
autos=[]
mapping={}; used=set()
def bt(k):
    if k==len(order):
        autos.append(dict(mapping)); return
    u=order[k]
    for v in CANDS[u]:
        if v in used: continue
        ok=True
        for u2,v2 in mapping.items():
            if ((u2 in ADJ[u]) != (v2 in ADJ[v])):
                ok=False; break
        if not ok: continue
        mapping[u]=v; used.add(v); bt(k+1); used.remove(v); del mapping[u]
bt(0)
assert len(autos)==4
expected=[]
for mode in range(4):
    m={}
    for w in WORDS:
        z=w
        if mode&1: z=complement(z)
        if mode&2: z=reverse(z)
        m[w]=z
    expected.append(m)
assert {tuple(m[w] for w in WORDS) for m in autos}=={tuple(m[w] for w in WORDS) for m in expected}

# Orbits of maximum codes under the full graph automorphism group.
maxset=set(max4)
orbits=[]
seen=set()
for C in max4:
    if C in seen: continue
    orb=set()
    for m in autos:
        orb.add(tuple(sorted(m[x] for x in C)))
    seen|=orb; orbits.append(orb)
assert len(orbits)==8
assert sorted(len(o) for o in orbits)==[2,2,4,4,4,4,4,4]

# Direction subspaces: reversal gives two fixed directions and six exchanged pairs;
# complement translates the two admissible cosets for each direction.
def revH(H): return tuple(sorted(reverse(x) for x in H))
dirset=set(dirs)
dir_orbits=[]; seenD=set()
for H in sorted(dirset):
    if H in seenD: continue
    o={H,revH(H)}
    assert o<=dirset
    seenD|=o; dir_orbits.append(o)
assert len(dir_orbits)==8
assert sorted(len(o) for o in dir_orbits)==[1,1,2,2,2,2,2,2]

# Distance profile: every maximum has either one or two distance-four pairs.
profile=Counter(tuple(sorted(D[a,b] for a,b in combinations(C,2))) for C in max4)
assert profile==Counter({(3,3,3,3,3,4):18,(3,3,3,3,4,4):10})

print('VERIFY_OK vertices=32 edges=%d maximum=4 labeled_maxima=28 affine_maxima=28 directions=14 admissible_cosets_per_direction=2 automorphism_group=4 max_orbits=8 max_orbit_sizes=2,2,4x6 direction_orbits=8 direction_orbit_sizes=1,1,2x6 distance_profiles=18x(3^5,4),10x(3^4,4^2)' % (sum(len(v) for v in ADJ.values())//2))
