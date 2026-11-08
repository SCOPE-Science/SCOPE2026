#!/usr/bin/env python3
"""Reproducible integral homotopy certificate for the bidirected complete bipartite multipath complex."""
from itertools import combinations,product
from collections import Counter,deque
from functools import lru_cache

A=tuple(range(3)); B=tuple(range(3,6)); V=A+B
E=tuple((i,j) for i in A for j in B)+tuple((j,i) for i in A for j in B)
ORDER=(17,15,14,2,7,3,10,11,0,4,8,16,12,5,9,6,13,1)
assert len(E)==18 and set(ORDER)==set(range(18))

def admissible(mask):
    nxt=[-1]*6; indeg=[0]*6
    for e,(src,tgt) in enumerate(E):
        if mask>>e & 1:
            if nxt[src]!=-1 or indeg[tgt]:return False
            nxt[src]=tgt; indeg[tgt]=1
    for src in range(6):
        v=src
        for _ in range(6):
            v=nxt[v] if v!=-1 else -1
            if v==src:return False
            if v==-1:break
    return True

# Method A: unordered arc subsets, limited by vertex count-1.
faces_a={sum(1<<x for x in c) for k in range(1,6) for c in combinations(range(18),k) if admissible(sum(1<<x for x in c))}
# Method B: for each source choose no outgoing arc or exactly one; enforce indegrees and acyclicity.
choices=[[None]+[j for j,(u,v) in enumerate(E) if u==i] for i in V]
faces_b=set()
for selection in product(*choices):
    picked=[i for i in selection if i is not None]
    if not picked:continue
    mask=sum(1<<i for i in picked)
    if admissible(mask):faces_b.add(mask)
assert faces_a==faces_b, (len(faces_a),len(faces_b))
faces=faces_a
fvector=tuple(sum(f.bit_count()==k for f in faces) for k in range(1,6))
assert fvector==(18,108,264,252,72),fvector
print('FACE_CENSUS_OK',len(faces),fvector,flush=True)

# Sequential element-toggle matching, each stage only on currently unpaired simplices.
active=set(faces); pairs=[]
for bit_id in ORDER:
    bit=1<<bit_id
    for lower in sorted(active):
        upper=lower|bit
        if not (lower&bit) and upper in active:
            active.remove(lower);active.remove(upper);pairs.append((lower,upper))
critical=frozenset(active)
cprofile=Counter(f.bit_count()-1 for f in critical)
assert cprofile=={0:1,3:19,4:12},cprofile
assert len(pairs)==341
lo_to_hi=dict(pairs);hi_to_lo={hi:lo for lo,hi in pairs}
assert len(lo_to_hi)==len(hi_to_lo)==len(pairs)
assert len(critical)+2*len(pairs)==len(faces)
for lower,upper in pairs:
    assert lower in faces and upper in faces
    assert (upper^lower).bit_count()==1 and lower&upper==lower
print('MORSE_PAIRS_OK',len(pairs),dict(sorted(cprofile.items())),flush=True)

# Entire oriented Hasse diagram must be acyclic after reversing matched incidences.
adj={f:[] for f in faces}; indegrees={f:0 for f in faces}; incidences=0
for upper in faces:
    for i in range(18):
        if upper>>i&1:
            lower=upper^(1<<i)
            if lower==0:continue
            incidences+=1
            source,target=(lower,upper) if lo_to_hi.get(lower)==upper else (upper,lower)
            adj[source].append(target);indegrees[target]+=1
queue=deque(f for f in faces if indegrees[f]==0);seen=0
while queue:
    x=queue.popleft();seen+=1
    for y in adj[x]:
        indegrees[y]-=1
        if indegrees[y]==0:queue.append(y)
assert seen==len(faces)
print('DIRECTED_HASSE_ACYCLIC_OK',seen,incidences,flush=True)

def simplex_boundary(face):
    ids=[i for i in range(18) if face>>i&1]
    return {face^(1<<i):(-1)**j for j,i in enumerate(ids) if face^(1<<i)}

# Algorithm 1: algebraic discrete-Morse recursion.
@lru_cache(None)
def project(face):
    if face in critical:return {face:1}
    if face in hi_to_lo:return {}
    upper=lo_to_hi[face]
    delta=simplex_boundary(upper)
    sign=delta[face]
    ans={}
    for child,coef in delta.items():
        if child==face:continue
        for final,v in project(child).items():ans[final]=ans.get(final,0)-sign*coef*v
    return {x:v for x,v in ans.items() if v}

morse_1={}
for face in sorted(critical):
    if face.bit_count()==5:
        d={}
        for sub,coef in simplex_boundary(face).items():
            for target,v in project(sub).items():d[target]=d.get(target,0)+coef*v
        morse_1[face]={x:v for x,v in d.items() if v}
assert len(morse_1)==12 and all(not row for row in morse_1.values())
print('MORSE_RECURSIVE_BOUNDARY_OK',len(morse_1),'zero columns',flush=True)

# Algorithm 2: independently eliminate every matched pair by integer unit pivots.
# Only one differential matrix in each degree gets the Schur-complement update;
# the next differential simply loses the eliminated upper basis row.
dimension={f:f.bit_count()-1 for f in faces}
boundary={f:simplex_boundary(f) for f in faces}
remaining=set(faces); pending=set(pairs); steps=0
while pending:
    chosen=None
    for lower,upper in sorted(pending):
        if abs(boundary[upper].get(lower,0))==1:
            chosen=(lower,upper);break
    assert chosen is not None, ('unit pivot not available',len(pending))
    lower,upper=chosen; factor=boundary[upper][lower]
    dupper=boundary[upper].copy()
    for cell in remaining:
        if cell in (lower,upper):continue
        d=boundary[cell]
        if dimension[cell]==dimension[upper]:
            c=d.pop(lower,0)
            if c:
                for sub,v in dupper.items():
                    if sub==lower:continue
                    d[sub]=d.get(sub,0)-factor*c*v
                    if d[sub]==0:del d[sub]
        elif dimension[cell]==dimension[upper]+1:d.pop(upper,None)
    remaining.remove(lower);remaining.remove(upper)
    pending.remove(chosen)
    boundary.pop(lower);boundary.pop(upper)
    steps+=1
assert remaining==critical
morse_2={f:{x:v for x,v in boundary[f].items() if v} for f in critical if f.bit_count()==5}
assert morse_1==morse_2,(morse_1,morse_2)
print('INTEGER_UNIT_ELIMINATION_OK',steps,'pairs; two methods identical',flush=True)

# Independent mod-two boundary ranks, from original faces, not from Morse model.
by_size={k:sorted(f for f in faces if f.bit_count()==k) for k in range(1,6)}
ranks=[]
for k in range(2,6):
    row={f:i for i,f in enumerate(by_size[k-1])};pivots={}
    for f in by_size[k]:
        x=0
        for j in range(18):
            if f>>j&1:x^=1<<row[f^(1<<j)]
        while x:
            b=x.bit_length()-1
            if b in pivots:x^=pivots[b]
            else:pivots[b]=x;break
    ranks.append(len(pivots))
assert ranks==[17,91,173,60],ranks
print('MOD_TWO_HOMOLOGY_OK',tuple(ranks),'reduced (H3,H4)=(19,12)',flush=True)
print('HOMOTOPY_OK wedge(19 S3,12 S4) ALL_VERIFY_OK',flush=True)
