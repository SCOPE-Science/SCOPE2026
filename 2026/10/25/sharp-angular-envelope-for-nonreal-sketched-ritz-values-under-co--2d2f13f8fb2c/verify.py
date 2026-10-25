"""Reproduce finite algebraic checks for a sharp sketched Ritz bound.

This program uses only Python's standard library. Infinite claims are proved
in the accompanying mathematical text, not by this finite check.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def t(a):
    return list(map(list, zip(*a)))


def sketched_2x2(A, gamma):
    s = sqrt(1 - gamma * gamma)
    q1 = [gamma, 0.0, s]
    q2 = [0.0, 1.0, 0.0]
    return [[sum(A[0][j]*q1[j] for j in range(3))/gamma, A[0][1]/gamma],
            [sum(A[1][j]*q1[j] for j in range(3)), A[1][1]]]


def imag_from_2x2(M):
    d = (M[0][0]-M[1][1])**2 + 4*M[0][1]*M[1][0]
    return sqrt(max(0., -d))/2

# Rational witness: A has eigenvalues 6 +/- sqrt(5), 6.
A = [[F(6), F(-1), F(0)],
     [F(-1), F(6), F(2)],
     [F(0), F(2), F(6)]]
g = F(3, 5)
q1 = [g, F(0), F(4, 5)]
q2 = [F(0), F(1), F(0)]
H = [[sum(A[0][j]*q1[j] for j in range(3))/g,
      sum(A[0][j]*q2[j] for j in range(3))/g],
     [sum(A[1][j]*q1[j] for j in range(3)),
      sum(A[1][j]*q2[j] for j in range(3))]]
assert H == [[F(6), F(-5,3)], [F(1), F(6)]]
assert (H[0][0]-H[1][1])**2+4*H[0][1]*H[1][0] == F(-20,3)
assert (F(5) * (1/g-F(1)) / 2) == F(5,3)
# Characteristic polynomial of A-6I is z*(z*z-5).
D = [[A[i][j] - (6 if i == j else 0) for j in range(3)] for i in range(3)]
assert sum(D[i][i] for i in range(3)) == 0
assert D[0][1]**2 + D[1][2]**2 == 5

count = 0
for gamma in (0.01, .15, .3, .6, .88, .99, .999999):
    s = sqrt(1-gamma*gamma)
    b = sqrt((1-gamma)/2)
    v = sqrt((1+gamma)/2)
    q1 = [gamma, 0., s]
    q3 = [-s, 0., gamma]
    hh = [b*q1[i]+v*q3[i] for i in range(3)]
    B = [[(hh[j] if i == 1 else 0.) + (hh[i] if j == 1 else 0.)
          for j in range(3)] for i in range(3)]
    # c=3,d=1, so m=2,L=4, positive definite endpoints attained.
    C = [[(3. if i==j else 0.)+B[i][j] for j in range(3)] for i in range(3)]
    M = sketched_2x2(C, gamma)
    rhs = sqrt((1/gamma-1)/2)
    assert abs(imag_from_2x2(M)-rhs) < 1e-8
    count += 1

rng = Random(0x41C01)
for i in range(2048):
    gamma = rng.uniform(0.01,1.)
    U = [[rng.uniform(-1.,1.) for _ in range(3)] for __ in range(3)]
    sym = [[(U[j][k]+U[k][j])/2 for k in range(3)] for j in range(3)]
    den = max(sum(abs(x) for x in row) for row in sym)
    B = [[x/den for x in row] for row in sym]
    # Gershgorin and symmetry: all eigenvalues(B) are in [-1,1].
    C = [[(3. if j==k else 0.)+B[j][k] for k in range(3)] for j in range(3)]
    M = sketched_2x2(C, gamma)
    rhs = sqrt((1/gamma-1)/2)
    assert imag_from_2x2(M) <= rhs+1e-10
    count += 1

print(f'PASS: rational witness and {count} three-dimensional sharpness/bound tests')
