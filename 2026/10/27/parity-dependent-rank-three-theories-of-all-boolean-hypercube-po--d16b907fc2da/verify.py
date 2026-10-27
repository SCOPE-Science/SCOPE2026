#!/usr/bin/env python3
"""Independent finite checks for the rank-three theories of Boolean Hamming-ball graphs.
Requires Python 3 standard library only. No external data.
"""
from collections import defaultdict


def orbit_profile(d, r, h):
    assert d >= 1 and r >= 1 and 0 <= h <= d
    patterns = set()
    for i in range(h+1):
        for j in range(d-h+1):
            a = i+j
            b = h-i+j
            if a == 0 or b == 0:
                continue
            patterns.add((int(a <= r), int(b <= r)))
    return (int(1 <= h <= r), h == 0, tuple(sorted(patterns)))


def symbolic_profile(d, r, h):
    if h == 0:
        return (0, True, tuple(sorted({(1,1)} | ({(0,0)} if d >= r+1 else set()))))
    edge = int(h <= r)
    patterns = set()
    both = h <= 2*r and (h >= 2 or (h == 1 and r >= 2 and d >= 2))
    if both: patterns.add((1,1))
    only = (d > r and h <= r) or (h == r+1 and d > h) or h >= r+2
    if only: patterns.update(((1,0), (0,1)))
    if d >= r + (h+1)//2 + 1:
        patterns.add((0,0))
    return (edge, False, tuple(sorted(patterns)))


def dim_signature(d,r,method=symbolic_profile):
    return frozenset(method(d,r,h) for h in range(d+1))


def direct_dim_signature(d,r):
    vertices=range(1<<d)
    def isedge(x,y):
        return x!=y and (x^y).bit_count()<=r
    rows=set()
    for y in vertices:
        patterns=set()
        for z in vertices:
            if z==0 or z==y:
                continue
            patterns.add((int(isedge(0,z)),int(isedge(y,z))))
        rows.add((int(isedge(0,y)), y==0, tuple(sorted(patterns))))
    return frozenset(rows)


def predicted_group(d,r):
    if d==1: return 'two-vertex'
    if d<=r: return 'complete'
    if d==r+1: return 'boundary-r+1'
    if d==2*r+1: return 'boundary-2r+1'
    if d>=2*r+2: return 'tail'
    if r%2:
        if d<=(3*r+1)//2: return 'early-mixed'
        return 'late-mixed'
    if d <= 3*r//2: return 'early-mixed'
    if d==3*r//2+1: return 'parity-boundary'
    return 'late-mixed'


def main():
    symbolic_cases=0
    for r in range(1,151):
        actual={};reverse={}
        for d in range(1,2*r+6):
            if r<=18:
                for h in range(d+1):
                    aa=orbit_profile(d,r,h)
                    bb=symbolic_profile(d,r,h)
                    assert aa==bb,(d,r,h,aa,bb)
                    symbolic_cases+=1
            sig=dim_signature(d,r)
            key=predicted_group(d,r)
            assert key not in actual or actual[key]==sig,(r,d,key)
            actual[key]=sig
            assert sig not in reverse or reverse[sig]==key,(r,d,key,reverse.get(sig))
            reverse[sig]=key
        expected = (4 if r==1 else 6 if r==2 else 7 if r%2 else 8)
        assert len(actual)==expected,(r,len(actual),expected)
        assert min(d for d in range(1,2*r+6) if predicted_group(d,r)=='tail')==2*r+2
    print('SYMBOLIC_PROFILE_OK radius=1..18 (full orbit); 1..150 (class partition) pairs_tested=%d'%symbolic_cases)
    print('PARAMETER_CLASSIFICATION_OK odd>=3:7 even>=4:8 r1:4 r2:6')
    concrete=0
    for d in range(1,10):
        for r in range(1,min(d,7)+1):
            x=direct_dim_signature(d,r)
            y=dim_signature(d,r)
            assert x==y,(d,r,x,y)
            concrete+=1
    print('DIRECT_GRAPH_SIGNATURE_OK dimensions=1..9 radii=1..min(d,7) instances=%d'%concrete)
    print('SHARP_STABILIZATION_OK representative_dimension=2r+2 vertices=2^(2r+2)')
    print('VERIFY_OK')

if __name__=='__main__':main()
