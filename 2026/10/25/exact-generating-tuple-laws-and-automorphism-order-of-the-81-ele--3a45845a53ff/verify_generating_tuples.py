"""Exact checks for the 81-element commutative distributive quandle D(1).

Uses only Python's standard library; performs complete finite identity checks.
"""
from itertools import product
from collections import deque

P = 3
Q = tuple(product(range(P), repeat=4))
W = tuple(product(range(P), repeat=3))
IDX = {x: i for i, x in enumerate(Q)}

def star(x, y):
    u, v = x[1:], y[1:]
    term = (u[0]*v[1] - u[1]*v[0])*(u[2]-v[2])
    return ((-x[0]-y[0]-term)%P, *((-u[j]-v[j])%P for j in range(3)))

def det(u,v,w):
    return (u[0]*(v[1]*w[2]-v[2]*w[1])
          -u[1]*(v[0]*w[2]-v[2]*w[0])
          +u[2]*(v[0]*w[1]-v[1]*w[0]))%P

def sub(v,u): return tuple((v[j]-u[j])%P for j in range(3))

# All 81^2 products, all idempotence/commutativity, and bijective right translations.
table = [[IDX[star(x,y)] for y in Q] for x in Q]
assert all(table[i][i] == i for i in range(81))
assert all(table[i][j] == table[j][i] for i in range(81) for j in range(81))
assert all(table[table[i][j]][j] == i for i in range(81) for j in range(81))
assert all(len({table[x][y] for x in range(81)}) == 81 for y in range(81))
# All 81^3 right self-distributivity instances: (x*y)*z = (x*z)*(y*z).
for z in range(81):
    for x in range(81):
        xz=table[x][z]
        for y in range(81):
            assert table[table[x][y]][z] == table[xz][table[y][z]]

# Every projected quadruple (27^4=531441): exact medial defect equals determinant.
# First coordinates of representatives have no influence on the defect.
rep = {(u): (0, *u) for u in W}
for a in W:
    aa=rep[a]
    for b in W:
        bb=rep[b]
        ab=star(aa,bb)
        for c in W:
            cc=rep[c]
            ac=star(aa,cc)
            for d in W:
                dd=rep[d]
                lhs=star(ab,star(cc,dd))
                rhs=star(ac,star(bb,dd))
                assert lhs[1:]==rhs[1:]
                assert (lhs[0]-rhs[0])%3 == det(sub(b,a),sub(c,a),sub(d,a))

# Actual multiplication closure of an affinely independent projected 4-tuple.
start={(0,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)}
S=set(start)
while True:
    expanded=S|{star(x,y) for x in S for y in S}
    if expanded==S:break
    S=expanded
assert len(S)==81

# A dependent projected quadruple remains in a proper affine plane.
dep={(0,0,0,0),(0,1,0,0),(0,0,1,0),(1,1,1,0)}
S=set(dep)
while True:
    expanded=S|{star(x,y) for x in S for y in S}
    if expanded==S:break
    S=expanded
assert len(S)<81 and all(x[3]==0 for x in S)

# Closed rank-of-difference-matrix enumeration for k=4.
independent=sum(det(u,v,w)!=0 for u in W for v in W for w in W)
assert independent == (27-1)*(27-3)*(27-9) == 11232
number=3**7*independent
assert number==24564384
from fractions import Fraction
assert Fraction(number,81**4)==Fraction(416,729)
# Formula for all k gives 0 at k <=3 and matches k=4 explicitly.
for k in range(1,9):
    m=k-1
    ranks = (3**m-1)*(3**m-3)*(3**m-9) if k>=4 else 0
    count=3**(k+3)*ranks
    if k==4: assert count==number
    assert 0<=count<=81**k
print('VERIFY_OK: all 81^3 distributivity tests; all 27^4 determinant instances; generating and non-generating closures; k=4 count and probability.')
