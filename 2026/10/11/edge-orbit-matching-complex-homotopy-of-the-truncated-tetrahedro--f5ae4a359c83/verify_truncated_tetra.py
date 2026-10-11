#!/usr/bin/env python3
"""Exhaustive simplex and acyclic-matching proof for a truncated-tetrahedral graph.
Reconstructs every simplicial face and the complete directed Hasse diagram.
Standard library only.
"""
import itertools, collections, hashlib, json
V=list(itertools.permutations(range(4),2)); id_of={v:i for i,v in enumerate(V)}
E=[]
for a,b in itertools.combinations(range(len(V)),2):
    x,y=V[a],V[b]
    if x[0]==y[0] or (x[0]==y[1] and x[1]==y[0]): E.append((a,b))
assert len(V)==12 and len(E)==18
assert collections.Counter(a for ab in E for a in ab)=={a:3 for a in range(12)}
classes={'triangular':[i for i,(a,b) in enumerate(E) if V[a][0]==V[b][0]],
         'reversal':[i for i,(a,b) in enumerate(E) if V[a]==tuple(reversed(V[b]))]}
assert tuple(map(len,classes.values()))==(12,6)
conflicts=[sum(1<<j for j,(c,d) in enumerate(E) if i!=j and ({a,b}&{c,d})) for i,(a,b) in enumerate(E)]
# All 18-bit masks that select pairwise vertex-disjoint edges.
allfaces=[0]
for i in range(18):
    allfaces += [s|(1<<i) for s in allfaces if not(s&conflicts[i])]
assert len(allfaces)==1010 and len(set(allfaces))==1010

def result(faces,label):
    fs=sorted(set(faces));face_set=set(fs)
    assert 0 in face_set
    for s in fs:
        for v in range(18):
            if s&(1<<v):assert s^(1<<v) in face_set
    unmatched=set(fs);matching=[];up={}
    for v in range(18):
        bit=1<<v
        for s in fs:
            if s in unmatched and not(s&bit) and (s|bit) in unmatched:
                t=s|bit;unmatched.remove(s);unmatched.remove(t)
                matching.append((s,t));up[s]=t
    # For simplicial complexes without the empty face, the unmatched
    # vertex matched to empty is instead retained as a critical 0-cell.
    assert 0 in up
    critical=[up[0]]+sorted(unmatched)
    sizes=collections.Counter(s.bit_count()-1 for s in critical)
    indeg={s:0 for s in fs if s!=0};out={s:[] for s in fs if s!=0};incidences=0
    # Drop augmented empty face and its pair when checking ordinary Hasse DAG.
    for s in fs:
        if not s: continue
        vs=[v for v in range(18) if s&(1<<v)]
        for v in vs:
            face=s^(1<<v)
            if not face:continue
            incidences+=1
            a,b=(face,s) if up.get(face)==s else (s,face)
            out[a].append(b);indeg[b]+=1
    Q=collections.deque(s for s in sorted(out) if indeg[s]==0);seen=0
    while Q:
        s=Q.popleft();seen+=1
        for t in out[s]:
            indeg[t]-=1
            if indeg[t]==0:Q.append(t)
    assert seen==len(fs)-1,(label,'acyclic DAG failed',seen)
    assert sum(sizes.values()) == len(fs)-1-2*(len(matching)-1)
    return {'label':label,'nonempty_simplices':len(fs)-1,
            'face_vector':{str(j):sum(s.bit_count()==j+1 for s in fs) for j in range(max(s.bit_count() for s in fs))},
            'matching_pairs_unaugmented':len(matching)-1,
            'critical_cells':{str(k):v for k,v in sorted(sizes.items())},
            'hasse_incidences':incidences,
            'acyclic_vertices_checked':seen,
            'matching_sha256':hashlib.sha256(json.dumps(matching, separators=(',',':')).encode()).hexdigest()}

base=result(allfaces,'full')
assert base['critical_cells']=={'0':1,'3':22}
print(json.dumps(base,sort_keys=True))
for orbit,ids in classes.items():
    i=ids[0];mask=1<<i
    dele=result([s for s in allfaces if not (s&mask)],f'{orbit} edge deletion')
    link=result([s^mask for s in allfaces if s&mask],f'{orbit} endpoint deletion')
    expected=({'0':1,'3':14},{'0':1,'2':8}) if orbit=='triangular' else ({'0':1,'3':20},{'0':1,'2':2})
    assert (dele['critical_cells'],link['critical_cells'])==expected,(orbit,dele,link)
    print(json.dumps(dele,sort_keys=True));print(json.dumps(link,sort_keys=True))
print('VERIFY_OK')
