#!/usr/bin/env python3
"""Exact arithmetic checks for the exceptional degree-two zonotope metric theorem."""
import itertools
from math import isqrt

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def matvec(m,v):return tuple(sum(m[i][j]*v[j] for j in range(3)) for i in range(3))
def cofactor_half(V):
    a,b,c=V
    cr=(cross(b,c),cross(c,a),cross(a,b))
    assert all(x%2==0 for v in cr for x in v)
    return tuple(tuple(x//2 for x in v) for v in cr)

U=((1,1,0),(-1,1,0),(1,1,2))
V=((1,1,-1),(1,-1,1),(-1,1,1))
T=((0,1,-1),(1,0,0),(-1,0,1))
assert det(*U)==4
assert det(*V)==-4
assert det(*tuple(zip(*T)))==-1
assert tuple(matvec(T,u) for u in U)==V
W0=cofactor_half(U)
W=cofactor_half(V)
assert W0==((1,1,-1),(-1,1,0),(0,0,1))
assert W==((-1,-1,0),(-1,0,-1),(0,-1,-1))
for B,WW in ((U,W0),(V,W)):
    assert abs(det(*WW))==2
    assert all(sum(w[i] for w in WW)%2==0 for i in range(3))
    assert all(dot(B[i],WW[j])==(det(*B)//2 if i==j else 0)
               for i in range(3) for j in range(3))
assert all(dot(w,w)==2 for w in W)
assert all(dot(V[i],V[j])==(3 if i==j else -1)
           for i in range(3) for j in range(3))

# Check the exact lattice point counts using the inverse-matrix cofactor rows.
mins=tuple(sum(min(0,v[j]) for v in V) for j in range(3))
maxs=tuple(sum(max(0,v[j]) for v in V) for j in range(3))
d=det(*V)
for m in range(0,5):
    count=0
    for point in itertools.product(*(range(m*mins[j],m*maxs[j]+1) for j in range(3))):
        signed_num=[dot(w,point)*2 for w in W]
        # Every barycentric coefficient equals signed_num/d.
        if all((0<=num<=m*d) if d>0 else (m*d<=num<=0)
               for num in signed_num):
            count+=1
    expected=1+3*m+6*m*m+4*m*m*m
    assert count==expected,(m,count,expected)

# At equality all integral half-cofactors have norm squared <=2.
# Their parity and determinant characterize the equality Gram class.
vectors=[t for t in itertools.product((-1,0,1),repeat=3)
         if 0<dot(t,t)<=2]
assert len(vectors)==18
count=0
for a,b,c in itertools.product(vectors,repeat=3):
    if abs(det(a,b,c))!=2:continue
    if any((a[j]+b[j]+c[j])%2 for j in range(3)):continue
    count+=1
    assert dot(a,a)==dot(b,b)==dot(c,c)==2
    x,y,z=dot(a,b),dot(a,c),dot(b,c)
    assert abs(x)==abs(y)==abs(z)==1
    assert x*y*z==1
assert count==192
print('VERIFY_OK degree-two-zonotope-inradius exact_unimodular=yes cofactor_det2=yes bounded_equality_normals=192 lattice_counts_m=0..4=yes')
