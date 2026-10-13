#!/usr/bin/env python3
"""Reproduce square-zero commuting rank counts from direct field-matrix arithmetic."""
from itertools import product
from collections import Counter


def field(q):
    if q == 4:  # F2[z]/(z*z+z+1), digit 2 encodes z
        add = lambda x,y: x ^ y
        def mul(x,y):
            v = 0
            for i in range(2):
                for j in range(2):
                    if ((x>>i)&1) and ((y>>j)&1):
                        v ^= 1<<(i+j)
            if v&8:
                v ^= 0b1001  # z^3 = 1 in F4
            if v&4:
                v ^= 0b111   # z^2 = z+1
            return v
    else:
        add = lambda x,y: (x+y)%q
        mul = lambda x,y: x*y%q
    inverse = {x:next(y for y in range(1,q) if mul(x,y)==1) for x in range(1,q)}
    neg = {x:next(y for y in range(q) if add(x,y)==0) for x in range(q)}
    return add,mul,inverse,neg


def mm(A,B,add,mul):
    n=len(A)
    return [[sumfield([mul(A[i][k],B[k][j]) for k in range(n)],add) for j in range(n)] for i in range(n)]


def sumfield(vals,add):
    s=0
    for x in vals:s=add(s,x)
    return s


def rank(A,add,mul,inv,neg):
    mat=[row[:] for row in A]
    n=len(mat); piv=0
    for j in range(n):
        k=next((i for i in range(piv,n) if mat[i][j]),None)
        if k is None: continue
        mat[piv],mat[k]=mat[k],mat[piv]
        scale=inv[mat[piv][j]]
        mat[piv]=[mul(scale,x) for x in mat[piv]]
        for i in range(n):
            if i==piv or not mat[i][j]:continue
            scale=neg[mat[i][j]]
            mat[i]=[add(x,mul(scale,y)) for x,y in zip(mat[i],mat[piv])]
        piv+=1
        if piv==n:break
    return piv


def from_parameters(a,b,c,n):
    X=[[0]*(n+1) for _ in range(n+1)]
    for j in range(n):
        for i in range(j,n):X[i][j]=a[i-j]
    X[n-1][n]=b
    X[n][0]=c
    return X


def nilpotent(n):
    N=[[0]*(n+1) for _ in range(n+1)]
    for j in range(n-1):N[j+1][j]=1
    return N


def predicted(q,n):
    k=n//2
    res=Counter({0:1,1:2*(q-1)})
    for r in range(1,k+1):res[r]+=(q-1)*(2*q-1)*q**(r-1)
    if n%2:res[k+1]+=(q-1)**2*q**k
    return res


def check(q,n,deep=False):
    add,mul,inv,neg=field(q)
    N=nilpotent(n)
    cnt=Counter(); zero=[[0]*(n+1) for _ in range(n+1)]
    for p in product(range(q),repeat=n+2):
        a=p[:n]; b=p[n];c=p[n+1]
        X=from_parameters(a,b,c,n)
        # Centralizer is checked without reducing to the scalar equations.
        assert mm(X,N,add,mul)==mm(N,X,add,mul)
        if mm(X,X,add,mul)==zero:
            cnt[rank(X,add,mul,inv,neg)]+=1
    expected=predicted(q,n)
    assert cnt==expected,(q,n,cnt,expected)
    if n%2:
        assert sum(cnt.values())==q**(n//2+2)
    else:
        assert sum(cnt.values())==(2*q-1)*q**(n//2)
    print('q',q,'n',n,'tested',q**(n+2),'zero-square rank counts',dict(sorted(cnt.items())))
    if deep:
        size=n+1
        brute=Counter(); commuting=0
        for v in product(range(q),repeat=size*size):
            X=[list(v[i*size:(i+1)*size]) for i in range(size)]
            if mm(X,N,add,mul)!=mm(N,X,add,mul):continue
            commuting+=1
            if mm(X,X,add,mul)==zero:
                brute[rank(X,add,mul,inv,neg)]+=1
        assert commuting==q**(n+3),(q,n,commuting)
        assert brute==expected,(q,n,brute,expected)
        print('  independent ambient exhaustive check',q**(size*size),'matrices; centralizer',commuting)


if __name__=='__main__':
    for q,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(5,2),(5,3)]:
        check(q,n,(q,n) in ((2,2),(2,3),(3,2)))
    print('VERIFY_OK_SQUARE_ZERO_ALMOST_REGULAR')
