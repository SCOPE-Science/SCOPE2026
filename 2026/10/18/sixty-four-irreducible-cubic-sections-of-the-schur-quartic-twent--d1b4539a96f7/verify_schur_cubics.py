#!/usr/bin/env python3
"""Exact check of the 24-line Schur-quartic cubic-section classification.

Uses only the Python standard library. All geometric input (line parameters)
is the explicit table of Naskrecki and Pokora, arXiv:2607.07898, Appendix A.
"""
from fractions import Fraction as Q
from itertools import combinations, product

class K:
    __slots__ = ('a','b')
    def __init__(self,a=0,b=0):
        self.a,self.b=Q(a),Q(b)
    def __add__(self,v):
        v=toK(v);return K(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,v):return self+-toK(v)
    def __rsub__(self,v):return toK(v)+-self
    def __mul__(self,v):
        v=toK(v);return K(self.a*v.a-3*self.b*v.b,self.a*v.b+self.b*v.a)
    __rmul__=__mul__
    def __truediv__(self,v):
        v=toK(v);norm=v.a*v.a+3*v.b*v.b
        if norm==0:raise ZeroDivisionError
        return self*K(v.a/norm,-v.b/norm)
    def __rtruediv__(self,v):return toK(v)/self
    def __pow__(self,n):
        if n<0:return (1/self)**(-n)
        ret=K(1)
        for _ in range(n):ret*=self
        return ret
    def __eq__(self,v):
        v=toK(v);return (self.a,self.b)==(v.a,v.b)
    def __repr__(self):return f'({self.a}+{self.b}tau)'

def toK(v):return v if isinstance(v,K) else K(v)
t=K(0,1)
LINES=[
(1,0,0,1),
(-1,0,0,-1),
(-1,0,0,(1-t)/2),
(-1,0,0,(1+t)/2),
(1,0,0,-(1+t)/2),
(1,0,0,(-1+t)/2),
(-t/3,-1-t/3,(-3-t)/6,(3-t)/6),
(-t/3,2*t/3,(3-t)/6,(3-t)/6),
(-t/3,1-t/3,t/3,(3-t)/6),
(t/3,-1+t/3,(-3+t)/6,(3+t)/6),
(t/3,-2*t/3,(3+t)/6,(3+t)/6),
(t/3,1+t/3,-t/3,(3+t)/6),
(t/3,-1+t/3,(3+t)/6,-t/3),
(t/3,-2*t/3,-t/3,-t/3),
(t/3,1+t/3,(-3+t)/6,-t/3),
(-t/3,-1-t/3,(3-t)/6,t/3),
(-t/3,2*t/3,t/3,t/3),
(-t/3,1-t/3,(-3-t)/6,t/3),
(-t/3,-1-t/3,t/3,(-3-t)/6),
(-t/3,2*t/3,(-3-t)/6,(-3-t)/6),
(-t/3,1-t/3,(3-t)/6,(-3-t)/6),
(t/3,-1+t/3,-t/3,(-3+t)/6),
(t/3,-2*t/3,(-3+t)/6,(-3+t)/6),
(t/3,1+t/3,(3+t)/6,(-3+t)/6),
]
TRIPLES=[
(1,5,6),(1,7,10),(1,8,12),(1,9,11),(2,3,4),(2,19,23),
(2,20,22),(2,21,24),(3,7,14),(3,8,13),(3,9,15),
(4,10,17),(4,11,16),(4,12,18),(5,13,19),(5,14,21),
(5,15,20),(6,16,22),(6,17,24),(6,18,23),(7,16,19),
(7,18,20),(8,16,21),(8,17,20),(9,17,19),(9,18,21),
(10,13,22),(10,15,23),(11,13,24),(11,14,23),
(12,14,22),(12,15,24),
]

