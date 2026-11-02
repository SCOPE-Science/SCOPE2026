#!/usr/bin/env python3
"""Independent finite checks for the planar grid-convex shattering profile.
Standard library only.  Run: python3 grid_shattering_check.py
"""
from itertools import combinations
from math import comb

def formulas(m,n):
    N=m*n
    a3=m*n*(m-1)*(n-1)*(2*m*n-m-n-4)//18
    a4=m*(m-1)**2*(m-2)*n*(n-1)**2*(n-2)//144
    return [1,N,comb(N,2) if N>=2 else 0,a3,a4]

def unique_extrema(points):
    if len(points)<2:
        return True
    for p in points:
        others=[q for q in points if q != p]
        if not any(p[c]<min(q[c] for q in others) or p[c]>max(q[c] for q in others) for c in (0,1)):
            return False
    return True

def rectangle_masks(m,n):
    return set(sum(1 << (i*n+j) for i in range(a,b+1) for j in range(c,d+1))
               for a in range(m) for b in range(a,m)
               for c in range(n) for d in range(c,n)) | {0}

def direct_trace_shattered(ids,rects):
    masks=[1<<v for v in ids]
    traces=set()
    for rec in rects:
        bits=sum((1<<k) for k,p in enumerate(masks) if rec&p)
        traces.add(bits)
        if len(traces)==1<<len(ids):return True
    return False

def test_rectangles():
    count=0
    for m,n in [(1,1),(1,2),(1,5),(2,2),(2,3),(2,5),(3,3),(3,4),(4,4),(5,5)]:
        vertices=[(i,j) for i in range(m) for j in range(n)]
        rects=rectangle_masks(m,n)
        got=[1,0,0,0,0]
        for k in range(1,min(4,m*n)+1):
            for ids in combinations(range(m*n),k):
                points=[vertices[z] for z in ids]
                direct=direct_trace_shattered(ids,rects)
                geometric=unique_extrema(points)
                assert direct==geometric,(m,n,ids,direct,geometric)
                got[k]+=int(direct)
                count+=1
        assert got==formulas(m,n),(m,n,got,formulas(m,n))
        print('RECTANGLE_TRACES_PASS',m,n,got)
    print('ALL_RECTANGLE_TRACE_CHECKS_PASS supports=',count)

def test_geodesic():
    count=0
    for m,n in [(1,2),(1,4),(2,2),(2,3),(3,3)]:
        N=m*n
        vertices=[(i,j) for i in range(m) for j in range(n)]
        shortest=lambda i,j:abs(vertices[i][0]-vertices[j][0])+abs(vertices[i][1]-vertices[j][1])
        rects=rectangle_masks(m,n)
        for mask in range(1<<N):
            chosen=[i for i in range(N) if mask>>i&1]
            # Written independently of rectangle generation and shattering routines:
            direct=True
            for i,j in combinations(chosen,2):
                for k in range(N):
                    if shortest(i,k)+shortest(k,j)==shortest(i,j) and not mask>>k&1:
                        direct=False
                        break
                if not direct:break
            assert direct==(mask in rects),(m,n,mask)
            count+=1
    print('GEODESIC_CONVEXITY_PASS tested_subsets=',count)

def test_quadruples():
    count=0
    for m,n in [(3,5),(4,6),(5,6),(6,6),(7,7),(8,8)]:
        vs=[(i,j) for i in range(m) for j in range(n)]
        actual=sum(unique_extrema([vs[v] for v in ids]) for ids in combinations(range(m*n),4))
        assert actual==formulas(m,n)[4],(m,n,actual,formulas(m,n)[4])
        count+=comb(m*n,4)
        print('QUADRUPLE_COUNT_PASS',m,n,actual)
    print('ALL_QUADRUPLE_COUNTS_PASS supports=',count)

if __name__=='__main__':
    test_geodesic()
    test_rectangles()
    test_quadruples()
    print('ALL_GRID_SHATTERING_CHECKS_PASS')
