#!/usr/bin/env python3
"""Exhaustive finite-field checks for idempotent-plus-square-zero fibers in M_2."""
from collections import Counter
from itertools import product

# For n>1 a field element is a base-p coefficient vector of degree < n.
SPECS = [(2,1,None),(3,1,None),(2,2,(1,1,1)),
         (5,1,None),(7,1,None),(2,3,(1,1,0,1)),
         (3,2,(1,0,1)),(11,1,None)]

class Field:
    def __init__(self,p,n,poly):
        self.p,self.n,self.q,self.poly=p,n,p**n,poly
        self.digits=[tuple((i//p**j)%p for j in range(n)) for i in range(self.q)]
        self.add=[[self.encode([(a+b)%p for a,b in zip(self.digits[i],self.digits[j])])
                   for j in range(self.q)] for i in range(self.q)]
        self.neg=[self.encode([(-a)%p for a in self.digits[i]]) for i in range(self.q)]
        self.mult=[[self._times(i,j) for j in range(self.q)] for i in range(self.q)]
    def encode(self,ls): return sum(c*self.p**j for j,c in enumerate(ls))
    def _times(self,i,j):
        p,n=self.p,self.n
        co=[0]*(2*n-1)
        for a,x in enumerate(self.digits[i]):
            for b,y in enumerate(self.digits[j]): co[a+b]=(co[a+b]+x*y)%p
        if n>1:
            for k in range(2*n-2,n-1,-1):
                h=co[k]
                for j in range(n):co[k-n+j]=(co[k-n+j]-h*self.poly[j])%p
        return self.encode(co[:n])
    def a(self,x,y):return self.add[x][y]
    def s(self,x,y):return self.add[x][self.neg[y]]
    def m(self,x,y):return self.mult[x][y]
    def matmul(self,A,B):
        a,m=self.a,self.m
        return (a(m(A[0],B[0]),m(A[1],B[2])),
                a(m(A[0],B[1]),m(A[1],B[3])),
                a(m(A[2],B[0]),m(A[3],B[2])),
                a(m(A[2],B[1]),m(A[3],B[3])))
    def det(self,A):return self.s(self.m(A[0],A[3]),self.m(A[1],A[2]))
    def tr(self,A):return self.a(A[0],A[3])
    def iszero(self,A):return A==(0,0,0,0)
    def minus(self,A,B):return tuple(self.s(x,y) for x,y in zip(A,B))
    def plus(self,A,B):return tuple(self.a(x,y) for x,y in zip(A,B))
    def eigenlines(self,A):
        out=0
        for y in range(self.q):
            # Line spanned by (1,y).
            Au=self.a(A[0],self.m(A[1],y))
            Av=self.a(A[2],self.m(A[3],y))
            out+= self.m(Au,y)==Av
        out+= A[1]==0  # Line spanned by (0,1).
        return out
    def fiber(self,delta):
        a,s,m=self.a,self.s,self.m
        cnt=0
        for h,v in product(range(self.q),repeat=2):
            F=a(a(m(h,h),m(h,v)),m(delta,m(v,v)))
            F=s(s(F,h),m(delta,v))
            cnt+=(F==0)
        return cnt

def one_case(p,n,poly):
    f=Field(p,n,poly);q=f.q;I=(1,0,0,1);zero=(0,0,0,0)
    mats=list(product(range(q),repeat=4))
    E=[A for A in mats if f.matmul(A,A)==A]
    N=[A for A in mats if f.matmul(A,A)==zero]
    fibers=Counter()
    for e in E:
        for n in N: fibers[f.plus(e,n)]+=1
    hist=Counter(fibers.values());hist[0]=q**4-len(fibers)
    for A in mats:
        direct=fibers[A]
        tr,det=f.tr(A),f.det(A)
        scalar=A[1]==A[2]==0 and A[0]==A[3]
        trivial=(f.matmul(A,A)==zero)+(f.matmul(f.minus(A,I),f.minus(A,I))==zero)
        if tr==1 and not scalar:
            pred=2*q-1 if det==0 else q+1-f.eigenlines(A)
        else:pred=trivial
        assert direct==pred,(q,A,direct,pred)
    assert len(E)==q*(q+1)+2 and len(N)==q*q,(q,len(E),len(N))
    assert sum(k*v for k,v in hist.items())==len(E)*len(N)
    assert sum(hist.values())==q**4
    assert hist[0]==q**4-q**3-2*q*q+(p!=2),(q,hist)
    assert hist[1]==2*q*q,(q,hist)
    assert hist[2*q-1] >=q*(q+1)
    for det in range(q):
        if det==0:pred=2*q-1
        else:
            C=(0,f.neg[det],1,1)
            pred=q+1-f.eigenlines(C)
        assert f.fiber(det)==pred,(q,det,f.fiber(det),pred)
    print('PASS',q,'idempotents',len(E),'nilpotents',len(N),
          'index_histogram',sorted(hist.items()))

if __name__=='__main__':
    for spec in SPECS:one_case(*spec)
    print('NIL_CLEAN_FIBER_EXHAUSTIVE_OK')
