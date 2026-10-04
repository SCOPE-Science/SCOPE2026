#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

def det(A):
    A=[list(map(Fraction,row)) for row in A]
    n=len(A); s=Fraction(1)
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None: return Fraction(0)
        if p!=c: A[c],A[p]=A[p],A[c]; s=-s
        piv=A[c][c]; s*=piv
        for j in range(c,n): A[c][j]/=piv
        for r in range(c+1,n):
            f=A[r][c]
            if f:
                for j in range(c,n): A[r][j]-=f*A[c][j]
    return s

def rank(A):
    A=[list(map(Fraction,row)) for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        piv=A[r][c]
        A[r]=[x/piv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def row(x,y): return [x*x,x*y,y*y,x,y,1]
def dx(x,y): return [2*x,y,0,1,0,0]
def dy(x,y): return [0,x,2*y,0,1,0]

pts=[(0,0),(1,0),(2,0),(3,0),(4,0),(0,1)]
M=[row(*p) for p in pts]
assert rank(M)==4
D=[[dx(*p),dy(*p)] for p in pts]

for i in range(6):
    for a in range(2):
        N=[r[:] for r in M]; N[i]=D[i][a][:]
        assert det(N)==0

H=[[Fraction(0) for _ in range(12)] for __ in range(12)]
def vi(i,a): return i if a==0 else 6+i
for i,j in combinations(range(6),2):
    for a in range(2):
        for b in range(2):
            N=[r[:] for r in M]; N[i]=D[i][a][:]; N[j]=D[j][b][:]
            c=det(N); u,v=vi(i,a),vi(j,b); H[u][v]=H[v][u]=c
assert rank(H)==3
A=[[H[6+i][6+j] for j in range(3)] for i in range(3)]
assert det(A)==-576

T=[]
for i in range(5):
    v=[Fraction(0)]*12; v[i]=1; T.append(v)
for k in (5,11):
    v=[Fraction(0)]*12; v[k]=1; T.append(v)
v=[Fraction(0)]*12
for i,t in enumerate([0,1,2,3,4]): v[6+i]=t
T.append(v)
v=[Fraction(0)]*12
for i in range(5): v[6+i]=1
T.append(v)
assert rank(T)==9
for v in T:
    Hv=[sum(H[i][j]*v[j] for j in range(12)) for i in range(12)]
    assert all(z==0 for z in Hv)
print("VERIFY_OK")
