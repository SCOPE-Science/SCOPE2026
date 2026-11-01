#!/usr/bin/env python3
"""Self-contained exact finite verification for the hexagonal prism matching complex."""
from collections import Counter, deque
from functools import lru_cache
from itertools import product

n = 6
edges = tuple([(layer*n+j, layer*n+(j+1)%n)
               for layer in range(2) for j in range(n)]
              +[(j,n+j) for j in range(n)])
assert len(edges)==18 and len(set(map(frozenset,edges)))==18
V = tuple((1<<u)|(1<<v) for u,v in edges)

# Direct enumeration from the definition of a matching.
faces = set()
def enumerate_faces(j, occupied, mask):
    if j == len(edges):
        faces.add(mask)
    else:
        enumerate_faces(j+1, occupied, mask)
        if not occupied & V[j]:
            enumerate_faces(j+1, occupied|V[j], mask | (1<<j))
enumerate_faces(0,0,0)
assert len(faces)==1104
face_vector=tuple(sum(x.bit_count()==k for x in faces) for k in range(1,7))
assert face_vector==(18,117,336,420,192,20)

# Maximal graph matchings distinguish this ordinary complex from the
# subcomplex generated only by perfect matchings.
facets=Counter()
for mask in faces:
    if not any((mask | (1<<j)) in faces for j in range(18) if not mask & (1<<j)):
        facets[mask.bit_count()]+=1
assert dict(facets)=={4:6,5:72,6:20}

# Independent vertex-deletion recurrence for the matching polynomial.
neighbors=[0]*12
for u,v in edges:
    neighbors[u] |=1<<v
    neighbors[v] |=1<<u
@lru_cache(None)
def mp(vertices):
    if vertices==0:return (1,)
    v=(vertices&-vertices).bit_length()-1
    remaining=vertices&~(1<<v)
    a=list(mp(remaining))
    candidates=neighbors[v]&remaining
    while candidates:
        wbit=candidates&-candidates; candidates-=wbit
        b=mp(remaining&~wbit)
        if len(a)<len(b)+1:a += [0]*(len(b)+1-len(a))
        for k,val in enumerate(b):a[k+1]+=val
    return tuple(a)
poly=mp((1<<12)-1)
assert poly==(1,)+face_vector

# Deterministic sequential coordinate-toggle Morse matching, initially
# on the augmented face poset including the empty simplex.
remaining=set(faces)
matching={};pairs=[]
for j in range(len(edges)):
    bit=1<<j
    low=tuple(x for x in remaining if not x&bit and (x|bit) in remaining)
    for x in low:
        y=x|bit
        assert x in remaining and y in remaining
        remaining.remove(x);remaining.remove(y)
        matching[x]=y; matching[y]=x
        pairs.append((x,y))
assert (0,1) in pairs
assert len(pairs)==546
assert len(remaining)==12 and set(x.bit_count()-1 for x in remaining)=={3}
critical_fourfaces=tuple(sorted(remaining))

# Remove only the augmented pair (empty simplex, first edge), leaving
# the 0-cell {first edge} critical for the ordinary CW Morse complex.
matching.pop(0);matching.pop(1)
actual_faces=faces-{0}
critical={x for x in actual_faces if x not in matching}
assert len(critical)==13
assert Counter(x.bit_count()-1 for x in critical)=={0:1, 3:12}
assert len(matching)//2==545

# Check every nonempty codimension-one incidence and the complete
# orientation of the Hasse diagram: matched incidences point upwards,
# all other ones downwards. A full Kahn topological sort proves DAG.
indeg={x:0 for x in actual_faces}
out={x:[] for x in actual_faces}
incidences=0
for upper in actual_faces:
    bits=upper
    while bits:
        bit=bits&-bits;bits-=bit
        lower=upper^bit
        if not lower:continue
        assert lower in actual_faces
        incidences+=1
        if matching.get(lower)==upper:
            a,b=lower,upper
        else:
            a,b=upper,lower
        out[a].append(b);indeg[b]+=1
queue=deque(x for x,d in indeg.items() if d==0)
visited=0
while queue:
    x=queue.popleft();visited+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:queue.append(y)
assert visited==len(actual_faces)

