#!/usr/bin/env python3
"""Exact-rational finite examples for a two-habitat competitive colonization model.

The analytical proof is in RESULT.md. These checks separately implement the
four-dimensional vector field, its linearization and the two invariant blocks.
No packages outside the Python standard library are required.
"""
from fractions import Fraction as F
from itertools import permutations


def det(a):
    n = len(a)
    return sum((-1) ** sum(pi[i] > pi[j] for i in range(n) for j in range(i+1,n))
               * __import__('math').prod(a[i][pi[i]] for i in range(n))
               for pi in permutations(range(n)))


def setup(r, d):
    s = (r - 1)/(2*r)
    fitness = (r+d, r-d, r-d, r+d)
    pstar = tuple(f * s/r for f in fitness)
    def derivative(p):
        means = ((p[0]+p[1])/2, (p[2]+p[3])/2)
        return tuple(-p[i]/fitness[i] + (1-p[i%2]-p[i%2+2])*means[i//2]
                     for i in range(4))
    # Jacobian directly differentiated by the product rule.
    J = [[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if i == j: J[i][j] -= 1/fitness[i]
            if i//2 == j//2: J[i][j] += F(1,2)/r
            if i%2 == j%2: J[i][j] -= s
    return s, pstar, derivative, J


def rank2_block(r,d, parity):
    s = (r-1)/(2*r)
    q = F(1,2)/r
    return [[-1/(r+d)-s+q, q-parity*s],
            [q-parity*s, -1/(r-d)-s+q]]


def verify_one(r,d):
    s,pstar,deriv,J=setup(r,d)
    assert all(x>0 for x in pstar)
    assert all(x<1 for x in pstar)
    assert deriv(pstar) == (0,0,0,0)
    assert sum(pstar[::2]) == 1-F(1,1)/r
    assert sum(pstar[1::2]) == 1-F(1,1)/r
    # Encode coordinates in symmetry sectors: even (x,y,y,x); odd (x,y,-y,-x).
    for parity in (-1,1):
        B=rank2_block(r,d,parity)
        for x,y in [(F(1),F(0)),(F(0),F(1)),(F(2),F(3))]:
            v=[x,y,parity*y,parity*x] # parity=+1 means even
            w=[sum(a*b for a,b in zip(row,v)) for row in J]
            z=[B[0][0]*x+B[0][1]*y,B[1][0]*x+B[1][1]*y]
            assert w==[z[0],z[1],parity*z[1],parity*z[0]]
    # Independent polynomial identity at five values: two quadratics vs full det.
    for lam in (F(-3),F(-1),F(0),F(1,2),F(2)):
        mat=[[lam*int(i==j)-J[i][j] for j in range(4)] for i in range(4)]
        two=F(1)
        for p in (-1,1):
            block=rank2_block(r,d,p)
            two *= (lam-block[0][0])*(lam-block[1][1])-block[0][1]*block[1][0]
        assert det(mat)==two
    t=r*r-d*d
    assert t>0
    # Squared-radical derivative inequality: strict for r>1.
    assert r*r*(t*t+4*d*d)>(r*r+d*d)**2
    print('PASS',str(r),str(d),'occupancy=',str((r-1)/r))


if __name__=='__main__':
    for r in (F(6,5),F(3,2),F(2),F(7,3),F(5)):
        for relative in (F(1,10),F(1,3),F(2,3),F(9,10)):
            verify_one(r,r*relative)
    print('All 20 exact finite-parameter tests passed.')
