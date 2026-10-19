#!/usr/bin/env python3
"""Exhaustive enumeration for truncated maximal-ideal-power polynomial algebras.
Uses only Python standard library; run: python3 check_retractions.py
"""
from itertools import product
from collections import Counter, defaultdict
from math import comb


def gaussian(n,r,q):
    if not 0 <= r <= n: return 0
    x=1
    for i in range(r):
        x=x*(q**(n-i)-1)//1
    y=1
    for i in range(r):
        y*=q**(r-i)-1
    return x//y


def predicted(n,d,q,r):
    s=n-r
    D=sum(comb(n+j-1,j) for j in range(2,d))
    R=sum(comb(r+j-1,j) for j in range(2,d)) if r else 0
    images=gaussian(n,r,q)*q**(r*(D-R))
    per_image=q**(s*(r+R))
    return images, per_image, images*per_image


class Trunc:
    def __init__(self,n,d,q):
        self.n,self.d,self.q=n,d,q
        self.mons=sorted((e for e in product(range(d),repeat=n) if sum(e)<d),key=lambda e:(sum(e),e))
        self.idx={e:i for i,e in enumerate(self.mons)}
        self.N=len(self.mons)
        self.unit=tuple(1 if i==0 else 0 for i in range(self.N))
        self.zero=(0,)*self.N
        self.m=tuple(range(1,self.N))
        self.x=[tuple(int(i==self.idx[tuple(int(k==j) for k in range(n))]) for i in range(self.N)) for j in range(n)]
        self.tab=[[self.idx.get(tuple(a+b for a,b in zip(e,f)),-1) if sum(e)+sum(f)<d else -1 for f in self.mons] for e in self.mons]
    def addmul(self,dest,src,coef):
        if coef:
            for i,v in enumerate(src):
                dest[i]=(dest[i]+coef*v)%self.q
    def mul(self,a,b):
        out=[0]*self.N
        for i,ai in enumerate(a):
            if ai:
                for j,bj in enumerate(b):
                    k=self.tab[i][j]
                    if bj and k>=0:out[k]=(out[k]+ai*bj)%self.q
        return tuple(out)
    def evals(self,fs):
        vals=[]
        for e in self.mons:
            acc=self.unit
            for f,powr in zip(fs,e):
                for _ in range(powr):acc=self.mul(acc,f)
            vals.append(acc)
        return vals
    def compose_idempotent(self,fs):
        vals=self.evals(fs)
        for f in fs:
            v=[0]*self.N
            for a,vec in zip(f,vals): self.addmul(v,vec,a)
            if tuple(v)!=f:return False,None
        return True,vals
    def rref_key(self,vecs):
        b=[]; piv=[]
        for vec in vecs:
            w=list(vec)
            for a,p in zip(b,piv):
                f=w[p]
                if f:
                    for k in range(p,self.N):w[k]=(w[k]-f*a[k])%self.q
            p=next((k for k,v in enumerate(w) if v),None)
            if p is None:continue
            inv=pow(w[p],-1,self.q)
            w=[v*inv%self.q for v in w]
            for a in b:
                f=a[p]
                if f:
                    for k in range(p,self.N): a[k]=(a[k]-f*w[k])%self.q
            j=sum(t<p for t in piv)
            b.insert(j,w);piv.insert(j,p)
        return tuple(tuple(a) for a in b)
    def tangent_rank(self,fs):
        mat=[[f[self.idx[tuple(int(i==j) for i in range(self.n))]] for j in range(self.n)] for f in fs]
        q=self.q;n=self.n
        rank=0
        for col in range(n):
            j=next((i for i in range(rank,n) if mat[i][col]),None)
            if j is None:continue
            mat[rank],mat[j]=mat[j],mat[rank]
            t=pow(mat[rank][col],-1,q)
            for k in range(col,n):mat[rank][k]=mat[rank][k]*t%q
            for i in range(rank+1,n):
                fac=mat[i][col]
                for k in range(col,n):mat[i][k]=(mat[i][k]-fac*mat[rank][k])%q
            rank+=1
        return rank


def exhaustive(n,d,q):
    A=Trunc(n,d,q);L=A.N-1
    counts=Counter();fibers=defaultdict(Counter)
    checked=0
    for coef in product(range(q),repeat=n*L):
        fs=[(0,)+tuple(coef[i*L:(i+1)*L]) for i in range(n)]
        ok,vals=A.compose_idempotent(fs)
        if not ok:continue
        checked+=1
        r=A.tangent_rank(fs)
        counts[r]+=1
        image_key=A.rref_key(vals)
        fibers[r][image_key]+=1
    for r in range(n+1):
        pred_img,pred_fiber,pred_total=predicted(n,d,q,r)
        assert counts[r]==pred_total, ('count',n,d,q,r,counts[r],pred_total)
        assert len(fibers[r])==pred_img, ('image number',n,d,q,r,len(fibers[r]),pred_img)
        assert set(fibers[r].values())=={pred_fiber},('fiber size',n,d,q,r,set(fibers[r].values()),pred_fiber)
        expected_len=comb(r+d-1,d-1)
        assert all(len(k)==expected_len for k in fibers[r]), ('image dimension',r,expected_len)
    print('OK',{'n':n,'d':d,'q':q,'total_endomorphisms':q**(n*L),'idempotents':checked,'ranks':dict(counts),'images_by_rank':{r:len(v) for r,v in fibers.items()}})


if __name__=='__main__':
    exhaustive(2,3,2)
    exhaustive(2,3,3)
    exhaustive(2,4,2)
    exhaustive(3,2,2)
    exhaustive(3,2,3)
    print('ALL_EXACT_CHECKS_PASSED')

# Separate extension-field check: F_4 = F_2[t]/(t^2+t+1).
def test_f4_linear():
    def mult(a,b):
        z=0
        if b&1:z^=a
        if b&2:z^=(a<<1)
        if z&4:z^=0b111
        return z
    by_r=Counter();by_image=defaultdict(Counter)
    for a,b,c,d in product(range(4),repeat=4):
        xx=mult(a,a)^mult(b,c)
        xy=mult(a,b)^mult(b,d)
        yx=mult(c,a)^mult(d,c)
        yy=mult(c,b)^mult(d,d)
        if (xx,xy,yx,yy)!=(a,b,c,d):continue
        det=mult(a,d)^mult(b,c)
        r=2 if det else (1 if (a or b or c or d) else 0)
        by_r[r]+=1
        if r==0:key='zero'
        elif r==2:key='full'
        else:
            v=(a,c) if a or c else (b,d)
            inv=next(t for t in range(1,4) if mult(t,next(w for w in v if w))==1)
            key=(mult(v[0],inv),mult(v[1],inv))
        by_image[r][key]+=1
    for r in range(3):
        images,fiber,total=predicted(2,2,4,r)
        assert by_r[r]==total and len(by_image[r])==images and set(by_image[r].values())=={fiber}
    print('OK',{'n':2,'d':2,'q':4,'idempotents':sum(by_r.values()),'ranks':dict(by_r),'images_by_rank':{r:len(v) for r,v in by_image.items()}})

if __name__=='__main__':
    test_f4_linear()
    print('ALL_EXACT_CHECKS_PASSED_WITH_F4')
