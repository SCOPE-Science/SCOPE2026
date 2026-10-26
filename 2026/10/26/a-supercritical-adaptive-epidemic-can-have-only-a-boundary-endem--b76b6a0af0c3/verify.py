"""Exact reproducibility checks for the adaptive two-group SIS boundary example."""
import sympy as sp

u, v = sp.symbols('u v', real=True)
B = sp.Matrix([[4, 1], [1, sp.Rational(1, 2)]])
F = B / 2
reproduction = (9 + sp.sqrt(65)) / 8
assert reproduction in F.eigenvals()
assert reproduction > 1
assert min(sum(F[i,j] for j in range(2)) for i in range(2)) == sp.Rational(3, 4)

# With the directed 2 <- 1 link closed, the stationary infection equations.
g1 = -u + (1-u)*(2*u + v/2)
g2 = -v + (1-v)*v/4
assert sp.simplify(g1 - (u*(1-2*u) + (1-u)*v/2)) == 0
assert sp.simplify(g2 + v*(3+v)/4) == 0
assert sp.simplify(g1.subs({u:sp.Rational(1,2),v:0})) == 0
assert sp.simplify(g2.subs({u:sp.Rational(1,2),v:0})) == 0

z11,z12,z21,z22 = sp.symbols('z11 z12 z21 z22')
state = sp.Matrix([u,v,z11,z12,z21,z22])
# At u>=1/2 the cubic hinge is zero together with its first derivative.
vector = sp.Matrix([
    -u + (1-u)*(4*u*z11 + v*z12),
    -v + (1-v)*(u*z21 + v*z22/2),
    1-2*z11, 1-2*z12, -z21, 1-2*z22,
])
point = {u:sp.Rational(1,2),v:0,z11:sp.Rational(1,2),
         z12:sp.Rational(1,2),z21:0,z22:sp.Rational(1,2)}
assert all(sp.simplify(entry.subs(point))==0 for entry in vector)
jac = vector.jacobian(state).subs(point)
assert jac == sp.Matrix([
    [-1,sp.Rational(1,4),1,0,0,0],
    [0,sp.Rational(-3,4),0,0,sp.Rational(1,2),0],
    [0,0,-2,0,0,0], [0,0,0,-2,0,0],
    [0,0,0,0,-1,0], [0,0,0,0,0,-2]
])
assert jac.eigenvals() == {-1:2,sp.Rational(-3,4):1,-2:3}

# Inward-Perron arguments apply even where minimum row-sum tests fail.
# This separate comparison uses constant strictly positive creation.
comparison = sp.Matrix([[1,16],[sp.Rational(16,45),1]])/2
assert min(sum(comparison[i,j] for j in range(2)) for i in range(2)) < 1
assert max(comparison.eigenvals().keys(), key=lambda t:float(t)) > 1
print('CHECK_OK')
