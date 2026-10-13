#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import comb

def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for a in range(1,n-k+2):
            for t in compositions(n-a,k-1):
                yield (a,)+t

def recs(n,k):
    p=list(compositions(n,k))
    assert len(p)==comb(n-1,k-1)
    out=[]
    for x,y in combinations(p,2):
        l1=sum(abs(a-b) for a,b in zip(x,y))
        c=sum(Fraction((a-b)*(a-b),a+b) for a,b in zip(x,y))
        out.append((l1,c,x,y))
    assert len(out)==comb(len(p),2)
    return out

def inversions(rs):
    vals=sorted({c for l,c,x,y in rs})
    rank={v:i+1 for i,v in enumerate(vals)}
    bit=[0]*(len(vals)+1)
    def add(i):
        while i<len(bit):
            bit[i]+=1; i+=i&-i
    def pre(i):
        s=0
        while i:
            s+=bit[i]; i-=i&-i
        return s
    groups={}
    for r in rs: groups.setdefault(r[0],[]).append(r)
    seen=ans=0
    for l in sorted(groups):
        g=groups[l]
        for _,c,_,_ in g:
            j=rank[c]; ans += seen-pre(j)
        for _,c,_,_ in g:
            add(rank[c]); seen+=1
    return ans

counts={}
for n in range(3,11):
    counts[n]={}
    for k in range(2,n):
        q=inversions(recs(n,k))
        if q: counts[n][k]=q

for n in range(3,10): assert counts[n]=={}
assert counts[10]=={3:288,4:8256,5:30100,6:17100}

N=10
a,b=(1,3,6),(3,1,6)
u,v=(1,2,7),(2,4,4)
def BC(x,y): return Fraction(sum(abs(s-t) for s,t in zip(x,y)),2*N)
def X2(x,y): return Fraction(2,N)*sum(Fraction((s-t)**2,s+t) for s,t in zip(x,y))
assert (BC(a,b),BC(u,v),X2(a,b),X2(u,v))==(Fraction(1,5),Fraction(3,10),Fraction(2,5),Fraction(4,11))
assert BC(a,b)<BC(u,v) and X2(a,b)>X2(u,v)
print("VERIFY_OK")
print("first_strict_total",10)
print("first_layer_counts",counts[10])
print("witness",BC(a,b),BC(u,v),X2(a,b),X2(u,v))
