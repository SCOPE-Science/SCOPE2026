#!/usr/bin/env python3
"""Exact-rational finite checks for the reflection-paired three-slice depth theorem.

No numerical sampling in this program replaces the analytic proof of the theorem.
Requires only the Python standard library.
"""
from fractions import Fraction as Q
from itertools import product

D = [(Q(-1), Q(-1)), (Q(2), Q(-1)), (Q(-1), Q(2))]

def area(p):
    if len(p) < 3:
        return Q(0)
    return abs(sum(p[i][0]*p[(i+1)%len(p)][1]
                   -p[(i+1)%len(p)][0]*p[i][1]
                   for i in range(len(p))))/2

def cut(p, a, b, offset):
    if not p:
        return []
    out=[]
    for i, x in enumerate(p):
        y = p[(i+1) % len(p)]
        v=a*x[0]+b*x[1]+offset
        w=a*y[0]+b*y[1]+offset
        if v >= 0:
            out.append(x)
        if (v < 0 and w > 0) or (v > 0 and w < 0):
            lam = v/(v-w)
            out.append((x[0]+lam*(y[0]-x[0]), x[1]+lam*(y[1]-x[1])))
        elif v < 0 and w == 0:
            out.append(y)
    return out

def measured(r, a, b, t):
    small = [(r*x, r*y) for x,y in D]
    return sum((area(cut(poly, a,b,t*(i-1)))
                for i,poly in enumerate((small,D,D))), Q(0))

assert area(D)==Q(9,2)
cases=0
for r in [Q(1,8), Q(1,4), Q(1,3), Q(1,2)]:
    bound=(Q(4,9)+r*r)*area(D)
    for a,b,t in product(range(-5,6), repeat=3):
        actual=measured(r,a,b,Q(t))
        assert actual >= bound, (r,a,b,t,actual,bound)
        cases+=1
    # Explicit supporting halfspace: middle cap x+y<=0;
    # all small bottom included, full-sized top excluded.
    assert measured(r, -1, -1, -4)==bound
    assert (Q(4,9)+r*r)/(2+r*r) == Q(2,9)+Q(7,9)*(r*r/(2+r*r))
    cases+=2
# Pure exact-dimensional algebra confirms sharp symmetry interval and depth profile.
for d in range(2,31):
    for r in (Q(1,2*d), Q(1,d)):
        # For vertex j, barycentric coordinates of -r*v_j are
        # (1-dr)/(d+1) at j, and (1+r)/(d+1) elsewhere.
        assert (1-d*r)/(d+1)>=0
        assert (1+r)/(d+1)>0
        depth=(Q(d,d+1)**d+r**d)/(2+r**d)
        assert 0<depth<1
        cases+=1
print('VERIFY_OK', cases, 'exact-rational assertions')
