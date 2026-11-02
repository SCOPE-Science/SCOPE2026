"""Exact characteristic-five Cartier identity and rank-stratification checks.
Requires Python 3 and SymPy. Run: python3 verify_symbolic.py
"""
import math
import sympy as s

p = 5
x, A, B, C, D = s.symbols('x A B C D')
params = (A, B, C, D)
f = x**6 + A*x**4 + B*x**3 + C*x**2 + D*x
basis = [(i,j) for j in range(4) for i in range(4) if 5*i+6*j <=18]
assert basis == [(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(0,2),(1,2),(0,3)]
M = s.zeros(10)
for col, (i,j) in enumerate(basis):
    for m in range(j+1):
        polynomial = s.Poly(s.expand(x**i * f**m), x)
        sign = (-1)**m * math.comb(j,m)
        for row, (r,ell) in enumerate(basis):
            if ell == j-m:
                coeff = s.Poly(sign*polynomial.nth(5*r+4), *params, modulus=5).as_expr()
                M[row,col] += coeff
M = M.applyfunc(lambda value: s.Poly(value,*params,modulus=5).as_expr())
expected = s.zeros(10)
for row,col,value in [
    (0,4,-A),(0,5,-B),(0,6,-C),
    (0,7,2*B*D+C**2),(0,8,2*C*D),(0,9,2*C*D**2),
    (1,7,2*B),(1,8,A**2+2*C),
    (1,9,2*A**2*D-A*B*C-B**3-C*D),
    (2,9,2*A**2+2*C),(4,7,-2*A),(4,8,-2*B),
    (4,9,B*D-2*C**2),(5,9,B),(7,9,2*A),
]:
    expected[row,col] = value
assert all(s.Poly(M[i,j]-expected[i,j],*params,modulus=5).is_zero for i in range(10) for j in range(10))
P = s.Matrix([[2*B,A**2+2*C],[-2*A,-2*B]])
Q = B**2 + 2*A**3 + 4*A*C
assert s.Poly(P.det()-Q,A,B,C,modulus=5).is_zero
z = s.symbols('z')
assert s.Poly((Q.subs(C,z-3*A**2))-(B**2+4*A*z),A,B,z,modulus=5).is_zero
assert M.subs({A:0,B:0,C:0}) == s.zeros(10)
print('CHAR5_CONDUCTOR6_EXACT_CARTIER_Q_AND_A1_OK')
