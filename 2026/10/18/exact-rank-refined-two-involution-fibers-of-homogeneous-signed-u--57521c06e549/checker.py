#!/usr/bin/env python3
"""Self-contained exact finite-field tests of reversing-involution fiber formulas."""
from itertools import product
from math import comb

def gb(n,r,q):
    if r < 0 or r > n: return 0
    a=b=1
    for i in range(r):
        a *= q**(n-i)-1
        b *= q**(r-i)-1
    return a//b

def predicted(n,m,q):
    k=n//2
    out={}
    for r in range(m+1):
        a=k*m if n%2==0 else k*m+r
        exp=k*m*m-r*(m-r) if n%2==0 else k*m*m+r*(m-r)
        out[(r,a)]=q**exp*gb(m,r,q)
    return out

def mul(U,V,p,m):
    Z=[0]*(m*m)
    for i in range(m):
        for k in range(m):
            a=U[i*m+k]
            if a:
                for j in range(m): Z[i*m+j]=(Z[i*m+j]+a*V[k*m+j])%p
    return tuple(Z)

def sigma_coefficients(M,p,n,m):
    # Sigma is induced on F_p[x]/x^n by x -> -(x/(1+x)).
    Y=[]
    for ell in range(n):
        row=[0]*(m*m)
        for j in range(ell+1):
            c=(1 if j==ell==0 else 0)
            if j>=1:
                c=(-1)**ell*comb(ell-1,j-1)
            if c:
                for h,z in enumerate(M[j]): row[h]=(row[h]+c*z)%p
        Y.append(tuple(row))
    return Y

def rank(M,p):
    a=[list(row) for row in M]
    if not a: return 0
    nr=len(a); nc=len(a[0]); j=0
    for k in range(nc):
        pivot=next((i for i in range(j,nr) if a[i][k]%p),None)
        if pivot is None: continue
        a[j],a[pivot]=a[pivot],a[j]
        c=pow(a[j][k],-1,p)
        a[j]=[(x*c)%p for x in a[j]]
        for i in range(nr):
            if i==j: continue
            c=a[i][k]
            if c: a[i]=[(x-c*y)%p for x,y in zip(a[i],a[j])]
        j+=1
        if j==nr: break
    return j

def plus_dimension(A,p,n,m):
    # S=A sigma in the polynomial basis of (F_p[x]/x^n)^m.
    size=n*m
    mat=[[0]*size for _ in range(size)]
    for j in range(n):
        for a in range(m):
            vec=[tuple((1 if h==a else 0) if ell==j else 0 for h in range(m)) for ell in range(n)]
            # sigma(x^j) = sum_{ell>=j} (-1)^ell C(ell-1,j-1) x^ell
            for r in range(n):
                val=0 if r<j else (1 if r==j==0 else ((-1)**r*comb(r-1,j-1) if j>0 else 0))
                if val:
                    for i in range(n-r):
                        for b in range(m):
                            mat[(i+r)*m+b][j*m+a] = (mat[(i+r)*m+b][j*m+a] + val*A[i][b*m+a])%p
    for k in range(size): mat[k][k]=(mat[k][k]-1)%p
    return size-rank(mat,p)

def exhaustive(p,n,m):
    ident=tuple(1 if i==j else 0 for i in range(m) for j in range(m))
    zero=(0,)*(m*m)
    options=list(product(range(p),repeat=m*m))
    found={}
    for C in product(options,repeat=n):
        S=sigma_coefficients(C,p,n,m)
        Z=[]
        for t in range(n):
            acc=[0]*(m*m)
            for j in range(t+1):
                v=mul(C[j],S[t-j],p,m)
                for k,x in enumerate(v): acc[k]=(acc[k]+x)%p
            Z.append(tuple(acc))
        if Z[0] != ident or any(x!=zero for x in Z[1:]): continue
        a=plus_dimension(C,p,n,m)
        r=m-rank([[(C[0][i*m+j]-(i==j))%p for j in range(m)] for i in range(m)],p)
        found[(r,a)]=found.get((r,a),0)+1
    expected=predicted(n,m,p)
    assert found==expected,(p,n,m,found,expected)
    return f'GF({p}) n={n} m={m}: {found}'

if __name__=='__main__':
    cases=[(3,1,1),(3,1,2),(3,1,3),(3,2,1),(3,2,2),(3,3,1),(3,3,2),(3,4,1),(3,5,1),
           (5,1,2),(5,2,1),(5,2,2),(5,3,1)]
    for args in cases:print(exhaustive(*args))
    print('ALL_EXACT_CHECKS_PASSED',len(cases))
