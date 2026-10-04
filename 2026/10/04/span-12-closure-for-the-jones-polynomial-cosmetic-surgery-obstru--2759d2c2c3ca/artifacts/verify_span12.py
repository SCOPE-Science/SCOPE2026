#!/usr/bin/env python3
"""Exact stdlib-only verifier for the span-12 Laurent-polynomial certificate."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=json.loads((HERE/'span12_solution_table.json').read_text(encoding='utf-8'))
DET=CERT['determinant_constant']
assert CERT['degree_bound']==12 and CERT['residue_modulus']==60 and DET==6998400000

def peval(p,x):
    s=0
    for a in reversed(p): s=s*x+a
    return s

def falling(x,k):
    y=1
    for a in range(k): y*=x-a
    return y

def matrix_at(R,n):
    r=60*n+R
    rows=[[falling(r+j,k) for j in range(13)] for k in range(5)]
    groups={}
    for m in (3,4,5):
        G=[[1 if (R+j)%m==a else 0 for j in range(13)] for a in range(m)]
        groups[m]=G
    G=groups[3]
    rows += [[G[0][j]-G[2][j] for j in range(13)],
             [G[1][j]-G[2][j] for j in range(13)]]
    G=groups[4]
    rows += [[G[0][j]-G[2][j] for j in range(13)],
             [G[1][j]-G[3][j] for j in range(13)]]
    G=groups[5]
    for a in range(4):
        rows.append([G[a][j]-G[4][j] for j in range(13)])
    return rows

def det_bareiss(A):
    A=[row[:] for row in A]
    N=len(A); sign=1; prev=1
    for k in range(N-1):
        if A[k][k]==0:
            q=next(i for i in range(k+1,N) if A[i][k]!=0)
            A[k],A[q]=A[q],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,N):
            for j in range(k+1,N):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
        prev=pivot
        for i in range(k+1,N): A[i][k]=0
        for j in range(k+1,N): A[k][j]=0
    return sign*A[-1][-1]

def divisors(a):
    a=abs(a)
    out=set()
    if a==0: return out
    d=1
    while d*d<=a:
        if a%d==0: out.add(d); out.add(a//d)
        d+=1
    return out

def trim(p):
    p=p[:]
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def integer_roots(poly):
    p=trim(poly)
    roots=set()
    while len(p)>1 and p[0]==0:
        roots.add(0); p=p[1:]
    if len(p)<=1: return roots
    for d in divisors(p[0]):
        for x in (d,-d):
            if peval(p,x)==0: roots.add(x)
    return roots

rhs=[1,0,0,0,0,1,0,1,0,1,0,0,0]
records=[]
for entry in CERT['residues']:
    R=entry['R']; polys=entry['coeff_polynomials']
    assert len(polys)==13 and all(len(p)==5 for p in polys)

    # Residual degree <= 8: nine exact samples prove each identity.
    for n0 in range(-4,5):
        c=[peval(p,n0) for p in polys]
        M=matrix_at(R,n0)
        assert [sum(row[j]*c[j] for j in range(13)) for row in M]==rhs

    # Determinant degree <= 10: eleven equal exact values prove constant nonzero determinant.
    for n0 in range(11):
        assert det_bareiss(matrix_at(R,n0))==DET

    alt=[0]*5
    for j,p in enumerate(polys):
        s=1 if j%2==0 else -1
        for k,a in enumerate(p): alt[k]+=s*a
    assert alt==entry['P_at_minus1_polynomial']

    found=[]
    for target in (1,-1):
        q=alt[:]; q[0]-=target
        for n0 in sorted(integer_roots(q)):
            found.append((target,n0))
            c=[peval(p,n0) for p in polys]
            r=60*n0+R
            assert [(r+j,v) for j,v in enumerate(c) if v]==[(0,1)]
            records.append((R,target,n0))
    expected=sorted((x['target'],x['n']) for x in entry['integer_roots_abs1'])
    assert sorted(found)==expected

# Regression anchor: the displayed span-12 formal solution in the source.
ex=[peval(p,0) for p in CERT['residues'][1]['coeff_polynomials']]
assert ex==[3,-4,5,-6,6,-7,7,-6,6,-5,4,-3,1]
assert len(records)==13
print('VERIFY_OK residues=60 determinant=6998400000 determinant_compatible=13 all_trivial=true')
