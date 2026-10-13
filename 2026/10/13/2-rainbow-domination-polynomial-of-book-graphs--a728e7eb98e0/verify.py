#!/usr/bin/env python3
from itertools import product
from collections import defaultdict

LABELS = (0,1,2,3)
WT = (0,1,1,2)

def padd(a,b):
    out=[0]*(max(len(a),len(b)))
    for i,v in enumerate(a): out[i]+=v
    for i,v in enumerate(b): out[i]+=v
    return out

def pscale(a,c,shift=0):
    out=[0]*(len(a)+shift)
    for i,v in enumerate(a): out[i+shift]=c*v
    return out

def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: out[i+j]+=x*y
    return out

def ppow(a,n):
    out=[1]
    base=a[:]
    while n:
        if n&1: out=pmul(out,base)
        n//=2
        if n: base=pmul(base,base)
    return out

def formula(n):
    A0=[0,0,6,4,1]
    A1=[0,0,3,1]
    B1=[0,1,6,4,1]
    B2=[0,2,6,4,1]
    B3=[0,3,6,4,1]
    B4=[1,4,6,4,1]
    out=ppow(A0,n)
    out=padd(out, pscale(pmul([1,1],ppow(A1,n)),-4))
    out=padd(out, [0]*(2*n)+[6])
    out=padd(out, pscale(ppow(B1,n),4,1))
    out=padd(out, pscale(ppow(B2,n),6,2))
    out=padd(out, pscale(ppow(B3,n),4,3))
    out=padd(out, pscale(ppow(B4,n),1,4))
    while out and out[-1]==0: out.pop()
    return out

def local_ok(p,q,a,b):
    if a==0 and (p|b)!=3: return False
    if b==0 and (q|a)!=3: return False
    return True

def state_poly(n):
    total=defaultdict(int)
    for p in LABELS:
        for q in LABELS:
            # state=(union of page-a labels, union of page-b labels, weight)
            dp={(0,0,WT[p]+WT[q]):1}
            for _ in range(n):
                nd=defaultdict(int)
                for (ua,ub,w),count in dp.items():
                    for a in LABELS:
                        for b in LABELS:
                            if local_ok(p,q,a,b):
                                nd[(ua|a,ub|b,w+WT[a]+WT[b])] += count
                dp=nd
            for (ua,ub,w),count in dp.items():
                if p==0 and (q|ua)!=3: continue
                if q==0 and (p|ub)!=3: continue
                total[w]+=count
    deg=max(total)
    return [total[i] for i in range(deg+1)]

def direct_ok(n,vals):
    p,q=vals[0],vals[1]
    ua=ub=0
    for i in range(n):
        a,b=vals[2+2*i],vals[3+2*i]
        ua |= a
        ub |= b
        if not local_ok(p,q,a,b): return False
    if p==0 and (q|ua)!=3: return False
    if q==0 and (p|ub)!=3: return False
    return True

def brute_poly(n):
    total=defaultdict(int)
    for vals in product(LABELS, repeat=2+2*n):
        if direct_ok(n,vals):
            total[sum(WT[v] for v in vals)] += 1
    deg=max(total)
    return [total[i] for i in range(deg+1)]

expected_min={1:(2,4),2:(3,4),3:(4,5),4:(4,1),5:(4,1),6:(4,1),7:(4,1),8:(4,1),9:(4,1),10:(4,1)}
expected_tot={1:183,2:2629,3:35991,4:486109,5:6575823,6:89538949,7:1229263911}

labelings=0
coefficient_checks=0
for n in range(1,5):
    b=brute_poly(n)
    f=formula(n)
    assert b==f, (n,b,f)
    labelings += 4**(2+2*n)
    coefficient_checks += len(f)

for n in range(1,11):
    s=state_poly(n)
    f=formula(n)
    assert s==f, (n,s,f)
    coefficient_checks += len(f)
    nz=[i for i,c in enumerate(f) if c]
    assert (nz[0],f[nz[0]])==expected_min[n]
    if n in expected_tot:
        assert sum(f)==expected_tot[n]

print("VERIFY_OK brute_n=1..4 labelings=%d state_n=1..10 coefficient_checks=%d minimum_checks=10 total_checks=7 max_order=22" % (labelings, coefficient_checks))
