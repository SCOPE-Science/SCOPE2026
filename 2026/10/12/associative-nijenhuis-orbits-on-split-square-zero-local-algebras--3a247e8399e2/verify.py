#!/usr/bin/env python3
"""Exhaustive finite-field checks of associative Nijenhuis classification.

Usage: python verify.py
Pure Python 3 standard library; no external data or packages.
"""
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
        self.add=[[self._a(i,j) for j in range(q)] for i in range(q)]
        self.neg=[next(j for j in range(q) if self.add[i][j]==0) for i in range(q)]
        self.mul=[[self._m(i,j) for j in range(q)] for i in range(q)]
        self.inv=[None]+[next(j for j in range(1,q) if self.mul[i][j]==1) for i in range(1,q)]
    def _a(self,a,b):return (a+b)%self.q if self.q!=4 else a^b
    def _m(self,a,b):
        if self.q!=4:return a*b%self.q
        out=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1):out^=(1<<(i+j))
        if out&8:out^=0b1110  # x^3=x*x^2, x^2=x+1 => x^3=1
        if out&4:out^=0b111  # x^2=x+1
        return out
    def mm(self,A,B,n):
        return tuple(self.sumprod((A[i*n+k],B[k*n+j]) for k in range(n)) for i in range(n) for j in range(n))
    def sumprod(self, products):
        s=0
        for a,b in products:s=self.add[s][self.mul[a][b]]
        return s
    def mv(self,A,v,n):
        return tuple(self.sumprod((A[i*n+j],v[j]) for j in range(n)) for i in range(n))
    def inverse(self,A,n):
        x=[[A[i*n+j] for j in range(n)]+[int(i==j) for j in range(n)] for i in range(n)]
        for j in range(n):
            pivot=next((i for i in range(j,n) if x[i][j]),None)
            if pivot is None:return None
            x[j],x[pivot]=x[pivot],x[j]
            b=self.inv[x[j][j]]
            x[j]=[self.mul[b][t] for t in x[j]]
            for i in range(n):
                if i!=j and x[i][j]:
                    t=x[i][j]
                    x[i]=[self.add[x[i][k]][self.neg[self.mul[t][x[j][k]]]] for k in range(2*n)]
        return tuple(x[i][n+j] for i in range(n) for j in range(n))
    def Nmul(self,a,b,n):
        a0,b0=a[0],b[0]
        return (self.mul[a0][b0],)+tuple(self.add[self.mul[a0][b[i]]][self.mul[b0][a[i]]] for i in range(1,n+1))
    def Nijenhuis(self,N,n):
        d=n+1
        es=[tuple(int(i==j) for i in range(d)) for j in range(d)]
        images=[self.mv(N,e,d) for e in es]
        for i in range(d):
            for j in range(d):
                rhs0=self.Nmul(images[i],es[j],n)
                rhs1=self.Nmul(es[i],images[j],n)
                rhs2=self.Nmul(es[i],es[j],n)
                Nr2=self.mv(N,rhs2,d)
                arg=tuple(self.add[self.add[rhs0[k]][rhs1[k]]][self.neg[Nr2[k]]] for k in range(d))
                if self.Nmul(images[i],images[j],n)!=self.mv(N,arg,d):return False
        return True

def verify(q,n, brute=True, orbit=True):
    F=Field(q); d=n+1
    allv=list(product(range(q),repeat=n))
    allT=list(product(range(q),repeat=n*n))
    params=set()
    for alpha in range(q):
        for T in allT:
            for u in allv:
                if F.mv(T,u,n)==tuple(F.mul[alpha][a] for a in u):
                    params.add((alpha,T,u))
    predicted=q*(2*q**(n*n)-q**(n*n-n))
    assert len(params)==predicted,(q,n,len(params),predicted)
    # Compare operator identity with predicted normal form, inspecting EVERY linear map.
    if brute:
        allmaps=product(range(q),repeat=d*d)
        seen=0
        for N in allmaps:
            valid=F.Nijenhuis(N,n)
            alpha=N[0]
            u=tuple(N[i*d] for i in range(1,d))
            T=tuple(N[(i+1)*d+j+1] for i in range(n) for j in range(n))
            f=tuple(N[j+1] for j in range(n))
            normal=(not any(f) and F.mv(T,u,n)==tuple(F.mul[alpha][a] for a in u))
            assert valid==normal,('NIJENHUIS_MISMATCH',q,n,N)
            seen+=valid
        assert seen==predicted,(q,n,seen,predicted)
    if orbit:
        G=[]
        for mat in allT:
            inv=F.inverse(mat,n)
            if inv is not None:G.append((mat,inv))
        remaining=set(params)
        sizes=[]
        while remaining:
            alpha,T,u=next(iter(remaining))
            orbitset=set()
            for g,gi in G:
                gt=F.mm(F.mm(g,T,n),gi,n)
                gu=F.mv(g,u,n)
                orbitset.add((alpha,gt,gu))
            assert orbitset<=params
            assert orbitset<=remaining,'orbit intersection not disjoint'
            sizes.append(len(orbitset))
            remaining-=orbitset
        # Number of similarity classes of matrices by brute-force conjugacy.
        mats=set(allT);similarity=0
        while mats:
            T=next(iter(mats))
            cls={F.mm(F.mm(g,T,n),gi,n) for g,gi in G}
            similarity+=1;mats-=cls
        # Count all matrix similarity classes in lower dimensions.
        csum=1+similarity
        for k in range(1,n):
            smallmats=set(product(range(q),repeat=k*k))
            smallG=[]
            for g in list(smallmats):
                gi=F.inverse(g,k)
                if gi is not None:smallG.append((g,gi))
            c=0
            while smallmats:
                T=next(iter(smallmats))
                cls={F.mm(F.mm(g,T,k),gi,k) for g,gi in smallG}
                c+=1;smallmats-=cls
            csum+=c
        assert len(sizes)==q*csum,(q,n,len(sizes),q*csum)
        assert sum(sizes)==predicted
        assert all(len(G)%s==0 for s in sizes)
        print(f'q={q}, n={n}: operators={predicted}, GL={len(G)}, orbits={len(sizes)}, sizes={sorted(set(sizes))}')
    else:print(f'q={q}, n={n}: operators={predicted}, Nijenhuis identity exhaustively matched normal form')

if __name__=='__main__':
    for q,n in ((2,1),(3,1),(4,1),(2,2),(3,2),(4,2),(2,3)):
        verify(q,n,brute=True,orbit=True)
    print('VERIFY_OK')
