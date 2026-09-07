#!/usr/bin/env python3
"""Self-contained replay for n=12 Kronecker vanishing census.
Recomputes S12 character table via Murnaghan-Nakayama, verifies
(dim hook formula, sum dim^2=12!, row/col orthogonality),
recomputes extremal triple T*=((5,3,2,1,1)^3) class sum = 945 exactly
via Fractions/integers, and spot-checks 20 random S3-orbits against
kron_table_S3.csv. Runs in <60s single-core pure Python (no deps beyond stdlib+numpy optional).
Usage: python3 replay.py [--full]  (--full recomputes all 79079 orbits exactly, ~5-30s)
"""
import math, csv, random, sys, time
from functools import lru_cache
from fractions import Fraction
N=12; FACT=math.factorial(N)

def partitions(n, max_part=None):
    if max_part is None: max_part=n
    if n==0: yield []
    else:
        for first in range(min(max_part,n),0,-1):
            for rest in partitions(n-first, first):
                yield [first]+rest

def main():
    full = ("--full" in sys.argv)
    t0=time.time()
    parts=[tuple(p) for p in partitions(N)]
    assert len(parts)==77, len(parts)
    from collections import Counter
    def zof(cyc):
        m=Counter(cyc); z=1
        for i,c in m.items(): z*=(i**c)*math.factorial(c)
        return z
    zs=[zof(c) for c in parts]
    cl=[FACT//zz for zz in zs]
    assert sum(cl)==FACT
    allparts={n:[tuple(p) for p in partitions(n)] for n in range(N+1)}
    def subdiagrams(lam, target):
        lam=list(lam); r=len(lam); out=[]; cur=[0]*r
        def rec(i, maxv, rem):
            if i==r:
                if rem==0: out.append(tuple(cur))
                return
            if rem<0: return
            s=0; mm=maxv
            for j in range(i,r):
                mm=min(mm,lam[j]); s+=mm
            if rem>s: return
            for v in range(min(lam[i],maxv,rem),-1,-1):
                cur[i]=v; rec(i+1,v,rem-v)
            cur[i]=0
        rec(0,10**9,target)
        return out
    def is_rim(lam, mu):
        skew=set(); r=len(lam)
        for i in range(r):
            for c in range(mu[i],lam[i]): skew.add((i,c))
        if not skew: return (False,0)
        for (i,c) in list(skew):
            if (i,c+1) in skew and (i+1,c) in skew and (i+1,c+1) in skew: return (False,0)
        s=[next(iter(skew))]; seen={s[0]}
        while s:
            i,c=s.pop()
            for d in ((1,0),(-1,0),(0,1),(0,-1)):
                nb=(i+d[0],c+d[1])
                if nb in skew and nb not in seen: seen.add(nb); s.append(nb)
        if len(seen)!=len(skew): return (False,0)
        return (True,len({i for (i,c) in skew})-1)
    trans={}
    for n in range(N+1):
        for lam in allparts[n]:
            for k in range(1,n+1):
                lst=[]
                for mu in subdiagrams(lam,n-k):
                    ok,h=is_rim(lam,mu)
                    if ok: lst.append((tuple(x for x in mu if x>0), -1 if h%2 else 1))
                trans[(lam,k)]=lst
    @lru_cache(maxsize=None)
    def chi(lam,cyc):
        if len(cyc)==0: return 1 if len(lam)==0 else 0
        if len(lam)==0: return 0
        if sum(lam)!=sum(cyc): return 0
        k=cyc[0]; rest=cyc[1:]
        return sum(sgn*chi(nu,rest) for (nu,sgn) in trans[(lam,k)])
    C=[[chi(l,c) for c in parts] for l in parts]
    print(f"[1/5] char table 77x77 built in {time.time()-t0:.1f}s")
    # dims via hook formula
    def hook_dim(lam):
        if not lam: return 1
        cmax=lam[0]
        conj=[sum(1 for x in lam if x>c) for c in range(cmax)]
        prod=1
        for i,row in enumerate(lam):
            for j in range(row):
                prod*=(row-j)+(conj[j]-i)-1
        return FACT//prod
    jid=parts.index(tuple([1]*12))
    dims=[C[i][jid] for i in range(77)]
    hd=[hook_dim(l) for l in parts]
    assert hd==dims, "hook/dim mismatch"
    assert sum(d*d for d in dims)==FACT, "sum dim^2"
    print("[2/5] dims match hook formula; sum dim^2 = 479001600 OK")
    # orthogonality (exact integer)
    for l in range(77):
        for m in range(77):
            s=sum(C[l][a]*C[m][a]*cl[a] for a in range(77))
            assert s==(FACT if l==m else 0), (l,m)
    for a in range(77):
        for b in range(77):
            s=sum(C[l][a]*C[l][b] for l in range(77))
            assert s==(zs[a] if a==b else 0), (a,b)
    print("[3/5] row+column orthogonality OK (5929+5929 exact dots)")
    # extremal certificate
    ts=parts.index((5,3,2,1,1))
    tot=Fraction(0)
    for a in range(77):
        tot+=Fraction(C[ts][a]*C[ts][a]*C[ts][a], zs[a])
    assert tot==945, tot
    s=sum(C[ts][a]**3*cl[a] for a in range(77))
    assert s==945*FACT and s%FACT==0
    print("[4/5] extremal T*=((5,3,2,1,1)^3) class sum = 945 EXACT OK")
    # spot checks vs CSV
    import os
    csvpath=os.path.join(os.path.dirname(__file__),"kron_table_S3.csv")
    rows=list(csv.DictReader(open(csvpath)))
    assert len(rows)==79079, len(rows)
    def g_exact(i,j,k):
        ss=sum(C[i][a]*C[j][a]*C[k][a]*cl[a] for a in range(77))
        q,r=divmod(ss,FACT)
        assert r==0
        return q
    random.seed(12)
    sample=random.sample(rows,20)
    for r in sample:
        i,j,k=int(r["i"]),int(r["j"]),int(r["k"])
        assert g_exact(i,j,k)==int(r["g"]), (i,j,k)
    print("[5/5] 20 random S3-orbits match kron_table_S3.csv OK")
    # zero/nonzero + max from CSV
    vs=[int(r["g"]) for r in rows]
    assert max(vs)==945 and sum(1 for v in vs if v==0)==30336
    print(f"CENSUS OK: 30336 zero / 48743 nonzero / M=945 in {time.time()-t0:.1f}s total")
    if full:
        t1=time.time()
        nbad=0
        for r in rows:
            i,j,k=int(r["i"]),int(r["j"]),int(r["k"])
            if g_exact(i,j,k)!=int(r["g"]): nbad+=1
        assert nbad==0
        print(f"FULL recompute of 79079 orbits OK in {time.time()-t1:.1f}s")
if __name__=="__main__":
    main()
