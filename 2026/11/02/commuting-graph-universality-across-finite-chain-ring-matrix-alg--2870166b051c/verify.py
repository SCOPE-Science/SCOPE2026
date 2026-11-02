#!/usr/bin/env python3
"""Independent finite-ring and commuting-graph checks for the stated mathematical formulas."""
from itertools import product
from collections import Counter
from hashlib import sha256

class Ring:
    def __init__(self,p,ell,kind):
        self.p,self.ell,self.kind=p,ell,kind
        self.order=p**ell
    def add(self,a,b):
        if self.kind=='mod': return (a+b)%self.order
        ans=0; t=1
        for _ in range(self.ell):
            ans+=((a%self.p+b%self.p)%self.p)*t
            a//=self.p; b//=self.p; t*=self.p
        return ans
    def neg(self,a): return self.sub(0,a)
    def sub(self,a,b):
        if self.kind=='mod':return (a-b)%self.order
        ans=0;t=1
        for _ in range(self.ell):
            ans+=((a%self.p-b%self.p)%self.p)*t
            a//=self.p;b//=self.p;t*=self.p
        return ans
    def mul(self,a,b):
        if self.kind=='mod':return a*b%self.order
        aa=[];bb=[]
        for _ in range(self.ell):
            aa.append(a%self.p);bb.append(b%self.p);a//=self.p;b//=self.p
        ans=0;t=1
        for k in range(self.ell):
            ans+=(sum(aa[i]*bb[k-i] for i in range(k+1))%self.p)*t
            t*=self.p
        return ans
    def unit(self,a):return a%self.p!=0
    def inv(self,a):
        assert self.unit(a)
        return next(b for b in range(self.order) if self.mul(a,b)==1)
    def valuation(self,a):
        if a==0:return self.ell
        if self.kind=='mod':
            k=0
            while a%self.p==0:
                k+=1;a//=self.p
            return k
        k=0
        while a%self.p==0:
            k+=1;a//=self.p
        return k
    def reduce(self,a,k):return a%(self.p**k)
    def quotient_divide(self,a,s):
        assert self.valuation(a)>=s
        return a//(self.p**s)

def wedge_zero(R,x,y):
    return all(R.sub(R.mul(x[i],y[j]),R.mul(x[j],y[i]))==0
               for i,j in ((0,1),(0,2),(1,2)))

def projective_paths(p,ell,kind):
    dirs={};path={}
    for k in range(1,ell+1):
        R=Ring(p,k,kind)
        d=set()
        for v in product(range(R.order),repeat=3):
            pivot=next((i for i,c in enumerate(v) if R.unit(c)),None)
            if pivot is None:continue
            inverse=R.inv(v[pivot]);d.add(tuple(R.mul(inverse,z) for z in v))
        dirs[k]=sorted(d)
        if k==1:
            for j,x in enumerate(dirs[k]):path[k,x]=(j,)
        else:
            groups={}
            for x in dirs[k]:
                parent=tuple(z%(p**(k-1)) for z in x)
                assert parent in dirs[k-1]
                groups.setdefault(parent,[]).append(x)
            assert len(groups)==len(dirs[k-1])
            for parent,children in groups.items():
                assert len(children)==p**2
                for j,x in enumerate(sorted(children)):
                    path[k,x]=path[k-1,parent]+(j,)
        assert len(dirs[k])==(p*p+p+1)*p**(2*(k-1))
    return path

def key_of(R,x,paths):
    s=min(R.valuation(z) for z in x)
    if s==R.ell:return ('zero',)
    k=R.ell-s; Q=Ring(R.p,k,R.kind)
    y=tuple(R.quotient_divide(z,s) for z in x)
    pivot=next(i for i,z in enumerate(y) if Q.unit(z))
    unit=y[pivot]; normalized=tuple(Q.mul(Q.inv(unit),z) for z in y)
    unitlabel=sorted(a for a in range(Q.order) if Q.unit(a)).index(unit)
    return (s,paths[k,normalized],unitlabel)

def direct_matrix_commute(R,A,B):
    a,b,c,d=A;e,f,g,h=B
    return all(R.sub(x,y)==0 for x,y in (
        (R.add(R.mul(a,e),R.mul(b,g)),R.add(R.mul(e,a),R.mul(f,c))),
        (R.add(R.mul(a,f),R.mul(b,h)),R.add(R.mul(e,b),R.mul(f,d))),
        (R.add(R.mul(c,e),R.mul(d,g)),R.add(R.mul(g,a),R.mul(h,c))),
        (R.add(R.mul(c,f),R.mul(d,h)),R.add(R.mul(g,b),R.mul(h,d))),))

def check_pair(p,ell):
    R=Ring(p,ell,'mod'); S=Ring(p,ell,'poly')
    paths_R=projective_paths(p,ell,'mod');paths_S=projective_paths(p,ell,'poly')
    X=list(product(range(R.order),repeat=3))
    Y=list(product(range(S.order),repeat=3))
    kr={key_of(R,x,paths_R):x for x in X}
    ks={key_of(S,x,paths_S):x for x in Y}
    assert len(kr)==len(X) and len(ks)==len(Y)
    assert kr.keys()==ks.keys()
    order=sorted(kr,key=str)
    A=[kr[z] for z in order];B=[ks[z] for z in order]
    adjR=[[wedge_zero(R,x,y) for y in A] for x in A]
    adjS=[[wedge_zero(S,x,y) for y in B] for x in B]
    assert adjR==adjS
    degrees=[sum(row)*R.order for row in adjR]
    empirical=Counter({size:count*R.order for size,count in Counter(degrees).items()})
    predicted=Counter()
    for s in range(ell):
        predicted[p**(2*ell+2*s)]+=R.order*(p**(3*(ell-s))-p**(3*(ell-s-1)))
    predicted[p**(4*ell)]+=R.order
    assert empirical==predicted
    paircount=sum(degrees)*R.order
    closed=p**(5*ell)+(p*p+p+1)*(p**(6*ell-2)-p**(5*ell-2))
    assert paircount==closed
    print('FOREST_ISOMORPHISM_OK',p,ell,'vector_vertices',len(X),
          'matrix_vertices',R.order**4,'commuting_pairs',paircount,
          'spectrum',sorted(empirical.items()))
    # Independent matrix identity, not derived from the tree.
    for i,x in enumerate(A[:min(len(A),100)]):
        for j,y in enumerate(A[:min(len(A),100)]):
            a=(R.add(x[0],0),x[1],x[2],0)
            b=(R.add(y[0],0),y[1],y[2],0)
            assert direct_matrix_commute(R,a,b)==wedge_zero(R,x,y)
    # Strongest small case: all 4^4 matrices, full 65,536 direct matrix comparisons.
    if p==2 and ell==2:
        matrices=list(product(range(R.order),repeat=4))
        cnt=sum(direct_matrix_commute(R,a,b) for a in matrices for b in matrices)
        assert cnt==closed
        print('FULL_MATRIX_CENSUS_OK',cnt)

if __name__=='__main__':
    for params in ((2,1),(2,2),(2,3),(3,2)):
        check_pair(*params)
    print('VERIFY_OK')
