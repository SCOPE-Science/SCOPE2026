"""Standalone exhaustive finite-field check for nilpotent-free hyperplanes in M_2.
This is finite verification, not the proof for arbitrary prime powers.
"""
from itertools import product

class F:
    def __init__(self,q):
        self.q=q
        assert q in [2,3,4,5]
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        poly=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:poly ^=1<<(i+j)
        if poly&8:poly ^=0b1100
        if poly&4:poly ^=0b111
        return poly
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)
    def div(self,a,b):return self.mul(a,self.inv(b))
    def vecadd(self,A,B):return tuple(self.add(a,b) for a,b in zip(A,B))
    def mul2(self,A,B):
        return tuple(self.add(self.mul(A[2*i],B[j]),self.mul(A[2*i+1],B[2+j])) for i in range(2) for j in range(2))
    def det(self,A):return self.sub(self.mul(A[0],A[3]),self.mul(A[1],A[2]))
    def trace(self,A):return self.add(A[0],A[3])
    def mulsc(self,k,A):return tuple(self.mul(k,a) for a in A)
    def conjugate(self,G,C):
        d=self.inv(self.det(G));Gi=self.mulsc(d,(G[3],self.neg(G[1]),self.neg(G[2]),G[0]))
        return self.mul2(self.mul2(G,C),Gi)
    def normsc(self,A):
        x=next(a for a in A if a)
        return self.mulsc(self.inv(x),A)
    def trace_pair(self,C,X):
        Y=self.mul2(C,X)
        return self.trace(Y)
    def irreducible(self,C):
        t,d=self.trace(C),self.det(C)
        return all(self.add(self.sub(self.mul(x,x),self.mul(t,x)),d)!=0 for x in range(self.q))

for q in [2,3,4,5]:
    Fq=F(q)
    mats=list(product(range(q),repeat=4)); zero=(0,0,0,0)
    nils=[X for X in mats if Fq.trace(X)==0 and Fq.det(X)==0]
    projective={Fq.normsc(C) for C in mats if C!=zero}
    good=[]
    for C in sorted(projective):
        property_no_nil=all(Fq.trace_pair(C,X)!=0 for X in nils if X!=zero)
        irreducible=Fq.irreducible(C)
        assert property_no_nil==irreducible,(q,C)
        if property_no_nil:good.append(C)
    goodset=set(good)
    gens=[G for G in mats if Fq.det(G)!=0]
    orbits=[]
    while goodset:
        C=next(iter(goodset))
        orb={Fq.normsc(Fq.conjugate(G,C)) for G in gens}
        assert orb<=goodset
        orbits.append(orb)
        goodset-=orb
    lens=sorted(len(x) for x in orbits)
    expected=[q*(q-1)//2]+[q*(q-1)]*((q-1)//2) if q%2 else [q*(q-1)]*(q//2)
    assert lens==sorted(expected),(q,lens,expected)
    assert len(good)==q*q*(q-1)//2,(q,len(good))
    print(f'q={q} all matrices={q**4} projective hyperplanes={len(projective)} nilpotent matrices={len(nils)} good={len(good)} orbit sizes={lens}')
print('VERIFY_OK')
