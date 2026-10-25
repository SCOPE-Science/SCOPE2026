#!/usr/bin/env python3
"""Standalone exact finite verification for Petersen odd-cycle/forest complexes."""
import itertools
from collections import Counter, deque

V=list(itertools.combinations(range(5),2))
E=[(i,j) for i,a in enumerate(V) for j,b in enumerate(V) if i<j and not(set(a)&set(b))]
assert len(V)==10 and len(E)==15
ADJ=[[] for _ in V]
for a,b in E:ADJ[a].append(b);ADJ[b].append(a)
assert sorted(map(len,ADJ))==[3]*10

def bipartite(mask):
    col={}
    for v in range(10):
        if not (mask>>v&1) or v in col:continue
        col[v]=0;todo=[v]
        for u in todo:
            for w in ADJ[u]:
                if not mask>>w&1:continue
                if w in col:
                    if col[w]==col[u]:return False
                else:
                    col[w]=1-col[u];todo.append(w)
    return True

def forest_uf(mask):
    parent=list(range(10))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for a,b in E:
        if mask>>a&1 and mask>>b&1:
            r,s=root(a),root(b)
            if r==s:return False
            parent[r]=s
    return True

def forest_rank(mask):
    unseen={i for i in range(10) if mask>>i&1}
    comp=0
    while unseen:
        comp+=1;v=next(iter(unseen));unseen.remove(v);todo=[v]
        for a in todo:
            for b in ADJ[a]:
                if b in unseen:unseen.remove(b);todo.append(b)
    edge_count=sum(bool(mask>>a&1 and mask>>b&1) for a,b in E)
    return edge_count==mask.bit_count()-comp

B={x for x in range(1024) if bipartite(x)}
F={x for x in range(1024) if forest_uf(x)}
assert all(forest_uf(x)==forest_rank(x) for x in range(1024))
assert F<=B
assert (len(B),len(F))==(806,786)
assert [sum(x.bit_count()==j for x in B) for j in range(8)]==[1,10,45,120,210,240,150,30]
assert [sum(x.bit_count()==j for x in F) for j in range(8)]==[1,10,45,120,210,240,140,20]

odd_min=[x for x in range(1,1024) if x not in B and all(((x^(1<<i)) in B) for i in range(10) if x>>i&1)]
assert len(odd_min)==12 and all(x.bit_count()==5 for x in odd_min)
assert all(any(x&f==f for f in odd_min)==(x not in B) for x in range(1024))

extra=B-F
low=sorted(x for x in extra if x.bit_count()==6)
high=sorted(x for x in extra if x.bit_count()==7)
assert len(extra)==20 and len(low)==len(high)==10
pairs=[]
for x in low:
    # Each six-set forms a chordless induced hexagon.
    assert all(sum(bool((x>>w)&1) for w in ADJ[v])==2 for v in range(10) if x>>v&1)
    successors=[z for z in B if x!=z and x&z==x]
    assert len(successors)==1 and successors[0] in high
    pairs.append((x,successors[0]))
assert len({b for _,b in pairs})==10
assert set(sum(([a,b] for a,b in pairs),[]))==extra
remaining=set(B)
for a,b in pairs:
    assert a in remaining and b in remaining
    assert [z for z in remaining if z!=a and z&a==a]==[b]
    remaining.remove(a);remaining.remove(b)
assert remaining==F

# A deterministic combinatorial discrete-Morse reduction of the forest complex.
active=set(F-{0})
sub={b:set() for b in active}
co={a:set() for a in active}
for b in active:
    q=b
    while q:
        t=q&-q;q-=t;a=b^t
        if a in active:sub[b].add(a);co[a].add(b)
matching=[];critical=[]
while active:
    choices=[a for a in active if len(co[a])==1]
    if choices:
        a=max(choices,key=lambda x:(x.bit_count(),-x))
        b=next(iter(co[a]));matching.append((a,b));removed=(a,b)
    else:
        tops=[x for x in active if not co[x]]
        b=max(tops,key=lambda x:(x.bit_count(),-x))
        critical.append(b);removed=(b,)
    for b in removed:
        active.remove(b)
        for a in sub[b]:co[a].remove(b)
assert len(matching)==389 and len(critical)==7
assert Counter(x.bit_count()-1 for x in critical)=={0:1,5:6}

# Check acyclicity of the full oriented face-incidence Hasse graph.
matched=set(matching)
faces=set(F)-{0}
indeg={x:0 for x in faces};out={x:[] for x in faces}
incidences=0
for b in faces:
    q=b
    while q:
        t=q&-q;q-=t;a=b^t
        if a not in faces:continue
        incidences+=1
        u,v=(a,b) if (a,b) in matched else (b,a)
        out[u].append(v);indeg[v]+=1
queue=deque(x for x in faces if indeg[x]==0)
seen=0
while queue:
    u=queue.popleft();seen+=1
    for v in out[u]:
        indeg[v]-=1
        if indeg[v]==0:queue.append(v)
assert seen==len(faces)

# Full S_5 symmetry and exact oriented Lefschetz character.
label={p:i for i,p in enumerate(V)}
traces=[];orders=Counter();pair_permutation_checks=0
for perm in itertools.permutations(range(5)):
    p=[label[tuple(sorted((perm[a],perm[b])))] for a,b in V]
    assert all((j in ADJ[i])==(p[j] in ADJ[p[i]]) for i in range(10) for j in range(10))
    def image(mask):
        return sum(1<<p[i] for i in range(10) if mask>>i&1)
    # The ten free pairs form a single invariant matching.
    assert {(image(a),image(b)) for a,b in pairs}==set(pairs)
    pair_permutation_checks+=1
    fixed_chain_trace=0
    for s in B-{0}:
        if image(s)!=s:continue
        sequence=[p[i] for i in range(10) if s>>i&1]
        inversions=sum(sequence[i]>sequence[j] for i in range(len(sequence)) for j in range(i+1,len(sequence)))
        fixed_chain_trace+=(-1)**(s.bit_count()-1+inversions)
    top_character=1-fixed_chain_trace
    fp=sum(perm[i]==i for i in range(5))
    fp2=sum(perm[perm[i]]==i for i in range(5))
    predicted=((fp-1)**2-(fp2-1))//2
    assert top_character==predicted
    traces.append(top_character)
assert len(traces)==120 and sum(x*x for x in traces)==120 and sum(traces)==0
print('VERTICES 10 EDGES 15')
print('MINIMAL_ODD_CYCLE_NONFACES 12 ALL_PENTAGONS')
print('BIPARTITE_F_VECTOR',*[sum(x.bit_count()==j for x in B) for j in range(1,8)])
print('FOREST_F_VECTOR',*[sum(x.bit_count()==j for x in F) for j in range(1,8)])
print('BIPARTITE_EXCESS 10_HEXAGONS_PLUS_10_SEVEN_SETS')
print('SIMPLICIAL_COLLAPSES 10 CHECKED_UNIQUE_FREE_COFACES')
print('FOREST_MORSE 389_PAIRS 1_CRITICAL_VERTEX 6_CRITICAL_5_CELLS')
print('MORSE_HASSE_ACYCLIC',incidences,'INCIDENCES')
print('S5_AUTOMORPHISMS',pair_permutation_checks)
print('S5_FIFTH_HOMOLOGY_CHARACTER_DISTRIBUTION',sorted(Counter(traces).items()))
print('CHARACTER_NORM_SQUARED 120 CHARACTER_SUM 0')
print('VERIFY_OK')
