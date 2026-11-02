#!/usr/bin/env python3
"""Exact checks for the four-season two-patch temporal rearrangement theorem.

Requires Python 3 and SymPy. This checker is supplementary: the theorem's
proof in RESULT.md establishes identities and inequalities for all parameters.
"""
from fractions import Fraction as F
from itertools import permutations
from random import Random
import sympy as S

v = S.symbols('a1 b1 a2 b2 a3 b3 a4 b4 m')
a1,b1,a2,b2,a3,b3,a4,b4,m=v
pairs=[(a1,b1),(a2,b2),(a3,b3),(a4,b4)]
D=[S.diag(a,b) for a,b in pairs]
M=S.Matrix([[1-m,m],[m,1-m]])

def tr(order):
    P=S.eye(2)
    for i in order: P=P*M*D[i]
    return S.trace(P)

Dij=lambda i,j: pairs[i][0]*pairs[j][1]-pairs[j][0]*pairs[i][1]
c=m*m*(1-2*m)
assert S.expand(tr((0,1,2,3))-tr((0,2,1,3))-c*Dij(0,3)*Dij(1,2))==0
assert S.expand(tr((0,1,2,3))-tr((0,1,3,2))+c*Dij(0,1)*Dij(2,3))==0
assert S.expand(tr((0,2,1,3))-tr((0,1,3,2))+c*Dij(0,2)*Dij(1,3))==0
print('Three four-season trace-difference polynomial identities: PASS')

for n in range(1,4):
    traces={S.expand(tr(o)) for o in permutations(range(n))}
    assert len(traces)==1
print('Trace invariance for all permutations of one, two, three seasons: PASS')

# Rational-matrix spectral ordering is equivalent to trace ordering, as
# the determinant of the four-season monodromy is permutation-invariant.
rng=Random(173951)
for k in range(400):
    xs=sorted(rng.sample(range(1,150),4))
    bs=[F(rng.randint(1,11),rng.randint(1,8)) for _ in range(4)]
    r=[F(x,11) for x in xs]
    ab=[(b*t,b) for t,b in zip(r,bs)]
    mm=F(rng.randint(1,49),100) if k%2==0 else F(rng.randint(51,99),100)
    sm=1-mm
    MM=((sm,mm),(mm,sm))
    def mult(X,Y):
        return tuple(tuple(sum(X[i][z]*Y[z][j] for z in range(2)) for j in range(2)) for i in range(2))
    def score(order):
        X=((F(1),F(0)),(F(0),F(1)))
        for i in order:
            a,b=ab[i]
            X=mult(X,((sm*a,mm*b),(mm*a,sm*b)))
        return X[0][0]+X[1][1]
    A=score((0,1,3,2)); B=score((0,1,2,3)); C=score((0,2,1,3))
    assert (A>B>C) if mm<F(1,2) else (A<B<C)
    assert len({score(o) for o in permutations(range(4))})==3
print('400 full 24-permutation exact-rational strict-order tests: PASS')

K=F(9,10); mm=F(3,4); ratios=[F(1,4),F(1,2),F(2),F(4)]
Ds=[(K*r,K) for r in ratios]
sm=1-mm
MM=((sm,mm),(mm,sm))
def mul(X,Y):
    return tuple(tuple(sum(X[i][z]*Y[z][j] for z in range(2)) for j in range(2)) for i in range(2))
def matrix(order):
    X=((F(1),F(0)),(F(0),F(1)))
    for i in order:
        a,b=Ds[i]
        X=mul(X,((sm*a,mm*b),(mm*a,sm*b)))
    return X
expected=[('cluster',(0,1,3,2),F(641568143,12800000000)),
          ('middle',(0,1,2,3),F(-539411857,12800000000)),
          ('alternating',(0,2,1,3),F(-13825436857,12800000000))]
for name,order,expected_ch in expected:
    X=matrix(order)
    trace=X[0][0]+X[1][1]
    det=X[0][0]*X[1][1]-X[0][1]*X[1][0]
    assert det==F(43046721,1600000000)
    assert 1-trace+det==expected_ch
    print(f'Exact persistence example, {name}: characteristic polynomial at 1 = {expected_ch}; PASS')

# Degenerate rank-one mixing, independent of order.
for o in permutations(range(4)):
    expr=tr(o).subs({m:S.Rational(1,2)})
    assert S.expand(expr-S.prod((a+b)/2 for a,b in pairs))==0
print('Half-mixing equal-order degeneracy: PASS')
