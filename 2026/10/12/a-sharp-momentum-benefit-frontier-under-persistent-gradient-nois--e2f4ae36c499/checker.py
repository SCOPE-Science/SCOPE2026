#!/usr/bin/env python3
"""Exact-rational reproducibility checks for stationary scalar heavy-ball AR(1) noise."""
from fractions import Fraction as F
from itertools import product


def solve(A, v):
    n = len(v)
    aug = [list(map(F, A[i])) + [F(v[i])] for i in range(n)]
    for col in range(n):
        pivot = next((j for j in range(col, n) if aug[j][col]), None)
        assert pivot is not None, "singular exact system"
        aug[col], aug[pivot] = aug[pivot], aug[col]
        fac = aug[col][col]
        aug[col] = [e/fac for e in aug[col]]
        for row in range(n):
            if row == col:
                continue
            fac = aug[row][col]
            if fac:
                aug[row] = [aug[row][j]-fac*aug[col][j] for j in range(n+1)]
    return [row[-1] for row in aug]

pairs = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]


def direct_variance(t, b, r):
    m = [[1-t+b, -b, -t], [F(1), F(0), F(0)], [F(0), F(0), r]]
    mats = []
    for ix, iy in pairs:
        e = [[F(0) for _ in range(3)] for _ in range(3)]
        e[ix][iy] = e[iy][ix] = F(1)
        mats.append(e)
    def mm(x):
        return [[sum(m[i][k] * x[k][l] * m[j][l] for k in range(3) for l in range(3)) for j in range(3)] for i in range(3)]
    evolved = [mm(mat) for mat in mats]
    co = [[int(pairs[k]==(ix,iy)) - evolved[k][ix][iy]
            for k in range(6)] for i, (ix, iy) in enumerate(pairs)]
    rhs = [int(ix==2 and iy==2) for ix, iy in pairs]
    return solve(co, rhs)[0]


def exact_variance(t, b, r):
    D = 1-r+r*t-b*r*(1-r)
    return (t/((1-r*r)*(1-b)*(2*(1+b)-t))) * ((1+b) + 2*r*(1-t+b-b*r*(1+b))/D)


def Q(t, b, r):
    A = r*(1+r*(1-t))
    B = r*r*(t-1)**2-r*t-1
    C = r*t*t-r*t-r+t-1
    return A*b*b+B*b+C


def exact_difference(t, b, r):
    D0 = 1-r+r*t
    Db = D0-b*r*(1-r)
    return -2*b*t*Q(t,b,r)/((1-b)*(1+r)*(2-t)*(2*(1+b)-t)*D0*Db)

num=0
for r,t,b in product([F(0),F(1,4),F(1,2),F(3,4),F(9,10)],
                     [F(1,5),F(1,2),F(4,5),F(1),F(6,5),F(7,5),F(3,2),F(9,5),F(19,10)],
                     [F(0),F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]):
    actual = direct_variance(t,b,r)
    asserted = exact_variance(t,b,r)
    assert actual == asserted,(t,b,r,actual,asserted)
    delta = asserted-exact_variance(t,F(0),r)
    assert delta == exact_difference(t,b,r),(t,b,r,delta,exact_difference(t,b,r))
    if b:
        assert (delta < 0) == (Q(t,b,r)>0)
        assert (delta > 0) == (Q(t,b,r)<0)
    num += 1

# Direct exact-rational witness: the same positive momentum helps for IID noise
# and worsens stationary error under positively autocorrelated AR(1) noise.
t,b=F(6,5),F(1,10)
assert exact_variance(t,b,F(0))-exact_variance(t,F(0),F(0)) == -F(1,30)
assert exact_variance(t,b,F(1,2))-exact_variance(t,F(0),F(1,2)) == F(446,7095)

# Boundary algebra at r=0: C(t,0)=t-1, Q(t,b,0)=t-1-b.
for t in [F(1,2),F(1),F(6,5),F(3,2),F(19,10)]:
    for b in [F(0),F(1,10),F(1,4),F(1,2),F(3,4)]:
        assert Q(t,b,F(0))==t-1-b

print(f'VERIFY_OK {num} exact covariance and difference cases, 2 contrasting rational witnesses')
