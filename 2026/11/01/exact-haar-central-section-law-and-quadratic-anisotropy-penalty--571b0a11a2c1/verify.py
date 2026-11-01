#!/usr/bin/env python3
"""Independent elementary checks for the anisotropic rhombic-dodecahedron central-section law.
Uses only Python standard library; does not substitute for the analytic argument.
"""
import itertools
import math
import random

V = set(itertools.product((-1, 1), repeat=3))
for i in range(3):
    for sign in (-2, 2):
        v = [0, 0, 0]; v[i] = sign
        V.add(tuple(v))
V = sorted(V)
EDGES = []
for a,b in itertools.combinations(V, 2):
    for i in range(3):
        if abs(a[i])==2 and max(abs(z) for z in b)==1 and a[i]*b[i]>0:
            EDGES.append((a,b))
        if abs(b[i])==2 and max(abs(z) for z in a)==1 and b[i]*a[i]>0:
            EDGES.append((a,b))
assert len(V)==14 and len(EDGES)==24
assert len(set(EDGES))==24

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def exact_edges(normal):
    signs=[dot(normal,v) for v in V]
    assert all(abs(x)>1e-10 for x in signs)
    return sum(dot(normal,a)*dot(normal,b)<0 for a,b in EDGES)

def section_type(normal):
    q=sorted((abs(x) for x in normal),reverse=True)
    return 8 if q[0]>q[1]+q[2] else 6

def p8(scales):
    total=0.0
    for i in range(3):
        j,k=[z for z in range(3) if z!=i]
        z=math.asinh(scales[j]/scales[i])+math.asinh(scales[k]/scales[i])
        total+=math.atan(math.exp(-z))
    return 4*total/math.pi

p0=(12/math.pi)*math.atan(3-2*math.sqrt(2))
assert abs(p8((1,1,1))-p0)<1e-14
assert abs(p0-(6/math.pi)*math.acos(-1/3)+3)<1e-14
check=0
rng=random.Random(17293)
for vals in ((1,1,1),(2,1,1),(1,2,3),(.2,1,5),(3,1.3,.75)):
    n8=0
    trial=30000
    for _ in range(trial):
        normal=tuple(x*y for x,y in zip(vals,(rng.gauss(0,1) for i in range(3))))
        if min(abs(dot(normal,v)) for v in V)<1e-8:continue
        direct=exact_edges(normal)
        formula=section_type(normal)
        assert direct==formula,(vals,normal,direct,formula)
        check+=1
        n8+=(formula==8)
    freq=n8/trial
    pred=p8(vals)
    assert abs(freq-pred)<.018,(vals, freq,pred)
    print('scale',vals,'P8',pred,'MC',freq)

for h in ((1,-1,0),(.3,.2,-.5),(2,-1,-1)):
    q=sum(x*x for x in h)
    for eps in (.025,.0125):
        plus=p8([math.exp(eps*x) for x in h]);minus=p8([math.exp(-eps*x) for x in h]);p=p0
        est=(plus+minus-2*p)/(2*eps*eps)
        expected=q/(math.sqrt(2)*math.pi)
        assert abs(est-expected)<.005,(h,eps,est,expected)
        check+=1
print('VERIFY_OK',check,'checks; all directional sign classifications and local spectral coefficients agree')
