#!/usr/bin/env python3
"""Exact, dependency-free polynomial-identity and Boolean-minor checks."""
import json
from collections import defaultdict
from pathlib import Path

N = 5
POS = [(i,j) for i in range(1,N+1) for j in range(i+1,N+1)]
D = len(POS)
ID = {e:i for i,e in enumerate(POS)}
PSI = {(1,4),(1,5),(2,4),(2,5)}
EXTRA = [((1,3),((3,4),(4,5))),
         ((2,3),((3,4),(4,5))),
         ((3,4),((1,2),(2,3))),
         ((3,5),((1,2),(2,3)))]

# Row indexed by (matrix output, sorted formal commuting monomial in x).
# Column indexed by (matrix output of f, matrix input of f).
def coefficient_matrices():
    R=defaultdict(lambda:defaultdict(int))
    for u,(i,j) in enumerate(POS):
        for a in range(1,N+1):
            for b in range(a+1,N+1):
                for c in range(b+1,N+1):
                    left=ID.get((i,c)) if j==a else None
                    right=ID.get((a,j)) if c==i else None
                    if left is None and right is None:continue
                    aa,bb=ID[(a,b)],ID[(b,c)]
                    for v in range(D):
                        mon=tuple(sorted((aa,bb,v)))
                        if left is not None:R[(left,mon)][u*D+v]+=1
                        if right is not None:R[(right,mon)][u*D+v]-=1
    formal_keys=sorted(R)
    formal=[[R[k].get(i,0) for i in range(D*D)] for k in formal_keys]
    reduced=defaultdict(lambda:[0]*(D*D))
    for k,row in zip(formal_keys,formal):
        out,mon=k
        key=(out,tuple(sorted(set(mon))))
        rr=reduced[key]
        for i,a in enumerate(row):rr[i]+=a
    binary_keys=sorted(reduced)
    binary=[[a%2 for a in reduced[k]] for k in binary_keys]
    return formal_keys,formal,binary_keys,binary

def gf2_rank(rows, width):
    basis={}
    for row in rows:
        v=sum(1<<i for i,a in enumerate(row) if a&1)
        while v:
            k=v.bit_length()-1
            if k not in basis:basis[k]=v;break
            v^=basis[k]
    return len(basis)

def det_bareiss(A):
    """Exact integer determinant; row swaps allowed, no rational rounding."""
    a=[list(x) for x in A]
    n=len(a);sign=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next((i for i in range(k+1,n) if a[i][k]),None)
            if r is None:return 0
            a[k],a[r]=a[r],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            aik=a[i][k]
            for j in range(k+1,n):
                num=a[i][j]*pivot-aik*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def columns_for_map(output, inputs):
    v=[0]*(D*D)
    for p in inputs:v[ID[output]*D+ID[p]]^=1
    return v

def test_null(A,v,mod):
    return all(sum(a*b for a,b in zip(row,v))%mod==0 for row in A)

def main():
    FK,F,BK,B=coefficient_matrices()
    cert=json.loads(Path(__file__).with_name('rank_certificate.json').read_text())
    assert len(FK)==cert['formal']['row_count']==93
    assert len(BK)==cert['binary']['row_count']
    assert len(F[0])==len(B[0])==100
    for kind,mat,expected in [('formal',F,59),('binary',B,55)]:
        d=cert[kind];rows=d['rows'];cols=d['cols']
        assert len(rows)==len(cols)==expected
        assert len(set(rows))==len(rows) and len(set(cols))==len(cols)
        minor=[[mat[r][c] for c in cols] for r in rows]
        if kind=='formal':
            det=det_bareiss(minor)
            assert abs(det)==1 and det==d['determinant']
        else:
            assert gf2_rank(minor,expected)==expected
    # Construct the 41-dimensional common solution space.
    std=[]
    for p in sorted(PSI):
        for inp in POS:std.append(columns_for_map(p,[inp]))
    identity=[0]*100
    for t in range(D):identity[t*D+t]=1
    std.append(identity)
    assert len(std)==41 and gf2_rank(std,100)==41
    for v in std:assert test_null(F,v,1000003) and test_null(B,v,2)
    # Four independent, binary-only solutions.
    extra=[columns_for_map(p,inputs) for p,inputs in EXTRA]
    assert gf2_rank(std+extra,100)==45
    for v in extra:assert test_null(B,v,2)
    assert gf2_rank(F,100)==59
    assert gf2_rank(B,100)==55
    # The formal minor ±1 is valid over *every* field, and 41
    # independent formal solutions provide the opposite rank bound.
    # For q>2 each variable's degree is <=2<q, hence the
    # polynomial vanishes on all F_q^10 iff all formal coefficients vanish.
    # For F2 every coordinate satisfies z^2=z, yielding B.
    print('VERIFY_OK formal rows:',len(FK),'binary rows:',len(BK),
          'ranks:',59,55,'kernel dimensions:',41,45)

if __name__=='__main__':main()
