#!/usr/bin/env python3
"""Finite digit and carry checks for reverse multiples (pure Python)."""
from itertools import product

def decode(n,b,c):
    k=len(c)-1
    if not (c[0]==c[-1]==0 and c==c[::-1]):return None
    if not all(0<=v<n for v in c):return None
    z=n*n-1
    ds=[]
    for j in range(k+1):
        top=n*b*(c[k-j+1] if k-j+1<=k else 0)-n*c[k-j]+b*(c[j+1] if j+1<=k else 0)-c[j]
        if top%z:return None
        d=top//z
        if not 0<=d<b:return None
        ds.append(d)
    if not ds[0] or not ds[-1]:return None
    v=sum(d*b**j for j,d in enumerate(ds))
    w=sum(ds[k-j]*b**j for j in range(k+1))
    if v!=n*w:return None
    for j in range(k+1):
        carry_after=c[j+1] if j+1<=k else 0
        if b*carry_after-c[j] != n*ds[k-j]-ds[j]:return None
    return ds

def finite_test():
    found=checked=0
    for n in range(2,13):
        for b in range(n+1,41):
            for k in range(2,8):
                for a in product(range(n),repeat=k//2):
                    c=[0]*(k+1)
                    for j,x in enumerate(a,1):
                        c[j]=x;c[k-j]=x
                    checked+=1
                    ds=decode(n,b,c)
                    if ds is not None:
                        found+=1
                        assert all(v%(n-1)==0 for v in c)
                        assert b%(n+1)==0
                        assert all(v in (0,n-1) for v in c)
    assert decode(4,10,[0,3,3,3,0])==[2,1,9,7,8]
    assert decode(9,10,[0,8,8,8,0])==[1,0,9,8,9]
    assert found>0
    return checked,found
if __name__=='__main__':
    print('VERIFY_OK: symmetric carry tuples tested, legitimate palintiples: %s' %(finite_test(),))
