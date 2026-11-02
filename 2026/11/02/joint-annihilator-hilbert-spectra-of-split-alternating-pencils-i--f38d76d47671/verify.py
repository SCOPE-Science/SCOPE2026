#!/usr/bin/env python3
"""Exhaustive finite-field validation of common annihilators for split alternating pencils."""
from itertools import product, combinations
from math import comb
from collections import Counter
MOD={1:0b11,2:0b111,3:0b1011}
def mul(a,b,d):
    p=MOD[d]; h=1<<d; z=0
    while b:
        if b&1:z^=a
        b>>=1; a<<=1
        if a&h:a^=p
    return z
def inv(a,d):
    assert a
    for v in range(1,1<<d):
        if mul(a,v,d)==1:return v
    raise ValueError(a)
def rank(M,n,d):
    if not M:return 0
    A=[row[:] for row in M]; i=0
    for j in range(n):
        t=next((k for k in range(i,len(A)) if A[k][j]),None)
        if t is None:continue
        A[i],A[t]=A[t],A[i]; u=inv(A[i][j],d)
        A[i]=[mul(u,a,d) for a in A[i]]
        for k in range(i+1,len(A)):
            v=A[k][j]
            if v:A[k]=[x^mul(v,y,d) for x,y in zip(A[k],A[i])]
        i+=1
        if i==len(A):break
    return i
def actual(r,lambdas,d):
    m=2*r; arr=[]
    for j in range(m+1):
        ss=[i for i in range(1<<m) if i.bit_count()==j]
        tt=[i for i in range(1<<m) if i.bit_count()==j+2]
        di={i:p for p,i in enumerate(tt)}
        d1=[[0]*len(ss) for _ in tt];d2=[[0]*len(ss) for _ in tt]
        for col,mask in enumerate(ss):
            for i,lam in enumerate(lambdas):
                two=3<<(2*i)
                if mask&two==0:
                    d1[di[mask|two]][col]^=1
                    d2[di[mask|two]][col]^=lam
        arr.append(len(ss)-rank(d1+d2,len(ss),d))
    return arr
def predicted(r,lambdas):
    out=[0]*(2*r+1)
    out[r]+=2**r
    for sz in range(1,r+1):
        for T in combinations(range(r),sz):
            equal=len({lambdas[i] for i in T})==1
            low=2 if equal else 4
            for k in range(sz if equal else sz-1):
                # dependent: t^2 (1+t^2)^(sz-1); independent: t^4 (1+t^2)^(sz-2)
                bound=sz-1 if equal else sz-2
                if k>bound:continue
                out[r-sz+low+2*k]+=2**(r-sz)*comb(bound,k)
    return out
def main():
    count=0
    for d in [1,2,3]:
        q=1<<d
        for r in range(1,5 if d==1 else 4):
            for lambdas in product(range(q),repeat=r):
                a=actual(r,lambdas,d)
                p=predicted(r,lambdas)
                assert a==p,(d,r,lambdas,a,p)
                total=2**(r-2)*(2**r+3+sum(2**v-1 for v in Counter(lambdas).values()))
                assert sum(a)==total,(d,r,lambdas,a,total)
                count+=1
            print('CASE',q,r,q**r)
    print('SPLIT_ALTERNATING_PENCIL_COMMON_KERNEL_OK',count)
if __name__=='__main__':main()
