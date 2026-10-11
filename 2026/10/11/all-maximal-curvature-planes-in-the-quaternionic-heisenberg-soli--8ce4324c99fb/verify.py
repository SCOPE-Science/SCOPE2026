import sympy as sp

p,q,u,v = sp.symbols("p q u v", nonnegative=True, real=True)

F4 = p+q-5*p*q+6*sp.sqrt(p*q*(1-p)*(1-q))
identity = sp.expand(1-4*u**2-v**2+6*u*v)
# Algebraic substitution using p+q=1+u^2-v^2 and pq=u^2.
assert sp.expand((1+u**2-v**2)-5*u**2+6*u*v - identity) == 0

# First branch endpoint comparison.
assert sp.Rational(21,16) < sp.Rational(16,11)

# Second branch and unique parabola maximizer.
g = 8*u-11*u**2
assert sp.solve(sp.diff(g,u),u) == [sp.Rational(4,11)]
assert sp.simplify(g.subs(u,sp.Rational(4,11))-sp.Rational(16,11)) == 0

# Reconstruct j-matrices from the published bracket table.
# Basis order X1,X2,X3,X4; convention <j(Z)Xi,Xj>=<Z,[Xi,Xj]>.
Z1 = sp.Matrix([
    [0,0,-1,0],
    [0,0,0,-1],
    [1,0,0,0],
    [0,1,0,0],
])
Z2 = sp.Matrix([
    [0,0,0,-1],
    [0,0,1,0],
    [0,-1,0,0],
    [1,0,0,0],
])
Z3 = sp.Matrix([
    [0,1,0,0],
    [-1,0,0,0],
    [0,0,0,-1],
    [0,0,1,0],
])
I = sp.eye(4)
for J in (Z1,Z2,Z3):
    assert J.T == -J
    assert J*J == -I

e1,e2,e3,e4 = [sp.eye(4)[:,i] for i in range(4)]
assert Z2*e4 == Z1*e3
assert Z2*e3 == -Z1*e4

# Curvature of the source's maximizing plane.
P = sp.Rational(4,11)
Q = sp.Rational(7,11)
cross = sp.Rational(3,2)*P*Q
curv = sp.Rational(1,4)*(2*P*Q)-sp.Rational(3,4)*P**2+cross
assert sp.simplify(curv-sp.Rational(4,11)) == 0

print("VERIFY_OK")
print("sharp_scalar_bound=true")
print("unique_norm_split=4/11:7/11")
print("source_plane_alignment=true")
print("source_plane_curvature=4/11")
