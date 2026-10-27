#!/usr/bin/env python3
"""Exact finite-field checks for a reciprocal genus-four hyperelliptic family.
Only standard Python; all arithmetic is finite-field arithmetic."""
from itertools import product


def coeffs(n, m):
    return tuple((n // 3**i) % 3 for i in range(m))


def polytrim(a):
    z = list(a)
    while z and z[-1] == 0:
        z.pop()
    return z


def modp(a, b):
    a, b = polytrim(a), polytrim(b)
    while len(a) >= len(b):
        c = a[-1] * pow(b[-1], -1, 3) % 3
        j = len(a)-len(b)
        for i,v in enumerate(b):a[j+i] = (a[j+i]-c*v)%3
        a=polytrim(a)
    return a


def irreducible(m):
    if m == 1: return (0,1)
    for low in product(range(3), repeat=m):
        if low[0] == 0:continue
        f = (*low,1)
        if all(modp(f,(*v,1)) for d in range(1,m//2+1)
               for v in product(range(3), repeat=d)):
            return f
    raise AssertionError('no irreducible modulus')

class Field:
    def __init__(self,m):
        self.m,self.q=m,3**m
        self.mod=irreducible(m)
        self.cs=[coeffs(i,m) for i in range(self.q)]
        self.idx={v:i for i,v in enumerate(self.cs)}
        self.add=[[self.idx[tuple((a+b)%3 for a,b in zip(u,v))]
                   for v in self.cs] for u in self.cs]
        self.neg=[self.idx[tuple((-a)%3 for a in u)] for u in self.cs]
        self.mul=[]
        for u in self.cs:
            row=[]
            for v in self.cs:
                s=[0]*(2*m-1)
                for i,a in enumerate(u):
                    for j,b in enumerate(v):s[i+j]=(s[i+j]+a*b)%3
                for k in range(2*m-2,m-1,-1):
                    c=s[k]
                    for j in range(m):s[k-m+j]=(s[k-m+j]-c*self.mod[j])%3
                row.append(self.idx[tuple(s[:m])])
            self.mul.append(row)
        self.inv=[None]*self.q
        for i in range(1,self.q):
            self.inv[i]=next(j for j in range(1,self.q) if self.mul[i][j]==1)

    def a(self,x,y):return self.add[x][y]
    def n(self,x):return self.neg[x]
    def s(self,x,y):return self.a(x,self.n(y))
    def mlt(self,x,y):return self.mul[x][y]
    def div(self,x,y):return self.mul[x][self.inv[y]]
    def power(self,x,k):
        z=1
        while k:
            if k%2:z=self.mlt(z,x)
            x=self.mlt(x,x);k//=2
        return z
    def rank(self,mat):
        A=[list(x) for x in mat]; nr=len(A); nc=len(A[0]); r=0
        for j in range(nc):
            pivot=next((i for i in range(r,nr) if A[i][j]),None)
            if pivot is None: continue
            A[r],A[pivot]=A[pivot],A[r]
            t=self.inv[A[r][j]]
            A[r]=[self.mlt(t,x) for x in A[r]]
            for i in range(nr):
                if i!=r and A[i][j]:
                    c=A[i][j]
                    A[i]=[self.s(z,self.mlt(c,w)) for z,w in zip(A[i],A[r])]
            r+=1
        return r
    def mm(self,A,B):
        return [[self.sum(self.mlt(A[i][k],B[k][j]) for k in range(len(B)))
                    for j in range(len(B[0]))] for i in range(len(A))]
    def sum(self,vals):
        v=0
        for x in vals:v=self.a(v,x)
        return v
    def pgcd(self,a,b):
        a=trim(a);b=trim(b)
        while b:a,b=b,self.prem(a,b)
        return a
    def prem(self,a,b):
        a=trim(a);b=trim(b)
        while len(a)>=len(b) and a:
            c=self.div(a[-1],b[-1]);offset=len(a)-len(b)
            for i,v in enumerate(b):a[i+offset]=self.s(a[i+offset],self.mlt(c,v))
            a=trim(a)
        return a

def trim(a):
    z=list(a)
    while z and z[-1]==0:z.pop()
    return z

def smooth_direct(F,a,b):
    h=[1,a,b,b,a,1]
    deriv=[F.mlt(i%3,h[i]) for i in range(1,6)]
    return len(F.pgcd(h,deriv))==1

def HW(F,a,b):
    return [[a,0,1,0],[0,b,0,a],[a,0,b,0],[0,1,0,a]]

def prank(F,H):
    mat=[[int(i==j) for j in range(4)] for i in range(4)]
    for i in range(4):
        mat=F.mm(mat,[[F.power(x,3**i) for x in row] for row in H])
    return F.rank(mat)

def verify(m):
    F=Field(m);q=F.q
    found={}
    for a in range(q):
        for b in range(q):
            direct=smooth_direct(F,a,b)
            a2=F.mlt(a,a)
            disc=F.s(F.a(F.s(a2,a),2),b)
            expected=(b!=1 and F.a(F.a(a,b),1)!=0 and disc!=0)
            assert direct==expected,(m,a,b,'smooth criterion')
            if not direct: continue
            H=HW(F,a,b)
            ra=F.rank(H);pr=prank(F,H)
            label=(pr,4-ra)
            if a==0:
                assert label==((0,2) if b==0 else (2,2)),(m,a,b,label)
            else:assert label==(4,0),(m,a,b,label)
            found[label]=found.get(label,0)+1
    target={(4,0):q*q-4*q+5,(2,2):q-3,(0,2):1}
    assert found=={key:v for key,v in target.items() if v},(q,found,target)
    print('F_%s: irreducible=%s smooth=%s strata=%s' % (q,F.mod,sum(found.values()),found))
    if m==4:
        squares={F.mlt(y,y) for y in range(q)}
        N=2+sum(1 if F.a(F.power(x,10),1)==0 else
                (2 if F.a(F.power(x,10),1) in squares else 0) for x in range(q))
        assert N==154,N
        print('F_81: #C_(0,0)(F_81)=154 (Hasse-Weil maximum)')

if __name__=='__main__':
    for m in (1,2,3,4):verify(m)
    print('VERIFY_OK')
