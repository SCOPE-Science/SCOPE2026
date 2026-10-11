#!/usr/bin/env python3
"""Exact union-find barcodes of the nested incidence-graph filtration."""
from fractions import Fraction as F
from itertools import combinations
from random import Random

def barcodes(L):
    L=list(map(F,L));k=len(L)
    events=[]
    for i,j in combinations(range(k),2):events.append((-(L[i]+L[j]),0,('p',i,j),None))
    for i in range(k):
        events.append((-L[i],0,('a',i),None))
        for j in range(k):
            if j!=i: events.append((-L[i],1,('a',i),('p',min(i,j),max(i,j))))
    events.sort(key=lambda z:(z[0],z[1],str(z[2]),str(z[3])))
    par={};birth={};h0=[];h1=[]
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]];x=par[x]
        return x
    for time,typ,x,y in events:
        r=-time
        if typ==0:
            par[x]=x;birth[x]=r
        else:
            a=find(x);b=find(y)
            if a==b:
                h1.append(r)
            else:
                if (birth[a],str(a))<(birth[b],str(b)):a,b=b,a
                if birth[b]>r:h0.append((r,birth[b]))
                par[b]=a
    roots={find(x) for x in par}
    assert len(roots)==1
    return sorted(h0),sorted(h1),birth[next(iter(roots))]

def expected(L):
    L=list(map(F,L));k=len(L)
    pairs=sorted(((L[i]+L[j],i,j) for i,j in combinations(range(k),2)),reverse=True)
    top=set(pairs[0][1:])
    finite=sorted((max(L[i],L[j]),s) for s,i,j in pairs if {i,j}!=top)
    long=sorted(L,reverse=True)
    h1=sorted(Lx for j,Lx in enumerate(long,1) for _ in range(max(j-2,0)))
    return finite,h1,pairs[0][0]

def run():
    rng=Random(781)
    for k in range(3,13):
        for _ in range(1000):
            L=[F(rng.randint(1,15),rng.choice([1,1,2,3])) for _ in range(k)]
            found=barcodes(L);pred=expected(L)
            assert found==pred,(L,found,pred)
    print('BARCODES_OK',10000,'exact filtered-graph barcode tests, k=3..12')

if __name__=='__main__':run()
