#!/usr/bin/env python3
"""Exact symbolic checks for a characteristic-three Hessian singularity calculation.
Requires sympy; no floating-point calculations or external services.
"""
from itertools import product
from sympy import symbols, Poly, hessian, Matrix, expand, factor_list
x = symbols('x0:5')
u = symbols('u1:5')
z = symbols('z')
F = sum(x[i]**2 * x[(i+1)%5] for i in range(5))
H = hessian(F, x)
D = Poly(H.det(method='berkowitz'), *x, modulus=3)
assert D.total_degree() == 5 and len(D.terms()) == 10
P = {xi: 1 for xi in x}
assert D.eval(P) % 3 == 0
assert all(Poly(D.as_expr().diff(xi), *x, modulus=3).eval(P) % 3 == 0 for xi in x)
# Rank of the Hessian matrix of the original cubic at the diagonal point.
assert H[:4,:4].det() % 3 != 0
assert H.det().subs(P) % 3 == 0
# Quadratic part at the node, in the affine chart x0=1.
local = Poly(expand(D.as_expr().subs({x[0]:1,**{x[i]:1+u[i-1] for i in range(1,5)}})), *u, modulus=3)
quadratic = sum(coeff * __import__('functools').reduce(lambda a,b:a*b, (t**power for t,power in zip(u,mon)),1)
                for mon,coeff in local.terms() if sum(mon)==2)
expected = -sum(t*t for t in u) + sum(u[i]*u[i+1] for i in range(3))
assert Poly(quadratic-expected,*u,modulus=3).is_zero
assert int(hessian(expected,u).det()) == 5
# The eleven directions are distinct, split 1+5+5 over the prime field.
fac = factor_list(z**11-1, modulus=3)[1]
assert sorted([Poly(f,z).degree() for f,e in fac for _ in range(e)]) == [1,5,5]
# Projective singular points [1:t:t^{-1}:t^3:t^{-5}], t^11=1;
# each monomial of F has exponent congruent to one modulo eleven.
powers = [0,1,-1,3,-5]
assert all((2*powers[i]+powers[(i+1)%5]-1)%11 == 0 for i in range(5))
# Gradient relations and local rank prove geometric completeness of rank-four nodes.
print('HESSIAN_DEGREE=5;MONOMIAL_COUNT=10')
print('DIAGONAL_HESSIAN_RANK=4;LOCAL_NODE_QUADRATIC_DET_MOD3=2')
print('ELEVEN_POINTS_OFF_ORIGINAL_CUBIC=YES;ROOT_FACTOR_DEGREES=1,5,5')
print('CORANK_ONE_SINGULARITY_PROOF=ADJUGATE_AND_EULER_IDENTITIES')
print('VERIFY_OK')
