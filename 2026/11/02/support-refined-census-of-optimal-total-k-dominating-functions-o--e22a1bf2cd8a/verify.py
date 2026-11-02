#!/usr/bin/env python3
"""Exact self-contained checks for optimal total {k}-dominating functions on cycles.

No external packages or data. Uses independent original-neighborhood dynamic
programming and direct assignment enumeration for small cases.
"""
from itertools import product

def formula(n,k):
    assert n>=3 and k>=1
    if n%4==0:
        return (k*n//2,(k+1)**2)
    if n%4==2:
        return (k*n//2+(k&1), (n//2)**2 if k&1 else 1)
    return ((k*n+1)//2 if k&1 else k*n//2, n if k&1 else 1)

def support_formula(n,k):
    assert n>=3 and k>=2
    if n%4==0:
        return {n//2:4, 3*n//4:4*(k-1), n:(k-1)**2}
    return {n:formula(n,k)[1]}

def direct(n,k):
    best=None;cnt=0;supports={}

    for x in product(range(k+1),repeat=n):
        if all(x[(i-1)%n]+x[(i+1)%n]>=k for i in range(n)):
            v=sum(x)
            if best is None or v<best:
                best,cnt=v,1
                supports={sum(a>0 for a in x):1}
            elif v==best:
                cnt+=1
                h=sum(a>0 for a in x)
                supports[h]=supports.get(h,0)+1
    return best,cnt,supports

def dynamic(n,k):
    # Independently enforce the graph's ORIGINAL cyclic constraints.
    # State tracks the first two and last two labels for a closure check.
    ans=None;count=0
    for first in range(k+1):
        for second in range(k+1):
            curr={(first,second):(first+second,1)}
            for pos in range(2,n):
                nxt={}
                for (a,b),(cost,multiplicity) in curr.items():
                    for c in range(k+1):
                        if a+c<k:continue
                        key=(b,c);w=cost+c
                        if key not in nxt or w<nxt[key][0]:
                            nxt[key]=(w,multiplicity)
                        elif w==nxt[key][0]:
                            nxt[key]=(w,nxt[key][1]+multiplicity)
                curr=nxt
            for (lastbutone,last),(w,multiplicity) in curr.items():
                # Edges of the constraint graph for i=n-1 and i=0.
                if lastbutone+first<k or last+second<k:continue
                if ans is None or w<ans:ans,count=w,multiplicity
                elif w==ans:count+=multiplicity
    return ans,count

full=0
for n in range(3,9):
    for k in range(1,4):
        z,c,supports=direct(n,k)
        assert (z,c)==formula(n,k),(n,k,(z,c),formula(n,k))
        if k>=2:
            assert supports=={h:c for h,c in support_formula(n,k).items() if c}, (n,k,supports,support_formula(n,k))
        full+=1
print('ORIGINAL_NEIGHBORHOOD_EXHAUSTIVE_OK',full)

cases=0
for n in range(3,31):
    for k in range(1,5):
        d=dynamic(n,k)
        f=formula(n,k)
        assert d==f,(n,k,d,f)
        cases+=1
print('INDEPENDENT_CYCLIC_DYNAMIC_PROGRAM_OK',cases)
print('VERIFY_OK')
