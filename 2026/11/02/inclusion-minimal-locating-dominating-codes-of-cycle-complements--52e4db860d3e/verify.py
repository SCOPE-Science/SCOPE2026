#!/usr/bin/env python3
"""Reproducible finite corroboration for minimal locating-dominating sets of cycle complements.
No external packages are needed; finite checks do not replace an infinite proof.
"""
from collections import defaultdict, Counter
import json
from pathlib import Path
from itertools import product


def graph_ld(n, mask):
    """Use actual adjacency of K_n minus C_n, not gap characterizations."""
    selected=[i for i in range(n) if mask>>i&1]
    outs=[i for i in range(n) if not(mask>>i&1)]
    fingerprints=[]
    for v in outs:
        fingerprint=0
        for i in selected:
            if i not in ((v-1)%n,v,(v+1)%n): fingerprint|=1<<i
        if fingerprint==0:return False
        fingerprints.append(fingerprint)
    return len(fingerprints)==len(set(fingerprints))


def gap_minimal(n,mask):
    selected=[i for i in range(n) if mask>>i&1]
    k=len(selected)
    if k<3:return False
    a=[(selected[(i+1)%k]-selected[i]-1)%n for i in range(k)]
    t=a.count(3)
    if max(a)>3 or t>1 or any(a[i]>=2 and a[(i+1)%k]>=2 for i in range(k)):
        return False
    for i in range(k):
        p,x,y,q=a[(i-2)%k],a[(i-1)%k],a[i],a[(i+1)%k]
        s=x+y
        if t==0: necessary=(s>=3 or (1<=s<=2 and (p>=2 or q>=2)))
        else: necessary=(s>=2 or (s==1 and (p>=2 or q>=2)))
        if not necessary:return False
    return True


def transfer_counts(max_n):
    """Enumerate closed walks in the 27- and 64-state weighted transfer systems."""
    results=defaultdict(int)
    for regime in (0,1):
        symbols=range(3) if regime==0 else range(4)
        triples=list(product(symbols,repeat=3))
        adjacency={}
        for p,x,y in triples:
            nxt=[]
            for q in symbols:
                if x>=2 and y>=2:continue
                if y>=2 and q>=2:continue
                s=x+y
                good=(s>=3 or (1<=s<=2 and (p>=2 or q>=2))) if regime==0 else (s>=2 or (s==1 and (p>=2 or q>=2)))
                if good:nxt.append(((x,y,q),q+1,int(q==3)))
            adjacency[(p,x,y)]=nxt
        for root in triples:
            # polynomial in length n, number of gaps k, number of gaps of length three
            frontier={(root,0,0):1}
            for k in range(1,max_n+1):
                new=defaultdict(int)
                for (state,n,t),v in frontier.items():
                    for dest,weight,mark in adjacency[state]:
                        N=n+weight;T=t+mark
                        if N<=max_n and T<=regime:new[(dest,N,T)]+=v
                frontier=new
                for (state,n,t),v in frontier.items():
                    if state==root and n>=7 and t==regime:
                        results[n,k]+=v  # number of rooted cyclic gap strings
    weighted={}
    for (n,k),v in results.items():
        assert (n*v)%k==0,((n,k),v)
        weighted[n,k]=n*v//k
    return {n:Counter({k:v for (m,k),v in weighted.items() if m==n}) for n in range(7,max_n+1)}


def check_density_certificate():
    data=json.loads((Path(__file__).parent/'density_potential.json').read_text(encoding='utf-8'))
    h={tuple(map(int,key.split(','))):val for key,val in data['potential'].items()}
    triples=list(product(range(4),repeat=3))
    assert set(h)==set(triples) and all(type(v) is int for v in h.values())
    edges=0
    for p,a,b in triples:
        for q in range(4):
            if (a>=2 and b>=2) or (b>=2 and q>=2):continue
            s=a+b
            if not (s>=2 or (s==1 and (p>=2 or q>=2))):continue
            assert h[(a,b,q)]<=h[(p,a,b)]+4*q-3
            edges+=1
    assert edges==136
    for m in range(31):
        gaps=[3,0,1,0,2]+[0,1,0,2]*m+[1]
        k=len(gaps); n=k+sum(gaps)
        mask=0;pos=0
        for g in gaps:
            mask|=1<<pos
            pos+=1+g
        assert pos==n and gap_minimal(n,mask)
        assert (k,n)==(6+4*m,13+7*m)
    return edges


def main():
    direct={}
    tests=0
    for n in range(7,15):
        out=Counter()
        for mask in range(1<<n):
            tests+=1
            valid=graph_ld(n,mask)
            minimal=valid and all(not graph_ld(n,mask^(1<<i)) for i in range(n) if mask>>i&1)
            gap=gap_minimal(n,mask)
            assert minimal==gap,(n,mask,minimal,gap)
            if minimal:out[mask.bit_count()]+=1
        direct[n]=out
    edges=check_density_certificate()
    trans=transfer_counts(20)
    for n,c in direct.items():
        assert trans[n]==c,(n,trans[n],c)
    checks={7:{3:21},8:{3:8,4:20},15:{6:95,7:450,8:15},16:{6:16,7:560,8:284}}
    for n,c in checks.items():assert dict(sorted(trans[n].items()))==c,(n,trans[n])
    print('VERIFY_OK graph_cases=8 graph_subsets=%d transfer_orders=14 density_edges=%d witness_family=31'%(tests,edges))
    for n in range(7,21):print(n,dict(sorted(trans[n].items())))

if __name__=='__main__':main()
