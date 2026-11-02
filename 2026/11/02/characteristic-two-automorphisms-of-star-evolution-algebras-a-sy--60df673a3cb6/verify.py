#!/usr/bin/env python3
"""Checks of characteristic-two star evolution-algebra automorphism formulas."""
from itertools import product
IRRED={1:0b11,2:0b111,3:0b1011}
def mul(a,b,f):
    p=IRRED[f];top=1<<f;mask=top-1;z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&top:a^=p
        a&=mask
    return z

def dot(u,v,f):
    x=0
    for a,b in zip(u,v):x^=mul(a,b,f)
    return x

def rank(M,f):
    a=[list(row) for row in M];n=len(a);r=0;q=1<<f
    for col in range(n):
        ix=next((i for i in range(r,n) if a[i][col]),None)
        if ix is None:continue
        a[r],a[ix]=a[ix],a[r]
        inv=next(x for x in range(1,q) if mul(x,a[r][col],f)==1)
        a[r]=[mul(inv,x,f) for x in a[r]]
        for i in range(n):
            if i!=r and a[i][col]:
                t=a[i][col]
                for j in range(col,n):a[i][j]^=mul(t,a[r][j],f)
        r+=1
    return r

def orthogonal(T,f):
    m=len(T)
    return all(dot([T[k][i] for k in range(m)],[T[k][j] for k in range(m)],f)==int(i==j)
               for i in range(m) for j in range(m))

def algebra_product(x,y,f):
    a,u=x[0],x[1:];b,v=y[0],y[1:]
    return (dot(u,v,f),)+tuple([mul(a,b,f)]*len(u))

def star_aut(M,f):
    n=len(M);m=n-1
    if rank(M,f)!=n:return False
    col=[tuple(M[i][j] for i in range(n)) for j in range(n)]
    for j in range(n):
        y=tuple([0]+[1]*m) if j==0 else tuple([1]+[0]*m)
        x=tuple(0 for _ in range(n))
        for k,b in enumerate(y):
            if b:
                x=tuple(x[i]^mul(b,M[i][k],f) for i in range(n))
        if algebra_product(col[j],col[j],f)!=x:return False
    for i in range(n):
        for j in range(i+1,n):
            if any(algebra_product(col[i],col[j],f)):return False
    return True

def brute_aut(m,f):
    q=1<<f;n=m+1;z=0
    for a in product(range(q),repeat=n*n):
        M=[a[i*n:(i+1)*n] for i in range(n)]
        if star_aut(M,f):z+=1
    return z

def ortho_count(m,f):
    q=1<<f;z=0
    for a in product(range(q),repeat=m*m):
        T=[a[i*m:(i+1)*m] for i in range(m)]
        if orthogonal(T,f):z+=1
    return z

def sp_size(r,q):
    out=q**(r*r)
    for i in range(1,r+1):out*=q**(2*i)-1
    return out

def expected(m,f):
    q=1<<f
    o=sp_size((m-1)//2,q) if m%2 else q**(m-1)*sp_size((m-2)//2,q)
    return (3 if f%2==0 else 1)*o

def main():
    for m,f in [(2,1),(3,1),(2,2)]:
        direct=brute_aut(m,f)
        assert direct==expected(m,f),(m,f,direct,expected(m,f))
        print('DIRECT_ALL_LINEAR_MAPS',m,1<<f,direct)
    for m,f in [(2,1),(3,1),(4,1),(2,2),(3,2)]:
        actual=ortho_count(m,f)
        pred=expected(m,f)//(3 if f%2==0 else 1)
        assert actual==pred,(m,f,actual,pred)
        print('DIRECT_ORTHOGONAL',m,1<<f,actual)
    for m in (2,3,4,5):
        for f in (1,2):
            q=1<<f
            for a in range(1,q):
                if mul(mul(a,a,f),a,f)!=1:continue
                # scalar orthogonal family and original multiplication identity
                T=[[mul(a,a,f)*int(i==j) for j in range(m)] for i in range(m)]
                M=[[0]*(m+1) for _ in range(m+1)]; M[0][0]=a
                for i in range(m):
                    for j in range(m): M[i+1][j+1]=T[i][j]
                assert star_aut(M,f)
    print('CHAR2_STAR_AUTOMORPHISMS_OK')
if __name__=='__main__':main()
