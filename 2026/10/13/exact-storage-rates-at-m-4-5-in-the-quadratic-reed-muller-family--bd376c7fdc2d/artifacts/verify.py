#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))

def nu(m,x):
    v=0; k=0
    for i in range(m):
        for j in range(i,m):
            if ((x>>i)&1) and ((x>>j)&1):
                v |= 1<<k
            k += 1
    return v

def rank_and_digest(m):
    D=m*(m+1)//2; N=1<<D
    support=[nu(m,x) for x in range(1<<m)]
    assert len(set(support))==(1<<m)
    piv={}
    for t in range(N):
        row=0
        for s in support:
            row |= 1<<(s^t)
        while row:
            p=row.bit_length()-1
            q=piv.get(p)
            if q is None:
                piv[p]=row
                break
            row ^= q
    width=(N+7)//8
    h=hashlib.sha256()
    for p in sorted(piv):
        h.update(p.to_bytes(4,'little'))
        h.update(piv[p].to_bytes(width,'little'))
    return len(piv),h.hexdigest()

for m in range(1,6):
    r,d=rank_and_digest(m)
    assert r==CERT['ranks'][str(m)]
    assert d==CERT['pivot_sha256'][str(m)]
    N=1<<(m*(m+1)//2)
    assert r<=N//2

assert (1024-448,32768-13658)==(576,19110)
assert CERT['rates']['4']=='9/16'
assert CERT['rates']['5']=='9555/16384'
assert 1024-1-448==CERT['bicycle_dimensions']['4']
assert 32768-1-13658==CERT['bicycle_dimensions']['5']
print('VERIFY_OK')
