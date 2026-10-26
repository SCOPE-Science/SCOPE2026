#!/usr/bin/env python3
"""Independent finite-field substitution-matrix checks for truncated Nottingham actions."""
from itertools import product
from collections import Counter
import random

class Field:
    def __init__(self,p,modulus=None):
        self.p=p
        self.mod=modulus or [0,1]
        self.e=len(self.mod)-1
        assert self.mod[-1]==1
        self.q=p**self.e
        self.digits=[self._digits(a) for a in range(self.q)]
        self.to_int={tuple(v):i for i,v in enumerate(self.digits)}
        self.add_table=[[self._add_slow(a,b) for b in range(self.q)] for a in range(self.q)]
        self.mul_table=[[self._mul_slow(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inverse=[None]+[next(b for b in range(1,self.q) if self.mul_table[a][b]==1) for a in range(1,self.q)]
    def _digits(self,a):
        out=[]
        for _ in range(self.e): out.append(a%self.p);a//=self.p
        return out
    def _add_slow(self,a,b):
        return self.to_int[tuple((x+y)%self.p for x,y in zip(self.digits[a],self.digits[b]))]
    def _mul_slow(self,a,b):
        x=self.digits[a];y=self.digits[b]
        z=[0]*(2*self.e-1)
        for i in range(self.e):
            for j in range(self.e):z[i+j]=(z[i+j]+x[i]*y[j])%self.p
        for d in range(2*self.e-2,self.e-1,-1):
            c=z[d]
            for j in range(self.e):z[d-self.e+j]=(z[d-self.e+j]-c*self.mod[j])%self.p
        return self.to_int[tuple(z[:self.e])]
    def add(self,a,b):return self.add_table[a][b]
    def neg(self,a):return self.to_int[tuple((-i)%self.p for i in self.digits[a])]
    def mul(self,a,b):return self.mul_table[a][b]


def mulpoly(a,b,F):
    n=len(a);r=[0]*n
    for i,x in enumerate(a):
        if not x:continue
        for j in range(n-i):
            y=b[j]
            if y:r[i+j]=F.add(r[i+j],F.mul(x,y))
    return r


def substitution_matrix(coeff,F):
    m=len(coeff)
    cur=[0]*m;cur[0]=1
    N=[[0]*m for _ in range(m)]
    for j in range(m):
        for i in range(m):
            N[i][j]=F.add(cur[i],F.neg(int(i==j)))
        cur=mulpoly(cur,coeff,F)
    return N


def matmul(A,B,F):
    n=len(A);r=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    if b:r[i][j]=F.add(r[i][j],F.mul(a,b))
    return r


def rank(A,F):
    a=[row[:] for row in A];n=len(a);s=0
    for col in range(n):
        pivot=next((i for i in range(s,n) if a[i][col]),None)
        if pivot is None:continue
        a[s],a[pivot]=a[pivot],a[s]
        z=F.inverse[a[s][col]]
        a[s]=[F.mul(z,u) for u in a[s]]
        for i in range(s+1,n):
            t=a[i][col]
            if t:
                a[i]=[F.add(v,F.neg(F.mul(t,w))) for v,w in zip(a[i],a[s])]
        s+=1
        if s==n:break
    return s


def rank_powers(N,F):
    m=len(N);A=N;out=[]
    for k in range(1,m+1):
        out.append(rank(A,F));A=matmul(A,N,F)
    return out


def validate(F,m,depth=None,exhaust=True,limit=80):
    p=F.p;q=F.q;rng=random.Random(1000*p+100*q+m+(depth or 0))
    cases=[]
    if exhaust or q**(m-2)<=limit:
        cases=list(product(range(q),repeat=m-2))
    else:
        cases=[tuple(rng.randrange(q) for _ in range(m-2)) for _ in range(limit)]
        cases.extend([tuple([0]*(s-2)+[1]+[0]*(m-s-1)) for s in range(2,m)])
    tested=0;hist=Counter()
    for tup in cases:
        c=[0,1]+list(tup)
        s=next((j for j in range(2,m) if c[j]),None)
        if depth is not None and s!=depth:continue
        N=substitution_matrix(c,F)
        got=rank_powers(N,F)
        if s is None:
            want=[0]*m
        else:
            d=s-1
            if m<=p+d:
                want=[max(m-1-k*d,0) for k in range(1,m+1)]
                # The entire fixed algebra is F + t^(m-d) A, coefficient-wise.
                assert all(all(N[i][j]==0 for i in range(m)) for j in [0]+list(range(m-d,m)))
            elif m==p+d+1:
                want=[max(p-1-(k-1)*d,0) for k in range(1,m+1)]
                # First wild jump: the Frobenius-fixed t^p is a new fixed vector.
                assert all(all(N[i][j]==0 for i in range(m)) for j in [0]+list(range(p,m)))
            else:continue
        assert got==want,(p,q,m,s,c,got,want)
        hist[m-got[0]]+=1
        tested+=1
    assert tested>0,(p,q,m,depth)
    if exhaust and depth is None and m<=p+1:
        expected={s:(q-1)*q**(m-s-1) for s in range(2,m)}
        expected[m]=1
        assert dict(hist)==expected,(p,q,m,hist,expected)
    print('PASS',f'characteristic={p}',f'field={q}',f'length={m}',f'specified_first_degree={depth}',f'matrices={tested}',f'fixed_dim_hist={dict(sorted(hist.items()))}')
    return tested


def main():
    count=0
    for p,m in [(2,3),(3,3),(3,4),(5,3),(5,4),(5,5),(5,6)]:
        count+=validate(Field(p),m)
    count+=validate(Field(2,[1,1,1]),3)
    count+=validate(Field(3,[1,0,1]),4)
    for p,d in [(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)]:
        m=p+d+1;s=d+1
        count+=validate(Field(p),m,s,exhaust=(p+d<=6),limit=45)
    for p,d in [(2,1),(2,3),(3,1),(3,2),(3,4),(5,1),(5,3),(5,4),(7,1),(7,6)]:
        F=Field(p);m=p+d+1
        c=[0,1]+[0]*(m-2);c[d+1]=1
        t=[0,1]+[0]*(m-2);t[d+2]=1
        w=rank_powers(substitution_matrix(c,F),F)
        v=rank_powers(substitution_matrix(t,F),F)
        assert (w==v)==(d>=p-1),(p,d,w,v)
        print('COLLISION' if w==v else 'DISTINCT',f'p={p}',f'first_depth={d}',f'second_depth={d+1}')
    print('VERIFY_OK',count,'matrix-power profiles; exhaustive runs, deterministic samples, and first-wild similarity collisions')

if __name__=='__main__':main()
