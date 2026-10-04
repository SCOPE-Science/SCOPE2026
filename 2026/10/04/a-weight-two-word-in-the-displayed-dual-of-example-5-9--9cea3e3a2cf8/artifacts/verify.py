#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json, math
ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text())
def pf(es):
    z=0
    for e in es:z^=1<<e
    return z
def pm(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
    return r
def sh(v,n,s):
    s%=n
    if not s:return v
    return ((v<<s)&((1<<n)-1))|(v>>(n-s))
def V(a,b,c):return a|(b<<31)|(c<<40)
def rr(vs):
    d={}
    for x in vs:
        while x:
            p=x.bit_length()-1
            if p in d:x^=d[p]
            else:d[p]=x;break
    ps=sorted(d,reverse=True);R=[d[p] for p in ps]
    for i,p in enumerate(ps):
        for j in range(i):
            if (R[j]>>p)&1:R[j]^=R[i]
    return R
def ins(x,R):
    for r in R:
        p=r.bit_length()-1
        if (x>>p)&1:x^=r
    return x==0
def dot(a,b):return (a&b).bit_count()&1
p=pf([0,3,5]);q=pf([0,2,5]);B0=pm(p,q);A0=pm(pf([0,1]),B0);H=pf(range(9));xp1=pf([0,1])
RC=[V(sh(A0,31,s),0,0) for s in range(31)]
RC += [V(0,sh(xp1,9,s),0) for s in range(9)]
RC += [V(sh(B0,31,s%31),0,sh(H,9,s%9)) for s in range(math.lcm(31,9))]
C=rr(RC);assert len(C)==29
f1=pf([0,1,2,3,5]);f2=pf([0,1,2,4,5]);f3=pf([0,1,3,4,5]);f4=pf([0,2,3,4,5])
B=pm(pm(f1,f2),pm(f3,f4));A=pm(pf([0,1]),B)
RD=[V(sh(A,31,s),0,0) for s in range(31)]
RD += [V(0,sh(H,9,s),0) for s in range(9)]
RD += [V(sh(B,31,s%31),0,1<<(s%9)) for s in range(math.lcm(31,9))]
D=rr(RD);assert len(D)==20
assert all(dot(c,d)==0 for c in C for d in D)
assert len(rr(C+D))==48
w=V(0,0,pf([0,1]));assert w.bit_count()==2 and ins(w,D)
assert [i+1 for i in range(49) if (w>>i)&1]==[41,42]
assert not any(ins(1<<i,D) for i in range(49))
dist=Counter()
for m in range(1<<20):
    x=0
    for i,r in enumerate(D):
        if (m>>i)&1:x^=r
    dist[x.bit_count()]+=1
assert sum(dist.values())==1<<20
assert min(k for k in dist if k>0)==2 and dist[2]==36
assert dict(dist)=={int(k):v for k,v in cert["verified"]["dual_weight_distribution"].items()}
print("VERIFY_OK")
