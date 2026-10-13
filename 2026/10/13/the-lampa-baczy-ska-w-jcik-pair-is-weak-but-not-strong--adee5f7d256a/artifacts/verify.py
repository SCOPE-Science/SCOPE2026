#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from math import gcd

C = lambda p: p[0]*p[0] + p[1]*p[1] - 25*p[2]*p[2]

CL1 = [
    (1,0,-4), (1,0,4), (3,4,0), (1,0,3), (6,1,21), (0,1,3)
]
CL2 = [
    (1,0,4), (1,0,0), (1,0,-4), (0,1,-3), (0,1,3), (3,-4,0)
]

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def normalize(p):
    g=0
    for v in p:
        g=gcd(g,abs(v))
    q=tuple(v//g for v in p)
    for v in q:
        if v:
            return tuple(-w for w in q) if v<0 else q
    raise AssertionError('zero projective point')

def on_line(l,p):
    return sum(a*b for a,b in zip(l,p)) == 0

def analyse(lines):
    pts={}
    for i,j in combinations(range(6),2):
        p=normalize(cross(lines[i],lines[j]))
        pts[p]=tuple(k for k,l in enumerate(lines) if on_line(l,p))
    # Every line is transverse to the smooth conic: for diag(1,1,-25),
    # tangency is equivalent to 25 a^2 + 25 b^2 - c^2 = 0.
    tangent_tests=[25*a*a+25*b*b-c*c for a,b,c in lines]
    assert all(v != 0 for v in tangent_tests)
    onC=[(p,s) for p,s in pts.items() if C(p)==0]
    offC=[(p,s) for p,s in pts.items() if C(p)!=0]
    used_conic_inc=sum(len(s) for p,s in onC)
    residual_nodes=12-used_conic_inc  # Bezout: 6 lines times 2 transverse intersections.
    assert residual_nodes >= 0
    mults=[]
    for p,s in pts.items():
        mults.append(len(s)+(1 if C(p)==0 else 0))
    mults.extend([2]*residual_nodes)
    global_counts=Counter(mults)
    conic_profile=Counter({2:residual_nodes})
    for p,s in onC:
        conic_profile[len(s)+1]+=1
    line_sing=[]
    for i in range(6):
        ll=sum(i in s for s in pts.values())
        on=sum(i in s for p,s in onC)
        line_sing.append(ll+(2-on))
    conic_sing=len(onC)+residual_nodes
    r=Counter(line_sing+[conic_sing])
    return {
        'points': pts,
        'onC': onC,
        'offC': offC,
        'tangent_tests': tangent_tests,
        'residual_nodes': residual_nodes,
        'global_counts': global_counts,
        'conic_profile': conic_profile,
        'line_singular_counts': line_sing,
        'conic_singular_count': conic_sing,
        'r': r,
    }

a=analyse(CL1); b=analyse(CL2)
assert a['global_counts'] == Counter({2:6,3:3,4:2})
assert b['global_counts'] == Counter({2:6,3:3,4:2})
assert a['conic_profile'] == Counter({2:4,3:1,4:2})
assert b['conic_profile'] == Counter({2:2,3:2,4:2})
assert a['line_singular_counts'] == [4,3,3,5,4,3]
assert b['line_singular_counts'] == [3,6,3,4,4,3]
assert a['conic_singular_count'] == 7
assert b['conic_singular_count'] == 6
assert a['r'] == Counter({3:3,4:2,5:1,7:1})
assert b['r'] == Counter({3:3,4:2,6:2})
assert a['r'] != b['r']
print('CL1 conic profile', tuple(a['conic_profile'][m] for m in (2,3,4)))
print('CL2 conic profile', tuple(b['conic_profile'][m] for m in (2,3,4)))
print('CL1 line counts', a['line_singular_counts'], 'conic', a['conic_singular_count'])
print('CL2 line counts', b['line_singular_counts'], 'conic', b['conic_singular_count'])
print('CL1 r', dict(sorted(a['r'].items())))
print('CL2 r', dict(sorted(b['r'].items())))
print('VERIFY_OK')
