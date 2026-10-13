#!/usr/bin/env python3
"""Independent brute-force verification of the commuting-idempotent rank enumerator for finite sandwich matrix semigroups. Public reusable checker."""
from itertools import product
from collections import Counter
from math import prod

def operation_tables(q):
    if q == 4:
        add=lambda a,b:a^b
        def mul(a,b):
            a0,a1=a&1,(a>>1)&1
            b0,b1=b&1,(b>>1)&1
            z0=(a0*b0) ^ (a1*b1)
            z1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
            return z0 | (z1<<1)
    else:
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
    return add,mul

def mm(A,B,add,mul):
    h,k=len(A),len(B)
    w=len(B[0])
    return tuple(tuple(__import__('functools').reduce(add,(mul(A[i][t],B[t][j]) for t in range(k)),0) for j in range(w)) for i in range(h))

def rank(A,q,add,mul):
    M=[list(row) for row in A]; h=len(M);w=len(M[0]); piv=0
    for j in range(w):
        i=next((i for i in range(piv,h) if M[i][j]!=0),None)
        if i is None: continue
        M[piv],M[i]=M[i],M[piv]
        iv=next(a for a in range(1,q) if mul(a,M[piv][j])==1)
        M[piv]=[mul(iv,x) for x in M[piv]]
        for ii in range(h):
            if ii!=piv and M[ii][j]:
                z=M[ii][j]
                M[ii]=[add(x,neg(mul(z,y),q)) for x,y in zip(M[ii],M[piv])]
        piv+=1
        if piv==h:break
    return piv

def neg(x,q):
    if q==4 or q==2:return x
    return (-x)%q

def gl(k,q):
    return prod(q**k-q**i for i in range(k))

def prediction(m,n,r,q):
    tau=m+n-2*r
    z=Counter()
    for a in range(r+1):
      for b in range(r-a+1):
       for c in range(r-a-b+1):
        d=r-a-b-c
        coeff=gl(r,q)//prod(gl(j,q) for j in (a,b,c,d))
        z[(b+d,c+d)]+=coeff*q**(tau*(b+c+d))
    return z

def direct(m,n,r,q):
    add,mul=operation_tables(q)
    J=tuple(tuple(1 if i==j and i<r else 0 for j in range(m)) for i in range(n))
    E=[]
    for entries in product(range(q),repeat=m*n):
        X=tuple(tuple(entries[i*n+j] for j in range(n)) for i in range(m))
        XJ=mm(X,J,add,mul)
        if mm(XJ,X,add,mul)==X:
            E.append((X,XJ,rank(X,q,add,mul)))
    z=Counter()
    for X,XJ,ri in E:
        for Y,YJ,rj in E:
            if mm(XJ,Y,add,mul)==mm(YJ,X,add,mul):
                z[(ri,rj)]+=1
    return z,len(E)

def main():
    for m,n,r,q in [(2,2,1,2),(2,3,1,2),(3,2,1,2),(3,3,2,2),(3,3,3,2),(2,2,1,3),(2,2,2,3),(2,2,1,4),(2,3,1,3),(1,2,1,4)]:
        observed,e=direct(m,n,r,q)
        predicted=prediction(m,n,r,q)
        assert observed==predicted,(m,n,r,q,observed,predicted)
        print('checked',m,n,r,q,'idempotents',e,'commuting_pairs',sum(predicted.values()))
    print('VERIFY_OK')
if __name__=='__main__':main()
