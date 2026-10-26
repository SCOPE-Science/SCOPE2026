"""Finite arithmetic checks for digit-rotation gcd theorem."""
from math import gcd
from functools import reduce
from collections import Counter

def digits(n,b,m):
    a=[]
    for _ in range(m):a.append(n%b);n//=b
    assert n==0
    return list(reversed(a))

def rotation_values(n,b,m):
    ds=digits(n,b,m)
    out=[]
    for _ in range(m):
        val=0
        for x in ds:val=b*val+x
        out.append(val)
        ds=ds[1:]+ds[:1]
    return out

def phi(q):
    n=q;v=q;p=2
    while p*p<=n:
        if n%p==0:
            v=v//p*(p-1)
            while n%p==0:n//=p
        p+=1
    if n>1:v=v//n*(n-1)
    return v

checks=0
rows=[]
for b in range(2,12):
    for m in range(1,6):
        if b**m>150000:continue
        Q=b**m-1
        num=0;all_coprime=0;bad=0
        for n in range(b**(m-1),b**m):
            dd=digits(n,b,m)
            d=reduce(gcd,dd,0)
            rotations=rotation_values(n,b,m)
            g=reduce(gcd,rotations,0)
            pred=gcd(n,Q*d)
            assert g==pred,(b,m,n,dd,rotations,g,pred)
            if g==1:num+=1
            if gcd(n,Q)==1:all_coprime+=1
            if gcd(n,Q)==1 and d>1:bad+=1
            checks+=1
        assert num==all_coprime-bad
        rows.append((b,m,num,all_coprime,bad,float(num/((b-1)*b**(m-1))),float(phi(Q)/Q)))
print('VERIFY_OK:',checks,'direct rotation gcd tests across',len(rows),'base/length blocks')
for row in rows:
 if row[0] in (2,3,10):print('block',row)
print('decimal 148 rotations',rotation_values(148,10,3),'gcd',reduce(gcd,rotation_values(148,10,3)))
