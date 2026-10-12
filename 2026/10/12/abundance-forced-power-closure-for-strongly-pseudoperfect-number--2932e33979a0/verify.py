#!/usr/bin/env python3
import math

def divisors(n):
    ds=[]
    for d in range(1, math.isqrt(n)+1):
        if n%d==0:
            ds.append(d)
            if d*d!=n:
                ds.append(n//d)
    return sorted(ds)

def orbits(n):
    seen=set(); out=[]
    for d in divisors(n):
        if d in seen: continue
        e=n//d; seen.add(d); seen.add(e)
        out.append((d,e,d if d==e else d+e))
    return out

def can_omit_one_pair(n):
    A=sum(divisors(n))-2*n
    if A<0: return False
    os=orbits(n)
    target=A-(n+1)
    if target<0: return False
    weights=[w for d,e,w in os if not (d==1 and e==n)]
    bits=1
    for w in weights:
        bits |= bits << w
    return ((bits >> target) & 1)==1

for n in range(2,720):
    assert not can_omit_one_pair(n), n
assert can_omit_one_pair(720)
assert sum(divisors(720)) == 2418
witness=[(1,720),(10,72),(16,45),(18,40),(20,36)]
assert all(a*b==720 for a,b in witness)
assert sum(a+b for a,b in witness)==978
assert 2418-978==2*720
print('VERIFY_OK first_one_pair_escape=720 sigma720=2418 omitted_mass=978 witness_pairs=5')
