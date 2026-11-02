#!/usr/bin/env python3
"""Self-contained exhaustive small-field checks for determinant-conditioned diagonals."""
from itertools import product
from collections import Counter

def det(m, p):
    n=len(m)
    a=[list(row) for row in m]
    z=1
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]%p),None)
        if pivot is None:return 0
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k];z=-z
        d=a[k][k]%p;z=z*d%p;inv=pow(d,-1,p)
        for i in range(k+1,n):
            mult=a[i][k]*inv%p
            for j in range(k+1,n):a[i][j]=(a[i][j]-mult*a[k][j])%p
    return z%p

def count(p,diag):
    n=len(diag); c=Counter()
    ij=[(i,j) for i in range(n) for j in range(n) if i!=j]
    for values in product(range(p),repeat=n*(n-1)):
        a=[[0]*n for _ in range(n)]
        for i in range(n):a[i][i]=diag[i]
        for (i,j),v in zip(ij,values):a[i][j]=v
        v=det(a,p)
        if v:c[v]+=1
    return c

def check():
    cases=[(2,(0,0)),(2,(1,1)),(3,(1,1)),(3,(0,1)),(5,(2,4)),
           (3,(1,1,1)),(3,(0,1,2)),(2,(1,0,1,1)),(2,(1,1,1,1))]
    for p,diag in cases:
        c=count(p,diag); total=sum(c.values()); n=len(diag)
        prod=1
        for x in diag: prod=prod*x%p
        h=p**(n*(n-1)//2)
        for d in range(1,p):
            if not prod:
                assert total%(p-1)==0
                want=total//(p-1)
            else:
                assert (total-h)%(p-1)==0
                want=(total-h)//(p-1)+(h if d==prod else 0)
            assert c[d]==want,(p,diag,d,c,want)
        print('CASE_OK',p,diag,dict(sorted(c.items())))
    print('VERIFY_OK',len(cases),'exhaustive configurations')
if __name__=='__main__':check()
