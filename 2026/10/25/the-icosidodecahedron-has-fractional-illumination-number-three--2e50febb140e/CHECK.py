"""Exact Q(sqrt(5)) combinatorics for the rectified icosahedron.
No external modules. Each pair (a,b) denotes a+b*phi, phi^2=phi+1.
"""
from itertools import combinations, product
from collections import Counter

ZERO=(0,0)
ONE=(1,0)
PHI=(0,1)

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]+a[1]*b[1], a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def dot(a,b):
    out=ZERO
    for x,y in zip(a,b): out=add(out,mul(x,y))
    return out

def sign(z):
    # twice (a+b phi) is (2a+b)+b sqrt(5).
    m,n=2*z[0]+z[1],z[1]
    if n==0: return (m>0)-(m<0)
    if m==0: return (n>0)-(n<0)
    if (m>0)==(n>0): return (m>0)-(m<0)
    diff=m*m-5*n*n
    assert diff != 0  # irrational sqrt(5)
    return ((m>0)-(m<0)) if diff>0 else ((n>0)-(n<0))

V=[]
for s,t in product((-1,1),repeat=2):
    ss=(s,0);tt=(t,0);sp=(0,s);tp=(0,t)
    V.extend(((ZERO,ss,tp),(ss,tp,ZERO),(sp,ZERO,tt)))
assert len(V)==12 and len(set(V))==12
square=lambda a: mul(a,a)
def dist2(a,b):
    z=ZERO
    for x,y in zip(a,b):z=add(z,square(sub(x,y)))
    return z
edges=tuple((i,j) for i,j in combinations(range(12),2) if dist2(V[i],V[j])==(4,0))
assert len(edges)==30
faces=tuple(f for f in combinations(range(12),3) if all(tuple(sorted(p)) in edges for p in combinations(f,2)))
assert len(faces)==20
opp={i:next(j for j in range(12) if all(add(x,y)==ZERO for x,y in zip(V[i],V[j]))) for i in range(12)}
pairs=tuple(sorted({tuple(sorted((i,j))) for i,j in opp.items()}))
assert len(pairs)==6

A=[[0]*6 for _ in range(6)]
for i,j in combinations(range(6),2):
    x,y=pairs[i][0],pairs[j][0]
    A[i][j]=A[j][i]=1 if (min(x,y),max(x,y)) in edges else -1
assert all(sum(A[i][k]*A[k][j] for k in range(6)) == (5 if i==j else 0) for i in range(6) for j in range(6))
dist=Counter()
for s in product((-1,1), repeat=6):
    q=(15+sum(A[i][j]*s[i]*s[j] for i,j in combinations(range(6),2)))//2
    S={pairs[i][0 if s[i]==1 else 1] for i in range(6)}
    direct=sum(i in S and j in S for i,j in edges)
    assert q == direct
    dist[q]+=1
assert dict(dist)=={5:12,6:20,9:20,10:12},dist

# Verify all 32 claimed supporting facets of the rectification.  For each
# supporting normal, the exact maximizers among edge midpoints must number
# five (original vertex) or three (original triangular face).
midpoints=[tuple(add(V[i][k],V[j][k]) for k in range(3)) for i,j in edges]
for norm in V:
    vals=[dot(norm,x) for x in midpoints]
    maximal=[k for k in range(30) if all(sign(sub(vals[k],v))>=0 for v in vals)]
    assert len(maximal)==5,("pentagonal facet",maximal)
for face in faces:
    norm=tuple((sum(V[i][k][0] for i in face),sum(V[i][k][1] for i in face)) for k in range(3))
    vals=[dot(norm,x) for x in midpoints]
    maximal=[k for k in range(30) if all(sign(sub(vals[k],v))>=0 for v in vals)]
    assert len(maximal)==3,("triangular facet",maximal)

# Certify that the proposed 32 facets form the entire boundary: they
# contain exactly 60 polygon sides, each incident to exactly two facets.
edge_index={e:i for i,e in enumerate(edges)}
side_count=Counter()
for a in range(12):
    neigh=[b for b in range(12) if tuple(sorted((a,b))) in edge_index]
    assert len(neigh)==5
    side_vertices=[]
    for b,c in combinations(neigh,2):
        if tuple(sorted((b,c))) in edge_index:
            i=edge_index[tuple(sorted((a,b)))]
            j=edge_index[tuple(sorted((a,c)))]
            side=tuple(sorted((i,j)))
            side_count[side]+=1
            side_vertices.append(side)
    assert len(side_vertices)==5
for a,b,c in faces:
    e=[edge_index[tuple(sorted((i,j)))] for i,j in combinations((a,b,c),2)]
    for i,j in combinations(e,2):side_count[tuple(sorted((i,j)))]+=1
assert len(side_count)==60 and all(n==2 for n in side_count.values())

u=((-2,0),(0,0),(-1,0))
def vecsum(ids):
    return tuple(sum_pair(V[i][j] for i in ids) for j in range(3))
def sum_pair(xs):
    a=b=0
    for x,y in xs:a+=x;b+=y
    return (a,b)

lit=[]
normal_min=[]
for i,j in edges:
    f=[k for k in faces if i in k and j in k]
    assert len(f)==2
    normals=[V[i],V[j]]+[vecsum(tri) for tri in f]
    vals=[dot(n,u) for n in normals]
    if all(sign(x)<0 for x in vals):
        lit.append((i,j))
        normal_min.extend(vals)
assert len(lit)==10,(len(lit),lit)
assert max(sign(z) for z in normal_min)==-1
print('EXACT_OK original_vertices=12 edges=30 faces=20 rectified_vertices=30')
print('SIGNED_CONFERENCE_MATRIX')
for row in A:print(' ', ' '.join(f'{a:+d}' if a else ' 0' for a in row))
print('SELECTION_EDGE_DISTRIBUTION',dict(sorted(dist.items())))
print('EXACT_ILLUMINATION_WITNESS',(-2,0,-1),'vertices_lit',len(lit),'edge_indices',lit)
