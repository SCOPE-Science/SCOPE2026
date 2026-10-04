#!/usr/bin/env python3
import json, itertools, collections, pathlib, sys
BASE=pathlib.Path(__file__).resolve().parent
C=json.loads((BASE/'morse_certificate.json').read_text(encoding='utf-8'))
V=C['graph']['vertices']; E={tuple(e) for e in C['graph']['edge_list']}
assert V==list(range(12)) and len(E)==30
N={v:set() for v in V}
for a,b in E:
    assert a<b and a in N and b in N
    N[a].add(b); N[b].add(a)
assert all(len(N[v])==5 for v in V)
assert len({v for v in V if N[v]})==12
# The explicit graph is the usual two-pentagonal-ring realization of the icosahedral graph.
faces=set()
for v in V:
    nb=sorted(N[v])
    for k in range(1,len(nb)+1):
        faces.update(itertools.combinations(nb,k))
bydim=collections.Counter(len(f)-1 for f in faces)
assert {str(k):bydim[k] for k in range(5)}==C['neighborhood_complex']['face_count_by_dimension']
assert len(faces)==C['neighborhood_complex']['total_nonempty_faces']==264
# Reconstruct the deterministic element matching from the archived vertex order.
unmatched=set(faces); regen=[]
for v in C['matching']['vertex_order']:
    for s in sorted(list(unmatched),key=lambda x:(len(x),x)):
        if s not in unmatched or v in s: continue
        t=tuple(sorted(s+(v,)))
        if t in unmatched:
            regen.append((s,t)); unmatched.remove(s); unmatched.remove(t)
arch=[(tuple(a),tuple(b)) for a,b in C['matching']['pairs']]
assert regen==arch and len(regen)==C['matching']['pair_count']==120
assert sorted([list(x) for x in unmatched],key=lambda x:(len(x),x))==C['matching']['critical_faces']
crit=collections.Counter(len(f)-1 for f in unmatched)
assert {str(k):crit.get(k,0) for k in range(5)}==C['matching']['expected_critical_by_dimension']
# Verify every pair is a cover and no simplex appears in two pairs.
used=set()
for a,b in regen:
    assert a in faces and b in faces and len(b)==len(a)+1 and set(a)<set(b)
    assert a not in used and b not in used
    used.add(a);used.add(b)
# Full Forman acyclicity check: orient unmatched covers downward and matched covers upward.
pairset=set(regen); adj={f:[] for f in faces}; indeg={f:0 for f in faces}; covers=0
for t in faces:
    for i in range(len(t)):
        s=t[:i]+t[i+1:]
        if s not in faces: continue
        covers+=1
        u,v=(s,t) if (s,t) in pairset else (t,s)
        adj[u].append(v); indeg[v]+=1
assert covers==C['matching']['hasse_cover_count']==780
q=collections.deque([f for f,d in indeg.items() if d==0]); seen=0
while q:
    u=q.popleft(); seen+=1
    for v in adj[u]:
        indeg[v]-=1
        if indeg[v]==0:q.append(v)
assert seen==len(faces), 'matching has a directed cycle'
# Independent mod-2 simplicial homology check.
by_k={k:sorted([f for f in faces if len(f)==k+1]) for k in range(5)}
def gf2_rank(columns):
    piv={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:
                piv[p]=x; break
    return len(piv)
ranks=[0]*6
for k in range(1,5):
    rows={s:i for i,s in enumerate(by_k[k-1])}; cols=[]
    for t in by_k[k]:
        bits=0
        for i in range(len(t)):
            s=t[:i]+t[i+1:]
            bits ^= 1<<rows[s]
        cols.append(bits)
    ranks[k]=gf2_rank(cols)
betti=[]
for k in range(5):
    betti.append(len(by_k[k])-ranks[k]-ranks[k+1])
assert betti==C['expected_mod2_betti']==[1,0,23,0,0]
print('VERIFY_OK')
print('f_vector', [len(by_k[k]) for k in range(5)])
print('matching_pairs',len(regen),'critical',dict(sorted(crit.items())),'hasse_covers',covers)
print('mod2_betti',betti)
