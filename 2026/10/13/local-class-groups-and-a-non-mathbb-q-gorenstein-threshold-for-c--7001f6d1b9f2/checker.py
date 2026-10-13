#!/usr/bin/env python3
"""Exact integer/rational cross-checks for local cones of crown-graph edge toric varieties.

Run: python3 checker.py. Uses only the Python 3 standard library.
Finite tests supplement, rather than replace, the general semigroup proof.
"""
from fractions import Fraction
from itertools import product
import json


def rank(rows):
    if not rows:
        return 0
    a = [[Fraction(v) for v in row] for row in rows]
    rr, cc = len(a), len(a[0]); p = 0
    for j in range(cc):
        piv = next((i for i in range(p, rr) if a[i][j]), None)
        if piv is None:
            continue
        a[p], a[piv] = a[piv], a[p]
        scale = a[p][j]
        a[p] = [q/scale for q in a[p]]
        for i in range(p+1, rr):
            if a[i][j]:
                factor = a[i][j]
                a[i] = [v-factor*w for v,w in zip(a[i], a[p])]
        p += 1
        if p == rr:
            break
    return p


def dot(u,v):
    return sum(a*b for a,b in zip(u,v))


def cone_data(n):
    """Coordinates (a_1,...,a_r,b_1,...,b_r,X,Y), r=n-2."""
    r = n-2; d = 2*r+2
    basis = [tuple(int(k == i) for k in range(d)) for i in range(d)]
    aa, bb, X, Y = basis[:r], basis[r:2*r], basis[-2], basis[-1]
    plus = lambda a,b: tuple(i+j for i,j in zip(a,b))
    gen = aa+bb+[plus(X,b) for b in bb]+[plus(Y,a) for a in aa]+[plus(X,Y)]
    up = tuple(([0]*r)+([1]*r)+[-1,1])
    down = tuple(([1]*r)+([0]*r)+[1,-1])
    inequalities = basis+[up,down]
    # Recompute every chart monomial exponent difference directly from the edges.
    anchor_left, anchor_right = 0,1
    left_remaining = [k for k in range(n) if k not in (anchor_left,anchor_right)]
    right_remaining = left_remaining[:]
    index_l = left_remaining+[anchor_right]
    index_r = right_remaining+[anchor_left]
    mon = []
    for i in range(n):
        for j in range(n):
            if i==j or (i,j)==(anchor_left,anchor_right):
                continue
            coords=(tuple(int(i==p) for p in left_remaining)+tuple(int(j==q) for q in right_remaining)+(int(i==anchor_right),int(j==anchor_left)))
            mon.append(coords)
    extra={plus(aa[p],bb[q]) for p in range(r) for q in range(r) if p!=q}
    assert set(mon)==set(gen)|extra, (n,set(mon)^(set(gen)|extra))
    assert len(set(gen))==4*n-7 and len(mon)==n*(n-1)-1
    assert rank(gen)==d
    assert rank(inequalities)==d
    assert all(dot(u,v)>=0 for u in inequalities for v in gen)
    assert all(rank([g for g in gen if dot(u,g)==0])==d-1 for u in inequalities)
    # For each generator the coordinate sum is 1 or 2. No sum of >=2 nonzero
    # generators represents another generator, by checking all two-summand cases.
    assert not any(plus(g,h) in gen for g in gen for h in gen)
    ones = (1,)*d
    assert all(dot(u,ones)==1 for u in basis)
    assert dot(up,ones)==n-2 and dot(down,ones)==n-2
    if n>=4:
        assert dot(up,ones)!=1
    else:
        assert dot(up,ones)==1
    return gen, inequalities


def integer_decompose(v):
    """Construct actual nonnegative generator coefficients for integer cone point."""
    d=len(v); r=(d-2)//2
    a=list(v[:r]); b=list(v[r:2*r]); X,Y=v[-2:]
    assert all(q>=0 for q in v)
    assert X-Y<=sum(b) and Y-X<=sum(a)
    coefs={}
    if X>=Y:
        coefs['X+Y']=Y
        remain=X-Y
        for k in range(r):
            used=min(b[k],remain)
            coefs['X+b'+str(k)]=used
            b[k]-=used;remain-=used
        assert remain==0
    else:
        coefs['X+Y']=X
        remain=Y-X
        for k in range(r):
            used=min(a[k],remain)
            coefs['Y+a'+str(k)]=used
            a[k]-=used;remain-=used
        assert remain==0
    for k in range(r):
        coefs['a'+str(k)]=a[k]
        coefs['b'+str(k)]=b[k]
    return coefs


def main():
    summaries=[]
    for n in range(3,9):
        gen, normals=cone_data(n)
        summaries.append({'n':n,'dimension':2*n-2,'generators':len(gen),
                          'facets':len(normals),'class_group_rank':len(normals)-(2*n-2),
                          'q_gorenstein':n==3})
    integer_points=0
    for n in range(3,6):
        d=2*n-2;r=n-2
        for v in product(range(3),repeat=d):
            a,b=v[:r],v[r:2*r]
            X,Y=v[-2:]
            if X-Y<=sum(b) and Y-X<=sum(a):
                integer_decompose(v)
                integer_points+=1
    print(json.dumps({'tested_cones':summaries,'integer_cone_points_decomposed':integer_points,
                      'method':'exact rational ranks, facet incidences, and constructive integer decompositions',
                      'finite_scope':'n=3,...,8 for cone ranks; n=3,...,5 and coordinates 0,1,2 for integer decompositions'},indent=2))

if __name__=='__main__':main()
