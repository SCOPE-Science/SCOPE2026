"""Exact, dependency-free finite certificate for the matching complex of J_5.
Run with Python 3.10+: python verify.py.  No downloads or auxiliary files.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 5
A = list(range(0, N)); B = list(range(N, 2*N))
C = list(range(2*N, 3*N)); D = list(range(3*N, 4*N))
E = []
for i in range(N):
    E += [(A[i], B[i]), (A[i], C[i]), (A[i], D[i]), (B[i], B[(i+1)%N])]
ring = C+D
for i in range(2*N):
    E.append((ring[i], ring[(i+1)%(2*N)]))
E = sorted({tuple(sorted(e)) for e in E})
assert len(E) == 30
assert Counter(v for e in E for v in e) == Counter({v:3 for v in range(20)})
edge_vertex_mask = [(1 << x)|(1 << y) for x,y in E]

# Every matching is produced once by its increasing edge indices.
faces = [0]
def enumerate_faces(start, used, f):
    for j in range(start, len(E)):
        if not (edge_vertex_mask[j] & used):
            g = f | (1<<j)
            faces.append(g)
            enumerate_faces(j+1, used | edge_vertex_mask[j], g)
enumerate_faces(0, 0, 0)
face_counts = Counter(f.bit_count()-1 for f in faces if f)
assert len(faces) == 112828
assert [face_counts[i] for i in range(10)] == [30,375,2540,10155,24485,34930,27765,10890,1625,32]
assert sum((-1)**i * face_counts[i] for i in range(10)) - 1 == 62

# Sequential toggle matching, with the augmented empty/vertex pair omitted
# from the *ordinary* simplicial matching; the vertex becomes critical.
unpaired=set(faces)
up={}; down={}
for vertex in range(len(E)):
    bit=1<<vertex
    for f in tuple(unpaired):
        g=f|bit
        if f&bit == 0 and g in unpaired:
            unpaired.remove(f); unpaired.remove(g)
            up[f]=g; down[g]=f
assert up.get(0) is not None
critical=defaultdict(list)
for f in unpaired:
    critical[f.bit_count()-1].append(f)
for f in critical.values(): f.sort()
assert {dim:len(c) for dim,c in critical.items()} == {4:1,5:25,6:86}

# Check acyclicity by fully sorting the directed Hasse graph on all
# nonempty faces; paired arrows are reversed, all others point down.
ids={f:i for i,f in enumerate(faces[1:])}
incidences=[[] for _ in ids]
indeg=[0]*len(ids); count=0

def facets(f):
    x=f; i=0
    while x:
        b=x&-x
        yield (f^b, -1 if i&1 else 1)
        x-=b; i+=1

for higher in faces[1:]:
    for lower,_ in facets(higher):
        if lower == 0: continue
        if up.get(lower) == higher:
            source,target=ids[lower],ids[higher]
        else:
            source,target=ids[higher],ids[lower]
        incidences[source].append(target)
        indeg[target]+=1; count+=1
assert count == 677415
queue=deque(i for i,d in enumerate(indeg) if d == 0)
sorted_count=0
while queue:
    f=queue.popleft(); sorted_count+=1
    for g in incidences[f]:
        indeg[g]-=1
        if indeg[g] == 0: queue.append(g)
assert sorted_count == len(ids) == 112827
# Release the incidence digraph: subsequent checks use gradient paths only.
del incidences,indeg,ids

# Integral Morse boundaries: recursively eliminate an upward-paired facet
# using its paired cofacet; downward-paired facets project to zero.
def morse_boundary(k):
    target=critical[k-1]; indexed={f:j for j,f in enumerate(target)}
    @lru_cache(None)
    def reduce_face(face):
        if face in indexed: return ((indexed[face],1),)
        if face in down: return ()
        assert face in up
        coface=up[face]
        epsilon=next(s for t,s in facets(coface) if t == face)
        result=defaultdict(int)
        for facet,sgn in facets(coface):
            if facet==face: continue
            for j,a in reduce_face(facet):
                result[j]-=epsilon*sgn*a
        return tuple(sorted((j,x) for j,x in result.items() if x))
    out=[]
    for f in critical[k]:
        result=defaultdict(int)
        for facet,sgn in facets(f):
            for j,a in reduce_face(facet):
                result[j]+=sgn*a
        out.append([result.get(j,0) for j in range(len(target))])
    return [[out[j][i] for j in range(len(out))] for i in range(len(target))]

b5=morse_boundary(5); b6=morse_boundary(6)
assert len(b5)==1 and len(b5[0])==25
assert len(b6)==25 and all(len(row)==86 for row in b6)
assert sum(x!=0 for x in b5[0])==8
assert b5[0][5]==-1
assert all(sum(b5[0][i]*b6[i][j] for i in range(25))==0 for j in range(86))

# A 24-by-24 integer minor with determinant +1 proves the 24 row
# constraints left after deleting the fifth-index row have primitive rank 24.
rows=[i for i in range(25) if i != 5]
cols=[1,2,3,4,5,6,7,9,10,11,12,13,14,16,17,18,21,24,27,28,39,49,69,70]
minor=[[b6[i][j] for j in cols] for i in rows]
def bareiss_determinant(mat):
    a=[list(row) for row in mat]
    n=len(a); prev=1; sign=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]
assert bareiss_determinant(minor)==1

# The Morse complex has one ordinary critical 0-cell, and 1,25,86 cells
# respectively in dimensions 4,5,6.  Boundary 5 is primitive; boundary 6
# is primitive of rank 24, and is contained in its kernel. Thus it has
# reduced homology Z^62 in degree 6, zero otherwise, and its high-dimensional
# CW attaching maps split it as a wedge of 62 six-spheres.
print('VERIFY_OK: J5 vertices=20 edges=30, nonempty simplices=112827')
print('VERIFY_OK: incidence arrows=677415, acyclic directed Hasse graph')
print('VERIFY_OK: critical cells=(one 0, one 4, twenty-five 5, eighty-six 6)')
print('VERIFY_OK: integral Morse d5 has a unit, d5*d6=0, d6 unit 24x24 minor=+1')
print('VERIFY_OK: homotopy type = wedge of 62 six-spheres')
