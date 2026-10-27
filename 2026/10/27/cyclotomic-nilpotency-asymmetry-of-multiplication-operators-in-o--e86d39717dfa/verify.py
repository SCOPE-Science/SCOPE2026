#!/usr/bin/env python3
"""Exact finite-field verification of multiplication-rank distributions for odd dihedral quandles.
Standard library only; constructs the nonassociative multiplication matrices directly.
"""
from collections import Counter
from itertools import product
from math import prod

class Field:
    def __init__(self,p,mod=None):
        self.p=p; self.mod=mod or [0,1]
        self.k=len(self.mod)-1; self.q=p**self.k
        self.vectors=[self.digits(a) for a in range(self.q)]
        self.add=[[self.encode([(x+y)%p for x,y in zip(self.vectors[a],self.vectors[b])])
                   for b in range(self.q)] for a in range(self.q)]
        self.mul=[[self.mulraw(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inv=[None]+[next(b for b in range(1,self.q) if self.mul[a][b]==1)
                         for a in range(1,self.q)]
    def digits(self,a):
        x=[]
        for _ in range(self.k): x.append(a%self.p);a//=self.p
        return x
    def encode(self,x):return sum(v*self.p**i for i,v in enumerate(x))
    def mulraw(self,a,b):
        t=[0]*(2*self.k-1)
        for i,x in enumerate(self.vectors[a]):
            for j,y in enumerate(self.vectors[b]):t[i+j]=(t[i+j]+x*y)%self.p
        for i in range(len(t)-1,self.k-1,-1):
            h=t[i]
            for j in range(self.k):t[i-self.k+j]=(t[i-self.k+j]-h*self.mod[j])%self.p
        return self.encode(t[:self.k])
    def sub(self,a,b):return self.add[a][self.neg(b)]
    def neg(self,a):return self.encode([(-u)%self.p for u in self.vectors[a]])

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def divmodpoly(a,b,F):
    a=trim(a);b=trim(b)
    if b==[0]:raise ZeroDivisionError
    q=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        d=len(a)-len(b); c=F.mul[a[-1]][F.inv[b[-1]]];q[d]=c
        for i,v in enumerate(b):a[i+d]=F.sub(a[i+d],F.mul[c][v])
        a=trim(a)
    return trim(q),a

def gcddegree(a,b,F):
    a=trim(a);b=trim(b)
    while b!=[0]:
        _,r=divmodpoly(a,b,F); a,b=b,r
    return len(a)-1

def factor(f,F):
    f=trim(f);ans=[]; degree=1
    while len(f)>1:
        if degree>=len(f):
            ans.append((f,1));break
        found=False
        for coeff in product(range(F.q),repeat=degree):
            g=list(coeff)+[1]
            cnt=0
            while len(f)>=len(g):
                h,r=divmodpoly(f,g,F)
                if r!=[0]:break
                cnt+=1;f=h
            if cnt:
                ans.append((g,cnt));found=True;break
        if not found:degree+=1
    return ans

def rank(M,F):
    B=[row[:] for row in M]; nr=len(B);nc=len(B[0]);r=0
    for j in range(nc):
        piv=next((i for i in range(r,nr) if B[i][j]),None)
        if piv is None:continue
        B[r],B[piv]=B[piv],B[r]
        iv=F.inv[B[r][j]]
        for z in range(j,nc):B[r][z]=F.mul[iv][B[r][z]]
        for i in range(nr):
            if i!=r and B[i][j]:
                a=B[i][j]
                for z in range(j,nc):B[i][z]=F.sub(B[i][z],F.mul[a][B[r][z]])
        r+=1
        if r==nr:break
    return r

def product_rank(a,n,F,left=True):
    M=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # Left multiplier a: sum_i a_i (e_i*e_j) ; right multiplier a: sum_j a_j (e_i*e_j).
            if left:
                M[(2*j-i)%n][j]=F.add[M[(2*j-i)%n][j]][a[i]]
            else:
                M[(2*j-i)%n][i]=F.add[M[(2*j-i)%n][i]][a[j]]
    return rank(M,F)

def predicted(n,F):
    poly=[F.neg(1)]+[0]*(n-1)+[1]
    ff=factor(poly,F)
    assert sum((len(f)-1)*e for f,e in ff)==n,(n,F.q,ff)
    counts={0:1}
    for f,e in ff:
        d=len(f)-1
        part={0:1}
        for k in range(1,e+1):part[k*d]=F.q**(d*k)-F.q**(d*(k-1))
        nxt=Counter()
        for i,a in counts.items():
            for j,b in part.items():nxt[i+j]+=a*b
        counts=dict(nxt)
    return counts,ff

def check(n,F,check_pairs=False):
    pre,ff=predicted(n,F)
    observed=Counter();a_list=list(product(range(F.q),repeat=n))
    for a in a_list:
        L=product_rank(a,n,F,True)
        R=product_rank(a,n,F,False)
        assert L==R,(n,F.q,a,L,R)
        A=list(a)
        poly=[F.neg(1)]+[0]*(n-1)+[1]
        expected=n-gcddegree(A,poly,F)
        assert L==expected,(n,F.q,a,L,expected)
        observed[L]+=1
    assert dict(observed)=={k:v for k,v in pre.items() if v},(n,F.q,observed,pre)
    predicted_zero=sum(pre.get(r,0)*F.q**(n-r) for r in range(n+1))
    # Integer product of rational factors, without premature division:
    numerator=F.q**n
    denominator=1
    for f,e in ff:
        d=len(f)-1
        numerator*=((e+1)*F.q**d-e)
        denominator*=F.q**d
    assert numerator%denominator==0
    assert predicted_zero==numerator//denominator
    if check_pairs:
        N=0
        for a in a_list:
            for b in a_list:
                c=[0]*n
                for i,x in enumerate(a):
                    if x:
                        for j,y in enumerate(b):
                            if y:c[(2*j-i)%n]=F.add[c[(2*j-i)%n]][F.mul[x][y]]
                if not any(c):N+=1
        assert N==predicted_zero,(n,F.q,N,predicted_zero)
    print('PASS n=%d q=%d factors=%s spectrum=%s zero_pairs=%d'%(n,F.q,[(len(f)-1,e) for f,e in ff],sorted(pre.items()),predicted_zero))
    return len(a_list)

if __name__=='__main__':
    cases=[(3,Field(2),True),(3,Field(3),True),(5,Field(2),True),
           (5,Field(3),False),(7,Field(2),False),(7,Field(3),False),
           (9,Field(2),False),(11,Field(2),False),(3,Field(5),False),
           (3,Field(7),False),(5,Field(2,[1,1,1]),False),
           (3,Field(2,[1,1,0,1]),False),(3,Field(3,[1,0,1]),False)]
    total=0
    for n,F,cp in cases:total+=check(n,F,cp)
    print('ALL_ODD_DIHEDRAL_QUANDLE_RANK_TESTS_PASSED cases=%d elements=%d'%(len(cases),total))
