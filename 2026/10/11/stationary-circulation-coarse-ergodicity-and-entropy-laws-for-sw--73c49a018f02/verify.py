#!/usr/bin/env python3
"""Small exact/finite tests for graph circulation and Perron entropy formulas.

These tests illustrate the analytic theorem and do not prove it for all graphs.
"""
from fractions import Fraction
from math import log, isclose, sqrt

def kirchhoff(vertices, edges, w):
    assert len(edges)==len(w)
    assert sum(w) == 1
    assert all(x >= 0 for x in w)
    return all(sum(w[i] for i,(u,v) in enumerate(edges) if u==k)
               ==sum(w[i] for i,(u,v) in enumerate(edges) if v==k)
               for k in vertices)

def entropy(vertices,edges,w):
    p={v:sum(w[i] for i,(u,_) in enumerate(edges) if u==v) for v in vertices}
    return -sum(float(w[i])*log(float(w[i]/p[u]))
                for i,(u,v) in enumerate(edges) if w[i]>0)

def rank_rational(mat):
    a=[[Fraction(z) for z in row] for row in mat]
    row=0
    for col in range(len(a[0])):
        pivot=next((j for j in range(row,len(a)) if a[j][col]!=0),None)
        if pivot is None: continue
        a[row],a[pivot]=a[pivot],a[row]
        z=a[row][col]
        a[row]=[x/z for x in a[row]]
        for j in range(len(a)):
            if j!=row and a[j][col]!=0:
                z=a[j][col]
                a[j]=[x-z*y for x,y in zip(a[j],a[row])]
        row+=1
        if row==len(a): break
    return row

# Bouquet with 3 loops: full 2-simplex and entropy interval [0, log 3].
v=(0,)
e=((0,0),(0,0),(0,0))
w=(Fraction(1,3),)*3
assert kirchhoff(v,e,w)
assert isclose(entropy(v,e,w),log(3),rel_tol=1e-13)
assert isclose(entropy(v,e,(Fraction(1),Fraction(0),Fraction(0))),0,abs_tol=1e-14)
assert rank_rational([[0,0,0],[1,1,1]])==1  # affine dimension 3-1

# Strongly connected graph with two parallel forwards and one return.
v=(0,1)
e=((0,1),(0,1),(1,0))
w=(Fraction(1,4),Fraction(1,4),Fraction(1,2))
assert kirchhoff(v,e,w)
assert isclose(entropy(v,e,w),log(sqrt(2)),rel_tol=1e-13)
assert kirchhoff(v,e,(Fraction(1,2),Fraction(0),Fraction(1,2)))
assert isclose(entropy(v,e,(Fraction(1,2),Fraction(0),Fraction(1,2))),0,abs_tol=1e-14)
assert rank_rational([[1,1,-1],[1,1,1]])==2  # affine dimension 3-2

# Two singleton strongly connected components and a transient bridge.
v=(0,1)
e=((0,0),(1,1),(0,1))
w=(Fraction(2,5),Fraction(3,5),Fraction(0))
assert kirchhoff(v,e,w)
assert rank_rational([[0,0,-1],[0,0,1],[1,1,1]])==2  # affine dimension 3-2
assert entropy(v,e,w)==0.0
print('FINITE_EXAMPLES_OK')