def det_bareiss(A):
    A=[list(map(int,row)) for row in A]
    n=len(A);sgn=1;prev=1
    if n==0:return 1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((r for r in range(k+1,n) if A[r][k]!=0),None)
            if r is None:return 0
            A[k],A[r]=A[r],A[k];sgn=-sgn
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
            A[i][k]=0
        prev=pivot
    return sgn*A[-1][-1]

def linear_solve(A, B):
    """Solve A*X=B over the rationals, returning a matrix of Fractions."""
    n=len(A);m=len(B[0]);T=[[Q(v) for v in A[i]+B[i]] for i in range(n)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if T[r][col]),None)
        assert pivot is not None
        T[pivot],T[col]=T[col],T[pivot]
        d=T[col][col];T[col]=[x/d for x in T[col]]
        for r in range(n):
            if r!=col:
                c=T[r][col]
                if c:T[r]=[T[r][j]-c*T[col][j] for j in range(n+m)]
    assert all(T[i][j]==(i==j) for i in range(n) for j in range(n))
    return [row[n:] for row in T]

def smith_diagonal(A):
    """Integer Euclidean row/column reductions to Smith form."""
    A=[list(map(int,row)) for row in A];n=len(A);i=0
    while i<n:
        available=[(abs(A[r][c]),r,c) for r in range(i,n) for c in range(i,n) if A[r][c]]
        if not available:break
        _,r,c=min(available)
        A[i],A[r]=A[r],A[i]
        for row in A:row[i],row[c]=row[c],row[i]
        loops=0
        while True:
            loops+=1;assert loops<5000
            changed=False
            for r in range(i+1,n):
                if A[r][i]:
                    q=A[r][i]//A[i][i]
                    A[r]=[A[r][c]-q*A[i][c] for c in range(n)]
                    if A[r][i]:A[i],A[r]=A[r],A[i]
                    changed=True;break
            if changed:continue
            for c in range(i+1,n):
                if A[i][c]:
                    q=A[i][c]//A[i][i]
                    for row in A:row[c]-=q*row[i]
                    if A[i][c]:
                        for row in A:row[i],row[c]=row[c],row[i]
                    changed=True;break
            if changed:continue
            rem=next(((r,c) for r in range(i+1,n) for c in range(i+1,n) if A[r][c]%A[i][i]),None)
            if rem is not None:
                r,c=rem;A[i]=[A[i][j]+A[r][j] for j in range(n)]
                continue
            break
        if A[i][i]<0:A[i]=[-z for z in A[i]]
        i+=1
    assert all(A[r][c]==0 for r in range(n) for c in range(n) if r!=c)
    diag=[A[j][j] for j in range(n)]
    assert all(b%a==0 for a,b in zip(diag,diag[1:]) if a)
    return diag

# Check every line really lies on the smooth Schur quartic.
assert len(LINES)==24 and len(TRIPLES)==32
for a,b,c,d in LINES:
    values=[1-a**4+a*b**3,
            -4*a**3*c+c*b**3+3*a*b*b*d,
            -6*a*a*c*c+3*c*b*b*d+3*a*b*d*d,
            -1-4*a*c**3+3*c*b*d*d+a*d**3,
            -c**4+c*d**3]
    assert all(v==0 for v in values),(a,b,c,d,values)

pairs={}
for i,j in combinations(range(24),2):
    a,b,c,d=LINES[i];A,B,C,D=LINES[j]
    delta=(a-A)*(d-D)-(b-B)*(c-C)
    pairs[i,j]=(delta==0)

M=[[-2 if i==j else int(pairs[min(i,j),max(i,j)]) for j in range(24)] for i in range(24)]
seen=set();points=set()
for tr in TRIPLES:
    i,j,k=[v-1 for v in tr]
    assert len({i,j,k})==3
    for a,b in combinations(sorted((i,j,k)),2):
        assert M[a][b]==1 and (a,b) not in seen
        seen.add((a,b))
    a,b,c,d=LINES[i];A,B,C,D=LINES[j]
    u,v=a-A,c-C
    if u==0 and v==0:u,v=b-B,d-D
    x,y=v,-u
    assert x!=0 or y!=0
    pos=[x,y,a*x+c*y,b*x+d*y]
    assert all(pos[p]==[x,y,LINES[k][0]*x+LINES[k][2]*y,LINES[k][1]*x+LINES[k][3]*y][p] for p in range(4))
    first=next(z for z in pos if z!=0)
    normalized=tuple((z/first).a for z in pos)+tuple((z/first).b for z in pos)
    assert normalized not in points
    points.add(normalized)
