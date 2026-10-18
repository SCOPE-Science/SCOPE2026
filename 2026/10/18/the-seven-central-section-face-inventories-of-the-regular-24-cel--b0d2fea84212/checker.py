"""Exact incidence census for central sections of the regular D4 root polytope.
Python 3 standard library; run `python checker.py`. All arithmetic is rational.
"""
from fractions import Fraction
from itertools import combinations, product
from collections import Counter, defaultdict

R = []
for i,j in combinations(range(4),2):
    for a,b in product((-1,1), repeat=2):
        v=[0]*4;v[i]=a;v[j]=b
        R.append(tuple(v))
assert len(R)==24 and len(set(R))==24
DOT=lambda v,w:sum(a*b for a,b in zip(v,w))
EDGES=[(i,j) for i,j in combinations(range(24),2) if DOT(R[i],R[j])==1]
assert len(EDGES)==96 and all(sum(i in e for e in EDGES)==8 for i in range(24))
CELLS=[]
for i in range(4):
    for s in (-1,1):
        CELLS.append(frozenset(j for j,r in enumerate(R) if s*r[i]==1))
for signs in product((-1,1),repeat=4):
    CELLS.append(frozenset(j for j,r in enumerate(R) if DOT(signs,r)==2))
assert len(CELLS)==24 and len(set(CELLS))==24
assert all(len(c)==6 for c in CELLS)
# Each facet vertex set affinely spans 3 dimensions; all its vertices lie on a supporting plane.

def rank(rows):
    a=[[Fraction(v) for v in row] for row in rows]
    m=len(a);n=len(a[0]) if m else 0
    piv=0
    for col in range(n):
        q=next((i for i in range(piv,m) if a[i][col]),None)
        if q is None: continue
        a[piv],a[q]=a[q],a[piv]
        s=a[piv][col]
        for k in range(col,n): a[piv][k]/=s
        for i in range(piv+1,m):
            s=a[i][col]
            if not s:continue
            for k in range(col,n): a[i][k]-=s*a[piv][k]
        piv+=1
        if piv==m:break
    return piv

def affine_rank(points):
    p=list(points)
    return rank([[a-b for a,b in zip(x,p[0])] for x in p[1:]]) if p else -1
assert all(affine_rank([R[j] for j in cell])==3 for cell in CELLS)
W=((1,0,0,0),(1,1,0,0),(1,1,1,-1),(1,1,1,1))

def section(normal):
    heights=[DOT(normal,v) for v in R]
    sec={}
    for i,h in enumerate(heights):
        if h==0: sec[('v',i)]=tuple(map(Fraction,R[i]))
    for i,j in EDGES:
        if heights[i]*heights[j]<0:
            t=Fraction(heights[i],heights[i]-heights[j])
            sec[('e',i,j)]=tuple((1-t)*R[i][k]+t*R[j][k] for k in range(4))
    assert len(sec)==len(set(sec.values()))
    faces=set()
    for cell in CELLS:
        pts={sec[('v',i)] for i in cell if heights[i]==0}
        for i,j in EDGES:
            if i in cell and j in cell and heights[i]*heights[j]<0:
                pts.add(sec[('e',i,j)])
        if len(pts)>=3 and affine_rank(pts)==2:
            faces.add(frozenset(pts))
    inventory=Counter(map(len,faces))
    f0=len(sec); f2=len(faces)
    degrees=sum(inventory[k]*k for k in inventory)
    assert degrees%2==0
    f1=degrees//2
    assert f0-f1+f2==2
    assert f0>=4 and f1>=6 and f2>=4
    return f0,f1,f2,tuple(sorted(inventory.items()))

EXPECTED={
  (0,1): (12,24,14,((3,8),(4,6))),
  (0,2): (18,30,14,((4,12),(6,2))),
  (0,3): (26,42,18,((4,12),(6,6))),
  (1,0): (14,24,12,((4,12),)),
  (1,1): (20,32,14,((4,6),(5,8))),
  (1,2): (26,40,16,((4,4),(5,8),(6,4))),
  (1,3): (32,48,18,((4,6),(6,12))),
}
mask_out={}
for flags in product((0,1),repeat=4):
    if not any(flags): continue
    normal=tuple(sum(flags[i]*W[i][k] for i in range(4)) for k in range(4))
    actual=section(normal)
    key=(flags[1],sum(flags[i] for i in (0,2,3)))
    assert actual==EXPECTED[key],(flags,normal,actual,EXPECTED[key])
    mask_out[flags]=actual
assert len(mask_out)==15
# Verify full D4 Weyl chamber sign invariance under positive real coefficients
# by evaluating all root signs for two sets of coefficients with each support.
for flags in mask_out:
    n1=tuple(sum((1 if flags[i] else 0)*W[i][k] for i in range(4)) for k in range(4))
    n2=tuple(sum(((7+11*i) if flags[i] else 0)*W[i][k] for i in range(4)) for k in range(4))
    assert [((DOT(n1,v)>0)-(DOT(n1,v)<0)) for v in R]==[((DOT(n2,v)>0)-(DOT(n2,v)<0)) for v in R]
    assert section(n2)==section(n1)
# Check signed coordinate permutation invariance with exact integer sample normals.
for q in ((9,5,2,1),(10,9,4,-2),(15,11,6,3)):
    target=section(q)
    assert target==EXPECTED[1,3]
    for perm in ((3,2,1,0),(2,0,3,1),(1,2,3,0)):
        p=tuple(q[i] for i in perm)
        assert section(p)==target
print('D4_CENTRAL_SECTIONS_OK root_vertices=24 edges=96 facets=24 chamber_strata=15 orbit_types=7 sample_normals=15')
for k in sorted(EXPECTED):
    print('b,k=',k,' f,polygon_inventory=',EXPECTED[k])
