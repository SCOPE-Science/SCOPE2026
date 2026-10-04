#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
PAIRS=list(itertools.combinations(range(5),2))

def rank3(rows):
    if not rows:
        return 0
    A=[list(r) for r in rows]
    rr=0
    n=len(A[0])
    for c in range(n):
        p=next((i for i in range(rr,len(A)) if A[i][c]%3),None)
        if p is None:
            continue
        A[rr],A[p]=A[p],A[rr]
        inv=1 if A[rr][c]%3==1 else 2
        A[rr]=[(inv*z)%3 for z in A[rr]]
        for i in range(len(A)):
            if i!=rr and A[i][c]%3:
                f=A[i][c]%3
                A[i]=[(A[i][j]-f*A[rr][j])%3 for j in range(n)]
        rr+=1
        if rr==len(A):
            break
    return rr

# Full torus evaluation matrix.
torus=list(itertools.product((1,2),repeat=5))
columns=[tuple((x[i]*x[j])%3 for i,j in PAIRS) for x in torus]
rows=[[columns[c][r] for c in range(32)] for r in range(10)]
assert rank3(rows)==10

mult=collections.Counter(columns)
assert len(mult)==16
assert set(mult.values())=={2}

# Projective representatives x_1=1.
labels=[(1,)+tail for tail in itertools.product((1,2),repeat=4)]
pts=[tuple((x[i]*x[j])%3 for i,j in PAIRS) for x in labels]
assert len(set(pts))==16

good8=[]
for I in itertools.combinations(range(16),8):
    if rank3([pts[i] for i in I])<=7:
        good8.append(I)
assert len(good8)==750
assert all(rank3([pts[i] for i in I])==7 for I in good8)

bad9=0
for I in itertools.combinations(range(16),9):
    if rank3([pts[i] for i in I])<=7:
        bad9+=1
assert bad9==0

# Natural signed-coordinate-permutation group, modulo global sign.
index={x:i for i,x in enumerate(labels)}
actions=set()
for eps_tail in itertools.product((1,2),repeat=4):
    eps=(1,)+eps_tail
    for perm in itertools.permutations(range(5)):
        image=[]
        for x in labels:
            y=tuple((eps[i]*x[i])%3 for i in range(5))
            y=tuple(y[perm[i]] for i in range(5))
            inv=1 if y[0]==1 else 2
            yn=tuple((inv*z)%3 for z in y)
            image.append(index[yn])
        actions.add(tuple(image))
assert len(actions)==1920

def to_mask(I):
    z=0
    for i in I:
        z|=1<<i
    return z

def act(mask,mp):
    z=0
    for i in range(16):
        if (mask>>i)&1:
            z|=1<<mp[i]
    return z

M={to_mask(I) for I in good8}
unseen=set(M)
orbits=[]
for seed in list(M):
    if seed not in unseen:
        continue
    orb={act(seed,mp) for mp in actions}
    assert orb<=M
    orbits.append(orb)
    unseen-=orb
assert not unseen
sizes=sorted(len(o) for o in orbits)
assert sizes==[10,20,240,480]
assert sum(sizes)==750

assert CERT["eight_subsets_rank_at_most_7"]==750
assert CERT["nine_subsets_rank_at_most_7"]==0
assert CERT["minimum_support_subcodes"]==750
assert CERT["natural_group_order"]==1920
assert CERT["natural_orbit_sizes"]==[10,20,240,480]
print("VERIFY_OK")
