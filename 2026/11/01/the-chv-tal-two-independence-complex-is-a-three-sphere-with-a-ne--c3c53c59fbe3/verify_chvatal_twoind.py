#!/usr/bin/env python3
"""Exact finite face-poset and character checks for a graph higher-independence complex.
Pure Python 3; run beside MORSE_PAIRS.json.
"""
import collections
import itertools
import json
from pathlib import Path

N = 12
EDGES = (
    (0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
    (2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
    (5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11),
)
ADJ=[0]*N
for u,v in EDGES:
    assert 0<=u<v<N
    ADJ[u]|=1<<v
    ADJ[v]|=1<<u
assert all(x.bit_count()==4 for x in ADJ)
assert all((ADJ[u]&ADJ[v])==0 for u,v in EDGES)  # triangle-free

def valid_by_degree(mask):
    return all((mask&ADJ[u]).bit_count()<=1 for u in range(N) if mask>>u&1)

# Completely different predicate: avoid every three-vertex path in the induced graph.
BAD_TRIPLES = {
    (1<<u)|(1<<v)|(1<<w)
    for v in range(N)
    for u,w in itertools.combinations([x for x in range(N) if ADJ[v]>>x&1],2)
}
assert len(BAD_TRIPLES)>0

def valid_by_forbidden_triple(mask):
    return not any(mask&T==T for T in BAD_TRIPLES)

FACES={x for x in range(1,1<<N) if valid_by_degree(x)}
assert FACES=={x for x in range(1,1<<N) if valid_by_forbidden_triple(x)}
FV=collections.Counter(x.bit_count() for x in FACES)
assert [FV[i] for i in range(1,7)]==[12,66,148,142,52,4]
assert len(FACES)==424
assert sum((-1)**(i-1)*FV[i] for i in FV)==0

# All element-matchings in descending vertex order, with empty face excluded.
# The resulting acyclic matching is checked AGAIN by a full directed Hasse census.
UNPAIRED=set(FACES)
PAIRS=[]
for i in range(N-1,-1,-1):
    bit=1<<i
    for lo in sorted(tuple(UNPAIRED), key=lambda x:(x.bit_count(),x)):
        hi=lo|bit
        if lo in UNPAIRED and lo&bit==0 and hi in UNPAIRED:
            UNPAIRED.remove(lo)
            UNPAIRED.remove(hi)
            PAIRS.append((lo,hi))
assert len(PAIRS)==211
assert sorted(UNPAIRED)==[232,2048]
assert {x.bit_count() for x in UNPAIRED}=={1,4}
assert all(hi.bit_count()==lo.bit_count()+1 and hi&lo==lo for lo,hi in PAIRS)
certificate=json.loads(Path(__file__).with_name('MORSE_PAIRS.json').read_text(encoding='utf-8'))
assert certificate['pairs']==[list(p) for p in PAIRS]
assert certificate['critical_faces']==[232,2048]

UP={lo:hi for lo,hi in PAIRS}
indegree={f:0 for f in FACES}
successors={f:[] for f in FACES}
incidences=0
for hi in FACES:
    for i in range(N):
        if hi>>i&1:
            lo=hi^(1<<i)
            if lo in FACES:
                incidences+=1
                if UP.get(lo)==hi: src,dst=lo,hi
                else: src,dst=hi,lo
                successors[src].append(dst)
                indegree[dst]+=1
Q=collections.deque([f for f in FACES if indegree[f]==0]);visited=0
while Q:
    f=Q.popleft();visited+=1
    for target in successors[f]:
        indegree[target]-=1
        if indegree[target]==0:Q.append(target)
assert visited==len(FACES)

# Independent ordinary simplicial boundary calculation over two characteristics.
by_size={k:sorted(f for f in FACES if f.bit_count()==k) for k in range(1,7)}
def rank_mod_p(size,p):
    if size==1:return 0
    rows=by_size[size-1]
    rowid={f:i for i,f in enumerate(rows)}
    pivots={}
    for hi in by_size[size]:
        v={}
        verts=[i for i in range(N) if hi>>i&1]
        for j,i in enumerate(verts):
            row=rowid[hi^(1<<i)]
            v[row]=(1 if j%2==0 else p-1)
        while v:
            k=min(v)
            if k not in pivots:
                inv=pow(v[k],-1,p)
                pivots[k]={i:(x*inv)%p for i,x in v.items()}
                break
            factor=v[k]
            for j,val in pivots[k].items():
                x=(v.get(j,0)-factor*val)%p
                if x:v[j]=x
                else:v.pop(j,None)
    return len(pivots)
rank_results={p:[rank_mod_p(k,p) for k in range(2,7)] for p in (2,3,5)}
for p,ranks in rank_results.items():
    betti=[FV[i+1]-(ranks[i-1] if i else 0)-(ranks[i] if i<len(ranks) else 0) for i in range(6)]
    assert betti==[1,0,0,1,0,0],(p,ranks,betti)

# Enumerate all automorphisms through exact adjacency/nonadjacency backtracking.
# No third-party graph package or assumed group order is involved.
ALL_AUT=[]
def enumerate_aut(mapping,unused):
    i=len(mapping)
    if i==N:
        ALL_AUT.append(tuple(mapping));return
    for j in range(N):
        if unused>>j&1 and all(bool(ADJ[i]>>k&1)==bool(ADJ[j]>>mapping[k]&1) for k in range(i)):
            mapping.append(j)
            enumerate_aut(mapping,unused^(1<<j))
            mapping.pop()
enumerate_aut([], (1<<N)-1)
assert len(ALL_AUT)==8 and len(set(ALL_AUT))==8
r=(1,5,11,6,0,4,7,10,9,2,3,8)
s=(0,4,3,2,1,5,9,8,7,6,11,10)
identity=tuple(range(N))
def comp(g,h):return tuple(g[h[i]] for i in range(N))
def pow_perm(g,k):
    ans=identity
    for _ in range(k):ans=comp(ans,g)
    return ans
assert pow_perm(r,4)==identity and pow_perm(s,2)==identity
assert comp(comp(s,r),s)==pow_perm(r,3)
all_expressions={(a,b):comp(pow_perm(r,a),pow_perm(s,b)) for a in range(4) for b in range(2)}
assert set(all_expressions.values())==set(ALL_AUT)

def orientation(images):
    inversions=sum(1 for i in range(len(images)) for j in range(i+1,len(images)) if images[i]>images[j])
    return -1 if inversions&1 else +1

def ordinary_lefschetz(g,face_set):
    value=0
    for face in face_set:
        vertices=[i for i in range(N) if face>>i&1]
        images=[g[i] for i in vertices]
        if set(images)==set(vertices):
            value+= (-1 if len(vertices)%2==0 else 1)*orientation(images)
    return value

# For X ≃ S^3, L(g)=1-tr(g|H3). On the pre-existing ordinary
# independence sphere S^2, L(g)=1+tr(g|H2).
IND1={f for f in range(1,1<<N) if all((f&ADJ[u])==0 for u in range(N) if f>>u&1)}
characters=[]
for (a,b),g in sorted(all_expressions.items()):
    new_degree=1-ordinary_lefschetz(g,FACES)
    old_degree=ordinary_lefschetz(g,IND1)-1
    assert new_degree==(-1)**a,(a,b,new_degree)
    assert old_degree==(-1)**(a+b),(a,b,old_degree)
    characters.append((a,b,new_degree,old_degree))
assert [t[2] for t in characters].count(1)==4

print('VERTICES',N,'EDGES',len(EDGES),'FORBIDDEN_TRIPLES',len(BAD_TRIPLES))
print('FACES',len(FACES),'FV',tuple(FV[i] for i in range(1,7)))
print('MATCHED_PAIRS',len(PAIRS),'DIRECTED_INCIDENCES',incidences,'ACYCLIC_VISITS',visited)
print('CRITICAL_MASKS',tuple(sorted(UNPAIRED)))
print('MODULAR_BOUNDARY_RANKS',rank_results)
print('AUTOMORPHISMS',len(ALL_AUT),'CHARACTERS',characters)
print('ALL_CHECKS_PASS')
