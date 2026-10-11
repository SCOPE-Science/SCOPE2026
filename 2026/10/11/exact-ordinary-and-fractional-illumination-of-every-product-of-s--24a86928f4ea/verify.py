#!/usr/bin/env python3
from itertools import product


def cone_memberships(d,u):
    out=[]
    if all(x>0 for x in u):
        out.append(0)
    s=sum(u)
    for i in range(d):
        if all(u[j]>0 for j in range(d) if j!=i) and s<0:
            out.append(i+1)
    return out

# Deterministic exact-integer sanity check: no direction lies in two simplex
# vertex tangent-cone interiors.
for d in range(1,9):
    for u in product(range(-2,3), repeat=d):
        if all(x==0 for x in u):
            continue
        assert len(cone_memberships(d,u))<=1,(d,u,cone_memberships(d,u))

# Integer partitions of n, used only to regression-check the sharp vertex-count gap.
def partitions(n,lo=1):
    if n==0:
        yield []
        return
    for a in range(lo,n+1):
        for tail in partitions(n-a,a):
            yield [a]+tail

for n in range(1,13):
    vals=[]
    for p in partitions(n):
        v=1
        for d in p:
            v*=d+1
        vals.append((v,p))
        assert v<=2**n
    assert max(vals)[0]==2**n
    if n>=2:
        noncube=[(v,p) for v,p in vals if any(d>1 for d in p)]
        mv=max(v for v,p in noncube)
        assert mv==3*2**(n-2),(n,mv)
        eq=[p for v,p in noncube if v==mv]
        assert eq==[[1]*(n-2)+[2]] or eq==[[2]]

print('VERIFY_OK')
print('simplex_cone_disjointness_samples = passed')
print('partition_gap_n_le_12 = passed')
