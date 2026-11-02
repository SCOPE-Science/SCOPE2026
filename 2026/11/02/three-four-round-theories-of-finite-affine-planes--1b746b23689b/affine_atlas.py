#!/usr/bin/env python3
"""Finite structural atlas of incidence configurations, independent of type recursion.
The enriched diagrams deliberately retain parallelism and concurrency as strategic
bookkeeping; they are not additional symbols in the asserted first-order language.
"""
from itertools import product

def ff_add(a,b,q): return a^b if q==4 else (a+b)%q
def ff_mul(a,b,q):
    if q!=4: return a*b%q
    return ((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))[a][b]

def plane(q):
    pts=tuple(product(range(q),repeat=2))
    lns=tuple(product(range(q+1),range(q)))
    n=len(pts)
    inc=[]
    for m,b in lns:
        inc.append(frozenset(i for i,(x,y) in enumerate(pts) if (x==b if m==q else y==ff_add(ff_mul(m,x,q),b,q))))
    return n,inc

def diagram(t,np,inc,full=False):
    k=len(t)
    ans=[]
    ans.extend(int(x>=np) for x in t)
    for i in range(k):
        for j in range(i+1,k):
            a,b=t[i],t[j]
            ans.append(int(a==b))
            ans.append(int((a<np and b>=np and a in inc[b-np]) or (b<np and a>=np and b in inc[a-np])))
    if full:
        for i in range(k):
            for j in range(i+1,k):
                a,b=t[i],t[j]
                ans.append(2 if a<np or b<np else int(inc[a-np].isdisjoint(inc[b-np])))
        if k==3:
            if all(z<np for z in t):
                ans.append(1 if any(all(z in l for z in t) for l in inc) else 0)
            elif all(z>=np for z in t):
                ans.append(1 if set.intersection(*(set(inc[z-np]) for z in t)) else 0)
            else:
                ans.append(2)
    return tuple(ans)

def atlas(q):
    np,inc=plane(q);n=np+len(inc)
    typ={}
    for k in (0,1,2,3):
        for t in product(range(n),repeat=k):
            d=diagram(t,np,inc,True)
            typ.setdefault(k,{})[d]=t
    results={}
    for k in range(4):
        results[k]={}
        for d,t in typ[k].items():
            results[k][d]=frozenset(diagram(t+(x,),np,inc,k+1<=3) for x in range(n))
    return results

a4=atlas(4)
a5=atlas(5)
for k in range(4):
    print('round',k,'enriched_classes',len(a4[k]),len(a5[k]),'diagrams_equal',a4[k].keys()==a5[k].keys(),'extension_sets_equal',a4[k]==a5[k])
assert a4==a5
print('PASS: universal diagrams and all extension sets match for affine orders four and five')
