#!/usr/bin/env python3
"""Exact finite-moment identities supporting the spherical Gamma-clock comparison.

No finite check establishes the infinite-array strong laws or singularity theorem.
"""
from fractions import Fraction as F
from itertools import product

N = 0


def eq(a, b):
    global N
    assert a == b, (a, b)
    N += 1


def gamma_moment(k, scale, r):
    ans = scale ** r
    for j in range(r):
        ans *= k + j
    return ans


def r_moment(d, r):
    ans = F(1)
    for j in range(r):
        ans *= 1 + F(2 * j, d)
    return ans


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def trans(A):
    return [list(v) for v in zip(*A)]


for k, scale, d in product((F(1, 3), F(1), F(5, 2), F(11)),
                           (F(1, 5), F(2), F(9, 4)),
                           (3, 5, 9, 51, 501)):
    m = [gamma_moment(k, scale, r) for r in range(1, 5)]
    # Chi-square mean, second and fourth normalized moments.
    eq(r_moment(d, 1), F(1))
    eq(r_moment(d, 2), 1 + F(2, d))
    eq(r_moment(d, 4), 1 + F(12, d) + F(44, d*d) + F(48, d**3))
    eq(r_moment(d, 4) - r_moment(d, 2) ** 2,
       F(8, d) + F(40, d*d) + F(48, d**3))
    # The squared multipole energy has the exact finite-degeneracy bias.
    eq(m[1] * r_moment(d, 2), scale**2 * k * (k+1) * (1+F(2,d)))
    # Gamma moment covariance matrix for first and second raw moments.
    V = [[m[1] - m[0]**2, m[2] - m[0]*m[1]],
         [m[2] - m[0]*m[1], m[3] - m[1]**2]]
    eq(V[0][0], k*scale**2)
    eq(V[0][1], 2*k*(k+1)*scale**3)
    eq(V[1][1], 2*k*(k+1)*(2*k+3)*scale**4)
    # Delta-method Jacobian for k = mean^2/variance, scale=variance/mean.
    J = [[2*(k+1)/scale, -1/scale**2],
         [-(2*k+1)/k, 1/(k*scale)]]
    O = mm(mm(J,V),trans(J))
    eq(O[0][0], 2*k*(k+1))
    eq(O[0][1], -2*scale*(k+1))
    eq(O[1][0], -2*scale*(k+1))
    eq(O[1][1], scale**2*(2*k+3)/k)
    eq(O[0][0]*O[1][1]-O[0][1]**2, 2*scale**2*(k+1))

print('CHECK_OK: %d exact rational moment, degeneracy and covariance identities' % N)
