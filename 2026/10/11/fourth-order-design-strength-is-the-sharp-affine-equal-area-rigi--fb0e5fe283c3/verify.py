import sympy as sp

sqrt = sp.sqrt
v1 = sp.Matrix([sqrt(sp.Rational(2,3)), 0, 1/sqrt(3)])
v2 = sp.Matrix([-1/sqrt(6), 1/sqrt(2), 1/sqrt(3)])
v3 = sp.Matrix([-1/sqrt(6), -1/sqrt(2), 1/sqrt(3)])
V = sp.Matrix.hstack(v1, v2, v3)

assert sp.simplify(V.T*V - sp.eye(3)) == sp.zeros(3)

nodes = [v1,-v1,v2,-v2,v3,-v3]
M2 = sum((x*x.T for x in nodes), sp.zeros(3))/6
assert sp.simplify(M2 - sp.eye(3)/3) == sp.zeros(3)

A = sp.diag(2/sqrt(5), 2/sqrt(5), sqrt(2))
Q = sp.simplify(A.inv()*A.inv().T)
Q_target = sp.diag(sp.Rational(5,4), sp.Rational(5,4), sp.Rational(1,2))
assert sp.simplify(Q-Q_target) == sp.zeros(3)

for x in nodes:
    assert sp.simplify((x.T*Q*x)[0]-1) == 0

assert Q[0,0] != Q[2,2]
assert sp.simplify(abs(A.det()) - 4*sqrt(2)/5) == 0

# The anisotropic quadratic defect vanishes on the 3-design nodes.
D = Q - sp.eye(3)
for x in nodes:
    assert sp.simplify((x.T*D*x)[0]) == 0
assert sp.trace(D) == 0
assert D != sp.zeros(3)

print("VERIFY_OK")
print("sharpness_nodes=orthonormal_antipodal_3_design")
print("nonsimilarity_Q=diag(5/4,5/4,1/2)")
print("all_six_affine_area_norms=1")
print("degree_three_threshold_counterexample=true")
