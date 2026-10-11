#!/usr/bin/env python3
from collections import Counter, defaultdict, deque

N = 18
EDGES = {(0,1),(0,5),(0,17),(1,2),(1,8),(2,3),(2,13),(3,4),(3,10),
         (4,5),(4,15),(5,6),(6,7),(6,11),(7,8),(7,14),(8,9),(9,10),
         (9,16),(10,11),(11,12),(12,13),(12,17),(13,14),(14,15),(15,16),(16,17)}
ORDER = [2,1,16,14,3,10,4,13,15,11,8,9,17,0,7,5,12,6]

adj = [0]*N
for a,b in EDGES:
    adj[a] |= 1<<b
    adj[b] |= 1<<a
assert len(EDGES) == 27
assert all(adj[v].bit_count() == 3 for v in range(N))

faces = []
for s in range(1,1<<N):
    t=s; ok=True
    while t:
        b=t & -t
        i=b.bit_length()-1
        t-=b
        if adj[i] & t:
            ok=False; break
    if ok: faces.append(s)
F=set(faces)
fvec=Counter(s.bit_count()-1 for s in faces)
assert [fvec[i] for i in range(max(fvec)+1)] == [18,126,438,801,756,348,90,18,2]
assert len(faces)==2597

# Sequential element matching: at stage v, pair every still-unmatched face s not
# containing v with s union {v}, whenever both are faces and still unmatched.
unmatched=set(faces)
pairs=[]
for v in ORDER:
    bv=1<<v
    candidates=sorted((s for s in unmatched if not(s&bv) and (s|bv) in unmatched),
                      key=lambda s:(s.bit_count(),s))
    for s in candidates:
        t=s|bv
        if s in unmatched and t in unmatched:
            unmatched.remove(s); unmatched.remove(t); pairs.append((s,t))
assert len(pairs)==1293
crit=Counter(s.bit_count()-1 for s in unmatched)
assert crit == Counter({4:10,0:1})
assert len(unmatched)==11

# Every matched pair is a codimension-one Hasse cover.
matched={(a,b) for a,b in pairs}
assert all(a in F and b in F and a < b and (b^a).bit_count()==1 for a,b in pairs)

# Exhaustive acyclicity check on the full directed Hasse graph: unmatched covers
# point upward, matched covers are reversed.
indeg={s:0 for s in faces}
out=defaultdict(list)
cover_count=0
for upper in faces:
    t=upper
    while t:
        bit=t & -t; t-=bit
        lower=upper^bit
        if lower==0 or lower not in F: continue
        cover_count+=1
        if (lower,upper) in matched:
            a,b=upper,lower
        else:
            a,b=lower,upper
        out[a].append(b); indeg[b]+=1
assert cover_count==11430
q=deque(sorted(s for s in faces if indeg[s]==0))
seen=0
while q:
    u=q.popleft(); seen+=1
    for v in out[u]:
        indeg[v]-=1
        if indeg[v]==0: q.append(v)
assert seen==len(faces)

# Independent mod-2 homology computation from all boundary matrices.
def rank2(columns):
    piv={}; r=0
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x; r+=1; break
    return r
bydim=defaultdict(list)
for s in faces: bydim[s.bit_count()-1].append(s)
ranks={}
for d in range(1,max(bydim)+1):
    row={s:i for i,s in enumerate(bydim[d-1])}
    columns=[]
    for s in bydim[d]:
        col=0; t=s
        while t:
            bit=t & -t; t-=bit
            col ^= 1<<row[s^bit]
        columns.append(col)
    ranks[d]=rank2(columns)
assert ranks == {1:17,2:109,3:329,4:472,5:274,6:74,7:16,8:2}
redbetti=[]
for d in range(max(bydim)+1):
    b=len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
    redbetti.append(b)
assert redbetti == [0,0,0,0,10,0,0,0,0]

chi=sum(((-1)**d)*len(bydim[d]) for d in bydim)
assert chi==11
print('VERIFY_OK')
print('vertices=18 edges=27 faces=2597 hasse_covers=11430')
print('f_vector=' + repr([len(bydim[d]) for d in range(max(bydim)+1)]))
print('matching_pairs=1293 critical={0:1,4:10}')
print('directed_hasse_acyclic=True')
print('mod2_boundary_ranks=' + repr(ranks))
print('reduced_mod2_betti=' + repr(redbetti))
print('euler_characteristic=11')
