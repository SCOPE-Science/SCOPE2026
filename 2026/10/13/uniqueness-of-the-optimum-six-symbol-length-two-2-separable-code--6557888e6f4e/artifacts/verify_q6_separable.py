#!/usr/bin/env python3
from itertools import permutations
from collections import Counter
from math import factorial
import hashlib, json

Q=6
MASKS=list(range(1<<Q))
W=[m.bit_count() for m in MASKS]

def compatible(a,b):
    return (a & b).bit_count() <= 1

# Enumerate row-multisets (rows sorted as masks; columns remain labeled).
def enumerate_target(target):
    out=[]
    def rec(rows,start,total):
        k=len(rows)
        if k==Q:
            if total==target: out.append(tuple(rows))
            return
        slots=Q-k
        if total>target: return
        # absolute weight bounds plus nondecreasing masks
        if total + 6*slots < target: return
        for m in range(start,1<<Q):
            wt=W[m]
            nt=total+wt
            if nt>target: continue
            if nt + 6*(slots-1) < target: continue
            if all(compatible(m,r) for r in rows):
                rec(rows+[m],m,nt)
    rec([],0,0)
    return out

M16=enumerate_target(16)
M17=enumerate_target(17)
assert len(M16)==90, len(M16)
assert len(M17)==0, len(M17)

def transpose(rows):
    return tuple(sorted(sum(((rows[i]>>j)&1)<<i for i in range(Q)) for j in range(Q)))

def permute_mask(m,p):
    # old column j moves to new column p[j]
    out=0
    for j in range(Q):
        if (m>>j)&1: out |= 1<<p[j]
    return out

COL_PERMS=list(permutations(range(Q)))
def canon_side(rows):
    best=None
    for p in COL_PERMS:
        t=tuple(sorted(permute_mask(m,p) for m in rows))
        if best is None or t<best: best=t
    return best

def canon_full(rows):
    a=canon_side(rows)
    b=canon_side(transpose(rows))
    return min(a,b)

cans={canon_full(r) for r in M16}
assert len(cans)==1, len(cans)
rep=min(cans)
FRIENDLY=(3,12,21,26,41,38)  # {0,1},{2,3},{0,2,4},{1,3,4},{0,3,5},{1,2,5}
assert canon_full(FRIENDLY)==rep

# Structural checks for every equality case.
for rows in M16:
    rw=sorted(W[m] for m in rows)
    cols=transpose(rows)
    cw=sorted(W[m] for m in cols)
    assert rw==[2,2,3,3,3,3], rw
    assert cw==[2,2,3,3,3,3], cw
    covered=Counter()
    for m in rows:
        pts=[j for j in range(Q) if (m>>j)&1]
        for a in range(len(pts)):
            for b in range(a+1,len(pts)):
                covered[(pts[a],pts[b])]+=1
    assert all(v==1 for v in covered.values())
    assert len(covered)==14
    leave=[(a,b) for a in range(Q) for b in range(a+1,Q) if (a,b) not in covered]
    assert len(leave)==1

# Labeled matrix count: columns are labeled in M16, row sorting removed row labels.
def multiset_row_labelings(rows):
    c=Counter(rows)
    den=1
    for v in c.values(): den*=factorial(v)
    return factorial(Q)//den
labeled=sum(multiset_row_labelings(r) for r in M16)
assert labeled==64800, labeled

# Direct orbit from representative under S6 x S6, and transpose.
orbit=set()
for cp in COL_PERMS:
    base=tuple(permute_mask(m,cp) for m in rep)
    for rp in permutations(range(Q)):
        rr=tuple(base[i] for i in rp)
        orbit.add(rr)
        orbit.add(tuple(transpose(rr)))
assert len(orbit)==64800, len(orbit)
full_group=2*(factorial(Q)**2)
stab=full_group//len(orbit)
assert stab==16, stab

# Build a Fano completion of the representative: two 2-blocks become triples through new point 6,
# and the unique uncovered pair plus 6 becomes the seventh triple.
blocks=[]
covered=Counter()
for m in rep:
    pts=tuple(j for j in range(Q) if (m>>j)&1)
    for a in range(len(pts)):
        for b in range(a+1,len(pts)):
            covered[tuple(sorted((pts[a],pts[b])))]+=1
    blocks.append(pts)
leave=[(a,b) for a in range(Q) for b in range(a+1,Q) if (a,b) not in covered]
assert len(leave)==1
completed=[tuple(sorted(b+(6,))) if len(b)==2 else b for b in blocks]
completed.append(tuple(sorted(leave[0]+(6,))))
pairs=Counter()
for b in completed:
    assert len(b)==3
    for i in range(3):
        for j in range(i+1,3): pairs[tuple(sorted((b[i],b[j])))]+=1
assert len(pairs)==21 and set(pairs.values())=={1}

# Descendant-definition spot/check equivalence on every enumerated maximum.
def desc(pairset):
    coords=[]
    for pos in range(2): coords.append(tuple(sorted({x[pos] for x in pairset})))
    return tuple(coords)
def code_from_rows(rows):
    return [(i,j) for i,m in enumerate(rows) for j in range(Q) if (m>>j)&1]
def separable2(code):
    coal=[]
    for i,x in enumerate(code): coal.append(((i,),desc([x])))
    for i in range(len(code)):
        for j in range(i+1,len(code)): coal.append(((i,j),desc([code[i],code[j]])))
    seen={}
    for idx,d in coal:
        if d in seen and seen[d]!=idx: return False
        seen[d]=idx
    return True
for rows in M16:
    assert separable2(code_from_rows(rows))

rep_pairs=code_from_rows(FRIENDLY)
rep_string=','.join(f'{a}{b}' for a,b in rep_pairs)
sha=hashlib.sha256(('\n'.join(','.join(f'{a}{b}' for a,b in code_from_rows(r)) for r in M16)+'\n').encode()).hexdigest()
print('VERIFY_OK',
      f'vertices=36 target17={len(M17)} row_multisets16={len(M16)} maximum=16',
      f'labeled_maxima={labeled} natural_group={full_group} orbits={len(cans)} orbit_size={len(orbit)} stabilizer={stab}',
      'degree_profile=2,2,3,3,3,3x2',
      f'representative={rep_string}',
      f'normalized_sha256={sha}')
