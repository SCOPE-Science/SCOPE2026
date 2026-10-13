#!/usr/bin/env python3
from math import gcd

def omega(n):
    c=0; d=2
    while d*d<=n:
        if n%d==0:
            c+=1
            while n%d==0:n//=d
        d+=1
    return c+(n>1)

def factor(n):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:n//=d;a+=1
            out.append((d,a))
        d+=1
    if n>1: out.append((n,1))
    return out

def formula(p,e):
    N=p**(e-1)*(p-1); Nm=p**(e-2)*(p-1)
    prod=1
    for ell,_ in factor(N):
        x=Nm; a=0
        while x%ell==0: x//=ell; a+=1
        prod*=1+ell**a
    return 1+2**omega(N)+prod

def order(a,m):
    if gcd(a,m)!=1:return 0
    x=1
    for k in range(1,m+1):
        x=x*a%m
        if x==1:return k
    raise AssertionError

def primitive_unit(m,p,e):
    target=p**(e-1)*(p-1)
    for a in range(2,m):
        if order(a,m)==target:return a
    raise AssertionError('no primitive unit found')

def enumerate_endos(p,e):
    m=p**e; g=primitive_unit(m,p,e)
    maps=set()
    for A in range(m):
      for B in range(m):
        f={1:1}; q=[1]; ok=True
        while q and ok:
            x=q.pop()
            y=f[x]
            for gen,img in ((g,A),(p,B)):
                xx=x*gen%m; yy=y*img%m
                if xx in f:
                    if f[xx]!=yy: ok=False; break
                else:
                    f[xx]=yy; q.append(xx)
        if not ok or len(f)!=m: continue
        tup=tuple(f[x] for x in range(m))
        # Full multiplication-table verification.
        if all(tup[x*y%m]==(tup[x]*tup[y])%m for x in range(m) for y in range(m)):
            maps.add(tup)
    return maps

for p,e in [(3,2),(3,3),(5,2),(7,2)]:
    maps=enumerate_endos(p,e)
    ids=[f for f in maps if all(f[f[x]]==f[x] for x in range(p**e))]
    want=formula(p,e)
    assert len(ids)==want,(p,e,len(ids),want)
    print(f'p={p} e={e} endomorphisms={len(maps)} idempotents={len(ids)} formula={want}')
print('CHECK_OK')
