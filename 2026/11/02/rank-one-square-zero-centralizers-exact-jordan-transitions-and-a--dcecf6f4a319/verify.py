#!/usr/bin/env python3
"""Independent finite-field verification of rank-one square-zero centralizer perturbations.
Run with Python >=3.8; no external packages are required.
"""
from collections import Counter
from itertools import product

class F:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def mul(self,a,b):
        if self.q != 4: return a*b%self.q
        x=0
        for i in range(2):
            if (b>>i)&1: x^=a<<i
        for i in (2,):
            if (x>>i)&1: x^=0b111<<(i-2)
        return x
    def inv(self,a):
        assert a
        return next(i for i in range(1,self.q) if self.mul(a,i)==1)
    def sub(self,a,b):return self.add(a,self.neg(b))

def rank(A,f):
    A=[row[:] for row in A]
    nr=len(A); nc=len(A[0]) if A else 0
    r=0
    for j in range(nc):
        k=next((i for i in range(r,nr) if A[i][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        inv=f.inv(A[r][j]);A[r]=[f.mul(inv,a) for a in A[r]]
        for i in range(r+1,nr):
            h=A[i][j]
            if h:
                A[i]=[f.sub(A[i][t],f.mul(h,A[r][t])) for t in range(nc)]
        r+=1
        if r==nr:break
    return r

def mm(A,B,f):
    n=len(A)
    return [[f.add_many([f.mul(A[i][k],B[k][j]) for k in range(n)]) for j in range(n)] for i in range(n)]

# Product of nilpotent Jordan blocks, with superdiagonal 1.
def jordan(parts):
    n=sum(parts);A=[[0]*n for _ in range(n)]; soc=[];head=[]
    k=0
    for z in parts:
        soc.append(k);head.append(k+z-1)
        for j in range(1,z):A[k+j-1][k+j]=1
        k+=z
    return A,soc,head

def formula(q,parts):
    r=len(parts);a=parts.count(1);b=parts.count(2);c=sum(z>=3 for z in parts);s=b+c
    total=((q**s-1)*(q**r-1)+(q**r-q**s)*(q**(r-1)-1))//(q-1)
    up=(q**a-1)*q**s*(q**(r-1)-q**s)//(q-1)
    down=0 if b==0 else (q**b-1)*q**c*q**(s-1)//(q-1)
    return {-1:down,0:total-up-down,1:up}

def add_many(f,values):
    s=0
    for v in values:s=f.add(s,v)
    return s

def inspect(q,parts):
    f=F(q);f.add_many=lambda v:add_many(f,v)
    N,soc,head=jordan(parts);n=len(N);r=len(parts)
    N2=mm(N,N,f)
    Nrank=rank(N,f)
    counts=Counter(); seen=set()
    for u0 in product(range(q),repeat=r):
        if not any(u0):continue
        first=next(t for t in u0 if t)
        if first!=1:continue # canonical normalized image vector
        u=[0]*n
        for i,idx in enumerate(soc):u[idx]=u0[i]
        for v0 in product(range(q),repeat=r):
            if not any(v0):continue
            v=[0]*n
            for i,idx in enumerate(head):v[idx]=v0[i]
            if f.add_many(f.mul(u[j],v[j]) for j in range(n)):continue
            T=[[f.mul(u[i],v[j]) for j in range(n)] for i in range(n)]
            # Check the original, not the parameter reduction.
            assert rank(T,f)==1
            assert mm(T,T,f)==[[0]*n for _ in range(n)]
            assert mm(N,T,f)==mm(T,N,f)
            assert mm(N,T,f)==[[0]*n for _ in range(n)]
            S=[[f.add(N[i][j],T[i][j]) for j in range(n)] for i in range(n)]
            assert mm(S,S,f)==N2
            d=rank(S,f)-Nrank
            assert d in (-1,0,1)
            counts[d]+=1
            key=tuple(a for row in T for a in row)
            assert key not in seen
            seen.add(key)
    expected=formula(q,parts)
    assert all(counts[d]==expected[d] for d in (-1,0,1)),(q,parts,dict(counts),expected)
    return len(seen), tuple(counts[d] for d in (-1,0,1))

def main():
    cases=[]
    partitions=[[1],[2],[3],[4],[1,1],[1,1,1],[1,1,1,1],
      [2,1],[2,2],[2,1,1],[2,2,1],[2,2,2],
      [3,1],[3,2],[3,3],[3,1,1],[3,2,1],[4,1],[4,2],[4,1,1],[5,1], [3,2,1,1],[4,2,1],[3,3,1]]
    for q in (2,3,4,5):
        for parts in partitions:
            if q==5 and len(parts)>3:continue
            if q==4 and len(parts)>3:continue
            if q==3 and len(parts)>3:continue
            cases.append((q,parts,inspect(q,parts)))
    for q,parts,info in cases:
        print('q=%d partition=%s nonzero=%d deltas(-1,0,+1)=%s'%(q,','.join(map(str,parts)),info[0],str(info[1])))
    print('RANK_ONE_NILPOTENT_PERTURBATION_OK %d_EXHAUSTIVE_PARAMETER_CASES'%len(cases))
if __name__=='__main__':main()
