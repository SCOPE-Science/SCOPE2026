#!/usr/bin/env python3
import json, itertools, sys
from collections import Counter, deque

P=13
Q={1,3,4,9,10,12}
adj={v:{(v+d)%P for d in Q} for v in range(P)}
# Independent graph sanity checks.
assert all(v not in adj[v] for v in range(P))
assert all(len(adj[v])==6 for v in range(P))
for u in range(P):
    for v in range(u+1,P):
        common=len(adj[u]&adj[v])
        assert common==(2 if v in adj[u] else 3)

faces=set()
for N in adj.values():
    L=sorted(N)
    for r in range(1,len(L)+1):
        faces.update(itertools.combinations(L,r))
by={}
for face in faces:
    by.setdefault(len(face)-1,[]).append(face)
for d in by:
    by[d].sort()
fvec=[len(by[d]) for d in range(max(by)+1)]
assert fvec==[13,78,221,195,78,13]
assert len(faces)==598
assert sum(((-1)**d)*len(by[d]) for d in by)==26

# Reconstruct the staged toggle matching from scratch.
unmatched=set(faces)
pairs=[]
for v in range(P):
    for face in sorted(list(unmatched), key=lambda z:(len(z),z)):
        if face not in unmatched or v in face:
            continue
        upper=tuple(sorted(face+(v,)))
        if upper in unmatched:
            unmatched.remove(face)
            unmatched.remove(upper)
            pairs.append((face,upper,v))
critical=sorted(unmatched,key=lambda f:(len(f),f))
assert len(pairs)==286
assert Counter(len(f)-1 for f in critical)==Counter({2:25,0:1})
assert critical[0]==(0,)

# Every pair is a codimension-one face relation and pairs are disjoint.
used=set()
for a,b,v in pairs:
    assert a in faces and b in faces and set(a)<set(b) and len(b)==len(a)+1
    assert set(b)-set(a)=={v}
    assert a not in used and b not in used
    used.add(a); used.add(b)
assert len(used)==572

# Direct global acyclicity check on the oriented Hasse diagram:
# matched covers point upward, all other covers point downward.
allfaces=sorted(faces,key=lambda f:(len(f),f))
idx={f:i for i,f in enumerate(allfaces)}
matched={(a,b) for a,b,_ in pairs}
out=[[] for _ in allfaces]; indeg=[0]*len(allfaces); covers=0
for upper in allfaces:
    if len(upper)<=1:
        continue
    for i in range(len(upper)):
        lower=upper[:i]+upper[i+1:]
        if lower not in idx:
            continue
        covers+=1
        if (lower,upper) in matched:
            s,t=idx[lower],idx[upper]
        else:
            s,t=idx[upper],idx[lower]
        out[s].append(t); indeg[t]+=1
q=deque(i for i,d in enumerate(indeg) if d==0); seen=0
while q:
    u=q.popleft(); seen+=1
    for w in out[u]:
        indeg[w]-=1
        if indeg[w]==0: q.append(w)
assert covers==2067
assert seen==len(allfaces)

# Check the stored certificate exactly matches the reconstructed one.
with open('CERTIFICATE.json',encoding='utf-8') as f:
    c=json.load(f)
assert c['face_vector']==fvec
assert c['total_nonempty_faces']==598
assert c['critical_faces']==[list(f) for f in critical]
assert c['critical_by_dimension']=={'0':1,'2':25}
assert c['matched_pairs']==[
    {'lower':list(a),'upper':list(b),'toggle_vertex':v} for a,b,v in pairs
]

# Independent finite-field boundary-rank cross-check.
def rank_mod(rows,p):
    piv={}; rank=0
    for row in rows:
        row={j:(v%p) for j,v in row.items() if v%p}
        while row:
            j=min(row)
            if j not in piv:
                inv=pow(row[j],-1,p)
                row={k:(v*inv)%p for k,v in row.items() if (v*inv)%p}
                piv[j]=row; rank+=1; break
            fac=row[j]
            for k,v in piv[j].items():
                nv=(row.get(k,0)-fac*v)%p
                if nv: row[k]=nv
                elif k in row: del row[k]
    return rank
for prime in (2,3,5):
    ranks=[]
    for d in range(1,max(by)+1):
        lo=by[d-1]; pos={f:i for i,f in enumerate(lo)}
        rows=[{} for _ in lo]
        for j,f in enumerate(by[d]):
            for i in range(len(f)):
                g=f[:i]+f[i+1:]
                rows[pos[g]][j]=1 if i%2==0 else -1
        ranks.append(rank_mod(rows,prime))
    assert ranks==[12,66,130,65,13]
    bet=[]
    for d in range(max(by)+1):
        bet.append(len(by[d])-(ranks[d-1] if d else 0)-(ranks[d] if d<len(ranks) else 0))
    assert bet==[1,0,25,0,0,0]
print('PASS: 598 faces; 2067 Hasse covers; 286 acyclic pairs; critical vector (1,0,25,0,0,0); mod-2/3/5 Betti vector (1,0,25,0,0,0).')
