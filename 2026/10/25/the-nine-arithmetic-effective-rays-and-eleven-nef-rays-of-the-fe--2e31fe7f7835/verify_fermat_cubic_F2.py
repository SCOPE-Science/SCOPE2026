#!/usr/bin/env python3
"""Exact standard-library certificate for the F2 Fermat cubic's arithmetic Picard lattice."""
from itertools import product, combinations
from fractions import Fraction
from collections import Counter
from functools import reduce
from math import gcd

# F4 = F2[a]/(a^2+a+1), elements 0,1,a,a+1 encoded by 0,1,2,3.
def fm(a,b):
    z=0
    for k in range(2):
        if (b>>k)&1:z^=a<<k
    if z&8:z^=12
    if z&4:z^=7
    return z

def fp(a,n):
    v=1
    for _ in range(n):v=fm(v,a)
    return v

def fr(v):return tuple(fp(x,2) for x in v)

def rr(rows):
    A=[list(x) for x in rows];i=0
    for j in range(4):
        k=next((k for k in range(i,len(A)) if A[k][j]),None)
        if k is None:continue
        A[i],A[k]=A[k],A[i]
        m=fp(A[i][j],2)
        A[i]=[fm(m,x) for x in A[i]]
        for k in range(len(A)):
            if k!=i and A[k][j]:
                d=A[k][j];A[k]=[x^fm(d,y) for x,y in zip(A[k],A[i])]
        i+=1
        if i==len(A):break
    return tuple(tuple(r) for r in A[:i])

partitions=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=set()
for ((i,j),(k,l)) in partitions:
    for u,v in product((1,2,3),repeat=2):
        A=[0]*4;B=[0]*4;A[i]=1;A[j]=u;B[k]=1;B[l]=v
        # Cubic vanishes identically on each of these 27 lines.
        assert fp(u,3)==fp(v,3)==1
        lines.add(rr([A,B]))
lines=sorted(lines)
assert len(lines)==27
for L in lines:
    assert len(L)==2
    for u,v in product(range(4),repeat=2):
        x=[u*0 for _ in range(4)]
        for a in range(4):x[a]=fm(u,L[0][a])^fm(v,L[1][a])
        assert reduce(lambda a,b:a^b,(fp(t,3) for t in x),0)==0

def rank4(rows):return len(rr(rows))
G=[[-1 if i==j else int(rank4(lines[i]+lines[j])==3) for j in range(27)] for i in range(27)]
assert Counter(G[i][j] for i in range(27) for j in range(i+1,27))=={0:216,1:135}
frob=[lines.index(rr([fr(v) for v in L])) for L in lines]
assert all(frob[frob[i]]==i for i in range(27))
fixed=[i for i in range(27) if frob[i]==i]
pairs=[(i,frob[i]) for i in range(27) if i<frob[i]]
assert len(fixed)==3 and len(pairs)==12
assert all(G[i][j]==1 for i,j in combinations(fixed,2))
assert sum(G[i][j] for i,j in pairs)==6

# All 45 F4 points, each on exactly 3 lines; exactly 7 are fixed by x -> x^2.
points=set()
for x in product(range(4),repeat=4):
    if x==(0,0,0,0):continue
    if reduce(lambda a,b:a^b,(fp(t,3) for t in x),0):continue
    points.add(min(tuple(fm(k,t) for t in x) for k in (1,2,3)))
assert len(points)==45
assert sum(fr(P)==P for P in points)==7
for P in points:
    containing=0
    for L in lines:
        if rank4(L+(P,))==2:containing+=1
    assert containing==3

# Exact rational matrix helper functions.
def determinant(mat):
    m=len(mat)
    if m==0:return 1
    A=[[Fraction(x) for x in row] for row in mat]
    det=Fraction(1)
    for j in range(m):
        k=next((k for k in range(j,m) if A[k][j]),None)
        if k is None:return 0
        if k!=j:A[j],A[k]=A[k],A[j];det=-det
        pivot=A[j][j];det*=pivot
        for k in range(j+1,m):
            z=A[k][j]/pivot
            for l in range(j+1,m):A[k][l]-=z*A[j][l]
            A[k][j]=0
    assert det.denominator==1
    return int(det)

