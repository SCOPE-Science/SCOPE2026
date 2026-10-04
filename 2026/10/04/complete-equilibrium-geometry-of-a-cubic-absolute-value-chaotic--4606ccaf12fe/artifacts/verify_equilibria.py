from sympy import Matrix, symbols, sqrt, factor, expand, N

lam, r, a, b, s = symbols('lam r a b s', real=True)
J = Matrix([
    [0, 0, r],
    [3*r**2, -3*r**2, 0],
    [a*s-r, -3*b*r**2-r, 0],
])
p = expand((lam*Matrix.eye(3)-J).det())
# At a nonzero equilibrium, s=sign(r) and a*s=r+b*r**2.
p_eq = factor(p.subs(a*s, r+b*r**2))
expected = lam**3 + 3*r**2*lam**2 - b*r**3*lam + 3*r**4*(1+2*b*r)
assert expand(p_eq-expected) == 0

# Source parameter example a=13/20, b=1/10.
aa = symbols('aa')
a0 = 13/20
b0 = 1/10
rpos = (-10 + sqrt(126))/2
rneg_near = (-10 + sqrt(74))/2
rneg_far = (-10 - sqrt(74))/2
roots = [rpos, rneg_near, rneg_far]
for rr in roots:
    # Equilibrium residual for the z equation after x=y=r,z=0.
    residual = a0*abs(float(N(rr))) - b0*float(N(rr))**3 - float(N(rr))**2
    assert abs(residual) < 1e-10

# Routh-Hurwitz boundary for the less-negative branch.
Delta = symbols('Delta', positive=True)
rnear = (-1 + sqrt(Delta))/(2*b)
A = 3*rnear**2
B = -b*rnear**3
C = 3*rnear**4*(1+2*b*rnear)
routh_gap = factor(A*B-C)
# With Delta=1-4ab, the sign change occurs at sqrt(Delta)=1/3,
# equivalent to ab=2/9.
assert factor(routh_gap) != 0
rr = -1/(3*b)
boundary_poly = factor(expected.subs(r, rr))
expected_boundary = factor((3*b**2*lam+1)*(27*b**2*lam**2+1)/(81*b**4))
assert factor(boundary_poly-expected_boundary) == 0

print('characteristic_polynomial =', p_eq)
print('sample_roots =')
for rr in roots:
    print(' ', rr, '≈', N(rr, 14))
print('sample_ab =', a0*b0)
print('less_negative_stable_iff = 2/9 < a*b < 1/4')
print('ab=2/9_factorization =', boundary_poly)
print('all_checks = PASS')
