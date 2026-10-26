#!/usr/bin/env python3
"""Independent finite checks for the length-refined MAS count of alternating binary words.
No external dependencies.
"""
from collections import Counter
from itertools import product

def subsequence(u,w):
    j=0
    for c in w:
        if j<len(u) and c==u[j]:
            j+=1
    return j==len(u)

def mas_direct(u,w):
    return not subsequence(u,w) and all(subsequence(u[:j]+u[j+1:],w) for j in range(len(u)))

def embedding_cost(u):
    if not u:return 0
    return len(u)+(u[0]=='1')+sum(u[i]==u[i-1] for i in range(1,len(u)))

def local_characterization(u,m):
    if len(u)<2:return False
    if u[:2]=='01' or any(u[i-1]==u[i+1]!=u[i] for i in range(1,len(u)-1)):
        return False
    E=embedding_cost(u)
    return E==2*m+1 or (E==2*m+2 and u[-1]==u[-2])

def poly_pred(max_m):
    polys=[Counter() for _ in range(max_m+1)]
    if max_m>=1:polys[1]=Counter({2:3})
    if max_m>=2:polys[2]=Counter({3:4,4:1})
    if max_m>=3:polys[3]=Counter({4:5,5:4})
    for m in range(4,max_m+1):
        v=Counter()
        for k,n in polys[m-1].items():v[k+1]+=2*n
        for k,n in polys[m-2].items():v[k+2]-=n
        for k,n in polys[m-3].items():v[k+4]+=n
        polys[m]=Counter({k:n for k,n in v.items() if n})
    return polys

def run_check():
    P=poly_pred(160)
    checked=0
    for m in range(1,10):
        w='01'*m
        hist=Counter()
        for k in range(1,2*m+2):
            for tup in product('01',repeat=k):
                u=''.join(tup)
                direct=mas_direct(u,w)
                predicted=local_characterization(u,m)
                if direct!=predicted:
                    raise AssertionError(('local',m,u,direct,predicted))
                if direct:hist[k]+=1
                checked+=1
        assert hist==P[m], ('enumeration',m,hist,P[m])
        assert hist[m+1]==m+2, ('sas',m,hist[m+1])
    # Independent stars-and-bars run count, not derived by GF recurrence.
    from math import comb
    def choose(n,r):
        return comb(n,r) if n>=0 and 0<=r<=n else 0
    run_profiles=0
    for m in range(1,161):
        whist=Counter()
        for k in range(2,2*m+2):
            for start in (0,1):
                for nruns in range(1,k+1):
                    E=2*k-nruns+start
                    if nruns==1:
                        allruns = equal_last = 1
                    elif start==0:
                        allruns=choose(k-nruns,nruns-1)
                        equal_last=choose(k-nruns-1,nruns-1)
                    else:
                        allruns=choose(k-nruns+1,nruns-1)
                        equal_last=choose(k-nruns,nruns-1)
                    if E==2*m+1:whist[k]+=allruns
                    if E==2*m+2:whist[k]+=equal_last
        assert whist==P[m], ('run-count',m,whist,P[m])
        run_profiles+=1
    totals=[sum(P[m].values()) for m in range(1,21)]
    assert totals[:10]==[3,5,9,16,28,49,86,151,265,465], totals[:10]
    print('ALTERNATING_BINARY_MAS_PASS brute_m=1..9 explicit_target_words=%d independent_run_m=1..15 run_profiles=%d gf_recurrence_m=1..160 initials=%s' %(checked,run_profiles,totals[:10]))

if __name__=='__main__':run_check()
