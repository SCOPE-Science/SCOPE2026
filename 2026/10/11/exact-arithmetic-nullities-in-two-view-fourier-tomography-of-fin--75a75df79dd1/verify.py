#!/usr/bin/env python3
"""Finite-field conic two-direction Fourier sampling: independent line-sum rank tests.
Run with Python 3 standard library. Tests only; theorem is proved separately.
"""
from collections import Counter
from math import gcd

class Field:
    def __init__(self, p, nonsquare=None):
        self.p=p
        self.degree=1 if nonsquare is None else 2
        self.nr=nonsquare
        self.q=p**self.degree
    def ab(self, a):
        return (a%self.p, 0 if self.degree==1 else a//self.p)
    def add(self,x,y):
        a,b=self.ab(x);c,d=self.ab(y)
        return (a+c)%self.p + (0 if self.degree==1 else self.p*((b+d)%self.p))
    def neg(self,x):return self.sub(0,x)
    def sub(self,x,y):
        a,b=self.ab(x);c,d=self.ab(y)
        return (a-c)%self.p+(0 if self.degree==1 else self.p*((b-d)%self.p))
    def mul(self,x,y):
        a,b=self.ab(x);c,d=self.ab(y)
        if self.degree==1:return (a*c)%self.p
        return (a*c+self.nr*b*d)%self.p+self.p*((a*d+b*c)%self.p)
    def pow(self,x,k):
        r=1
        while k:
            if k&1:r=self.mul(r,x)
            x=self.mul(x,x);k//=2
        return r
    def inv(self,x):
        assert x!=0
        return self.pow(x,self.q-2)
    def square(self,x):return self.mul(x,x)
    def dot(self,u,p):return self.add(self.mul(u[0],p[0]),self.mul(u[1],p[1]))
    def norm(self,u):return self.add(self.square(u[0]),self.square(u[1]))
    def cmul(self,z,w):
        a,b=z;c,d=w
        return (self.sub(self.mul(a,c),self.mul(b,d)),self.add(self.mul(a,d),self.mul(b,c)))
    def ccj(self,z):return (z[0],self.neg(z[1]))
    def cpow(self,z,k):
        r=(1,0)
        while k:
            if k&1:r=self.cmul(r,z)
            z=self.cmul(z,z);k//=2
        return r
    def torus(self,u):
        den=self.inv(self.norm(u))
        return tuple(self.mul(x,den) for x in self.cmul(u,u))

def rank_mod(A,mod):
    A=[[(x%mod) for x in row] for row in A]
    if not A:return 0
    h=len(A);w=len(A[0]);r=0
    for col in range(w):
        pivot=next((i for i in range(r,h) if A[i][col]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][col],-1,mod)
        A[r]=[(v*inv)%mod for v in A[r]]
        for k in range(r+1,h):
            if A[k][col]:
                fac=A[k][col]
                for j in range(col,w):A[k][j]=(A[k][j]-fac*A[r][j])%mod
        r+=1
        if r==h:break
    return r

def nullity_expected(F,u,v,n):
    a=F.torus(u);b=F.torus(v)
    t=F.cmul(b,F.ccj(a));z=(1,0);d=None
    for k in range(1,n+1):
        z=F.cmul(z,t)
        if z==(1,0):d=k;break
    assert d is not None and n%d==0,(n,d,t)
    h=n//d
    square=F.norm(u) in {F.square(s) for s in range(F.q)}
    fixed=1 if h%2 else 2 if square else 0
    return (h-fixed)//2,d,h,square

def run_field(p,nr=None):
    F=Field(p,nr);q=F.q
    C=[(x,y) for x in range(q) for y in range(q) if F.norm((x,y))==1]
    n=len(C);assert n==q-(1 if q%4==1 else -1)
    dirs=[(1,s) for s in range(q)]+[(0,1)]
    iso=[u for u in dirs if F.norm(u)==0]
    non=[u for u in dirs if F.norm(u)!=0]
    assert len(non)==n and len(iso)==q+1-n
    bydir={}
    for u in dirs:
        rowmap={}
        for j,c in enumerate(C):rowmap.setdefault(F.dot(u,c),[]).append(j)
        bydir[u]=[[int(j in jj) for j in range(n)] for jj in rowmap.values()]
    full_non=0;bad=0;hist=Counter();checks=0
    for i,u in enumerate(non):
        for v in non[i+1:]:
            want,d,h,square=nullity_expected(F,u,v,n)
            M=bydir[u]+bydir[v]
            observed=n-rank_mod(M,1000003)
            assert observed==want,(q,u,v,want,observed,d,h,square)
            if q<=13 or i%7==0:
                observed2=n-rank_mod(M,1009)
                assert observed2==want,(q,u,v,observed2,want)
            hist[want]+=1
            full_non+=want==0
            checks+=1
    phi=lambda N: sum(gcd(j,N)==1 for j in range(1,N+1))
    expected_count=n*phi(n)//2+n*phi(n//2)//4
    assert full_non==expected_count,(q,full_non,expected_count)
    if iso:
        for u in iso:
            assert n-rank_mod(bydir[u],1000003)==0
            for v in non[:min(5,n)]:
                assert n-rank_mod(bydir[u]+bydir[v],1000003)==0
    print(f'q={q:>2} n={n:>2} iso={len(iso)} pair_tests={checks:>4} injective_pairs={full_non:>4} phi_formula={expected_count:>4} nullity_hist={sorted(hist.items())}')
    return checks

if __name__=='__main__':
    total=0
    for p,nr in [(3,None),(5,None),(7,None),(11,None),(13,None),(17,None),(19,None),(3,2),(5,2),(7,3)]:
        total+=run_field(p,nr)
    print('VERIFY_OK independent_exact_modular_incidence_rank_tests=',total,'extension_fields=[9,25,49]','pair_count=PASS','isotropic_single_view=PASS')
