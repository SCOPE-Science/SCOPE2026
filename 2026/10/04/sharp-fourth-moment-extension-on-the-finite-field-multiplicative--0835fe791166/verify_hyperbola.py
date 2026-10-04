#!/usr/bin/env python3
from collections import defaultdict
from math import isqrt


def primes_upto(n):
    out=[]
    for x in range(3,n+1,2):
        ok=True
        for d in range(3,isqrt(x)+1,2):
            if x%d==0:
                ok=False
                break
        if ok:
            out.append(x)
    return out


def pair_fibers(p, weights=None):
    if weights is None:
        weights={t:1 for t in range(1,p)}
    fib=defaultdict(list)
    for a in range(1,p):
        ia=pow(a,-1,p)
        for b in range(1,p):
            ib=pow(b,-1,p)
            fib[((a+b)%p,(ia+ib)%p)].append((a,b,weights[a]*weights[b]))
    return fib

checks=0
ext_checks=0
for p in primes_upto(101):
    fib=pair_fibers(p)
    energy=sum(len(v)**2 for v in fib.values())
    target=3*(p-1)*(p-2)
    assert energy==target,(p,energy,target)
    assert len(fib[(0,0)])==p-1
    assert max(len(v) for k,v in fib.items() if k!=(0,0))<=2
    checks+=1

    # Deterministic constant-modulus extremizer with common antipodal product +1.
    w={}
    for t in range(1,p):
        if t in w:
            continue
        u=(-t)%p
        s=-1 if min(t,u)%2 else 1
        w[t]=s
        w[u]=s
    wfib=pair_fibers(p,w)
    Q=0
    for entries in wfib.values():
        z=sum(c for _,_,c in entries)
        Q+=z*z
    S=p-1
    qtarget=3*(p-2)*(p-1)  # [3(p-2)/(p-1)] S^2
    assert Q==qtarget,(p,Q,qtarget)
    ext_checks+=1

print(f"VERIFY_OK primes={checks} max_prime=101 energy_checks={checks} extremizer_checks={ext_checks}")
