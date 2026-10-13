#!/usr/bin/env python3
"""Exact finite checks supporting a moment-instability theorem for doubly stochastic Gauss-Seidel.
The infinite-time assertions are proved analytically, not by this script.
"""
from fractions import Fraction as F
from itertools import product

q = F(1, 10)
alpha = F(1, 2)
A = ((F(1), q), (q, F(1)))
S = sum(z*z for row in A for z in row)
assert S == F(101, 50)

# Rows i and coordinates j are selected with |A_ij|^2/S.
choices = []
for i,j in product(range(2), repeat=2):
    p = A[i][j]**2/S
    # x_j' = x_j - alpha * <A_i,x> / A_ij; other coordinate fixed
    B = [[F(int(k == l)) for l in range(2)] for k in range(2)]
    for l in range(2):
        B[j][l] -= alpha*A[i][l]/A[i][j]
    choices.append((p, tuple(tuple(row) for row in B)))
assert sum(p for p,B in choices) == 1

M = [[sum(p*sum(B[k][i]*B[k][j] for k in range(2)) for p,B in choices)
      for j in range(2)] for i in range(2)]
G = [[sum(A[k][i]*A[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
for i,j in product(range(2),repeat=2):
    assert M[i][j] == F(int(i == j)) - (2*alpha*(1-alpha)/S)*G[i][j]

# This is the sharp uniform quadratic-error contraction factor.
q2 = 1 - alpha*(1-alpha)*(1-q)**2/(1+q*q)
assert q2 == F(323,404)
assert F(0)<q2<F(1)

# Lower bound from the two rare off-diagonal updates.
poff = q*q/S
assert poff == F(1,202)
low = (alpha-(1-alpha)*q)**4/(4*q*q*(1+q*q))
assert low == F(6561,6464) > 1

# Exact all-state proof inequalities in a finite collection of rational test vectors.
starts = [(F(i),F(j)) for i in range(-9,10) for j in range(-9,10) if i or j]
for x in starts:
    norm2 = x[0]**2+x[1]**2
    moments = {}
    for degree in (2,4,6):
        val = sum(p*(sum((sum(B[k][j]*x[j] for j in range(2)))**2
                      for k in range(2)))**(degree//2) for p,B in choices)
        moments[degree] = val
    expected2 = sum(x[i]*sum(M[i][j]*x[j] for j in range(2)) for i in range(2))
    assert moments[2] == expected2 <= q2*norm2
    assert moments[4] >= low*norm2**2

# Full enumeration of independent update paths for a few fixed horizons.
for x0 in ((F(1),F(0)), (F(1),F(1)), (F(2),-F(3))):
    states=[(F(1),x0)]
    for k in range(1,7):
        states = [(w*p, tuple(sum(B[i][j]*x[j] for j in range(2)) for i in range(2)))
                  for w,x in states for p,B in choices]
        second=sum(w*(x[0]*x[0]+x[1]*x[1]) for w,x in states)
        fourth=sum(w*(x[0]*x[0]+x[1]*x[1])**2 for w,x in states)
        n0=x0[0]*x0[0]+x0[1]*x0[1]
        assert second <= q2**k*n0
        assert fourth >= low**k*n0**2

print('VERIFY_OK: 360 rational-direction tests, 18 exact finite-horizon expectations, quadratic matrix identity')
