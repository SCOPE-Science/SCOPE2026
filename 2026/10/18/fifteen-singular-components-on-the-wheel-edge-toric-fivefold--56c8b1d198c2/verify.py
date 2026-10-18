"""Exact-arithmetic verification of the edge-polytope normal fan of K_1*C_5.
Requires Python 3 and SymPy. All face/Smith calculations use integers/rationals.
"""
from itertools import combinations
from collections import Counter, defaultdict
from math import gcd, lcm, prod
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

EDGES=[(0,i) for i in range(1,6)]+[(i,i+1 if i<5 else 1) for i in range(1,6)]
V=[]
for i,j in EDGES:
    a=[0]*6; a[i]=a[j]=1; V.append(tuple(a[:-1]))
full=(1<<10)-1

def selected(mask):return [i for i in range(10) if mask & (1<<i)]
def dim_face(mask):
    xs=selected(mask)
    return Matrix([[V[j][k]-V[xs[0]][k] for k in range(5)] for j in xs[1:]]).rank()
def smith_index(rows, rank):
    D=smith_normal_form(Matrix(rows),domain=ZZ)
    assert sum(int(D[i,i])!=0 for i in range(min(D.shape)))==rank
    return prod(abs(int(D[i,i])) for i in range(rank))

# 5 affinely independent vertices define each facet of a 5-polytope.
facets={}
for ids in combinations(range(10),5):
    mat=Matrix([[V[i][j]-V[ids[0]][j] for j in range(5)] for i in ids[1:]])
    kern=mat.nullspace()
    if len(kern)!=1:continue
    q=kern[0]; den=lcm(*(z.q for z in q)); n=[int(z*den) for z in q]; g=gcd(*n); n=[z//g for z in n]
    dot=[sum(n[j]*v[j] for j in range(5)) for v in V]
    c=dot[ids[0]]
    if c==max(dot) and c>min(dot):
        n=[-z for z in n];dot=[-z for z in dot];c=-c
    if c!=min(dot) or c==max(dot):continue
    m=sum(1<<i for i,x in enumerate(dot) if x==c)
    if dim_face(m)==4:
        assert m not in facets or facets[m]==(tuple(n),c)
        facets[m]=(tuple(n),c)
assert len(facets)==12
assert smith_index([[V[i][j]-V[0][j] for j in range(5)] for i in range(1,10)],5)==1

# All nonempty faces are intersections of facet vertex masks.
faces={full}; todo=[full]
while todo:
    nxt=[]
    for m in todo:
        for f in facets:
            z=m & f
            if z and z not in faces: faces.add(z);nxt.append(z)
    todo=nxt
assert len(faces)==153
fvec=Counter(dim_face(m) for m in faces)
assert tuple(fvec[d] for d in range(6))==(10,35,55,40,12,1)

sing=[]
for m in faces:
    if m==full:continue
    d=dim_face(m); codim=5-d
    normals=[facets[f][0] for f in facets if f&m==m]
    rank=Matrix(normals).rank()
    assert rank==codim
    idx=smith_index(normals,codim)
    if len(normals)==codim: assert idx==1  # every simplicial cone is unimodular
    if len(normals)>codim or idx>1:sing.append((m,d,normals,idx))
assert Counter(d for _,d,_,_ in sing)=={0:10,1:25,2:10}
maximal=[(m,d,ns,idx) for m,d,ns,idx in sing if not any(m!=t and m&t==m for t,_,_,_ in sing)]
assert Counter(d for _,d,_,_ in maximal)=={1:5,2:10}
edge_max={tuple(selected(m)) for m,d,_,_ in maximal if d==1}
tri_max={tuple(selected(m)) for m,d,_,_ in maximal if d==2}
assert edge_max=={(0,2),(0,3),(1,3),(1,4),(2,4)}
assert tri_max=={(0,5,9),(5,6,9),(1,5,6),(2,6,7),(5,6,7),
                 (4,8,9),(5,8,9),(7,8,9),(3,7,8),(6,7,8)}
for m,d,ns,idx in maximal:
    assert idx==1 and len(ns)==(5-d)+1
    rel=Matrix(ns).T.nullspace()
    assert len(rel)==1
    q=rel[0]; den=lcm(*(z.q for z in q)); coeff=[int(z*den) for z in q];g=gcd(*coeff);coeff=[z//g for z in coeff]
    assert sorted(coeff)==([-1,-1,1,1] if d==2 else [-1,-1,-1,1,1]) or sorted(coeff)==([-1,-1,1,1,1] if d==1 else [-1,-1,1,1])
    if d==2:
        ids=selected(m)
        assert smith_index([[V[i][k]-V[ids[0]][k] for k in range(5)] for i in ids[1:]],2)==1

print('VERIFY_OK', {'facets':len(facets),'faces':len(faces),'f_vector':tuple(fvec[d] for d in range(6)), 'singular_orbits':dict(Counter(d for _,d,_,_ in sing)), 'maximal_singular_faces':dict(Counter(d for _,d,_,_ in maximal))})