# Independent GF(2) boundary-matrix elimination on the *original* complex.
by_size={k:sorted(s for s in actual_faces if s.bit_count()==k) for k in range(1,7)}
ranks={1:0,7:0}
for k in range(2,7):
    rowidx={s:i for i,s in enumerate(by_size[k-1])}
    pivots={}
    for upper in by_size[k]:
        column=0
        bits=upper
        while bits:
            bit=bits&-bits;bits-=bit
            column ^= 1<<rowidx[upper^bit]
        while column:
            h=column.bit_length()-1
            if h not in pivots:
                pivots[h]=column
                break
            column ^=pivots[h]
    ranks[k]=len(pivots)
bettis={k-1:len(by_size[k])-ranks[k]-ranks[k+1] for k in range(1,7)}
bettis[0]-=1  # reduced H_0
assert bettis=={0:0,1:0,2:0,3:12,4:0,5:0}

# Full dihedral by layer-exchange action on graph vertices and edges.
edge_index={frozenset(e):j for j,e in enumerate(edges)}
def graph_perm(a,b,c):
    return lambda x: ((x//n)^c)*n + (a+(-1 if b else 1)*(x%n))%n
def edge_perm(a,b,c):
    p=graph_perm(a,b,c)
    return tuple(edge_index[frozenset((p(u),p(v)))] for u,v in edges)
def sign_perm(vals):
    return -1 if sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))%2 else 1
chars={}
for a,b,c in product(range(n),range(2),range(2)):
    perm=edge_perm(a,b,c)
    assert set(perm)==set(range(18))
    trace=0
    for mask in faces:
        ids=[j for j in range(18) if (mask>>j)&1]
        im=[perm[j] for j in ids]
        if set(ids)==set(im):
            trace+=(-1)**len(ids)*sign_perm(im)
    chars[a,b,c]=trace
assert len(chars)==24
expected={
    (0,0):(12,0,0,6,0,0),
    (0,1):(-2,-2,-2,4,-2,-2),
    (1,0):(0,-2,0,-2,0,-2),
    (1,1):(2,4,2,4,2,4)
}
for b,c in product(range(2),range(2)):
    assert tuple(chars[a,b,c] for a in range(6))==expected[b,c]

# Decompose by exact orthogonality into irreducible rational characters of
# D_6 x C_2: four 1D and two 2D reps of D_6, each with +/- layer sign.
mult={}
for eta,eps,zeta in product((1,-1),repeat=3):
    s=sum(chars[a,b,c]*eta**a*eps**b*zeta**c for a,b,c in chars)
    assert s%24==0 and s>=0
    mult[f'A({eta},{eps})*T({zeta})']=s//24
for k,rot in [(1,(2,1,-1,-2,-1,1)),(2,(2,-1,-1,2,-1,-1))]:
    for zeta in (1,-1):
        s=sum(chars[a,0,c]*rot[a]*zeta**c for a in range(6) for c in range(2))
        assert s%24==0 and s>=0
        mult[f'E{k}*T({zeta})']=s//24
expected_mult={'A(1,1)*T(1)':1, 'A(1,-1)*T(-1)':2,
               'A(-1,1)*T(-1)':1, 'E1*T(-1)':1,
               'E2*T(1)':2,'E2*T(-1)':1}
assert {k:v for k,v in mult.items() if v}==expected_mult
assert sum(v*(2 if k.startswith('E') else 1) for k,v in mult.items())==12
assert (12+chars[0,0,1])//2==5  # layer-invariant dimension
assert (12-chars[0,0,1])//2==7  # layer-anti-invariant dimension
assert mult['A(1,1)*T(1)']==1  # unique full-group invariant class
print('VERIFY_OK mod2_reduced_betti='+repr(bettis))
print('VERIFY_OK facets_by_number_of_edges='+repr(dict(facets)))
print('VERIFY_OK faces=1104 face_vector='+repr(face_vector)+' independent_matching_polynomial='+repr(poly))
print(f'VERIFY_OK nonempty_faces={len(actual_faces)} pairs=545 critical=(one_0_cell,twelve_3_cells) incidences={incidences} dag_vertices={visited}')
for b,c in product(range(2),range(2)):
    print(f'CHARACTER b={b} layer={c}: '+str([chars[a,b,c] for a in range(6)]))
print('VERIFY_OK symmetry_irreducible_multiplicities='+repr(expected_mult))
print('VERIFY_OK homotopy=wedge_of_12_three_spheres layer_eigenspaces=(5,7) full_group_invariants=1')
