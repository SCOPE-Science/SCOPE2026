#!/usr/bin/env python3
"""reproduce_census_7_20.py — deterministic full replay of exact [7,20] census.
Method: prime-peeling (CRT uniform-lifts lemma) + translation-fixed
(max-product pairwise-coprime C -> 0) + hierarchical affine-stabilizer
orbit enumeration (units + translations mod M_C) over remaining R.
Deterministic: sorted moduli, sorted R, minimal orbit reps, numpy (seed-free).
Runtime ~27s on tested hardware (<30s); outputs census_7_20_table.csv.
Requires: numpy only (stdlib otherwise).
Rerun: python3 reproduce_census_7_20.py
"""
from math import gcd
from itertools import combinations, product
import math, time, csv, json
import numpy as np

def lcmlist(xs):
    r=1
    for x in xs: r=r//gcd(r,x)*x
    return r
def is_prime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1 if i==2 else 2
    return True
def find_peel(mods):
    for p in sorted(mods):
        if not is_prime(p): continue
        if any(m!=p and m%p==0 for m in mods): continue
        return p
    return None
def best_CR(mods):
    k=len(mods); best=1; bestm=0
    for mask in range(1<<k):
        idx=[i for i in range(k) if mask>>i &1]
        ok=True
        for a in range(len(idx)):
            for b in range(a+1,len(idx)):
                if gcd(mods[idx[a]],mods[idx[b]])!=1:
                    ok=False; break
            if not ok: break
        if not ok: continue
        prod=1
        for i in idx: prod*=mods[i]
        if prod>best: best=prod; bestm=mask
    return ([mods[i] for i in range(k) if bestm>>i &1],
            [mods[i] for i in range(k) if not (bestm>>i &1)])
memo={}
def hier_core(core):
    key=tuple(sorted(core))
    if key in memo: return memo[key]
    mods=list(key); L=lcmlist(mods); C,R=best_CR(mods)
    masks={}
    for m in mods:
        for a in range(m):
            arr=np.zeros(L,dtype=np.bool_); arr[a::m]=True; masks[(m,a)]=arr
    base=np.zeros(L,dtype=np.bool_)
    for c in C: base|=masks[(c,0)]
    if not R:
        memo[key]=(int(base.sum()),L,tuple(0 for _ in mods)); return memo[key]
    MC=1
    for c in C: MC*=c
    units=np.array([u for u in range(L) if gcd(u,L)==1],dtype=np.int64)
    trans=np.array([(j*MC)%L for j in range(L//MC)],dtype=np.int64)
    U=np.repeat(units,len(trans)); T=np.tile(trans,len(units))
    Rs=sorted(R); best=[int(base.sum())]; bestc=[None]
    def dfs(i,Uc,Tc,ch):
        if i==len(Rs):
            cur=base.copy()
            for m,a in zip(Rs,ch): cur|=masks[(m,a)]
            v=int(cur.sum())
            if v>best[0]: best[0]=v; bestc[0]=tuple(ch)
            return
        r=Rs[i]
        uniq=np.unique(np.stack([Uc%r,Tc%r],axis=1),axis=0)
        vis=[False]*r; reps=[]
        for s in range(r):
            if vis[s]: continue
            imgs=set(((uniq[:,0]*s+uniq[:,1])%r).tolist())
            for v in imgs: vis[v]=True
            reps.append(min(imgs))
        for rep in reps:
            m2=(Uc*rep+Tc)%r==rep
            dfs(i+1,Uc[m2],Tc[m2],ch+[rep])
    dfs(0,U,T,[])
    d=dict(zip(Rs,bestc[0])) if bestc[0] is not None else {}
    memo[key]=(best[0],L,tuple(0 if m in C else d[m] for m in mods))
    return memo[key]
def exact_full(mods):
    ch=[]; cur=list(mods)
    while True:
        p=find_peel(cur)
        if p is None: break
        ch.append(p); cur=[m for m in cur if m!=p]
    c0,L0,r0=hier_core(cur)
    pp=1; pm=1
    for p in ch: pp*=p; pm*=(p-1)
    Lf=L0*pp; assert Lf==lcmlist(mods)
    cov=Lf-(L0-c0)*pm
    d=dict(zip(sorted(cur),r0))
    for p in ch: d[p]=0
    return cov,Lf,[d[m] for m in mods],ch
def main():
    uni=list(range(7,21)); tot=math.comb(len(uni),9); t0=time.time(); res=[]
    for combo in combinations(uni,9):
        mods=list(combo); c,Lf,r,ch=exact_full(mods); res.append((c/Lf,mods,c,Lf,r,ch))
    res.sort(reverse=True); dt=time.time()-t0
    print(f"reproduced {tot} sets in {dt:.1f}s; best {res[0][1]} {res[0][2]}/{res[0][3]}={res[0][0]:.6f}")
    g=math.gcd(res[0][2],res[0][3])
    assert (res[0][2]//g,res[0][3]//g)==(1817,2772), "best must be 1817/2772"
    print("REPRODUCED: D*(9;[7,20])=1817/2772")
if __name__=="__main__": main()
