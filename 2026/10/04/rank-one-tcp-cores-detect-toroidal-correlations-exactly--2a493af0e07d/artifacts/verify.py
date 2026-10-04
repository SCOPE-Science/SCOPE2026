#!/usr/bin/env python3
import sympy as sp

I = sp.I
r2 = sp.sqrt(2)
# Columns are four unit vectors in C^2.
U = sp.Matrix([
    [1, 0, 1/r2, 1/r2],
    [0, 1, 1/r2, I/r2],
])
Z = sp.conjugate(U.T) * U
Z_expected = sp.Matrix([
    [1, 0, 1/r2, 1/r2],
    [0, 1, 1/r2, I/r2],
    [1/r2, 1/r2, 1, (1+I)/2],
    [1/r2, -I/r2, (1-I)/2, 1],
])
assert sp.simplify(Z - Z_expected) == sp.zeros(4)
assert Z.rank() == 2
assert all(sp.simplify(Z[i,i]-1) == 0 for i in range(4))
# PSD follows from Z=U^*U; eigenvalues are displayed as an extra exact check.
evals = sorted([sp.simplify(e) for e,m in Z.eigenvals().items() for _ in range(m)], key=sp.default_sort_key)
assert sum(1 for e in evals if sp.simplify(e)==0) == 2
assert all(sp.N(e) >= -sp.Float('1e-30') for e in evals)

# Extremality check: for X=[[a,c],[conj(c),b]], c=x+i y,
# the four equations u_i^* X u_i=0 have coefficient matrix below.
E = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [sp.Rational(1,2), sp.Rational(1,2), 1, 0],
    [sp.Rational(1,2), sp.Rational(1,2), 0, -1],
])
assert E.det() != 0

# Endpoint arithmetic in the recent DOC family.
a = sp.Integer(1)
r = (a + 1/a)/2
s = 1 + 3*r
M = sp.Matrix([
    [1,a,1/a,r],
    [1/a,1,a,r],
    [a,1/a,1,r],
    [r,r,r,1],
])
J = sp.ones(4)
assert r == 1 and s == 4 and M == J
A = M/s
B = J/s
C = Z/s
assert A == J/4 and B == J/4 and C == Z/4
# PPT inequalities at a=1: A_ij A_ji=1/16 and |B_ij|^2=1/16;
# correlation entries satisfy |Z_ij|<=1 (checked for this witness exactly).
for i in range(4):
    for j in range(4):
        assert sp.simplify(A[i,j]*A[j,i] - sp.Rational(1,16)) == 0
        assert sp.simplify(B[i,j]*sp.conjugate(B[i,j]) - sp.Rational(1,16)) == 0
        assert sp.simplify(sp.Rational(1,16) - C[i,j]*sp.conjugate(C[i,j])) >= 0

print('VERIFY_OK')
print('rank_Z=', Z.rank())
print('extremality_matrix_det=', E.det())
print('eigenvalues_Z=', evals)
print('endpoint_s=', s)
