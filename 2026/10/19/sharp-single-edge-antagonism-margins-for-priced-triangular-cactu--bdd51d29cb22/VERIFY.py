#!/usr/bin/env python3
"""Exact finite spot checks for a priced triangular-cactus resistance design.

Run with Python 3 standard library. Universal inequalities follow from the
algebraic proof, not from this finite program.
"""
from fractions import Fraction as F
from random import Random


def resistance3(x, y, z):
    d = x*y+z*(x+y)
    assert d > 0
    return ((y+z)/d, (x+z)/d, (x+y)/d)


def grounded_resistances(vertex_count, edges):
    # All edge conductances are exact Fractions; the final vertex is grounded.
    n=vertex_count-1
    A=[[F(0) for _ in range(n+1)] for _ in range(n)]
    for u,v,w in edges:
        for i,j,coef in ((u,u,1),(v,v,1),(u,v,-1),(v,u,-1)):
            if i<n and j<n: A[i][j] += coef*w
    def solve(terminal_u,terminal_v):
        T=[row[:] for row in A]
        for i in range(n): T[i][-1]=F((i==terminal_u)-(i==terminal_v))
        for i in range(n):
            pivot=next(j for j in range(i,n) if T[j][i]!=0)
            T[i],T[pivot]=T[pivot],T[i]
            z=T[i][i]
            for j in range(i,n+1):T[i][j]/=z
            for k in range(n):
                if k==i:continue
                coef=T[k][i]
                for j in range(i,n+1):T[k][j]-=coef*T[i][j]
        p=[T[i][-1] for i in range(n)]+[F(0)]
        return p[terminal_u]-p[terminal_v]
    return [solve(u,v) for u,v,_ in edges]


if __name__=='__main__':
    count=0
    # Direct rational three-edge calculations, including asymmetric contenders.
    rng=Random(20261015)
    for z in [F(0),F(1,20),F(1),F(3),F(15)]:
        for _ in range(100):
            x=F(rng.randint(1,25),rng.randint(1,19))
            y=F(rng.randint(1,25),rng.randint(1,19))
            lhs=max(resistance3(x,y,z))
            a=(x+y)/2
            rhs=max(resistance3(a,a,z))
            assert lhs>=rhs
            if x!=y: assert lhs>rhs
            count+=1
    # Local explicit critical thresholds and the degenerate t=4 family.
    for t, a, b, k in [
        (F(2,13),F(13,30),F(13,15),F(18,13)),
        (F(2,5),F(5,12),F(5,12),F(8,5)),
        (F(2),F(1,4),F(1,4),F(8,3)),
        (F(4),F(1,2),F(0),F(4)),
        (F(5),F(1,2),F(0),F(4)),
    ]:
        assert 2*a+t*b==1
        assert max(resistance3(a,a,b))==k
        count+=2
    for r in [F(0),F(1,10),F(1,2),F(3,4),F(1)]:
        a=F(1)/(2+4*r); b=r*a
        assert max(resistance3(a,a,b))==4
        count+=1
    # A connected 8-vertex cactus with three priced triangles and one bridge.
    # Choosing B=sum block coefficients makes the optimal edge-risk resistance 1.
    edges=[(0,1,F(3,5)),(0,2,F(3,5)),(1,2,F(6,5)),
           (2,3,F(2,3)),(2,4,F(2,3)),(3,4,F(2,3)),
           (4,5,F(2)),(4,6,F(2)),(5,6,F(0)),(6,7,F(1))]
    prices=[F(1),F(1),F(2,13),F(1),F(1),F(2),F(1),F(1),F(5),F(3,2)]
    budget=F(18,13)+F(8,3)+F(4)+F(3,2)
    assert sum(w*p for (_,_,w),p in zip(edges,prices))==budget
    expected=[F(1),F(1),F(2,3),F(1),F(1),F(1),F(1,2),F(1,2),F(1),F(1)]
    assert grounded_resistances(8,edges)==expected
    count+=11
    # For rational positive candidates with the same budget, the exact
    # worst-edge resistance cannot beat the derived optimum 1.
    for _ in range(36):
        vv=[F(rng.randint(1,60),rng.randint(1,30)) for _ in edges]
        scale=budget/sum(p*w for p,w in zip(prices,vv))
        trial=[(u,v,w*scale) for (u,v,_),w in zip(edges,vv)]
        assert max(grounded_resistances(8,trial))>=1
        count+=1
    print('PASS: %d exact rational assertions' % count)
