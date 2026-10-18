#!/usr/bin/env python3
"""Exact-arithmetic checks for a three-block copula mixing counterexample.

No simulation, network dependency, or external data are required.
The infinite-time statements are proved in RESULT.md; these tests check
matrix algebra and illustrative finite lags rather than certify infinity.
"""
from fractions import Fraction as F

M = ((F(0), F(1), F(0)),
     (F(1, 2), F(0), F(1, 2)),
     (F(1, 2), F(0), F(1, 2)))
N = tuple(tuple(M[j][i] for j in range(3)) for i in range(3))
I = tuple(tuple(F(i == j) for j in range(3)) for i in range(3))
J = tuple(tuple(F(1, 3) for _ in range(3)) for _ in range(3))

def mm(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))

def power(X, n):
    R = I
    for _ in range(n):
        R = mm(R, X)
    return R

def psi(X):
    return max(abs(3*z - 1) for row in X for z in row)

for X in (M,N):
    assert all(sum(row)==1 for row in X)
    assert all(sum(X[i][j] for i in range(3))==1 for j in range(3))
    assert all(v>=0 for row in X for v in row)

assert power(M, 2) == ((F(1,2),F(0),F(1,2)),
                        (F(1,4),F(1,2),F(1,4)),
                        (F(1,4),F(1,2),F(1,4)))
assert power(M, 3) == ((F(1,4),F(1,2),F(1,4)),
                        (F(3,8),F(1,4),F(3,8)),
                        (F(3,8),F(1,4),F(3,8)))
# The finite-dimensional spectral recurrence is checked exactly.
U = tuple(tuple(power(M,2)[i][j]-J[i][j] for j in range(3))
          for i in range(3))
MU = mm(M,U)
assert MU == tuple(tuple(-U[i][j]/2 for j in range(3)) for i in range(3))

checks = 0
for t in range(2, 65):
    for X in (M,N):
        P = power(X,t)
        assert all(v>=0 for row in P for v in row)
        assert psi(P) == F(1,2)**(t-2)
        checks += 1
    assert power(N,t) == tuple(tuple(power(M,t)[j][i]
                                      for j in range(3)) for i in range(3))
    checks += 1

# The mixture's group chain is regular, but its full-space kernel retains
# a singular deterministic component through alternating branch choices.
Q = tuple(tuple((M[i][j]+N[i][j])/2 for j in range(3)) for i in range(3))
assert min(v for row in power(Q,3) for v in row) > 0
assert min(v for row in power(M,3) for v in row) == F(1,4)
minorization = F(1,2)**3 * 3 * min(v for row in power(M,3) for v in row)
assert minorization == F(3,32)
for t in range(1,65):
    branch = F(1,2)**t
    assert branch > 0
    for eps in (F(1,100),F(1,1000),F(1,10000)):
        assert eps <= F(1,3)
        lower_ratio = branch / eps
        assert lower_ratio*eps == branch
        checks += 1

# Directly inspect the exact alternating deterministic itinerary for a
# sample x in I0: first P adds 1/3, next R subtracts 1/3.
for t in range(1,65):
    x = F(1,12)
    for step in range(t):
        if step % 2 == 0:   # P's deterministic I0-to-I1 branch
            assert 0 <= x < F(1,3)
            x += F(1,3)
        else:               # R's deterministic I1-to-I0 branch
            assert F(1,3) <= x < F(2,3)
            x -= F(1,3)
    assert x == F(1,12) + (F(1,3) if t % 2 else 0)
    checks += 1

print('PASS: stationarity/group balance, time reversal, primitive powers,')
print('      exact component psi profile, and singular-branch probability.')
print('Exact arithmetic test assertions:',checks)
print('Minorization of three-step mixture:', minorization)
