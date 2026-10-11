#!/usr/bin/env python3
"""Exact self-contained certificate for the icosahedral matching-complex homotopy type.
Requires Python 3 standard library only. All graph edges, face incidences, signs,
matching pairs, and Morse boundary entries are reconstructed, not read from a log.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

# Standard icosahedron: apex 0, upper cycle 1..5, lower cycle 6..10,
# and opposite apex 11, with the ten triangles joining the staggered cycles.
edges=[]
for i in range(5):
    upper=1+i; lower=6+i
    edges.extend([(0,upper),(11,lower),
                  (upper,1+(i+1)%5),(lower,6+(i+1)%5),
                  (upper,lower),(upper,6+(i-1)%5)])
E=sorted((min(u,v),max(u,v)) for u,v in edges)
assert len(E)==30 and len(set(E))==30
assert Counter(v for edge in E for v in edge)==Counter({i:5 for i in range(12)})
# Verify 20 triangular faces with every edge in exactly two; Euler = 12-30+20=2.
triangles=[(i,j,k) for i in range(12) for j in range(i+1,12) for k in range(j+1,12)
           if all(e in E for e in [(i,j),(i,k),(j,k)])]
assert len(triangles)==20
assert all(sum(set(e).issubset(t) for t in triangles)==2 for e in E)
for v in range(12):
    nbrs={u if w==v else w for u,w in E if v in (u,w)}
    local=[(u,w) for u,w in E if u in nbrs and w in nbrs]
    assert len(nbrs)==5 and len(local)==5
    assert all(sum(vv in edge for edge in local)==2 for vv in nbrs)
    # A 2-regular graph on five vertices could be a 3-cycle plus a 2-cycle,
    # but a simple graph has no 2-cycles: it must be the 5-cycle.


VE=[(1<<u)|(1<<v) for u,v in E]
faces={}
def enumerate_faces(start,occupied,face,size):
    if face:faces[face]=size-1
    for idx in range(start,len(E)):
        if not (occupied & VE[idx]):
            enumerate_faces(idx+1,occupied|VE[idx],face|(1<<idx),size+1)
enumerate_faces(0,0,0,0)
assert Counter(faces.values())=={0:30,1:315,2:1400,3:2535,4:1482,5:125}
assert len(faces)==5887

# Ordered independent element toggles define the discrete-Morse pairing.
order=[26,16,11,10,23,1,5,29,7,20,9,28,17,13,0,19,22,6,12,21,14,15,3,8,2,24,25,27,18,4]
remaining=set(faces);lower_to_upper={};upper_to_lower={}
for idx in order:
    bit=1<<idx
    pairs=[(f,f|bit) for f in remaining if not (f&bit) and (f|bit) in remaining]
    for lower,upper in pairs:
        assert lower in remaining and upper in remaining
        remaining.remove(lower);remaining.remove(upper)
        lower_to_upper[lower]=upper;upper_to_lower[upper]=lower
assert len(lower_to_upper)==len(upper_to_lower)
critical=Counter(faces[f] for f in remaining)
assert critical=={0:1,3:109,4:45},critical

# Verify every oriented incidence of the FULL Hasse diagram is acyclic.
indegree={f:0 for f in faces};adj={f:[] for f in faces};count_inc=0
for face in faces:
    bits=face
    while bits:
        bit=bits & -bits;bits^=bit
        sub=face^bit
        if not sub:continue
        count_inc+=1
        if lower_to_upper.get(sub)==face:source,target=sub,face
        else:source,target=face,sub
        adj[source].append(target);indegree[target]+=1
queue=deque([f for f,d in indegree.items() if d==0]);seen=0
while queue:
    x=queue.popleft();seen+=1
    for y in adj[x]:
        indegree[y]-=1
        if not indegree[y]:queue.append(y)
assert seen==len(faces),(seen,len(faces))
assert count_inc==sum((k+1)*v for k,v in Counter(faces.values()).items() if k)

@lru_cache(None)
def reduce_to_critical(face):
    """Integral gradient-path projection of a face, preserving orientations."""
    if face in upper_to_lower:return {}
    if face not in lower_to_upper:return {face:1}
    upper=lower_to_upper[face]
    boundary=[]; coeff_face=None;bits=upper;sign=1
    while bits:
        b=bits&-bits;bits^=b
        facet=upper^b
        if facet==face:coeff_face=sign
        else:boundary.append((facet,sign))
        sign=-sign
    assert coeff_face in (-1,1)
    result=defaultdict(int)
    for facet,sign in boundary:
        for t,value in reduce_to_critical(facet).items():
            result[t]-=coeff_face*sign*value
    return {f:v for f,v in result.items() if v}

crit3=sorted(f for f in remaining if faces[f]==3)
crit4=sorted(f for f in remaining if faces[f]==4)
indices={f:i for i,f in enumerate(crit3)}
D=[[0 for _ in crit4] for _ in crit3]
for col,face in enumerate(crit4):
    bits=face;sign=1
    while bits:
        b=bits&-bits;bits^=b
        facet=face^b
        for t,value in reduce_to_critical(facet).items():
            assert t in indices
            D[indices[t]][col]+=sign*value
        sign=-sign
assert len(D)==109 and all(len(row)==45 for row in D)

def rank_mod_prime(M,p):
    # Row-span echelon reduction on a prime field.
    basis={}
    for row in M:
        data={i:x%p for i,x in enumerate(row) if x%p}
        while data:
            pivot=max(data)
            if pivot not in basis:
                inv=pow(data[pivot],-1,p)
                basis[pivot]={k:(v*inv)%p for k,v in data.items()}
                break
            factor=data[pivot]
            for k,v in basis[pivot].items():
                r=(data.get(k,0)-factor*v)%p
                if r:data[k]=r
                else:data.pop(k,None)
    return len(basis)

assert rank_mod_prime(D,3)==44
assert rank_mod_prime(D,2)==45

# One 45-by-45 full-rank minor of determinant +3 is an integral
# certificate that the index of the saturated image divides 3.
# Fixed independently selected 45-row certificate (indices in increasing
# critical-face-bitmask order), not a search performed during verification.
rows_for_minor=[39,23,9,104,10,61,20,90,4,36,33,88,38,50,98,70,93,65,73,
                16,14,86,107,66,24,22,108,74,5,76,100,87,106,30,80,25,
                43,31,78,51,19,94,91,103,7]
assert len(rows_for_minor)==45 and len(set(rows_for_minor))==45

def determinant_bareiss(a):
    a=[row[:] for row in a];n=len(a);previous=1;sgn=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=a[i][j]*pivot-a[i][k]*a[k][j]
                assert val%previous==0
                a[i][j]=val//previous
            a[i][k]=0
        previous=pivot
    return sgn*a[-1][-1]
minor_det=determinant_bareiss([D[i] for i in rows_for_minor])
assert minor_det==3,minor_det
print('ICOSAHEDRON_MORSE_PASS')
print('graph=12 vertices, 30 edges, 20 triangle facets')
print('matching_complex_nonempty_faces=5887; incidences=%d'%count_inc)
print('matching_pairs=%d; critical=%s'%(len(lower_to_upper),dict(critical)))
print('morse_boundary=109x45, rank_mod_3=44, rank_mod_2=45')
print('45x45_minor_determinant=%d; exact_rows=%s'%(minor_det,rows_for_minor))
print('integral_Morse_SNF=1^44,3^1; Htilde_3=Z^64+Z/3; homotopy=64 S^3 wedge M(Z/3,3)')
