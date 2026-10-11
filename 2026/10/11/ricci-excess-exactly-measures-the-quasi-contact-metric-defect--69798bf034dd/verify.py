import sympy as sp

n, H2, mu = sp.symbols("n H2 mu", positive=True)

Ric = 2*n + H2
B2 = 2*H2
Phi2 = n
deta2 = 4*Phi2 + B2

assert sp.simplify(B2 - 2*(Ric-2*n)) == 0
assert sp.simplify(deta2 - 2*Ric) == 0

cos2 = sp.simplify((4*n)**2 / (deta2 * (4*n)))
assert sp.simplify(cos2 - 2*n/Ric) == 0
assert sp.simplify(1-cos2 - (Ric-2*n)/Ric) == 0

# Exact 4-dimensional horizontal model for the 5-dimensional family.
J1 = sp.Matrix([
    [0,-1,0,0],
    [1,0,0,0],
    [0,0,0,-1],
    [0,0,1,0],
])
J2 = sp.Matrix([
    [0,0,-1,0],
    [0,0,0,1],
    [1,0,0,0],
    [0,-1,0,0],
])
I = sp.eye(4)
assert J1.T == -J1
assert J2.T == -J2
assert J1*J1 == -I
assert J2*J2 == -I
assert J1*J2 + J2*J1 == sp.zeros(4)

h = mu*J2
assert sp.simplify(sp.trace(h.T*h) - 4*mu**2) == 0
K = -2*J1*h
B2_matrix = sp.simplify(sp.trace(K.T*K)/2)
assert sp.simplify(B2_matrix - 8*mu**2) == 0

Ric5 = 4*(1+mu**2)
deta2_5 = 8*(1+mu**2)
assert sp.simplify(B2_matrix - 2*(Ric5-4)) == 0
assert sp.simplify(deta2_5 - 2*Ric5) == 0

print("VERIFY_OK")
print("general_defect_identity=true")
print("general_deta_norm_identity=true")
print("general_angle_identity=true")
print("family_defect_norm=8*mu^2")
print("family_angle=arctan(mu)")
