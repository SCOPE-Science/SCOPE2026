#!/usr/bin/env python3
"""Exact rational tests for the cube-octahedron facet-network spectrum."""
from fractions import Fraction as F
from itertools import product

TRI = list(product((-1, 1), repeat=3))
AX = [(i, s) for i in range(3) for s in (-1, 1)]


def weights(t):
    if 1 < t <= 2:
        u = t * (-2*t*t + 6*t - 3) / 2
        v = 2 * (t-1)**2
        a = t * (t-1)
        d = t*t*(2-t)/2
        b = F(0)
    elif 2 < t < 3:
        u = t * (3-t)**2 / 2
        v = 4 - 2*(3-t)**2
        a = t * (3-t)
        d = F(0)
        b = 2*(t-2)
    else:
        raise ValueError("parameter must be strictly between 1 and 3")
    return u, v, a, d, b


def operator(t, f):
    u,v,a,d,b=weights(t)
    masses=[u]*8+[v]*6
    edge=[]
    for i,s in enumerate(TRI):
        for j in range(i+1,8):
            if sum(p!=q for p,q in zip(s,TRI[j])) == 1:
                edge.append((i,j,d))
        for j,(coordinate,sign) in enumerate(AX):
            if s[coordinate]==sign:
                edge.append((i,8+j,a))
    for i,(ci,si) in enumerate(AX):
        for j in range(i+1,6):
            if ci != AX[j][0]:
                edge.append((8+i,8+j,b))
    out=[F(0)]*14
    for i,j,w in edge:
        out[i] += w*(f[i]-f[j])
        out[j] += w*(f[j]-f[i])
    return [out[k]/masses[k] for k in range(14)]


def test(t):
    u,v,a,d,b=weights(t)
    lt=(4*d+3*a)/u
    ls=(4*a+6*b)/v
    lx=3*a/u+4*a/v
    constants=[F(1)]*14
    vectors=[(F(0), constants)]
    # On antipodally even triangle facets, there are four distinct pairs.
    tri_pairs=[]
    visited=set()
    for i,s in enumerate(TRI):
        if i in visited:
            continue
        j=TRI.index(tuple(-q for q in s))
        visited.update((i,j))
        tri_pairs.append((i,j))
    for k in range(1,4):
        vec=[F(0)]*14
        for i in tri_pairs[k]:vec[i]=1
        for i in tri_pairs[0]:vec[i]=-1
        vectors.append((lt,vec))
    for k in range(1,3):
        vec=[F(0)]*14
        for i,(axis,sign) in enumerate(AX):
            if axis==k:vec[8+i]=1
            if axis==0:vec[8+i]=-1
        vectors.append((ls,vec))
    vectors.append((lx,[3*a/u]*8+[-4*a/v]*6))
    assert len(vectors)==7
    for eigenvalue,vec in vectors:
        assert operator(t,vec)==[eigenvalue*x for x in vec],(t,eigenvalue)
    # The seven independent eigenvectors span the full even space.
    # Three triangle contrasts, two axial contrasts, and two type-constants.
    assert u>0 and v>0 and a>0
    return lt,ls,lx


def main():
    parameters=[F(101,100),F(6,5),F(5,4),F(3,2),F(7,4),F(19,10),
                F(2),F(21,10),F(5,2),F(14,5),F(299,100)]
    for t in parameters:
        lt,ls,lx=test(t)
        assert lx>max(lt,ls)
    print("VERIFY_OK exact even facet-network eigenvectors, 11 rational parameters")


if __name__=='__main__':
    main()
