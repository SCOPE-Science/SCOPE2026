#!/usr/bin/env python3
"""Exact finite-field cross-checks for the Fourier transform of XY=YX=0 in M_2(F_q)^2.

The zero criterion and closed count are tested independently at q=2,3,4,5;
for prime q<=3 the raw Fourier transform is evaluated at *every* frequency,
and for q=4 at a deterministic sample using the field trace to F_2.
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        self.q=q
        if q==4:
            self.add=lambda x,y:x^y
            def mul(x,y):
                a=(x&1)*(y&1)
                b=((x&1)*((y>>1)&1))^(((x>>1)&1)*(y&1))
                c=((x>>1)&1)*((y>>1)&1)
                return (a^c)|((b^c)<<1)
            self.mul=mul
            self.neg=lambda x:x
            self.trace=lambda x: (0 if x in (0,1) else 1)
        else:
            self.add=lambda x,y:(x+y)%q
            self.mul=lambda x,y:(x*y)%q
            self.neg=lambda x:-x%q
            self.trace=lambda x:x
    def plus(self,x,y,z):return self.add(x,self.add(y,z))
    def matrix_add(self,A,B,t):return tuple(self.add(a,self.mul(t,b)) for a,b in zip(A,B))
    def adj(self,A):a,b,c,d=A;return (d,self.neg(b),self.neg(c),a)
    def det(self,A):a,b,c,d=A;return self.add(self.mul(a,d),self.neg(self.mul(b,c)))
    def rank(self,A):return 0 if A==(0,0,0,0) else (1 if self.det(A)==0 else 2)
    def mm(self,A,B):
        a,b,c,d=A;e,f,g,h=B
        return (self.add(self.mul(a,e),self.mul(b,g)),self.add(self.mul(a,f),self.mul(b,h)),self.add(self.mul(c,e),self.mul(d,g)),self.add(self.mul(c,f),self.mul(d,h)))
    def trprod(self,A,B):
        a,b,c,d=A;e,f,g,h=B
        return self.add(self.add(self.mul(a,e),self.mul(b,g)),self.add(self.mul(c,f),self.mul(d,h)))

def formula(F,A,B):
    q=F.q
    C=F.adj(B)
    n0=n1=0
    for t in range(1,q):
        rank=F.rank(F.matrix_add(A,C,t))
        n0+=(rank==0)
        n1+=(rank==1)
    return q*q*(q*q*(A==(0,0,0,0))+q*q*(B==(0,0,0,0))-1+n1+(q+1)*n0)

def exhaustive(q):
    F=Field(q)
    mats=list(product(range(q),repeat=4));zero=(0,)*4
    vals=Counter();points=[]
    if q<5:
        points=[(X,Y) for X in mats for Y in mats if F.mm(X,Y)==zero and F.mm(Y,X)==zero]
        assert len(points)==3*q**4-2*q*q
    tested=0
    for i,A in enumerate(mats):
        for j,B in enumerate(mats):
            v=formula(F,A,B)
            vals[v]+=1
            if q in (2,3) or q==4 and ((i*257+j*23)%313)<1:
                if q==4:
                    brute=sum((1 if F.trace(F.add(F.trprod(A,X),F.trprod(B,Y)))==0 else -1) for X,Y in points)
                    assert v==brute, (q,A,B,v,brute)
                else:
                    counts=[0]*q
                    for X,Y in points:counts[F.add(F.trprod(A,X),F.trprod(B,Y))]+=1
                    assert counts[1:]==[counts[1]]*(q-1)
                    assert v==counts[0]-counts[1],(q,A,B,v,counts)
                tested+=1
    nzeros=vals[0]
    predicted=q*(q-1)**3*(q+1)**2*(3*q-1)+(36 if q==2 else 0)
    assert nzeros==predicted,(q,nzeros,predicted)
    assert sum(vals.values())==q**8
    print('EXACT_FIELD_OK',q,'nullity',nzeros,'rank',q**8-nzeros,'brute_frequencies',tested)

if __name__=='__main__':
    for q in (2,3,4,5):exhaustive(q)
    print('ALL_EXACT_MUTUAL_ANNIHILATION_CHECKS_OK')
