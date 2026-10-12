from itertools import product
from math import comb

def comps(total,n,prefix=()):
    if n==1:
        yield prefix+(total,); return
    for a in range(total+1):
        yield from comps(total-a,n-1,prefix+(a,))

def local_ranks(alpha):
    coeff=[1]
    for a in alpha:
        nxt=[0]*(len(coeff)+a)
        for i,c in enumerate(coeff):
            for j in range(a+1): nxt[i+j]+=c
        coeff=nxt
    return coeff

def local_max(alpha): return max(local_ranks(alpha))

def predicted_local(alpha):
    d=sum(alpha)
    nz=sorted([a for a in alpha if a], reverse=True)
    if len(nz)==1: return 1
    if d==2 and nz==[1,1]: return 2
    if d>=3 and nz==[d-1,1]: return 2
    return 3

def a(n,d):
    if d==1:return 0
    if d==2:return comb(n,2)
    return n*(n-1)

def formula(ns,ds):
    p=1
    for n in ns:p*=n
    out=p
    for i in range(len(ns)):
        q=a(ns[i],ds[i])
        for j,n in enumerate(ns):
            if i!=j:q*=n
        out+=q
    return out

local_tests=0
for n in range(2,6):
    for d in range(1,7):
        for alpha in comps(d,n):
            r=local_max(alpha)
            p=predicted_local(alpha)
            assert (r if r<=2 else 3)==p
            local_tests+=1

formats=[]
for n1 in range(2,5):
    for n2 in range(2,5):
        for d1 in range(1,5):
            for d2 in range(1,5): formats.append(((n1,n2),(d1,d2)))
for ds in product(range(1,5), repeat=3): formats.append(((2,2,2),ds))
formats += [((3,2,2),(2,3,4)),((2,3,2),(4,2,3)),((2,2,3),(3,4,2))]

coord_tests=0
for ns,ds in formats:
    locals_=[[local_max(alpha) for alpha in comps(d,n)] for n,d in zip(ns,ds)]
    count=0
    for rs in product(*locals_):
        rank=1
        for r in rs: rank*=r
        if rank<=2: count+=1
        coord_tests+=1
    assert count==formula(ns,ds),(ns,ds,count,formula(ns,ds))

print('VERIFY_OK', local_tests, len(formats), coord_tests)
