#!/usr/bin/env python3
from math import isqrt
LIMIT=1_000_000
spf=list(range(LIMIT+1))
for p in range(2,isqrt(LIMIT)+1):
    if spf[p]==p:
        for m in range(p*p,LIMIT+1,p):
            if spf[m]==m:spf[m]=p

def prime(n):
    if n<2:return False
    if n<=LIMIT:return spf[n]==n
    return all(n%d for d in range(2,isqrt(n)+1))
branches=[]
for q,c,a in [(7,288,17),(11,80,9)]:
    for d in range(1,isqrt(c)+1):
        if c%d:continue
        r=a+d;s=a+c//d
        if q<r<s and prime(r) and prime(s):
            branches.append(3*q*r*s)
assert sorted(branches)==[10659,12441,24969],branches
hits=[];checked=0
for n in range(2,LIMIT+1):
    x=n;fac=[];sig=1;phi=1
    while x>1:
        p=spf[x];e=0
        while x%p==0:
            x//=p;e+=1
        fac.append((p,e))
        if len(fac)>4:break
    if len(fac)!=4 or any(e!=1 for p,e in fac):continue
    checked+=1
    for p,e in fac:sig*=p+1;phi*=p-1
    if sig==3*phi:hits.append(n)
assert hits==[10659,12441,24969],hits
print("VERIFY_OK", "limit",LIMIT,"checked",checked,"hits",hits,"branches",branches)
