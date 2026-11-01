#!/usr/bin/env python3
"""Finite exact integral Morse certificate for the two-independence complex
of the truncated tetrahedral graph. Python standard library only.
"""
from collections import Counter, deque, defaultdict
from functools import lru_cache

# Vertices are directed half-edges (a,b), a != b, of the tetrahedral K4.
# Each truncation-triangle connects half-edges with a common tail a;
# an original tetrahedron edge connects the reversed pair (a,b),(b,a).
vertices=[(a,b) for a in range(4) for b in range(4) if a!=b]
assert len(vertices)==12
n=len(vertices)
edges={(i,j) for i in range(n) for j in range(i+1,n)
       if (vertices[i][0]==vertices[j][0]
           or vertices[i]==vertices[j][::-1])}
assert len(edges)==18
neighbors=[0]*n
for a,b in edges:
    neighbors[a]|=1<<b
    neighbors[b]|=1<<a
assert all(mask.bit_count()==3 for mask in neighbors)
assert len({vertices[i][0] for i in range(n)})==4

# For an induced graph, all components have size <=2 iff its max degree <=1.
faces={f for f in range(1<<n) if all((neighbors[i]&f).bit_count()<=1
                                     for i in range(n) if f&(1<<i))}
assert len(faces)==864
face_counts=Counter(f.bit_count()-1 for f in faces if f)
assert dict(sorted(face_counts.items()))=={0:12,1:66,2:192,3:303,4:228,5:62}
facets={f for f in faces if all((f|(1<<i)) not in faces for i in range(n)
                                 if not f&(1<<i))}
facet_counts=Counter(f.bit_count()-1 for f in facets)
assert dict(sorted(facet_counts.items()))=={3:3,5:62}

# Acyclic successive element-toggle matching, on augmented faces first.
order=(7,4,1,3,8,5,9,11,6,0,10,2)
unpaired=set(faces)
pairs=[]
for v in order:
    for lower in sorted(unpaired):
        if (lower>>v)&1: continue
        upper=lower|(1<<v)
        if upper in unpaired:
            unpaired.remove(lower)
            unpaired.remove(upper)
            pairs.append((lower,upper))
assert len(pairs)==429
assert 0 not in unpaired
crit3=sorted(f for f in unpaired if f.bit_count()==4)
crit4=sorted(f for f in unpaired if f.bit_count()==5)
assert crit3==[540,1122,2313]
assert crit4==[2101,2164,3153]
assert len(unpaired)==6
nonempty_pairs={(lo,hi) for lo,hi in pairs if lo}
assert len(nonempty_pairs)==428
nonempty_faces=faces-{0}
critical=nonempty_faces-{f for p in nonempty_pairs for f in p}
assert Counter(f.bit_count()-1 for f in critical)=={0:1,3:3,4:3}

# Forman acyclicity: direct all Hasse covers down, reverse matched covers.
adj={f:[] for f in nonempty_faces}
indeg={f:0 for f in nonempty_faces}
hasse_count=0
for upper in nonempty_faces:
    for v in range(n):
        if (upper>>v)&1:
            lower=upper^(1<<v)
            if lower==0: continue
            hasse_count+=1
            a,b=(lower,upper) if (lower,upper) in nonempty_pairs else (upper,lower)
            adj[a].append(b)
            indeg[b]+=1
q=deque(f for f in nonempty_faces if indeg[f]==0)
visited=0
while q:
    f=q.popleft()
    visited+=1
    for g in adj[f]:
        indeg[g]-=1
        if indeg[g]==0:q.append(g)
assert visited==len(nonempty_faces)

# Exact signed gradient path expansion of dimension-3 faces in critical basis.
# Matched lower a with upper b: 0 = boundary b = eps*a + remaining,
# hence replace a by -eps*remaining, recursively in the DAG.
lo_to_hi=dict(pairs)
hi_to_lo={hi:lo for lo,hi in pairs}
@lru_cache(None)
def project(f):
    if f in unpaired:return {f:1}
    if f in hi_to_lo:return {}
    upper=lo_to_hi[f]
    verts=[i for i in range(n) if upper&(1<<i)]
    change=(upper^f).bit_length()-1
    pivot=(-1)**verts.index(change)
    result=Counter()
    for i,v in enumerate(verts):
        smaller=upper^(1<<v)
        if smaller==f:continue
        for cell,coeff in project(smaller).items():
            result[cell]-=pivot*((-1)**i)*coeff
    return {cell:coeff for cell,coeff in result.items() if coeff}

matrix=[]
for upper in crit4:
    reduced=Counter()
    for i,v in enumerate(j for j in range(n) if upper&(1<<j)):
        face=upper^(1<<v)
        for c,coefficient in project(face).items():
            reduced[c]+=((-1)**i)*coefficient
    assert not any(c not in crit3 and coeff for c,coeff in reduced.items())
    matrix.append([reduced[c] for c in crit3])
assert matrix==[[0,0,0]]*3

# Independent exact finite-field rank reconstruction from all simplicial faces.
dims=defaultdict(list)
for f in sorted(faces):dims[f.bit_count()-1].append(f)
ranks={}
for d in range(1,max(dims)+1):
    rowpos={f:i for i,f in enumerate(dims[d-1])}
    pivots={}
    for c in dims[d]:
        boundary=0
        for i in range(n):
            if (c>>i)&1:
                boundary ^=1<<rowpos[c^(1<<i)]
        while boundary:
            lead=boundary.bit_length()-1
            if lead in pivots:boundary ^=pivots[lead]
            else:pivots[lead]=boundary;break
    ranks[d]=len(pivots)
assert [ranks[d] for d in range(1,6)]==[11,55,137,163,62]
betti={d:len(dims[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
       for d in range(6)}
assert {d:b for d,b in betti.items() if b}=={3:3,4:3}

print('TRUNCATED_TETRAHEDRON_IND2_INTEGRAL_MORSE_OK')
print('vertices',n,'edges',len(edges),'augmented_faces',len(faces))
print('f-vector',dict(sorted(face_counts.items())))
print('facet_dimensions',dict(sorted(facet_counts.items())))
print('element_toggle_order',list(order))
print('ordinary_acyclic_pairs',len(nonempty_pairs),'hasse_incidence_count',hasse_count,'DAG_vertices',visited)
print('critical_cells_by_dimension',dict(sorted(Counter(f.bit_count()-1 for f in critical).items())))
print('critical_dimension_three_face_bitmasks',crit3)
print('critical_dimension_four_face_bitmasks',crit4)
print('signed_integral_Morse_boundary_4_to_3',matrix)
print('independent_mod_two_boundary_ranks',ranks)
print('independent_reduced_mod_two_betti',betti)
