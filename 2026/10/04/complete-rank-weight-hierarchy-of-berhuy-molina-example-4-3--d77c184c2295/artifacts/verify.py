#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))
P=3
# GF(9)=GF(3)[i]/(i^2+1), represented by (a,b)=a+b*i, so i^2=2.
def add(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def neg(x): return ((-x[0])%P,(-x[1])%P)
def mul(x,y):
    a,b=x; c,d=y
    return ((a*c+2*b*d)%P,(a*d+b*c)%P)
Z=(0,0); O=(1,0); I=(0,1)
assert mul(I,I)==(2,0)

def padd(a,b):
    n=max(len(a),len(b)); out=[Z]*n
    for k in range(n): out[k]=add(a[k] if k<len(a) else Z,b[k] if k<len(b) else Z)
    while len(out)>1 and out[-1]==Z: out.pop()
    return out

def pmul(a,b):
    out=[Z]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b): out[j+k]=add(out[j+k],mul(x,y))
    while len(out)>1 and out[-1]==Z: out.pop()
    return out

# (x-i)(x+i)=x^2+1 over GF(9).
assert pmul([neg(I),O],[I,O])==[O,Z,O]

G1=[[tuple(x) for x in row] for row in cert['component1_generator_matrix_pairs']]
assert G1==[
    [neg(I),O,Z,Z],
    [Z,neg(I),O,Z],
    [Z,Z,neg(I),O],
]

# Rank over GF(3).
def rank3(A):
    A=[[x%3 for x in r] for r in A]
    if not A:return 0
    m=len(A); n=len(A[0]); rr=0
    for c in range(n):
        p=next((j for j in range(rr,m) if A[j][c]),None)
        if p is None: continue
        A[rr],A[p]=A[p],A[rr]
        inv=1 if A[rr][c]==1 else 2
        A[rr]=[(inv*x)%3 for x in A[rr]]
        for j in range(m):
            if j!=rr and A[j][c]:
                q=A[j][c]
                A[j]=[(A[j][t]-q*A[rr][t])%3 for t in range(n)]
        rr+=1
        if rr==m:break
    return rr

# Explicit rank-one and rank-two base-field words in C1.
w1=[tuple(x) for x in cert['component1_rank_one_word_pairs']]
B2=[[tuple(x) for x in row] for row in cert['component1_rank_two_basis_pairs']]
assert w1==[O,Z,O,Z]
assert B2==[[O,Z,O,Z],[Z,O,Z,O]]
assert rank3([[x[0] for x in row] for row in B2])==2

# Verify w1=i*r0+r1 and shift=x*w1=i*r1+r2.
def smul(a,row): return [mul(a,x) for x in row]
def vadd(a,b): return [add(x,y) for x,y in zip(a,b)]
assert vadd(smul(I,G1[0]),G1[1])==B2[0]
assert vadd(smul(I,G1[1]),G1[2])==B2[1]

# Expand generator rows in basis 1,i. The K-row support must have rank 4.
support_rows=[]
for row in G1:
    support_rows.append([x[0] for x in row])
    support_rows.append([x[1] for x in row])
assert rank3(support_rows)==4
C1=[1,2,4]

# C2 is one-dimensional and generated over the base field by (x+1)^2.
g2=[tuple(x) for x in cert['component2_generator_pairs']]
assert g2==[O,(2,0),O]
assert rank3([[x[0] for x in g2]])==1
C2=[1]

# Exact generalized-weight convolution; M_0=0.
def conv(A,B):
    k=len(A)+len(B); out=[]
    AA=[0]+A; BB=[0]+B
    for r in range(1,k+1):
        vals=[]
        for a in range(0,len(A)+1):
            b=r-a
            if 0<=b<=len(B): vals.append(AA[a]+BB[b])
        out.append(min(vals))
    return out
hier=conv(C1,C2)
assert hier==[1,2,3,5]
assert hier==cert['full_hierarchy']
assert cert['active_component_dimensions']==[3,1]
assert cert['length']==9 and cert['dimension']==4
print('VERIFY_OK')
