#!/usr/bin/env python3
"""Independent characteristic-three Hom-Jacobi rank computation.

Uses flattened elementary matrices, an alternative basis ordering, and
incremental elimination of linear constraint columns over the prime field.
"""
from itertools import combinations

q=3
units=((1,2),(2,0),(0,1),(2,1),(0,2),(1,0))

def unit(a,b):
    v=[0]*9;v[3*a+b]=1;return v

def bracket(x,y):
    return [sum(x[3*i+t]*y[3*t+j]-y[3*i+t]*x[3*t+j] for t in range(3))%q for i in range(3) for j in range(3)]

def coords(M,projective):
    entries=[M[3*i+j] for i,j in units]
    if projective:return entries+[(M[0]-M[8])%q]
    return entries+[(-M[8])%q,M[0]%q]

def basis(projective):
    mats=[unit(i,j) for i,j in units]
    # This order is deliberately different from the other verifier.
    h2=[0,0,0,0,1,0,0,0,-1];mats.append(h2)
    if not projective:
        h1=[1,0,0,0,-1,0,0,0,0];mats.append(h1)
    return mats

def rref_rank(rows,n):
    # Maintain a pivot row with normalized leading coefficient, eliminating all new rows.
    piv={}
    for row in rows:
        v=[a%3 for a in row]
        for j in sorted(piv):
            if v[j]:
                f=v[j];v=[(a-f*b)%q for a,b in zip(v,piv[j])]
        for j,x in enumerate(v):
            if x:
                m=pow(x,-1,q);piv[j]=[(m*z)%q for z in v];break
    return len(piv)

def evaluate(projective):
    B=basis(projective);n=len(B)
    C=[[[0]*n for _ in range(n)] for __ in range(n)]
    # Output coefficients in alternate basis for each input commutator.
    for i in range(n):
        for j in range(n):C[i][j]=coords(bracket(B[i],B[j]),projective)
    R=[]
    for a,b,c in combinations(range(n),3):
        for out in range(n):
            eq=[0]*(n*n)
            for first,second,argument in ((a,b,c),(b,c,a),(c,a,b)):
                for target in range(n):
                    term=sum(C[first][second][inner]*C[inner][target][out] for inner in range(n))
                    eq[n*argument+target]=(eq[n*argument+target]+term)%q
            R.append(eq)
    dim=n*n-rref_rank(R,n*n)
    return dim

if __name__=='__main__':
    d7=evaluate(True);d8=evaluate(False)
    assert (d7,d8)==(1,9),(d7,d8)
    print('Independent basis/rank: HomLie(psl3) =',d7,', HomLie(sl3) =',d8)
    print('VERIFY_OK')
