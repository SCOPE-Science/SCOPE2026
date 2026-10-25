"""Independent monomial-by-monomial verification of Gauss fibers on orbit representatives.
This checker does not reuse derivative masks from classify.py.
"""
import csv
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent
EXPS=[]
for a in range(4):
    for b in range(4-a):
        for c in range(4-a-b):
            EXPS.append((a,b,c,3-a-b-c))

def monomial_value(exp,pt):
    return int(all(e==0 or pt[i]==1 for i,e in enumerate(exp)))

def data(mask):
    coeff=[(mask>>i)&1 for i in range(20)]
    vals=[]
    for n in range(1,16):
        pt=[(n>>i)&1 for i in range(4)]
        f=sum(coeff[i]*monomial_value(e,pt) for i,e in enumerate(EXPS))%2
        if f:continue
        grad=[]
        for j in range(4):
            terms=0
            for i,e in enumerate(EXPS):
                if not coeff[i] or not (e[j]&1):continue
                d=list(e);d[j]-=1
                terms+=monomial_value(d,pt)
            grad.append(terms%2)
        vals.append(sum(v<<j for j,v in enumerate(grad)))
    return tuple(sorted(Counter(vals).values(),reverse=True))

with open(ROOT/'cubic_orbit_certificate.csv',newline='',encoding='utf8') as f:
    rows=list(csv.DictReader(f))
counts=Counter();smooth=0
for row in rows:
    if int(row['geometrically_smooth'])!=1:continue
    smooth+=1
    part=data(int(row['mask']))
    assert part==tuple(int(x) for x in row['gauss_fiber_partition'].split(';')),(row['mask'],part)
    counts[(sum(part),part)]+=int(row['orbit_size'])
with open(ROOT/'gauss_profile.csv',newline='',encoding='utf8') as f:
    profile={(int(r['rational_point_count']),tuple(map(int,r['gauss_fiber_partition'].split(';')))):int(r['number_of_equations']) for r in csv.DictReader(f)}
assert counts==profile
assert smooth==36 and sum(counts.values())==322560
print('Independent Gauss derivatives agree on all 36 smooth representatives.')
print('Fourteen profile cells and the weighted total of 322560 match.')
