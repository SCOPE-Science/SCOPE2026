#!/usr/bin/env python3
"""Reproduce the detector-code polynomial on the PG(2,3) incidence graph.

No third-party packages are required. This file implements both an original
neighborhood test and an independent finite-geometry test.
"""
from itertools import product
from collections import Counter

def canonical(v,q):
    a=next(x for x in v if x)
    inv=pow(a,-1,q)
    return tuple(x*inv%q for x in v)

def plane(q):
    obj=sorted({canonical(v,q) for v in product(range(q),repeat=3) if any(v)})
    point_lines=[]
    line_points=[]
    for p in obj:
        line_mask=sum(1<<i for i,l in enumerate(obj) if sum(a*b for a,b in zip(p,l))%q==0)
        point_lines.append(line_mask)
    for l in obj:
        point_mask=sum(1<<i for i,p in enumerate(obj) if sum(a*b for a,b in zip(p,l))%q==0)
        line_points.append(point_mask)
    return obj,point_lines,line_points

def geometry_ok(line_mask,point_lines,line_points):
    deg=[(line_mask & x).bit_count() for x in point_lines]
    if any(d<2 for d in deg):
        return False
    weak=sum(1<<i for i,d in enumerate(deg) if d==2)
    return all((weak & pts).bit_count()<=1 for j,pts in enumerate(line_points) if line_mask & (1<<j))

def original_ok(code,point_lines,line_points,mode="DET"):
    n=len(point_lines)
    neighborhoods=[m<<n for m in point_lines] + line_points
    ns=[v & code for v in neighborhoods]
    if any(m.bit_count()<2 for m in ns):
        return False
    return all((max((ns[i]&~ns[j]).bit_count(),(ns[j]&~ns[i]).bit_count())>=2 if mode=="DET" else (ns[i]^ns[j]).bit_count()>=2)
               for i in range(2*n) for j in range(i+1,2*n))

def redundant_ok(line_mask,point_lines):
    deg=[(line_mask & x).bit_count() for x in point_lines]
    return min(deg)>=2 and all(((point_lines[i]^point_lines[j])&line_mask).bit_count()>=2
                                for i in range(len(deg)) for j in range(i+1,len(deg)))

def run(q):
    objs,P,L=plane(q)
    N=len(objs)
    assert N==q*q+q+1
    assert all(x.bit_count()==q+1 for x in P+L)
    assert all((P[i]&P[j]).bit_count()==1 for i in range(N) for j in range(i+1,N))
    geometric=[];hist=Counter();hist_red=Counter()
    for m in range(1<<N):
        if redundant_ok(m,P): hist_red[m.bit_count()]+=1
        if geometry_ok(m,P,L):
            hist[m.bit_count()]+=1
            geometric.append(m)
        # Split conditions: one side may be chosen differently from other side.
        assert geometry_ok(m,P,L)==original_ok(m<<N | ((1<<N)-1),P,L)
        assert redundant_ok(m,P)==original_ok(m<<N | ((1<<N)-1),P,L,mode="RED")
    print('q',q,'N',N,'DET_SIDE_DISTRIBUTION',sorted(hist.items()),'RED_SIDE_DISTRIBUTION',sorted(hist_red.items()))
    if q==3:
        expected={10:234,11:78,12:13,13:1}
        assert dict(hist_red)=={9:234,10:234,11:78,12:13,13:1}
        assert dict(hist)==expected,(hist,expected)
        noncollinear=0
        for m in geometric:
            if m.bit_count()!=10: continue
            omitted=((1<<N)-1)^m
            assert omitted.bit_count()==3
            assert all((omitted&x).bit_count()<=2 for x in L)
            noncollinear+=1
        assert noncollinear==234
        opts=[m for m in geometric if m.bit_count()==10]
        checks=0
        for a in opts:
            for b in opts:
                assert original_ok((a<<N)|b,P,L)
                checks+=1
        assert checks==54756
        # Verify the full graph criterion on a deterministic selection of
        # subsets across all sizes, not just the optimal sets.
        for j in range(20001):
            code=(j*0x9e3779b1 + (j*j*0x11eab)) & ((1<<(2*N))-1)
            fact=geometry_ok(code & ((1<<N)-1),P,L) and geometry_ok(code>>N,P,L)
            assert original_ok(code,P,L)==fact
        # Independent direct check of every size-20 candidate via the
        # subproblem-optimum Cartesian product, justified by the proof.
        counts=Counter()
        for a,c in hist.items():
            for b,d in hist.items():
                counts[a+b]+=c*d
        assert counts=={20:54756,21:36504,22:12168,23:2496,24:325,25:26,26:1}
        print('DET_FULL_POLYNOMIAL',sorted(counts.items()),'min_direct_checks',checks)
        red=Counter()
        for a,c in hist_red.items():
            for b,d in hist_red.items(): red[a+b]+=c*d
        print('RED_FULL_POLYNOMIAL',sorted(red.items()))
        assert red[18]==234**2
    return hist

if __name__=='__main__':
    run(2)
    run(3)
    print('VERIFY_OK')
