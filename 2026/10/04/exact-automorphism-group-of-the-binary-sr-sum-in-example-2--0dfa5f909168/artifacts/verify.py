#!/usr/bin/env python3
from itertools import product, permutations
from collections import Counter, deque
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
G = cert["code"]["generator_basis"]

def rowcomb(c):
    return tuple(sum(c[i]*G[i][j] for i in range(3)) % 2 for j in range(9))

C = {rowcomb(c) for c in product([0,1], repeat=3)}
assert len(C) == 8

weights = Counter(sum(w) for w in C)
assert weights == Counter({0:1,3:2,4:1,5:1,6:2,9:1})
assert min(w for w in weights if w) == 3

def act_word(w,p):
    return tuple(w[p[j]] for j in range(9))

autos = set()
for p in permutations(range(9)):
    if all(act_word(w,p) in C for w in C):
        autos.add(p)
assert len(autos) == 192

# Coordinate orbits.
unseen=set(range(9)); orbits=[]
while unseen:
    x=min(unseen)
    orb={p[x] for p in autos}
    orbits.append(tuple(sorted(i+1 for i in orb)))
    unseen -= orb
assert orbits == [(1,2,4,5),(3,6,7,8),(9,)]

# GF(2) rank.
def rank2(A):
    A=[row[:] for row in A]
    r=0
    for c in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][c]), None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                A[i]=[x^y for x,y in zip(A[i],A[r])]
        r+=1
    return r

def mat_vec(A,v):
    return tuple(sum(A[i][j]*v[j] for j in range(3))%2 for i in range(3))

cols=[tuple(G[i][j] for i in range(3)) for j in range(9)]
target=Counter(cols)
pres=[]
for bits in product([0,1], repeat=9):
    A=[list(bits[3*i:3*i+3]) for i in range(3)]
    if rank2(A)!=3:
        continue
    image=Counter(mat_vec(A,v) for v in cols)
    if image==target:
        pres.append(A)

assert len(pres)==2
expected=[
    [[1,0,0],[0,1,0],[0,0,1]],
    [[0,0,1],[0,1,0],[1,0,0]],
]
assert all(A in pres for A in expected)

# For each preserving row action, count matching coordinate bijections by type.
def matching_count(A):
    src=[mat_vec(A,v) for v in cols]
    classes={}
    for j,v in enumerate(cols):
        classes.setdefault(v,[]).append(j)
    count=1
    for v,inds in classes.items():
        m=sum(1 for x in src if x==v)
        assert m==len(inds)
        # factorial of class size
        f=1
        for x in range(2,len(inds)+1): f*=x
        count*=f
    return count
assert [matching_count(A) for A in pres]==[96,96] or sorted(matching_count(A) for A in pres)==[96,96]

# Permutation utilities: p gives images of positions; compose(p,q)=p after q.
def compose(p,q):
    return tuple(p[q[i]] for i in range(9))
def cyc(*cycles):
    p=list(range(9))
    for cyc1 in cycles:
        cyc0=[x-1 for x in cyc1]
        for a,b in zip(cyc0,cyc0[1:]+cyc0[:1]):
            p[a]=b
    return tuple(p)

gens=[
    cyc((1,2)),
    cyc((2,4)),
    cyc((4,5)),
    cyc((1,4),(2,5),(3,6)),
    cyc((1,2),(4,5),(7,8)),
    cyc((2,4),(3,7),(6,8)),
]
identity=tuple(range(9))
generated={identity}
q=deque([identity])
while q:
    h=q.popleft()
    for g in gens:
        u=compose(g,h)
        if u not in generated:
            generated.add(u); q.append(u)
assert len(generated)==192
assert generated==autos

saved={tuple(x-1 for x in p) for p in (tuple(a) for a in cert["all_automorphisms_one_based_images"])}
assert saved==autos

print("VERIFY_OK")
