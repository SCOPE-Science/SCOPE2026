#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product

def solve(A,b):
    n=len(A)
    M=[[Fraction(x) for x in A[i]]+[Fraction(b[i])] for i in range(n)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if M[r][col]),None)
        if pivot is None:
            return None
        M[col],M[pivot]=M[pivot],M[col]
        q=M[col][col]
        M[col]=[x/q for x in M[col]]
        for r in range(n):
            if r==col:
                continue
            q=M[r][col]
            if q:
                M[r]=[M[r][j]-q*M[col][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def brute(c,k):
    n=len(c)
    C=sum(c)
    L=[i for i,ci in enumerate(c) if k<C-ci]
    U=[i for i,ci in enumerate(c) if k>ci]

    # Variables x_1,...,x_n,delta.  All rows encode lhs >= rhs.
    rows=[]
    for i,ci in enumerate(c):
        row=[0]*(n+1); row[i]=1
        rows.append((row,0))
        row=[0]*(n+1); row[i]=-1
        rows.append((row,-ci))
    for i in L:
        row=[0]*(n+1); row[i]=1; row[-1]=-1
        rows.append((row,0))
    for i in U:
        row=[0]*(n+1); row[i]=-1; row[-1]=-1
        rows.append((row,-c[i]))
    row=[0]*(n+1); row[-1]=1
    rows.append((row,0))

    best=Fraction(-1)
    # One equality plus n active inequalities determines a candidate LP vertex.
    for active in combinations(range(len(rows)),n):
        A=[[1]*n+[0]]
        b=[k]
        for j in active:
            A.append(rows[j][0])
            b.append(rows[j][1])
        sol=solve(A,b)
        if sol is None:
            continue
        if all(sum(Fraction(a)*x for a,x in zip(row,sol)) >= Fraction(rhs)
               for row,rhs in rows):
            best=max(best,sol[-1])
    return best,L,U

cases=[
    ((1,1,1),1),((1,1,1),2),
    ((1,2,3),1),((1,2,3),2),((1,2,3),3),((1,2,3),5),
    ((2,3,5),2),((2,3,5),4),((2,3,5),7),((2,3,5),9),
    ((1,4,7),2),((1,4,7),5),((1,4,7),10),
    ((1,1,2,4),1),((1,1,2,4),3),((1,1,2,4),5),((1,1,2,4),7),
    ((2,3,4,6),2),((2,3,4,6),5),((2,3,4,6),8),((2,3,4,6),13),
    ((1,3,7,9),4),((1,3,7,9),10),((1,3,7,9),17),
]
checked=0
for c,k in cases:
    n=len(c)
    C=sum(c)
    assert 0<k<C and n>=3
    want=min(Fraction(k,n),Fraction(C-k,n),Fraction(min(c),2))
    got,L,U=brute(c,k)
    assert got==want,(c,k,want,got,L,U)

    # Independent facet-dimension test by the residual-sum criterion.
    for i,ci in enumerate(c):
        lower=(0<k<C-ci)
        upper=(0<k-ci<C-ci)
        assert lower==(i in L)
        assert upper==(i in U)
    checked+=1

print(f"VERIFY_OK prism-slice-inradius cases={checked} active_set_lp=yes")
