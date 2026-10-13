#!/usr/bin/env python3
"""Exact finite-field witness and integer incidence consistency checks.

Only the finite-field witness and arithmetic are computational checks;
the universal incidence obstructions are proved in RESULT.md.
"""
from collections import Counter
from math import comb
P=11
Z=3
assert pow(Z,5,P)==1 and all(pow(Z,k,P)!=1 for k in range(1,5))

def normalize(v):
    v=tuple(x%P for x in v)
    i=next((i for i,x in enumerate(v) if x),None)
    assert i is not None
    inv=pow(v[i],-1,P)
    return tuple(x*inv%P for x in v)

def cross(a,b):
    return normalize((a[1]*b[2]-a[2]*b[1],
                      a[2]*b[0]-a[0]*b[2],
                      a[0]*b[1]-a[1]*b[0]))

# 5 lines x - zeta^i*y, 5 lines y - zeta^j*z, 3 lines z - zeta^k*x.
lines=[normalize((1,-pow(Z,i,P),0)) for i in range(5)]
lines += [normalize((0,1,-pow(Z,j,P))) for j in range(5)]
lines += [normalize((-pow(Z,k,P),0,1)) for k in range(3)]
assert len(lines)==len(set(lines))==13
points={}
for i in range(13):
    for j in range(i):
        q=cross(lines[i],lines[j])
        points.setdefault(q,set()).update((i,j))
for q,users in points.items():
    assert all(sum(a*b for a,b in zip(q,lines[i]))%P==0 for i in users)
    assert all(sum(a*b for a,b in zip(q,lines[i]))%P!=0 for i in range(13) if i not in users)
counts=Counter(len(v) for v in points.values())
assert counts=={2:10,3:16,5:2},counts
assert sum(comb(m,2)*number for m,number in counts.items())==comb(13,2)
r=[sum(i in users for users in points.values()) for i in range(13)]
assert max(r)==min(r)==6,r
assert sum((m-1)**2*number for m,number in counts.items())==106

# Arithmetic and local constraints that enter the two obstructions.
assert 2*15+3*11+5*3==13*6  # every line in the 3-quintuple type has r=6
assert sum(comb(m,2)*n for m,n in [(2,15),(3,11),(5,3)])==comb(13,2)
assert 2*7+3*17+5*2<=13*6
assert sum(comb(m,2)*n for m,n in [(2,7),(3,17),(5,2)])==comb(13,2)
# With exactly two quintuple points and no quadruple points, all external lines
# have (r, n_2, n_3)=(6,0,6), and the source candidate n_3=17 is forbidden
# by the pencil-crossing case distinction (15, 16, or 18).
assert 17 not in {15,16,18}
print('VERIFY_OK')
print('GF11 fifth root:', Z)
print('witness count:', dict(sorted(counts.items())))
print('singular points per line:', r)
