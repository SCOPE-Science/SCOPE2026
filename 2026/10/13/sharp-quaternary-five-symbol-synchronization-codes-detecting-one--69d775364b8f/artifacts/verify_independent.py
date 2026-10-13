#!/usr/bin/env python3
"""Independent integer-encoded certificate reader and direct adjacency audit."""
from pathlib import Path
import json
from itertools import combinations

BASE=Path(__file__).resolve().parent
C=json.loads((BASE/'upper_certificate.json').read_text())

def symbol(z,j):
    return (z>>(2*(4-j)))&3

def unbordered(z):
    for k in range(1,5):
        if z>>(2*(5-k)) == (z&((1<<(2*k))-1)):
            return False
    return True

def clashing(z,y):
    mismatch=sum(symbol(z,j)!=symbol(y,j) for j in range(5))
    if mismatch<=1:return True
    for k in range(1,5):
        mask=(1<<(2*k))-1
        if (z>>(2*(5-k)))==(y&mask):return True
        if (y>>(2*(5-k)))==(z&mask):return True
    return False

for a in (1,2):
    candidates=[z for z in range(1024) if symbol(z,0)<a and symbol(z,4)>=a and unbordered(z)]
    strings=[''.join(str(symbol(z,j)) for j in range(5)) for z in candidates]
    record=C['cases'][str(a)]
    assert strings==record['words']
    groups=record['cliques']
    hit=[False]*len(candidates)
    for group in groups:
        for i in group:hit[i]=True
        for i,j in combinations(group,2):
            assert clashing(candidates[i],candidates[j]),(a,i,j)
    assert len(groups)==32 and all(hit)
    print(f'INDEPENDENT_UPPER_OK a={a} vertices={len(candidates)} groups=32')

code=[]
for seed in range(32):
    a,b,t,u,v=tuple((seed>>j)&1 for j in (4,3,2,1,0))
    w=a^b^u^v
    s=(a,b,2*t+u,2*(1-t)+v,2+w)
    z=sum(s[j]<<(2*(4-j)) for j in range(5))
    code.append(z)
assert len(set(code))==32
assert all(unbordered(z) for z in code)
assert all(not clashing(x,y) for x,y in combinations(code,2))
print('INDEPENDENT_LOWER_OK code_size=32 pairs=496')
print('INDEPENDENT_VERIFY_OK upper=32 lower=32')
