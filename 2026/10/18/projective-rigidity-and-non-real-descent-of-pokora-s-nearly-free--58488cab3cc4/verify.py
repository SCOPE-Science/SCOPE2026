#!/usr/bin/env python3
"""Exact rational/Gaussian-integer checks for the degree-nine conic-line arrangement."""
from fractions import Fraction as F
from itertools import permutations, combinations
from math import gcd

# Lines of the divisor in homogeneous coordinates x,y,z.
lines = [(1,0,0),(0,1,0),(0,0,1),(1,-1,0),(2,0,-1),(0,1,-1),(2,1,-1)]
P0 = (0,0,1)
P = [(0,1,0),(0,1,1),(1,0,0),(1,0,2)]

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def normal(v):
    v=tuple(F(q) for q in v)
    first=next(t for t in v if t)
    return tuple(t/first for t in v)
def dot(a,b): return sum(x*y for x,y in zip(a,b))

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def inv(A):
    T=[[F(a) for a in row]+[F(int(i==j)) for j in range(3)] for i,row in enumerate(A)]
    for j in range(3):
        r=next(k for k in range(j,3) if T[k][j]);T[j],T[r]=T[r],T[j]
        h=T[j][j];T[j]=[a/h for a in T[j]]
        for k in range(3):
            if k!=j:
                h=T[k][j];T[k]=[x-h*y for x,y in zip(T[k],T[j])]
    return [r[3:] for r in T]
def transpose(A):return [list(row) for row in zip(*A)]
def matpts(Q):return [[F(Q[j][i]) for j in range(3)] for i in range(3)]
def mulmv(A,v):return tuple(sum(A[i][j]*v[j] for j in range(3)) for i in range(3))
def eqv(A,B):
    a=next(x for row in A for x in row if x)
    b=next(x for row in B for x in row if x)
    return all(A[i][j]*b==B[i][j]*a for i in range(3) for j in range(3))

# Every triple point is a pairwise intersection of three distinct lines.
intersections={}
for a,b in combinations(lines,2):
    pt=normal(cross(a,b))
    intersections[pt]=sum(dot(l,pt)==0 for l in lines)
triple={pt for pt,m in intersections.items() if m==3}
assert triple == {normal(pt) for pt in (P0,*P)}
assert sum(m==2 for m in intersections.values())==6
Tpts=[P0]+P
collinear=[comb for comb in combinations(range(5),3)
           if dot(Tpts[comb[0]],cross(Tpts[comb[1]],Tpts[comb[2]]))==0]
assert collinear==[(0,1,2),(0,3,4)],collinear

# A projectivity preserves P0 and the two pairs {P1,P2}, {P3,P4},
# either separately or after interchanging the pairs. Four other triple
# points constitute a projective frame; it therefore has at most 8 forms.
U=matpts(P[:3]);UI=inv(U)
coeff=mulmv(UI,P[3])
assert all(coeff)
autos=[];candidates=0
for perm in permutations(range(4)):
    image0={perm[0],perm[1]};image1={perm[2],perm[3]}
    if not ((image0=={0,1} and image1=={2,3}) or
            (image0=={2,3} and image1=={0,1})):
        continue
    candidates+=1
    V=matpts([P[j] for j in perm[:3]]);VI=inv(V)
    dest=mulmv(VI,P[perm[3]])
    Diag=[[F(dest[i]/coeff[i]) if i==j else F(0) for j in range(3)] for i in range(3)]
    M=mm(mm(V,Diag),UI)
    backT=transpose(inv(M))
    transformed={normal(mulmv(backT,l)) for l in lines}
    if transformed=={normal(l) for l in lines}:
        autos.append(M)
assert candidates==8 and len(autos)==2,(candidates,len(autos))
E=[[F(int(i==j)) for j in range(3)] for i in range(3)]
N=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(2),F(1),F(-1)]]
assert all(any(eqv(M,W) for W in [E,N]) for M in autos)
assert all(any(eqv(M,W) for M in autos) for W in [E,N])
assert mm(N,N)==E

# The conic Q=z(z-2x-y)+(1-i)xy, and its conjugate have coefficients
# differing at xy only. The involution N replaces z by 2x+y-z,
# leaving the product z(z-2x-y) unchanged.
def poly_sum(A,B):
    C=A.copy()
    for m,v in B.items():
        C[m]=C.get(m,(0,0))
        C[m]=(C[m][0]+v[0],C[m][1]+v[1])
    return {m:v for m,v in C.items() if v!=(0,0)}
def poly_mul(A,B):
    C={}
    for ma,va in A.items():
        for mb,vb in B.items():
            m=tuple(i+j for i,j in zip(ma,mb))
            t=(va[0]*vb[0]-va[1]*vb[1],va[0]*vb[1]+va[1]*vb[0])
            C=poly_sum(C,{m:t})
    return C
def scale(A,a,b=0):return poly_mul(A,{(0,0,0):(a,b)})
def add(*polys):
    s={}
    for p in polys:s=poly_sum(s,p)
    return s
x={(1,0,0):(1,0)};y={(0,1,0):(1,0)};z={(0,0,1):(1,0)}
lin=lambda *ps:add(*ps)
znew=add(scale(x,2),y,scale(z,-1))
def q(a,b,c):
    return add(poly_mul(c,add(c,scale(a,-2),scale(b,-1))),
               scale(poly_mul(a,b),1,-1))
Q=q(x,y,z)
assert Q==q(x,y,znew)
Qbar=add(poly_mul(z,add(z,scale(x,-2),scale(y,-1))),scale(poly_mul(x,y),1,1))
assert Qbar==add(poly_mul(znew,add(znew,scale(x,-2),scale(y,-1))),scale(poly_mul(x,y),1,1))
assert Q!=Qbar
# Coefficient of z^2 is 1 in both, so they are not scalar multiples.
assert Q[(0,0,2)]==(1,0)==Qbar[(0,0,2)]
assert Q[(1,1,0)]==(1,-1) and Qbar[(1,1,0)]==(1,1)

# The free companion becomes real after the substitution y=iY.
Yi=scale(y,0,1)
Fpoly=add(scale(poly_mul(Yi,poly_mul(add(Yi,scale(x,-1)),add(Yi,x))),1))
for a in (add(Yi,scale(x,-1),scale(z,-2)),add(Yi,scale(x,-1),scale(z,2)),
          add(Yi,x,scale(z,-2)),add(Yi,x,scale(z,2))):
    Fpoly=poly_mul(Fpoly,a)
Fpoly=poly_mul(Fpoly,add(poly_mul(x,x),scale(poly_mul(Yi,Yi),-1),
                              scale(poly_mul(Yi,z),0,4),scale(poly_mul(z,z),-4)))
# Division by i is multiplication by -i.
Freal=scale(Fpoly,0,-1)
assert all(v[1]==0 for v in Freal.values())
assert len(Freal)>0
print('VERIFY_OK: five triple points; six nodes; eight projective-frame candidates;')
print('two automorphisms I,N; Q and Qbar inequivalent; F has a real polynomial model.')
