#!/usr/bin/env python3
from itertools import combinations, permutations, product
from collections import Counter
import hashlib, json
Q=(0,1,2)
WORDS=tuple(product(Q, repeat=3))
N=len(WORDS)

# descendant signature as coordinate masks in {1,...,7}
def sig_indices(idxs):
    m=[0,0,0]
    for i in idxs:
        w=WORDS[i]
        m[0]|=1<<w[0]; m[1]|=1<<w[1]; m[2]|=1<<w[2]
    return tuple(m)

def valid_code(C):
    seen={}
    L=list(C)
    for r in (1,2,3):
        for sub in combinations(L,r):
            s=sig_indices(sub)
            if s in seen and seen[s]!=sub:
                return False
            seen[s]=sub
    return True

# Exhaustive lexicographic DFS.  The state contains exactly all descendant
# signatures of subsets of chosen vertices of sizes 1,2,3.  When v is added,
# the only new subsets are {v}, {u,v}, {u,w,v}; thus the collision test is exact.
best=0
maxima=[]
nodes=0
rejections=0

def dfs(chosen, start, seen):
    global best,maxima,nodes,rejections
    nodes += 1
    k=len(chosen)
    if k + (N-start) < best:
        return
    if k>best:
        best=k; maxima=[tuple(chosen)]
    elif k==best and k>0:
        maxima.append(tuple(chosen))
    for v in range(start,N):
        if k + (N-v) < best:
            break
        newsubs=[(v,)]
        newsubs += [(u,v) for u in chosen]
        newsubs += [(u,w,v) for u,w in combinations(chosen,2)]
        local={}
        ok=True
        for sub in newsubs:
            s=sig_indices(sub)
            if s in seen or s in local:
                ok=False; break
            local[s]=sub
        if not ok:
            rejections+=1
            continue
        seen.update(local)
        chosen.append(v)
        dfs(chosen,v+1,seen)
        chosen.pop()
        for s in local: del seen[s]

dfs([],0,{})
# The running maxima list may contain codes recorded before a later larger best;
# reset logic removed them, but ensure distinct final tuples and exact size.
maxima=sorted(set(C for C in maxima if len(C)==best))
assert best==6, best
assert len(maxima)==135, len(maxima)
assert all(valid_code(C) for C in maxima)
# An independent exhaustive size-7 test uses recursive combinations with early validity.
# Every size-7 valid code would have a valid size-6 prefix and thus would extend one maximum.
# Check all one-vertex extensions of all 135 size-6 maxima, covering every possible size-7 code 7 times.
size7_extensions=0
for C in maxima:
    S=set(C)
    for v in range(N):
        if v not in S and valid_code(tuple(sorted((*C,v)))):
            size7_extensions += 1
assert size7_extensions==0

# Natural Hamming-isometry group: independent S3 symbol permutations in each
# coordinate, followed by coordinate permutation.
perms=list(permutations(Q))
coord_perms=list(permutations(range(3)))
word_to_i={w:i for i,w in enumerate(WORDS)}
transforms=[]
for cp in coord_perms:
    for p0 in perms:
      for p1 in perms:
       for p2 in perms:
        ps=(p0,p1,p2)
        mp=[]
        for w in WORDS:
            z=(ps[0][w[0]],ps[1][w[1]],ps[2][w[2]])
            z=tuple(z[cp[j]] for j in range(3))
            mp.append(word_to_i[z])
        transforms.append(tuple(mp))
assert len(transforms)==1296 and len(set(transforms))==1296
Mset=set(maxima)
assert all(tuple(sorted(T[i] for i in C)) in Mset for C in maxima for T in transforms)

unseen=set(maxima)
orbits=[]
while unseen:
    C=min(unseen)
    orb={tuple(sorted(T[i] for i in C)) for T in transforms}
    assert orb <= Mset
    orbits.append((C,orb))
    unseen-=orb
orbits.sort(key=lambda z:(len(z[1]),z[0]))
assert [len(o) for _,o in orbits]==[27,108]
stabs=[1296//len(o) for _,o in orbits]
assert stabs==[48,12]

# Coordinate symbol-multiplicity profiles and pair-projection multiplicities.
def profile(C):
    coord=[]
    pairs=[]
    for j in range(3):
        cnt=Counter(WORDS[i][j] for i in C)
        coord.append(tuple(sorted(cnt.values(), reverse=True)))
    for a,b in ((0,1),(0,2),(1,2)):
        cnt=Counter((WORDS[i][a],WORDS[i][b]) for i in C)
        pairs.append(tuple(sorted(cnt.values(), reverse=True)))
    return tuple(coord),tuple(pairs)
P=Counter(profile(C) for C in maxima)
assert sorted(P.values())==[27,108]
for rep,orb in orbits:
    pr=profile(rep)
    assert len({profile(C) for C in orb})==1
    print('ORBIT',len(orb),'STAB',1296//len(orb),'REP',[WORDS[i] for i in rep],'PROFILE',pr)

# Expected representative profiles: one has (4,1,1) in each coordinate and
# pair projections (2,1,1,1,1); the other is (2,2,2) with six distinct pairs.
profile_counts=[]
for pr,c in sorted(P.items(), key=lambda kv:kv[1]):
    profile_counts.append((c,pr))
print('PROFILE_COUNTS',profile_counts)
assert {tuple(pr[0]) for pr in P} == {((4,1,1),)*3, ((2,2,2),)*3}

# Census hash uses canonical word strings for all maximum codes.
lines=[]
for C in maxima:
    lines.append(','.join(''.join(map(str,WORDS[i])) for i in C))
blob=('\n'.join(lines)+'\n').encode()
h=hashlib.sha256(blob).hexdigest()
print('VERIFY_OK maximum=%d labeled_maxima=%d size7_extensions=%d natural_group=%d orbits=%d orbit_sizes=%s stabilizers=%s nodes=%d rejections=%d census_sha256=%s' % (
    best,len(maxima),size7_extensions,len(transforms),len(orbits),','.join(map(str,[len(o) for _,o in orbits])),','.join(map(str,stabs)),nodes,rejections,h))
