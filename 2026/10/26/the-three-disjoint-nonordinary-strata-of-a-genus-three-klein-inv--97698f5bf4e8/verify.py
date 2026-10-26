#!/usr/bin/env python3
"""Exact finite-field and Hasse--Witt checks for the genus-three family.
Public scientific verification; no network or non-standard packages.
"""
from collections import Counter

class Field:
    def __init__(self, m, polynomial):
        self.m=m
        self.q=3**m
        assert len(polynomial)==m+1 and polynomial[-1]==1
        self.poly=polynomial
        self.digits=[self.unpack(i) for i in range(self.q)]
        self.addtab=[[self.pack([(a+b)%3 for a,b in zip(self.digits[x],self.digits[y])]) for y in range(self.q)] for x in range(self.q)]
        self.multab=[[self.mulslow(x,y) for y in range(self.q)] for x in range(self.q)]
    def unpack(self,x):
        r=[]
        for _ in range(self.m):r.append(x%3);x//=3
        return r
    def pack(self,d):return sum(x*3**i for i,x in enumerate(d))
    def mulslow(self,x,y):
        a,b=self.digits[x],self.digits[y]
        tmp=[0]*(2*self.m-1)
        for i in range(self.m):
            for j in range(self.m):tmp[i+j]=(tmp[i+j]+a[i]*b[j])%3
        for d in range(2*self.m-2,self.m-1,-1):
            v=tmp[d]
            for j in range(self.m):tmp[d-self.m+j]=(tmp[d-self.m+j]-v*self.poly[j])%3
        return self.pack(tmp[:self.m])
    def add(self,x,y):return self.addtab[x][y]
    def neg(self,x):return self.add(x*0,self.pack([(-t)%3 for t in self.digits[x]]))
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):return self.multab[x][y]
    def power(self,x,n):
        z=1
        while n:
            if n&1:z=self.mul(z,x)
            x=self.mul(x,x); n//=2
        return z
    def inv(self,x):
        assert x
        return self.power(x,self.q-2)

def rank(M,F):
    B=[list(row) for row in M]
    piv=0
    for c in range(len(B[0])):
        i=next((i for i in range(piv,len(B)) if B[i][c]),None)
        if i is None: continue
        B[piv],B[i]=B[i],B[piv]
        inv=F.inv(B[piv][c])
        B[piv]=[F.mul(inv,y) for y in B[piv]]
        for i in range(len(B)):
            if i==piv:continue
            fac=B[i][c]
            if fac:
                B[i]=[F.sub(x,F.mul(fac,y)) for x,y in zip(B[i],B[piv])]
        piv+=1
        if piv==len(B):break
    return piv

def matmul(A,B,F):
    return [[sum_field([F.mul(A[i][k],B[k][j]) for k in range(3)],F) for j in range(3)] for i in range(3)]

def sum_field(a,F):
    z=0
    for x in a:z=F.add(z,x)
    return z

def f_coeff(a,b,F):
    # Direct polynomial multiplication of x^4+a x^2+1 and x^4+b x^2+1
    f=[0]*9
    for i,x in [(0,1),(2,a),(4,1)]:
        for j,y in [(0,1),(2,b),(4,1)]: f[i+j]=F.add(f[i+j],F.mul(x,y))
    return f

def cartier(a,b,F):
    f=f_coeff(a,b,F)
    return [[f[3*(i+1)-(j+1)] for j in range(3)] for i in range(3)]

def elliptic_quotient_hasse(a,b,F):
    # x^2+a*x+1 and x^2+b*x+1: coefficient of x^2 in product
    e_sigma=F.add(F.mul(a,b),2)
    # x^2+a-2, x^2+b-2 and x^2+a+2,x^2+b+2
    e_tau=F.sub(F.add(a,b),1)
    e_sigma_tau=F.add(F.add(a,b),1)
    return [e_sigma,e_tau,e_sigma_tau]

def semilinear_rank(H,F):
    # Three Cartier iterates suffice in genus three. Twist entries by 3^k.
    P=[[int(i==j) for j in range(3)] for i in range(3)]
    for k in range(3):
        twist=[[F.power(v,3**k) for v in row] for row in H]
        P=matmul(P,twist,F)
    return rank(P,F)

def verify(m,poly):
    F=Field(m,poly); q=F.q
    vals=[a for a in range(q) if a not in (1,2)]
    cnt=Counter(); comps=Counter(); bad=[]
    for a in vals:
        for b in vals:
            if a==b:continue
            H=cartier(a,b,F)
            u=F.add(a,b)
            v=F.add(F.mul(a,b),2)
            expected = 3 - sum(z==0 for z in [F.add(u,1),F.sub(u,1),v])
            assert expected == sum(x!=0 for x in elliptic_quotient_hasse(a,b,F))
            found=semilinear_rank(H,F)
            if rank(H,F)!=expected or found!=expected:bad.append((a,b,found,expected,H))
            cnt[found]+=1
            if expected==2:
                if F.add(u,1)==0:comps['a+b=-1']+=1
                if F.sub(u,1)==0:comps['a+b=1']+=1
                if v==0:comps['ab=1']+=1
    assert not bad, bad[:5]
    assert cnt[2]==3*(q-3), (q,cnt)
    assert cnt[3]==(q-3)*(q-5), (q,cnt)
    assert cnt[0]==cnt[1]==0
    assert all(comps[k]==q-3 for k in ('a+b=-1','a+b=1','ab=1')), comps
    print(f'F_{q}: smooth={sum(cnt.values())}, p_rank_2={cnt[2]}, p_rank_3={cnt[3]}, three_components={dict(comps)}')

if __name__=='__main__':
    verify(1,[0,1])
    verify(2,[1,0,1])                 # T^2+1
    verify(3,[1,2,0,1])               # T^3-T+1; no roots in F3
    print('VERIFY_OK')
