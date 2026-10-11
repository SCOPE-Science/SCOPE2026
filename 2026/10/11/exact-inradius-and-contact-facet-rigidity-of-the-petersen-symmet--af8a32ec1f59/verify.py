"""Exact integer verifier for the Petersen symmetric edge polytope.

No external dependencies. Enumerates every integral 1-Lipschitz potential
up to constants using a spanning tree, tests the facet rank condition,
then independently checks the orbit of maximizers and contact-normal span.
"""
from collections import Counter
from itertools import combinations, product
from fractions import Fraction

V = list(combinations(range(5), 2))
N = len(V)
E = [(i,j) for i in range(N) for j in range(i+1,N)
     if set(V[i]).isdisjoint(V[j])]
assert N == 10 and len(E) == 15
ADJ = [[] for _ in V]
for i,j in E:
    ADJ[i].append(j); ADJ[j].append(i)

# Spanning-tree coordinates: all possible facet potentials, root fixed at zero.
parent = [-1] * N
parent[0] = 0
order = [0]
for u in order:
    for v in ADJ[u]:
        if parent[v] < 0:
            parent[v] = u
            order.append(v)
assert len(order) == N

feasible = 0
vertices = 0
max_sq_numerator = -1
maximizers = set()
for ds in product((-1,0,1), repeat=N-1):
    a=[0]*N
    for v,d in zip(order[1:],ds):
        a[v]=a[parent[v]]+d
    if any(abs(a[i]-a[j])>1 for i,j in E):
        continue
    feasible += 1
    # Vertices have connected tight edges (rank nine).
    tight = [ [] for _ in V]
    for i,j in E:
        if abs(a[i]-a[j])==1:
            tight[i].append(j)
            tight[j].append(i)
    seen={0}; todo=[0]
    for i in todo:
        for j in tight[i]:
            if j not in seen:
                seen.add(j); todo.append(j)
    if len(seen)<N:
        continue
    vertices += 1
    norm10 = N*sum(x*x for x in a) - sum(a)**2
    if norm10 > max_sq_numerator:
        max_sq_numerator = norm10
        maximizers = {tuple(a)}
    elif norm10 == max_sq_numerator:
        maximizers.add(tuple(a))
assert feasible == 2613, (feasible, 2613)
assert vertices == 1410, (vertices, 1410)
assert max_sq_numerator == 56 and len(maximizers) == 30

# Independently generate the 30 proposed equality potentials, and compare
# them exactly against the exhaustive maximizer list.
contact_vectors=[]
orbit=set()
for i,j in E:
    A,B=set(V[i]),set(V[j]); center=[0]*N
    for k,U in enumerate(V):
        U=set(U)
        center[k] = (6 if k in (i,j) else -4 if U & A and U & B else 1)
    assert sum(center)==0 and sum(t*t for t in center)==140
    assert all(abs(center[a]-center[b]) <= 5 for a,b in E)
    for sign in (1,-1):
        p=[sign*x for x in center]
        mn=min(p)
        canon=tuple((x-mn)//5 for x in p)
        assert all((x-mn)%5 ==0 for x in p)
        # Root normalization rather than minimum normalization.
        canon=tuple(x-canon[0] for x in canon)
        orbit.add(canon)
    contact_vectors.append(center)
assert len(orbit)==30 and orbit==maximizers

# Compute exact Gram matrix for 15 unoriented contact normals.
S=[[sum(f[i]*f[j] for f in contact_vectors) for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        expected=(210 if i==j else -65 if set(V[i]) & set(V[j]) else 60)
        assert S[i][j] == expected, (i,j,S[i][j],expected)

# Integer row elimination verifies the contact vectors span R^10 modulo constants.
def rank_over_rationals(matrix):
    A=[[Fraction(x) for x in row] for row in matrix]
    nr=len(A); nc=len(A[0]); pos=0
    for j in range(nc):
        pivot=next((i for i in range(pos,nr) if A[i][j]),None)
        if pivot is None: continue
        A[pos],A[pivot]=A[pivot],A[pos]
        z=A[pos][j]
        A[pos]=[t/z for t in A[pos]]
        for i in range(nr):
            if i!=pos and A[i][j]:
                z=A[i][j]
                A[i]=[x-z*y for x,y in zip(A[i],A[pos])]
        pos+=1
        if pos==nr:break
    return pos
assert rank_over_rationals(contact_vectors)==9
assert Fraction(10,max_sq_numerator)==Fraction(5,28)   # radius squared
print("VERIFY_OK: 10 vertices, 15 graph edges; 2613 admissible potentials;"
      " 1410 facets; 30 distinct maximizers; max norm squared 28/5;"
      " contact-rank 9; squared inradius 5/28.")
