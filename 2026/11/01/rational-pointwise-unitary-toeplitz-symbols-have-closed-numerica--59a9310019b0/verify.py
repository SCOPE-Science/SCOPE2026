#!/usr/bin/env python3
"""Finite numerical diagnostics for rational and nonrational matrix symbols."""
import cmath, math

nchecks = 0
for k in range(1, 721):
    z = cmath.exp(2j * math.pi * k / 721)
    # Rational conjugacy: U(z)=diag(z,1), A=[[0,1],[0,0]].
    # M(z)=[[0,z],[0,0]], p(z)=(z,1) gives maximal numerical radius 1/2.
    p = (z, 1+0j)
    numerator = z * p[1] * p[0].conjugate()
    value = numerator / (abs(p[0])**2 + abs(p[1])**2)
    assert abs(value - 0.5) < 2e-12
    nchecks += 1
    u = cmath.exp(z-1/z)
    assert abs(abs(u)-1) < 2e-12
    # P=[[1,conj(u)],[u,1]]/2: projection identities algebraically.
    P = ((0.5, u.conjugate()/2), (u/2, 0.5))
    for i in range(2):
        for j in range(2):
            lhs = sum(P[i][h]*P[h][j] for h in range(2))
            assert abs(lhs-P[i][j]) < 2e-12
            nchecks += 1
            assert abs(P[i][j] - P[j][i].conjugate()) < 2e-12
            nchecks += 1
print(f'FINITE_CHECKS_OK {nchecks}')
