#!/usr/bin/env python3
from itertools import product, combinations

def is_poset(n, state):
    # state on unordered pairs: 0 incomparable, 1 lower index < higher, 2 higher < lower
    lt=[[False]*n for _ in range(n)]
    k=0
    for i in range(n):
        for j in range(i+1,n):
            s=state[k]; k+=1
            if s==1: lt[i][j]=True
            elif s==2: lt[j][i]=True
    for i in range(n):
        for j in range(n):
            if lt[i][j]:
                for z in range(n):
                    if lt[j][z] and not lt[i][z]:
                        return None
    le=[[i==j or lt[i][j] for j in range(n)] for i in range(n)]
    return le

def inc_deg(le,i):
    return sum(1 for j in range(len(le)) if j!=i and not le[i][j] and not le[j][i])

def isotone(le,f):
    n=len(le)
    for i in range(n):
        for j in range(n):
            if le[i][j] and not le[f[i]][f[j]]:
                return False
    return True

def canonical(k):
    n=2*k
    le=[[False]*n for _ in range(n)]
    for i in range(n):
        li=i//2
        for j in range(n):
            lj=j//2
            le[i][j]=(i==j or li<lj)
    return le

def brute_general(max_n=4):
    totals=[]
    for n in range(1,max_n+1):
        m=n*(n-1)//2
        posets=eligible=with_fpf=0
        for st in product(range(3), repeat=m):
            le=is_poset(n,st)
            if le is None: continue
            posets+=1
            if max(inc_deg(le,i) for i in range(n))>1: continue
            eligible+=1
            fpfs=[]
            for f in product(range(n), repeat=n):
                if any(f[i]==i for i in range(n)): continue
                if isotone(le,f): fpfs.append(f)
            # theorem predicts existence iff every vertex has inc-degree 1 and mate map isotone
            mates=[]; perfect=True
            for i in range(n):
                js=[j for j in range(n) if j!=i and not le[i][j] and not le[j][i]]
                if len(js)!=1: perfect=False; break
                mates.append(js[0])
            pred = perfect and isotone(le,tuple(mates))
            assert (len(fpfs)>0)==pred
            if pred:
                assert len(fpfs)==1 and tuple(fpfs[0])==tuple(mates)
                with_fpf+=1
        totals.append((n,posets,eligible,with_fpf))
    return totals

def brute_canonical(kmax=3):
    out=[]
    for k in range(1,kmax+1):
        le=canonical(k); n=2*k
        mate=tuple(i^1 for i in range(n))
        assert isotone(le,mate) and all(mate[i]!=i for i in range(n))
        if k<=3:
            fpfs=[]
            for f in product(range(n), repeat=n):
                if any(f[i]==i for i in range(n)): continue
                if isotone(le,f): fpfs.append(f)
            assert fpfs==[mate]
            out.append((k,n,len(fpfs)))
    return out

if __name__=='__main__':
    print('GENERAL', brute_general(4))
    print('CANONICAL', brute_canonical(3))
    print('VERIFY_OK')
