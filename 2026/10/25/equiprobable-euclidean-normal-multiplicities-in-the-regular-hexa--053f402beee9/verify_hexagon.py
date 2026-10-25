#!/usr/bin/env python3
"""Exact rational audit of the regular-hexagon normal-multiplicity law.

Coordinates (u,v) mean the Euclidean point (u,sqrt(3)*v).  Consequently
all vertices, normal-sheet equations, and relative areas are rational.
Only standard-library integer and rational arithmetic is used.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations

V = [(Q(1),Q(0)), (Q(1,2),Q(1,2)), (Q(-1,2),Q(1,2)),
     (Q(-1),Q(0)), (Q(-1,2),Q(-1,2)), (Q(1,2),Q(-1,2))]

def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def dot(a,b): return a[0]*b[0]+3*a[1]*b[1]
def affine(A,x): return A[0]*x[0]+A[1]*x[1]+A[2]
def signed_area2(poly):
    return sum(poly[i][0]*poly[(i+1)%len(poly)][1]
               -poly[i][1]*poly[(i+1)%len(poly)][0]
               for i in range(len(poly))) if len(poly)>=3 else Q(0)
def clip(poly,L,sgn=1):
    if len(poly)<3: return []
    ans=[]
    for i,a in enumerate(poly):
        b=poly[(i+1)%len(poly)]
        da=sgn*affine(L,a);db=sgn*affine(L,b)
        if da>=0: ans.append(a)
        if da*db<0:
            ans.append(tuple((db*a[k]-da*b[k])/(db-da) for k in range(2)))
    result=[]
    for x in ans:
        if not result or result[-1]!=x:result.append(x)
    if result and result[-1]==result[0]: result.pop()
    return result if len(result)>=3 and signed_area2(result)>0 else []

# For each directed endpoint-edge incidence, the positive sign means
# that the projection along that edge points strictly into the edge.
INC=[]
for i,a in enumerate(V):
    for j in ((i-1)%6,(i+1)%6):
        d=sub(V[j],a)
        A,B=d[0],3*d[1]
        INC.append((i,j,(A,B,-A*a[0]-B*a[1])))
SHEETS=sorted(set(L for _,_,L in INC))
assert len(INC)==12 and len(SHEETS)==6
assert all(sum(int(LL==L) for _,_,LL in INC)==2 for L in SHEETS)

# The six strict halfspaces are the complement caps of the central hexagon.
CAPS=[(Q(-1),Q(0),Q(1,2)),(Q(1),Q(0),Q(1,2)),
      (Q(-1),Q(-3),Q(1)),(Q(1),Q(3),Q(1)),
      (Q(-1),Q(3),Q(1)),(Q(1),Q(-3),Q(1))]
assert all(any(A==tuple(k*z for z in L) for k in (Q(1),Q(2)) for A in CAPS) for L in SHEETS)

def base_counts(p):
    I={(i,j):int(affine(L,p)>0) for i,j,L in INC}
    sides=sum(I[(j,(j+1)%6)]*I[((j+1)%6,j)] for j in range(6))
    vertices=sum(I[(j,(j-1)%6)]*I[(j,(j+1)%6)] for j in range(6))
    return sides,vertices

def center(poly):
    return tuple(sum(p[k] for p in poly)/len(poly) for k in (0,1))

# Partition exactly by all the sheets; each open cell has a fixed sign vector.
cells=[V]
for L in SHEETS:
    cells=[part for poly in cells for sgn in (1,-1)
                 if (part:=clip(poly,L,sgn))]
assert len(cells)==13
assert sum(map(signed_area2,cells))==signed_area2(V)==Q(3)
area={};joint=defaultdict(Q);counts=Counter();support=defaultdict(Q)
for poly in cells:
    p=center(poly)
    edges,vertices=base_counts(p)
    n=edges+vertices
    k=sum(affine(L,p)<0 for L in CAPS)
    assert n==12-4*k and k<=2
    assert edges==vertices
    counts[n]+=1
    support[n]+=signed_area2(poly)/signed_area2(V)
    joint[(edges,vertices)]+=signed_area2(poly)/signed_area2(V)
assert counts=={4:6,8:6,12:1}
assert dict(support)=={4:Q(1,3),8:Q(1,3),12:Q(1,3)}
assert dict(joint)=={(2,2):Q(1,3),(4,4):Q(1,3),(6,6):Q(1,3)}

# Independent-by-inclusion computation using the six cap triangles:
cap_areas=[]
for L in CAPS:
    cap=clip(V,L,-1)
    cap_areas.append(signed_area2(cap)/signed_area2(V))
assert cap_areas==[Q(1,6)]*6
pairareas=[]
for i,j in combinations(range(6),2):
    c=clip(clip(V,CAPS[i],-1),CAPS[j],-1)
    if c: pairareas.append((i,j,signed_area2(c)/signed_area2(V)))
assert len(pairareas)==6 and all(a==Q(1,18) for _,_,a in pairareas)
for a,b,c in combinations(range(6),3):
    if clip(clip(clip(V,CAPS[a],-1),CAPS[b],-1),CAPS[c],-1):
        raise AssertionError('positive-area triple overlap')

print('exact normal distribution:',dict(sorted(support.items())))
print('joint side/vertex normal distribution:',dict(sorted(joint.items())))
print('partition cells:',len(cells),'cap areas:',cap_areas)
print('nonempty cap overlaps:',pairareas)
print('mean:',sum(n*a for n,a in support.items()))
print('variance:',sum(n*n*a for n,a in support.items())-Q(8)**2)