def solve(A,b):
    n=len(A)
    M=[[Fraction(t) for t in row]+[Fraction(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if M[k][j])
        M[j],M[k]=M[k],M[j]
        z=M[j][j];M[j]=[v/z for v in M[j]]
        for k in range(n):
            if k!=j:
                z=M[k][j];M[k]=[x-z*y for x,y in zip(M[k],M[j])]
    return [M[i][-1] for i in range(n)]

def six_skew(candidates,chosen):
    if len(chosen)==6:return chosen
    for n,i in enumerate(candidates):
        z=six_skew([j for j in candidates[n+1:] if G[i][j]==0],chosen+[i])
        if z is not None:return z
    return None
six=six_skew(list(range(27)),[])
assert six and len(six)==6
seventh=next(i for i in range(27) if i not in six and sum(G[i][j] for j in six)==2)
basis=six+[seventh]
B=[[G[i][j] for j in basis] for i in basis]
assert abs(determinant(B))==1

def coord(indices):
    b=[sum(G[i][j] for i in indices) for j in basis]
    out=solve(B,b)
    assert all(t.denominator==1 for t in out)
    return [int(t) for t in out]

# A nonrational Galois pair of skew lines meeting exactly one of the three rational lines.
pair=next((i,j) for i,j in pairs if G[i][j]==0 and sum(G[i][k]+G[j][k] for k in fixed)==2)
sets=[[i] for i in fixed]+[list(pair)]
T=list(map(coord,sets));C=[[T[j][i] for j in range(4)] for i in range(7)]
minor=next(((rows,determinant([[C[i][j] for j in range(4)] for i in rows]))
            for rows in combinations(range(7),4)
            if abs(determinant([[C[i][j] for j in range(4)] for i in rows]))==1),None)
assert minor is not None
GG=[[sum(B[a][b]*T[i][a]*T[j][b] for a in range(7) for b in range(7))
     for j in range(4)]for i in range(4)]
assert determinant(GG)==-8
assert GG[:3]==[[-1,1,1,0],[1,-1,1,0],[1,1,-1,2]] or GG[:3]==[[-1,1,1,0],[1,-1,1,2],[1,1,-1,0]] or GG[:3]==[[-1,1,1,2],[1,-1,1,0],[1,1,-1,0]]
assert GG[3][3]==-2
# The fixed lattice has rank four: Frobenius on the rank-seven Picard group is an
# involution with trace 1, since X(F2) has 7 points. Unit minor proves saturation.
assert sum(1 for P in points if fr(P)==P)==7
# Split 2-primary discriminant group: gcd minors of Gram matrix of sizes 1,2,3,4.
gcds=[reduce(gcd,(abs(determinant([[GG[i][j] for j in cols] for i in rows]))
          for rows in combinations(range(4),k) for cols in combinations(range(4),k)))
      for k in range(1,5)]
assert gcds==[1,2,4,8]
print('VERIFY_OK: 27 lines=3+12*2, 45 Eckardt points=7+19*2, Picard rank 4, trace basis primitive, discriminant -8, Smith [1,2,2,2]')
print('basis_indices',basis,'rational_lines',fixed,'trace_pair',pair)
print('unit_minor',minor,'gram',GG)

# Effective divisor cone over F2: three rational (-1)-curves and the six
# Frobenius traces of pairs of disjoint geometric (-1)-curves.
skew=[p for p in pairs if G[p[0]][p[1]]==0]
meeting=[p for p in pairs if G[p[0]][p[1]]==1]
assert len(skew)==len(meeting)==6
full_orbits=[[i] for i in fixed]+[list(p) for p in skew]
minor_rows=minor[0]
Tminor=[[C[i][j] for j in range(4)] for i in minor_rows]
rays=[]
for orbit in full_orbits:
    coeff=coord(orbit)
    ans=solve(Tminor,[coeff[i] for i in minor_rows])
    assert all(x.denominator==1 for x in ans)
    vec=tuple(int(x) for x in ans)
    assert all(sum(C[k][j]*vec[j] for j in range(4))==coeff[k] for k in range(7))
    rays.append(vec)
assert len(rays)==9 and len(set(rays))==9
# Each skew-pair trace differs from the chosen fourth basis class by a unit.
assert all(abs(v[3])==1 for v in rays[3:])
assert rays[:4]==[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
H=tuple(sum(coord([i])[j] for i in fixed) for j in range(7))
for p in meeting:
    u=coord(p)
    assert sum(1 for i in fixed if u==[H[j]-coord([i])[j] for j in range(7)])==1

def rank_q(a):
    if not a:return 0
    M=[[Fraction(x) for x in row] for row in a]
    h=0
    for col in range(len(M[0])):
        piv=next((i for i in range(h,len(M)) if M[i][col]),None)
        if piv is None:continue
        M[h],M[piv]=M[piv],M[h]
        t=M[h][col];M[h]=[x/t for x in M[h]]
        for i in range(len(M)):
            if i!=h and M[i][col]:
                t=M[i][col];M[i]=[x-t*y for x,y in zip(M[i],M[h])]
        h+=1
        if h==len(M):break
    return h

nef=set()
for ids in combinations(range(9),3):
    mat=[rays[i] for i in ids]
    if rank_q(mat)!=3:continue
    normal=[(-1)**j*determinant([[mat[i][k] for k in range(4) if k!=j]
                                 for i in range(3)]) for j in range(4)]
    dots=[sum(a*b for a,b in zip(normal,ray)) for ray in rays]
    if all(x>=0 for x in dots):pass
    elif all(x<=0 for x in dots):normal=[-x for x in normal]
    else:continue
    g=reduce(gcd,(abs(x) for x in normal))
    nef.add(tuple(x//g for x in normal))
assert len(nef)==11
for ray in rays:
    supporting=[normal for normal in nef if sum(a*b for a,b in zip(normal,ray))==0]
    assert rank_q(supporting)==3
print('VERIFY_CONE_OK: 9 invariant effective extremal rays; 11 nef extremal rays; 6 skew-pair trace generators and 6 decomposable meeting-pair traces')
print('rays',rays)
print('nef_dual',sorted(nef))
