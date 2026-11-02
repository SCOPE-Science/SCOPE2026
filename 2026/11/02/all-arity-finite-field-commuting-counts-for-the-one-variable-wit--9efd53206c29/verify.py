#!/usr/bin/env python3
"""Finite-field elimination checks for commuting tuples of truncated derivations."""
from itertools import product

def arithmetic(p, modulus=None):
    d=1 if modulus is None else len(modulus)
    q=p**d
    def mul(a,b):
        if d==1:return a*b%p
        aa=[(a//p**i)%p for i in range(d)]
        bb=[(b//p**i)%p for i in range(d)]
        c=[0]*(2*d-1)
        for i,x in enumerate(aa):
            for j,y in enumerate(bb):c[i+j]=(c[i+j]+x*y)%p
        for h in range(2*d-2,d-1,-1):
            w=c[h]
            for j in range(d):c[h-d+j]=(c[h-d+j]-w*modulus[j])%p
        return sum(c[i]*p**i for i in range(d))
    add=lambda a,b:sum((((a//p**i)%p+(b//p**i)%p)%p)*p**i for i in range(d))
    neg=lambda a:sum((-(a//p**i)%p)*p**i for i in range(d))
    one=1
    def power(a,n):
        c=one
        while n:
            if n&1:c=mul(c,a)
            a=mul(a,a);n//=2
        return c
    inv=lambda a:power(a,q-2)
    return q,mul,add,neg,inv

def rref(mat,p,field):
    q,mul,add,neg,inv=field
    a=[list(row) for row in mat]
    h=len(a);w=len(a[0]);z=0;pivot=[]
    for j in range(w):
        i=next((i for i in range(z,h) if a[i][j]),None)
        if i is None:continue
        a[z],a[i]=a[i],a[z]
        c=inv(a[z][j]);a[z]=[mul(x,c) for x in a[z]]
        for i in range(h):
            if i!=z and a[i][j]:
                c=neg(a[i][j]);a[i]=[add(x,mul(c,y)) for x,y in zip(a[i],a[z])]
        pivot.append(j);z+=1
        if z==h:break
    return z,pivot,a

def null_vectors(mat,p,field):
    q,mul,add,neg,inv=field
    n=len(mat[0]);r,piv,a=rref(mat,p,field)
    free=[j for j in range(n) if j not in piv]
    for vals in product(range(q),repeat=len(free)):
        g=[0]*n
        for j,v in zip(free,vals):g[j]=v
        for i,j in enumerate(piv):
            s=0
            for k in free:s=add(s,mul(a[i][k],g[k]))
            g[j]=neg(s)
        yield tuple(g)

def ad(f,p,field):
    q,mul,add,neg,inv=field
    mat=[[0]*p for _ in range(p)]
    for i,c in enumerate(f):
        if c==0:continue
        for j in range(p):
            h=i+j-1
            if 0<=h<p:
                v=(j-i)%p
                mat[h][j]=add(mat[h][j],mul(c,v))
    return mat

def formula(p,q,m):
    s=(p-1)//2
    return 1+(q**m-1)*(q**(p-1)+sum(q**(p-2*r+(r-1)*m) for r in range(1,s+1)) +sum(q**((p-r-1)*m) for r in range(s+1,p)))

def verify(p,mod=None):
    field=arithmetic(p,mod);q=field[0]
    fs=list(product(range(q),repeat=p))
    ads={f:ad(f,p,field) for f in fs}
    paircount=0;triplecount=0
    for f in fs:
        a=ads[f]
        vals=next((j for j,v in enumerate(f) if v!=0),p)
        # Exact rank from elimination, not from the proposed stratum formula.
        cdim=p-rref(a,p,field)[0]
        if vals==p: want=p
        elif vals==0: want=1
        elif 2*vals<=p: want=vals
        else:want=vals-1
        assert cdim==want,(p,q,f,cdim,want)
        for g in null_vectors(a,p,field):
            paircount+=1
            c=p-rref(a+ads[g],p,field)[0]
            triplecount+=q**c
    assert paircount==formula(p,q,2),(p,q,paircount,formula(p,q,2))
    assert triplecount==formula(p,q,3),(p,q,triplecount,formula(p,q,3))
    print('field',q,'char',p,'tuple2',paircount,'tuple3',triplecount)

if __name__=='__main__':
    verify(2)
    verify(2,(1,1))      # F_4 = F_2[u]/(u^2+u+1)
    verify(3)
    verify(3,(1,0))      # F_9 = F_3[u]/(u^2+1)
    verify(5)
    assert formula(7,7,1)==7**7
    assert formula(11,11,0)==1
    print('WITT_ALL_ARITY_POINT_COUNT_OK')
