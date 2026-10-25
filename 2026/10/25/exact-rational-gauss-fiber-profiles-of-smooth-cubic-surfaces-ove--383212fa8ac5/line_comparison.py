"""Comparison of rational point/line/Eckardt invariants with Gauss partitions.
All line restrictions use direct binary-form expansions.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parent
E=[(a,b,c,3-a-b-c) for a in range(4) for b in range(4-a) for c in range(4-a-b)]
LINES=sorted({tuple(sorted([p,q,p^q])) for p in range(1,16) for q in range(p+1,16)})
assert len(LINES)==35

def multiply(a,b):
    c=0
    for i in range(4):
        if a>>i&1:
            for j in range(4-i):
                if b>>j&1:c^=1<<(i+j)
    return c

def binary_restriction(mask,u,v):
    out=0
    for b,e in enumerate(E):
        if not(mask>>b&1):continue
        coeff=1
        for i in range(4):
            lin=((u>>i)&1)|(((v>>i)&1)<<1)
            for _ in range(e[i]):coeff=multiply(coeff,lin)
        out^=coeff
    return out

def invariants(mask):
    incidence=Counter();nr=0
    for a,b,c in LINES:
        if binary_restriction(mask,a,b)==0:
            nr+=1
            for p in (a,b,c):incidence[p]+=1
    return nr,sum(v==3 for v in incidence.values()),sum(v==2 for v in incidence.values())

with open(ROOT/'cubic_orbit_certificate.csv',newline='',encoding='utf8') as f:
    rows=[r for r in csv.DictReader(f) if r['geometrically_smooth']=='1']
by=defaultdict(list)
for r in rows:
    mask=int(r['mask']);n=int(r['rational_point_count'])
    lines,eckardt,double=invariants(mask)
    by[(n,lines,eckardt,double)].append((mask,r['gauss_fiber_partition']))
key=(9,3,1,0)
items=by[key]
assert (66913,'1;1;1;1;1;1;1;1;1') in items
assert (66920,'2;2;1;1;1;1;1') in items
print('Two smooth surfaces share (rational points, lines, Eckardt points, double-line points) = (9,3,1,0)')
print('but their rational Gauss fiber partitions differ:')
for mask,p in items:print(mask,p)
