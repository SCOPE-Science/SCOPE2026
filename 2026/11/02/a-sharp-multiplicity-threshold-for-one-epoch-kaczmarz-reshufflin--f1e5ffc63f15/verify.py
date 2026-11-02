#!/usr/bin/env python3
"""Exact-rational checks for one-epoch Kaczmarz row-order risk."""
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial, exp

checks = 0

def ck(b, name):
    global checks
    assert b, name
    checks += 1

def probabilities(m):
    """Coefficient of k**j in E[k**number_of_type_switches]."""
    a, b = F(m-1, m), F(1, m)
    states = {(1, 0): F(1)}  # initially exceptional type B
    for _ in range(m-1):
        nxt = {}
        for (old, switches), weight in states.items():
            for new, p in ((0, a), (1, b)):
                key = (new, switches + (new != old))
                nxt[key] = nxt.get(key, F(0)) + weight * p
        states = nxt
    coeff = [F(0)] * m
    for (last, j), weight in states.items():
        coeff[j] += weight
    return coeff

def poly(coeff, z):
    return sum((c*z**j for j,c in enumerate(coeff)), F(0))

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))

def project(a,x):
    # normal a has unit Euclidean norm
    t = dot(a,x)
    return (x[0]-a[0]*t, x[1]-a[1]*t)

def squared(x):
    return dot(x,x)

def direct_risk(rows, e, orders):
    total = F(0)
    ct = 0
    for indices in orders:
        x = e
        for i in indices:
            x = project(rows[i],x)
        total += squared(x)
        ct += 1
    return total / ct

for m in range(2, 15):
    c = probabilities(m)
    a,b = F(m-1,m),F(1,m)
    ck(sum(c)==1, ('total',m))
    ck(c[0] == b**(m-1), ('zero switches',m))
    one = sum(b**(j-1)*a**(m-j) for j in range(1,m))
    ck(c[1] == one, ('one switch',m))
    ck(sum(j*c[j] for j in range(m)) == a+2*(m-2)*a*b, ('mean',m))
    for z in [F(0), F(1,25), F(1,4), F(1,2), F(16,25), F(1)]:
        ck(F(0)<=poly(c,z)<=1, ('generating polynomial bounds',m,z))
        ck(sum((w*z**j for j,w in enumerate(c)),F(0))==poly(c,z), ('polynomial',m,z))

ck(probabilities(3) == [F(1,9),F(6,9),F(2,9)],'m3 polynomial')
ck(probabilities(4) == [F(1,64),F(39,64),F(15,64),F(9,64)],'m4 polynomial')
ck(F(1,2)*F(1,2)==F(1,4),'rational arithmetic')
for z in [F(0),F(1,4),F(49,100),F(1,2),F(16,25),F(99,100),F(1)]:
    h=poly(probabilities(3),z)-z
    ck(h == (z-1)*(2*z-1)/9, ('exact cubic factorization',z))

for m in range(2,7):
    a = (F(1),F(0))
    v = (F(4,5),F(3,5))
    rows = [a]*(m-1)+[v]
    e = a
    k = F(16,25)
    theory_rr = (1-k)*k/m
    theory_iid = (1-k)*poly(probabilities(m), k)/m
    rr = direct_risk(rows,e,permutations(range(m)))
    iid = direct_risk(rows,e,product(range(m),repeat=m))
    ck(rr == theory_rr,('permutation projection',m,rr,theory_rr))
    ck(iid == theory_iid,('iid projection',m,iid,theory_iid))
    if m>=3:
        ck(rr>iid,('strict reversal',m))
    else:
        ck(rr<iid,('m2 comparison',m))

# Fully distinct rows, rationally normalized, one epoch of three exact updates.
a=(F(1),F(0))
a2=(F(312,313),F(25,313))
b=(F(4,5),F(3,5))
rows=[a,a2,b]
for i in range(3):
    ck(dot(rows[i],rows[i])==1,('normalization',i))
for i in range(3):
    for j in range(i+1,3):
        ck(abs(dot(rows[i],rows[j]))<1,('distinct lines',i,j))
rr=direct_risk(rows,a,permutations(range(3)))
iid=direct_risk(rows,a,product(range(3),repeat=3))
ck(rr-iid==F(234845527130732528,396688687243963171875),'distinct-row witness exact gap')
ck(rr>iid,'distinct-row positive gap')

# Asymptotic sanity diagnostics: these are NOT proof of a limiting statement.
for m in [6,8,10,14]:
    c=probabilities(m)
    z=F(1,2)
    ck(poly(c,z)<z, ('asymptotic side at 1/2',m))

print('PASS:',checks,'exact-rational assertions')
print('Distinct-row gap:',rr-iid,'=',float(rr-iid))
