#!/usr/bin/env python3
"""Exact finite-field checks of the star-structured determinant rank strata.
Proof for all m is given separately in the accompanying mathematical text;
finite checks here are corroboration, not an all-size certification.
"""
from itertools import product
from math import comb

def determinant(M,p):
    a=[list(row) for row in M]; n=len(a); r=0; d=1
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]%p),None)
        if pivot is None: return 0
        if pivot!=j:
            a[pivot],a[j]=a[j],a[pivot]; d=-d
        c=a[j][j]%p; d=d*c%p
        inv=pow(c,-1,p)
        for i in range(j+1,n):
            t=a[i][j]*inv%p
            for k in range(j+1,n):a[i][k]=(a[i][k]-t*a[j][k])%p
            a[i][j]=0
    return d%p

def rank(M,p):
    a=[list(row) for row in M]; rows=len(a); cols=len(a[0]); q=0
    for j in range(cols):
        pivot=next((i for i in range(q,rows) if a[i][j]%p),None)
        if pivot is None:continue
        a[pivot],a[q]=a[q],a[pivot]
        inv=pow(a[q][j]%p,-1,p)
        for k in range(j,cols):a[q][k]=a[q][k]*inv%p
        for i in range(q+1,rows):
            t=a[i][j]
            for k in range(j,cols):a[i][k]=(a[i][k]-t*a[q][k])%p
        q+=1
        if q==rows:break
    return q

def mat(a,b):
    m=len(b); M=[[0]*(m+1) for _ in range(m+1)]; M[0][0]=a[0]
    for i in range(m):M[0][i+1]=M[i+1][0]=b[i];M[i+1][i+1]=a[i+1]
    return M

def prod(xs):
    z=1
    for x in xs:z*=x
    return z

def formula(a,b):
    m=len(b)
    return a[0]*prod(a[1:])-sum(b[i]**2*prod(a[1:j+1]+a[j+2:]) for i,j in [(i,i) for i in range(m)])

def smaller(a,b,i):
    return formula([a[0]]+[a[j+1] for j in range(len(b)) if j!=i],[v for j,v in enumerate(b) if j!=i])

def in_components(a,b,p):
    m=len(b)
    zs=[i for i in range(m) if a[i+1]%p==b[i]%p==0 and smaller(a,b,i)%p==0]
    ts=sum(a[i+1]%p==0 for i in range(m))>=3
    return bool(zs) or ts

def gradient(a,b,p):
    m=len(b); ds=[prod(a[1:])]
    for i in range(m):
        h=a[0]*prod([a[j+1] for j in range(m) if j!=i])
        h-=sum(b[k]**2*prod([a[j+1] for j in range(m) if j!=i and j!=k]) for k in range(m) if k!=i)
        ds.append(h)
    ds.extend(-2*b[i]*prod([a[j+1] for j in range(m) if j!=i]) for i in range(m))
    return all(z%p==0 for z in ds)

def run(m,p):
    n=m+1; seen=0; singular=0
    for coords in product(range(p),repeat=2*m+1):
        if all(x==0 for x in coords):continue
        # one representative of each projective point
        first=next(x for x in coords if x)
        if first!=1:continue
        a=list(coords[:m+1]);b=list(coords[m+1:])
        F=formula(a,b)%p
        assert F==determinant(mat(a,b),p),(m,p,a,b)
        g=gradient(a,b,p);c=in_components(a,b,p)
        assert g==c,(m,p,a,b,g,c)
        if g:
            assert F==0 and rank(mat(a,b),p)<=m-1,(a,b)
            singular+=1
        else:
            assert rank(mat(a,b),p)>m-1,(a,b)
        seen+=1
    assert m*m+comb(m,3)==comb(m+2,3)
    print(f'm={m},p={p}: {seen} projective points, {singular} singular points: OK')

if __name__=='__main__':
    run(3,3)
    run(3,5)
    run(4,3)
    print('VERIFY_OK')
