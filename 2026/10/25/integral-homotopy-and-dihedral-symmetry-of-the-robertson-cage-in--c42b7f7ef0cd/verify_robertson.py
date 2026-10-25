#!/usr/bin/env python3
"""Exact finite certificate for Robertson cage independence-complex homology."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import networkx as nx

# Vertices 0,...,18. The graph is the unique 19-vertex 4-regular girth-5 graph.
FIRST_TEN = {
 0:(1,2,3,4), 1:(0,7,8,9), 2:(0,11,13,15),
 3:(0,10,17,18), 4:(0,12,14,16),
 5:(6,13,16,18), 6:(5,14,15,17),
 7:(1,12,13,17), 8:(1,10,15,16), 9:(1,11,14,18)
}
LAST_SIX = [(10,13),(10,14),(11,16),(11,17),(12,15),(12,18)]
G=nx.Graph();G.add_nodes_from(range(19))
G.add_edges_from((v,w) for v,ns in FIRST_TEN.items() for w in ns)
G.add_edges_from(LAST_SIX)
assert (G.number_of_nodes(),G.number_of_edges()) == (19,38)
assert all(d==4 for _,d in G.degree())
assert min(len(c) for c in nx.cycle_basis(G))==5
shortest_cycles=[]
for a,b in list(G.edges()):
    H=G.copy();H.remove_edge(a,b)
    shortest_cycles.append(nx.shortest_path_length(H,a,b)+1)
assert min(shortest_cycles)==5  # True girth, not just minimum fundamental-cycle length.
assert nx.diameter(G)==3
adj=[sum(1<<j for j in G.neighbors(i)) for i in range(19)]

faces=[0]
for v in range(19):
    faces += [f|(1<<v) for f in faces if not(f&adj[v])]
faces_set=set(faces[1:])
fvec=tuple(Counter(f.bit_count()-1 for f in faces[1:])[d] for d in range(7))
assert (len(faces_set),fvec)==(1949,(19,133,437,703,516,137,4))

# Independent full-boundary mod-two rank computation (separate from Morse).
by_dimension={d:sorted(f for f in faces_set if f.bit_count()-1==d) for d in range(7)}
mod2_ranks={0:0}
for d in range(1,7):
    index={f:i for i,f in enumerate(by_dimension[d-1])}
    pivots={}
    for face in by_dimension[d]:
        col=sum(1<<index[face^(1<<v)] for v in range(19) if face>>v&1)
        while col:
            leading=col.bit_length()-1
            if leading in pivots:col ^= pivots[leading]
            else:pivots[leading]=col;break
    mod2_ranks[d]=len(pivots)
assert [mod2_ranks[d] for d in range(7)]==[0,18,115,322,380,133,4]
assert [len(by_dimension[d])-mod2_ranks[d]-mod2_ranks.get(d+1,0)
        -(1 if d==0 else 0) for d in range(7)]==[0,0,0,1,3,0,0]

# Lexicographic vertex-toggle matching (the empty simplex is omitted).
remaining=set(faces_set);pairs=[]
for v in range(19):
    for f in sorted((f for f in remaining if not (f>>v)&1),
                    key=lambda z:(z.bit_count(),z)):
        h=f|(1<<v)
        if h in remaining:
            remaining.remove(f);remaining.remove(h);pairs.append((f,h))
critical=remaining
assert len(pairs)==970
assert Counter(f.bit_count()-1 for f in critical)=={0:1,3:3,4:5}

# Full oriented Hasse graph. Matched covers run upward; others downward.
up={f:g for f,g in pairs};down={g:f for f,g in pairs}
vertices=faces_set
indeg={f:0 for f in vertices}
outs={f:[] for f in vertices}
def boundary(face):
    return [(face^(1<<v),(-1)**i) for i,v in
            enumerate(j for j in range(19) if face>>j&1)]
cover_count=0
for high in vertices:
    for low,co in boundary(high):
        if not low:continue
        cover_count+=1
        a,b=(low,high) if up.get(low)==high else (high,low)
        outs[a].append(b);indeg[b]+=1
q=deque(f for f in vertices if indeg[f]==0)
visited=0
while q:
    x=q.popleft();visited+=1
    for y in outs[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert visited==len(vertices)

# Exact Morse differential, computed by eliminating all matched (3,4) pairs.
@lru_cache(None)
def project_three(f):
    if f in critical:return {f:1}
    if f in down:return {}
    h=up[f];pivot=dict(boundary(h))[f]
    result=defaultdict(int)
    for other,c in boundary(h):
        if other==f:continue
        for t,v in project_three(other).items():
            result[t]-=c*v*pivot
    return {t:v for t,v in result.items() if v}
crit3=sorted(f for f in critical if f.bit_count()==4)
crit4=sorted(f for f in critical if f.bit_count()==5)
morse=[]
for f in crit4:
    z=defaultdict(int)
    for h,a in boundary(f):
        for t,v in project_three(h).items():z[t]+=a*v
    morse.append([z[t] for t in crit3])
assert crit3==[2248,4420,82052]
assert crit4==[3280,5700,6472,172560,368642]
assert morse==[[-1,0,0],[0,-1,0],[1,-1,0],[0,0,0],[0,0,0]]
# Thus two unit cancellations give H_3 = Z and H_4 = Z^3.

# Produce an actual simplicial 3-cycle representing the remaining generator.
low2=sorted(f for f in up if f.bit_count()==3 and up[f].bit_count()==4)
low2_set=set(low2)
depend={f:{h for h,_ in boundary(up[f]) if h!=f and h in low2_set} for f in low2}
in2={f:0 for f in low2}
for f in low2:
    for h in depend[f]:in2[h]+=1
q=deque(sorted(f for f in low2 if in2[f]==0));schedule=[]
while q:
    f=q.popleft();schedule.append(f)
    for h in sorted(depend[f]):
        in2[h]-=1
        if not in2[h]:q.append(h)
assert len(schedule)==len(low2)
cycle=defaultdict(int,{crit3[2]:1});bd=defaultdict(int)
for f,c in boundary(crit3[2]):bd[f]+=c
for lower in schedule:
    if bd[lower]:
        upper=up[lower];pivot=dict(boundary(upper))[lower]
        mult=-bd[lower]*pivot
        cycle[upper]+=mult
        for f,c in boundary(upper):bd[f]+=mult*c
cycle={f:c for f,c in cycle.items() if c}
assert all(c==0 for c in bd.values())
assert len(cycle)==25 and sum(abs(x) for x in cycle.values())==25

def compose(a,b):return tuple(a[b[i]] for i in range(19))
identity=tuple(range(19))
def perm_power(a,k):
    result=identity
    for _ in range(k):result=compose(a,result)
    return result
def inverse(a):return tuple(a.index(i) for i in range(19))
def perm_order(a):
    t=identity
    for k in range(1,25):
        t=compose(a,t)
        if t==identity:return k
    raise AssertionError('bad order')
def sign_image(face,perm):
    mapped=[perm[i] for i in range(19) if face>>i&1]
    sign=(-1)**sum(mapped[i]>mapped[j] for i in range(len(mapped))
                   for j in range(i+1,len(mapped)))
    return sum(1<<i for i in mapped),sign

perms={tuple(a[i] for i in range(19)) for a in
       nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()}
assert len(perms)==24
rot=min(a for a in perms if perm_order(a)==12)
ref=min(a for a in perms if perm_order(a)==2 and
        compose(compose(a,rot),a)==inverse(rot))
assert rot==(5,6,13,18,16,1,0,17,15,14,12,10,11,7,4,2,8,3,9)
assert ref==(0,1,2,4,3,6,5,8,7,9,12,11,10,15,18,13,17,16,14)

def top_three_action(a):
    image=defaultdict(int)
    for f,c in cycle.items():
        h,sg=sign_image(f,a)
        for t,m in project_three(h).items():image[t]+=c*sg*m
    return image[crit3[2]]
def reduced_lefschetz(a):
    trace=-1
    for f in faces_set:
        h,sg=sign_image(f,a)
        if h==f:trace+=(-1)**(f.bit_count()-1)*sg
    return trace
results={}
for b in (0,1):
    for k in range(12):
        a=compose(ref if b else identity,perm_power(rot,k))
        assert a in perms
        h3=top_three_action(a)
        h4=reduced_lefschetz(a)+h3
        assert h3==(-1)**(k+b), (k,b,h3)
        assert h4==1+2*((-1)**k),(k,b,h4)
        results[a]=(h3,h4)
assert len(results)==24

# Recover the full integral action in degree four, rather than just its character.
@lru_cache(None)
def project_four(f):
    if f in critical:return {f:1}
    if f in down:return {}
    upper=up[f];pivot=dict(boundary(upper))[f]
    result=defaultdict(int)
    for other,c in boundary(upper):
        if other==f:continue
        for t,v in project_four(other).items():result[t]-=c*v*pivot
    return {t:v for t,v in result.items() if v}

low3=sorted(f for f in up if f.bit_count()==4 and up[f].bit_count()==5)
low3_set=set(low3)
deps3={f:{h for h,_ in boundary(up[f]) if h!=f and h in low3_set} for f in low3}
in3={f:0 for f in low3}
for f in low3:
    for h in deps3[f]:in3[h]+=1
q=deque(sorted(f for f in low3 if in3[f]==0));schedule3=[]
while q:
    f=q.popleft();schedule3.append(f)
    for h in sorted(deps3[f]):
        in3[h]-=1
        if not in3[h]:q.append(h)
assert len(schedule3)==len(low3)

def lift_four(morse_chain):
    chain=defaultdict(int,morse_chain);bd=defaultdict(int)
    for f,v in morse_chain.items():
        for h,c in boundary(f):bd[h]+=v*c
    for low in schedule3:
        if bd[low]:
            upper=up[low];pivot=dict(boundary(upper))[low]
            mult=-bd[low]*pivot
            chain[upper]+=mult
            for h,c in boundary(upper):bd[h]+=mult*c
    assert all(x==0 for x in bd.values())
    return {f:v for f,v in chain.items() if v}

basis4=[{crit4[0]:1,crit4[1]:-1,crit4[2]:1},
        {crit4[3]:1},{crit4[4]:1}]
cycles4=[lift_four(f) for f in basis4]
assert tuple(len(z) for z in cycles4)==(56,98,56)

def h4_matrix(a):
    columns=[]
    for z in cycles4:
        coeff=defaultdict(int)
        for f,v in z.items():
            h,sg=sign_image(f,a)
            for t,c in project_four(h).items():coeff[t]+=v*sg*c
        assert coeff[crit4[0]]==coeff[crit4[2]]
        assert coeff[crit4[1]]==-coeff[crit4[2]]
        columns.append((coeff[crit4[2]],coeff[crit4[3]],coeff[crit4[4]]))
    return tuple(tuple(columns[j][i] for j in range(3)) for i in range(3))

rotation_matrix=h4_matrix(rot)
reflection_matrix=h4_matrix(ref)
assert rotation_matrix==((0,0,1),(0,-1,0),(1,0,0))
assert reflection_matrix==((1,0,0),(0,1,0),(0,0,1))
# The first and third basis vectors exchange; the middle one changes sign.
# Thus H4 is Z[C2] direct sum the negative 1-dimensional lattice.
print('H4_INTEGRAL_ROTATION_MATRIX',rotation_matrix)
print('H4_INTEGRAL_REFLECTION_MATRIX',reflection_matrix)
print('H4_INTEGRAL_MODULE_REGULAR_PLUS_SIGN_INDEX_TWO_EIGENLATTICES')
print('VERIFY_OK_ROBERTSON_INDEPENDENCE_MIXED_WEDGE_INTEGRAL_DIHEDRAL')
print('GRAPH_VERTICES_EDGES_AUTOMORPHISMS',19,38,len(perms))
print('F_VECTOR',fvec,'NONEMPTY_FACES',len(faces_set))
print('DIRECT_MOD2_BOUNDARY_RANKS',mod2_ranks)
print('HASSE_COVERS_ACYCLIC_VISITED',cover_count,visited)
print('MORSE_MATCHING_PAIRS',len(pairs),'CRITICAL_DIMS',dict(Counter(f.bit_count()-1 for f in critical)))
print('CRITICAL_THREE',crit3,'CRITICAL_FOUR',crit4)
print('MORSE_BOUNDARY_FOUR_TO_THREE',morse)
print('SIMPICIAL_THREE_GENERATOR_TERMS',len(cycle),'INTEGRAL_GENERATOR',1)
print('WEDGE_S3_PLUS_THREE_S4')
print('D12_ROTATION_TRACES_H3',tuple(results[perm_power(rot,k)][0] for k in range(12)))
print('D12_ROTATION_TRACES_H4',tuple(results[perm_power(rot,k)][1] for k in range(12)))
print('D12_REFLECTION_TRACES_H3',tuple(results[compose(ref,perm_power(rot,k))][0] for k in range(12)))
print('D12_REFLECTION_TRACES_H4',tuple(results[compose(ref,perm_power(rot,k))][1] for k in range(12)))