assert len(seen)==96 and sum(pairs.values())==96 and len(points)==32
assert all(sum(M[i])==6 for i in range(24))
assert not any(all(M[a][b]==1 for a,b in combinations(S,2)) for S in combinations(range(24),4))

# Sixteen independent line classes form an integral basis of the line-generated lattice.
I=[0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16]
J=[j for j in range(24) if j not in I]
B=[[M[i][j] for j in I] for i in I]
assert det_bareiss(B)==-1728
assert smith_diagonal(B)==[1]*10+[2]*4+[6,18]

# Exact rank and generation: all eight remaining line classes have integral
# expansions in the displayed basis, checked against all 24 intersections.
rhs=[[M[i][j] for j in J]+[3,1] for i in I]
coeff=linear_solve(B,rhs)
for jidx,j in enumerate(J):
    z=[row[jidx] for row in coeff]
    assert all(v.denominator==1 for v in z)
    assert all(sum(M[i][I[h]]*z[h] for h in range(16))==M[i][j] for i in range(24))

# 3H is in the lattice but H is not; note H meets every line once.
threed=[row[-2] for row in coeff]
one=[row[-1] for row in coeff]
assert all(v.denominator==1 for v in threed)
assert any(v.denominator!=1 for v in one)
assert all(sum(M[i][I[h]]*threed[h] for h in range(16))==3 for i in range(24))
assert all(3*one[k]==threed[k] for k in range(16))
assert sum(threed)==12

# The rank-16 lattice generated by the line classes plus H has index 3.
# Replace basis vector indexed 1 (coefficient -1 in 3H) by H.
assert threed[1]==-1
h=[row[-1] for row in coeff]
W=[[Q(int(r==c)) if c!=1 else h[r] for c in range(16)] for r in range(16)]
Qh=[[sum(W[k][i]*B[k][ell]*W[ell][j] for k in range(16) for ell in range(16)) for j in range(16)] for i in range(16)]
assert all(v.denominator==1 for row in Qh for v in row)
assert det_bareiss(Qh)==-192
assert smith_diagonal(Qh)==[1]*10+[2]*5+[6]

# All cubic-section subsets are binary solutions to M*x=3*ones.
# The 8 coordinates indexed by J determine the 16 coordinates indexed by I.
solutions=[]
for bits in product((0,1),repeat=8):
    inner=[coeff[h][-2]-sum(coeff[h][j]*bits[j] for j in range(8)) for h in range(16)]
    if not all(v in (0,1) for v in inner):continue
    x=[0]*24
    for i,v in zip(I,inner):x[i]=int(v)
    for j,v in zip(J,bits):x[j]=v
    assert sum(x)==12
    assert all(sum(M[i][j]*x[j] for j in range(24))==3 for i in range(24))
    solutions.append(tuple(i+1 for i,v in enumerate(x) if v))
assert len(solutions)==64 and len(set(solutions))==64
ss={frozenset(S) for S in solutions}
assert all(frozenset(set(range(1,25))-set(S)) in ss for S in solutions)
print('VERIFIED: 24 lines, 32 triple points, 96 incident pairs, clique number <=3')
print('VERIFIED: line lattice rank 16, discriminant 1728; H has order 3 modulo it')
print('VERIFIED: adjoined H lattice discriminant 192')
print('VERIFIED: precisely 64 twelve-line cubic sections, 32 complementary pairs')
print('REPRESENTATIVE:',solutions[0])
