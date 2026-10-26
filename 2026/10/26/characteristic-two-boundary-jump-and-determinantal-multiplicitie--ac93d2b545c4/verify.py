#!/usr/bin/env python3
"""Dependency-free exact checks for the second principal-parts ranks of the projected Togliatti surface.

No floating-point arithmetic is used.  All identities hold over the integers,
with the separate mod-2 assertions performed by coefficient reduction.
"""
from itertools import combinations
from math import comb

POLY = ((2, 0), (2, 1), (1, 2), (0, 2), (0, 1), (1, 0))
CHART = ((0, 0), (1, 0), (0, 1), (2, 1), (1, 2), (2, 2))
JET = ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))


def det2(M):
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]


def rank_mod(M, p):
    A = [[int(x) % p for x in row] for row in M]
    rr = 0
    for j in range(len(A[0])):
        t = next((i for i in range(rr, len(A)) if A[i][j]), None)
        if t is None:
            continue
        A[rr], A[t] = A[t], A[rr]
        inv = pow(A[rr][j], -1, p)
        A[rr] = [(v*inv) % p for v in A[rr]]
        for i in range(len(A)):
            if i != rr:
                v = A[i][j]
                A[i] = [(u-v*w) % p for u, w in zip(A[i], A[rr])]
        rr += 1
    return rr


def chart_exponents():
    # All six corner charts have unimodular adjacent ray differences,
    # and the same six displayed sections after possibly swapping a,b.
    for i, vertex in enumerate(POLY):
        d1 = tuple(POLY[(i-1) % 6][q] - vertex[q] for q in range(2))
        d2 = tuple(POLY[(i+1) % 6][q] - vertex[q] for q in range(2))
        dd = d1[0]*d2[1] - d1[1]*d2[0]
        assert abs(dd) == 1
        exps = []
        for v in POLY:
            t = (v[0]-vertex[0], v[1]-vertex[1])
            i0 = (t[0]*d2[1]-t[1]*d2[0]) // dd
            i1 = (d1[0]*t[1]-d1[1]*t[0]) // dd
            assert i0 >= 0 and i1 >= 0
            assert (i0*d1[0]+i1*d2[0], i0*d1[1]+i1*d2[1]) == t
            exps.append((i0, i1))
        assert set(exps) == set(CHART), (vertex, exps)


def minor_poly_B():
    # B = [[b, 0, b^2], [2a,2b,4ab], [0,a,a^2]].
    # Represent each polynomial as a dictionary (a-degree,b-degree)->coefficient.
    B = [
        [{(0,1):1}, {}, {(0,2):1}],
        [{(1,0):2}, {(0,1):2}, {(1,1):4}],
        [{}, {(1,0):1}, {(2,0):1}],
    ]
    def mul(x,y):
        z={}
        for (a,b),c in x.items():
            for (d,e),f in y.items():
                z[(a+d,b+e)]=z.get((a+d,b+e),0)+c*f
        return {k:v for k,v in z.items() if v}
    def sub(x,y):
        z=dict(x)
        for k,v in y.items():z[k]=z.get(k,0)-v
        return {k:v for k,v in z.items() if v}
    mins=[]
    for I in combinations(range(3),2):
        for J in combinations(range(3),2):
            v=sub(mul(B[I[0]][J[0]],B[I[1]][J[1]]),
                  mul(B[I[0]][J[1]],B[I[1]][J[0]]))
            assert len(v)==1, (I,J,v)
            mins.append((I,J,v))
    # In odd characteristic the defining ideal is (a^2,ab,b^2).
    # In characteristic 2 it is the reduced toric boundary ideal (ab).
    assert any(v=={(2,0):2} for _,_,v in mins)
    assert any(v=={(1,1):1} for _,_,v in mins)
    assert any(v=={(0,2):2} for _,_,v in mins)
    assert all(min(sum(e) for e in v) >= 2 for _,_,v in mins)
    mod2=[{k:c%2 for k,c in v.items() if c%2} for _,_,v in mins]
    assert {(1,1):1} in mod2
    assert all((not v) or all(a>=1 and b>=1 for a,b in v) for v in mod2)
    # Every entry of B generates the ideal (a,b), independent of characteristic.
    assert {(1,0):1} in [c for row in B for c in row]
    assert {(0,1):1} in [c for row in B for c in row]
    assert all((not v) or all(a+b>=1 for a,b in v) for row in B for v in row)


def torus_ranks():
    # Hasse-Taylor matrix for six cubic characters on x,y,z (z=1) at (1,1).
    monoms=((2,1),(2,0),(1,2),(0,2),(1,0),(0,1))
    J=[[comb(a,i)*comb(b,j) if a>=i and b>=j else 0 for a,b in monoms] for i,j in JET]
    for p in (2,3,5,7,11):
        assert rank_mod(J,p)==5


def boundary_ranks():
    # At a=0,b=1, the first three jets give rank3; the B-block adds rank1 in
    # characteristic 2 and rank2 in odd characteristic. At a=b=0 B=0.
    def B(a,b,p):
        return [[b,0,b*b],[2*a,2*b,4*a*b],[0,a,a*a]]
    for p in (2,3,5,7,11):
        assert rank_mod(B(0,0,p),p)==0
        assert rank_mod(B(0,1,p),p)==(1 if p==2 else 2)
        assert rank_mod(B(1,0,p),p)==(1 if p==2 else 2)
        assert rank_mod(B(1,1,p),p)==2


if __name__ == '__main__':
    chart_exponents()
    minor_poly_B()
    torus_ranks()
    boundary_ranks()
    print('VERIFY_OK: six affine corner charts, integral determinantal identities, all rank strata')
