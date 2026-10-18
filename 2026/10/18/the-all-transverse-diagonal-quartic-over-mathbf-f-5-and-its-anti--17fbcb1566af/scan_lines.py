#!/usr/bin/env python3
"""Exact independent resultant scan of diagonal quartic line sections over F5.

Runs without third-party packages: python3 scan_lines.py
"""
from collections import Counter
from itertools import product
import json

Q=5

def normalize(v):
    for a in v:
        if a%Q:
            inverse=pow(a,-1,Q)
            return tuple(x*inverse%Q for x in v)
    raise ValueError('zero vector')

plane=sorted({normalize(v) for v in product(range(Q),repeat=3) if any(v)})
assert len(plane)==31

def kernel_basis(l):
    k=next(i for i in range(3) if l[i])
    result=[]
    for j in range(3):
        if j==k:
            continue
        v=[0,0,0]; v[j]=1; v[k]=(-l[j]*pow(l[k],-1,Q))%Q
        assert sum(l[i]*v[i] for i in range(3))%Q==0
        result.append(v)
    return result

def f_coefficients(weights,l):
    """Return coeffs of s^i*t^(4-i) for restriction to plane line l."""
    u,v=kernel_basis(l)
    binom=(1,4,6,4,1)
    return [sum(weights[k]*binom[i]*u[k]**i*v[k]**(4-i) for k in range(3))%Q for i in range(5)]

def resultant_cubics(p,q):
    """Homogeneous cubic resultant, Sylvester determinant over F5.

    p and q are in order s^i t^(3-i). The 6x6 matrix treats formal
    homogeneous degrees, correctly including any common infinity root.
    """
    p=list(reversed(p));q=list(reversed(q))
    m=[]
    for poly in (p,q):
        for shift in range(3):
            m.append([0]*shift+poly+[0]*(2-shift))
    det=1
    for col in range(6):
        pivot=next((i for i in range(col,6) if m[i][col]%Q),None)
        if pivot is None:return 0
        if pivot!=col:
            m[pivot],m[col]=m[col],m[pivot]
            det=-det
        t=m[col][col]%Q;det=det*t%Q
        inverse=pow(t,-1,Q)
        for r in range(col+1,6):
            factor=m[r][col]*inverse%Q
            for j in range(col,6):m[r][j]=(m[r][j]-factor*m[col][j])%Q
    return det%Q

def nonsingular_section(weights,l):
    c=f_coefficients(weights,l)
    ds=[(i*c[i])%Q for i in range(1,5)]
    dt=[((4-i)*c[i])%Q for i in range(4)]
    assert len(ds)==len(dt)==4
    return resultant_cubics(ds,dt)!=0

def legendre(x):
    x%=Q
    return 0 if x==0 else 1 if x in (1,4) else -1

def section_points(weights,l):
    n=0
    for p in plane:
        if sum(l[i]*p[i] for i in range(3))%Q==0:
            val=sum(weights[i]*pow(p[i],4,Q) for i in range(3))%Q
            n+=1+legendre(val)
    return n

def surface_points(weights):
    return sum(1+legendre(sum(weights[i]*pow(p[i],4,Q) for i in range(3))) for p in plane)

profile=Counter(); accepted=[]
for a,b,c in product(range(1,5),repeat=3):
    weights=(a,b,c)
    cnt=sum(nonsingular_section(weights,l) for l in plane)
    profile[cnt]+=1
    if cnt==31:accepted.append(weights)

assert profile=={15:16,23:12,27:24,31:12}
expected=sorted({tuple(k*u%Q for u in (1,1,2)) for k in range(1,5)})
expected=sorted({tuple(v[i] for i in permutation) for v in expected for permutation in __import__('itertools').permutations(range(3))})
assert sorted(accepted)==expected

report={'smooth_section_counts_by_coefficient_tuple':dict(sorted(profile.items())),'fully_smooth_coefficients':accepted,'twists':{}}
for scalar in (1,2):
    weights=(scalar,scalar,2*scalar%Q)
    hist=Counter(section_points(weights,l) for l in plane)
    assert sum(hist.values())==31
    # Every line through a fixed rational point occurs in six pencils.
    assert sum(n*k for n,k in hist.items())==6*surface_points(weights)
    report['twists'][str(scalar)]={'weights':list(weights),'smooth_section_point_histogram':dict(sorted(hist.items())),'surface_rational_points':surface_points(weights)}
assert report['twists']['1']['smooth_section_point_histogram']=={2:2,4:1,6:16,8:4,10:8}
assert report['twists']['2']['smooth_section_point_histogram']=={2:8,4:4,6:16,8:1,10:2}
assert report['twists']['1']['surface_rational_points']==36
assert report['twists']['2']['surface_rational_points']==26
print(json.dumps(report,indent=2,sort_keys=True))
