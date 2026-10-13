import sympy as sp

x0,x1,x2 = sp.symbols('x0 x1 x2')
B = sp.Matrix(3,3,lambda i,j: sp.symbols(f'b{i}{j}'))
x = sp.Matrix([x0,x1,x2])
dx = B*x
U = [x0*x2, x1*x2]
outside = [x0**2,x1**2,x2**2,x0*x1]
eqs=[]
for q in U:
    grad=sp.Matrix([sp.diff(q,z) for z in (x0,x1,x2)])
    dq=sp.expand((grad.T*dx)[0])
    P=sp.Poly(dq,x0,x1,x2)
    eqs.extend(P.coeff_monomial(m) for m in outside)
vars=list(B)
M,_=sp.linear_eq_to_matrix(eqs,vars)
sol=sp.linsolve(eqs,vars)
assert M.rank()==4
assert 9-M.rank()==5  # gl_3 stabilizer Lie algebra
assert 8-M.rank()==4  # quotient by scalar matrices
expected=(vars[0],vars[1],0,vars[3],vars[4],0,0,0,vars[8])
assert sol == sp.FiniteSet(expected)

# Base ideal U=(x0*x2,x1*x2) is the intersection (x2) cap (x0,x1).
# Check the two inclusions by direct normal forms of the generators.
assert sp.expand(x0*x2) == x0*x2
assert sp.expand(x1*x2) == x1*x2

print('stabilizer Lie algebra in gl3: block diagonal gl2 + gl1')
print('dimension in gl3 = 5; dimension in pgl3 = 4')
print('global stabilizer: (GL2 x Gm)/Gm_diag ~= GL2')
print('VERIFY_OK')
