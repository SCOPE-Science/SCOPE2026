"""Reproduce the dyadic divisibility census for Fibonacci-type recurrences.

Run: python3 verify.py
All arithmetic uses exact Python integers; no optional dependencies.
"""
from math import gcd

def val2(x):
    return None if x == 0 else (abs(x) & -abs(x)).bit_length()-1

def terms(u,v,nmax):
    a,b=u,v
    yield a
    for _ in range(nmax):
        yield b
        a,b=b,a+b

def branch(u,v):
    assert (u|v)&1
    z=list(terms(u,v,5))
    even=[i for i in range(6) if z[i]%2 == 0]
    high=[i for i in even if z[i]%4 == 0]
    assert len(even)==2 and len(high)==1
    return high[0], (z[high[0]]%8==0)

def compute_census(u,v,k):
    mod=2**k
    r,has_root=branch(u,v)
    period=6*2**max(0,k-3)
    z=list(terms(u,v,period-1))
    hits=[n for n in range(period) if z[n]%mod==0]
    if k==1: assert len(hits)==period//3
    if k==2: assert len(hits)==period//6
    if k>=3:
        assert len(hits)==(1 if has_root else 0),(u,v,k,r,hits)
        if hits: assert hits[0]%6==r
    # Recheck period: U_{n+period} congruent U_n modulo 2^k for k>=1.
    nextz=list(terms(u,v,2*period-1))
    assert all(nextz[n+period]%mod==pow(5,2**max(0,k-3),mod)*nextz[n]%mod for n in range(period)),(u,v,k)
    return hits

def direct_reference(u,v,nmax):
    r,root=branch(u,v)
    s=list(terms(u,v,nmax))
    rr=(r+3)%6
    for n,x in enumerate(s):
        vv=val2(x)
        if n%6==rr: assert vv==1,(u,v,n,x,vv,'low')
        elif n%6==r:
            if not root: assert vv==2,(u,v,n,x,vv,'high')
            else: assert vv is None or vv>=3,(u,v,n,x,vv,'root')
        else: assert vv==0,(u,v,n,x,vv,'odd')

pair_count=0; count_root=0; census_tests=0
for u in range(8):
 for v in range(8):
    if (u|v)&1 == 0: continue
    r,yes=branch(u,v)
    count_root+=yes
    pair_count+=1
    for k in range(1,12):
        compute_census(u,v,k)
        census_tests+=1
    direct_reference(u,v,450)
assert pair_count==48 and count_root==24
extra_pairs=0
for u in range(-30,31):
 for v in range(-30,31):
    if (u|v)&1 == 0: continue
    direct_reference(u,v,250)
    extra_pairs+=1
assert extra_pairs==2760
print(f'VERIFY_OK primitive_classes_mod8={pair_count} unbounded_classes={count_root} modular_censuses={census_tests} additional_integer_pairs={extra_pairs}')
