#!/usr/bin/env python3
"""Finite exact modular checks of the four-particle theta top-cycle calculation.
All claims for arbitrary arm numbers require the accompanying algebraic proof.
"""
from itertools import combinations_with_replacement
from math import comb

def monomials(k,degree):
    return [tuple(t.count(i) for i in range(k)) for t in combinations_with_replacement(range(k),degree)]

def rank_sparse(cols,p=1000003):
    pivots={}
    for c in cols:
        v={i:x%p for i,x in c.items() if x%p}
        while v:
            i=min(v)
            if i not in pivots:
                inv=pow(v[i],-1,p)
                pivots[i]={j:(x*inv)%p for j,x in v.items()}
                break
            factor=v[i]
            for j,x in pivots[i].items():
                new=(v.get(j,0)-factor*x)%p
                if new: v[j]=new
                elif j in v: del v[j]
    return len(pivots)

def add(a,b,scale=1):
    r=a.copy()
    for i,x in b.items():
        t=r.get(i,0)+scale*x
        if t:r[i]=t
        else:r.pop(i,None)
    return r

def rows(k,n):
    m=k-1
    src=monomials(k,n-2)
    tgt=monomials(k,n-1)
    rr={a:i for i,a in enumerate(tgt)}
    ret={}
    for i in range(1,k):
        for j in range(1,k):
            for t in src:
                def plus(a): return tuple(v+(h==a) for h,v in enumerate(t))
                col={}
                for a,s in ((i,1),(0,-1)):
                    r=(m+j-1)*len(tgt)+rr[plus(a)]
                    col[r]=col.get(r,0)+s
                for a,s in ((j,-1),(0,1)):
                    r=(i-1)*len(tgt)+rr[plus(a)]
                    col[r]=col.get(r,0)+s
                ret[(i,j,t)]={a:b for a,b in col.items() if b}
    return ret

def dim_s211(m):return m*(m+1)*(m-1)*(m-2)//8 if m>=3 else 0
def dim_s22(m):return m*m*(m*m-1)//12

def check(k,n):
    entries=rows(k,n)
    rank=rank_sparse(entries.values())
    total=len(entries)-rank
    print('arms',k,'particles',n,'cycles',total,'d2_rank',rank,flush=True)
    if n==3:
        assert total==comb(k-1,3) if k>=4 else total==0
    if n==4:
        m=k-1; src=monomials(k,2)
        plus=[add(entries[(i,j,t)],entries[(j,i,t)],-1) for i in range(1,k) for j in range(i+1,k) for t in src]
        minus=[add(entries[(i,j,t)],entries[(j,i,t)],+1) for i in range(1,k) for j in range(i+1,k) for t in src]
        minus += [entries[(i,i,t)] for i in range(1,k) for t in src]
        dp=len(plus)-rank_sparse(plus)
        dm=len(minus)-rank_sparse(minus)
        wanted_p=(comb(m,3) if m>=3 else 0)+dim_s211(m)
        wanted_m=dim_s22(m)
        assert (total,dp,dm)==(wanted_p+wanted_m,wanted_p,wanted_m),(k,total,dp,dm,wanted_p,wanted_m)
        print(' pole_plus',dp,' pole_minus',dm,'MATCH',flush=True)

if __name__=='__main__':
    for k in (3,4,5,6): check(k,3)
    for k in (3,4,5,6): check(k,4)
    print('VERIFY_OK')
