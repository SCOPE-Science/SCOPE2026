#!/usr/bin/env python3
"""Finite direct checks of geometric fixed-space face rule and predicted mod-two Betti ranks.
Parameters are orbit weights of part-preserving permutation groups.
"""
from itertools import combinations, product
from collections import defaultdict
from random import Random

def predicted(parts,d):
    if all(sum(p)<d for p in parts): return None
    if any(sum(p)<d for p in parts): return {}
    polys=[]
    for p in parts:
        T=sum(p)-d
        if T<0:return {}
        if T==0 or min(p)>T:
            polys.append({0:1});continue
        weights=sorted(p)
        first=weights[0]
        P=defaultdict(int)
        for mask in range(1 << (len(weights)-1)):
            size=mask.bit_count()
            total=sum(weights[j+1] for j in range(len(weights)-1) if mask>>j&1)
            if T-first < total <= T: P[size]+=1
        if not P:return {}
        polys.append(P)
    poly={0:1}
    for p in polys:
        new=defaultdict(int)
        for i,x in poly.items():
            for j,y in p.items():new[i+j]+=x*y
        poly=new
    k=len(parts)
    return {j+k-2:c for j,c in poly.items() if c}

def gf2_rank(rows):
    piv={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k not in piv:
                piv[k]=x;break
            x ^= piv[k]
    return len(piv)

def computed(parts,d):
    p=[i for x in parts for i in x]
    if all(sum(x)<d for x in parts):return None
    r=len(p)
    fs=defaultdict(list)
    for mask in range(1<<r):
        off=0;valid=False
        for weights in parts:
            if sum(w for j,w in enumerate(weights) if not mask>>(off+j)&1)>=d:valid=True
            off+=len(weights)
        if valid:fs[mask.bit_count()-1].append(mask)
    ranks={}
    for j in range(0,r):
        faces=fs[j];lower=fs[j-1]
        ids={f:i for i,f in enumerate(lower)}
        rows=[]
        for f in faces:
            row=0
            for bit in range(r):
                if f>>bit&1:
                    lo=f^(1<<bit)
                    if lo in ids:row ^= 1<<ids[lo]
            rows.append(row)
        ranks[j]=gf2_rank(rows)
    output={}
    for j in range(0,r):
        dimension=len(fs[j]);boundary=ranks.get(j,0);higher=ranks.get(j+1,0)
        rank=dimension-boundary-higher
        if rank:output[j]=rank
    return output

def all_comp(n):
    if n==0:yield []
    else:
        for i in range(1,n+1):
            for rest in all_comp(n-i):yield [i]+rest

if __name__=='__main__':
    # The full family comprises all orbit profiles, realized by cycles on each block.
    count=0
    for a in range(2,6):
        for b in range(2,6):
            for A in all_comp(a):
                for B in all_comp(b):
                    if len(A)+len(B)>8:continue
                    for d in range(2,min(a,b)+1):
                        actual=computed([A,B],d)
                        pred=predicted([A,B],d)
                        assert actual==pred, (A,B,d,actual,pred)
                        count+=1
    print('exhaustive bipartite weight-profile checks:',count)
    example=[[1,1,2,2,3],[4]]
    actual=computed(example,4); pred=predicted(example,4)
    assert actual==pred=={2:2,3:1},(actual,pred)
    print('mixed-dimensional example',example,'threshold',4,'Betti',actual)
    rng=Random(20261026)
    for i in range(80):
        k=rng.randint(2,4)
        parts=[]
        for _ in range(k):
            r=rng.randint(1,3)
            parts.append([rng.randint(1,3) for _ in range(r)])
        if sum(map(len,parts))>8:continue
        d=rng.randint(2,6)
        a=computed(parts,d);p=predicted(parts,d)
        assert a==p,(parts,d,a,p)
    print('80 seeded multipartite profiles checked (up to 8 orbit vertices)')
