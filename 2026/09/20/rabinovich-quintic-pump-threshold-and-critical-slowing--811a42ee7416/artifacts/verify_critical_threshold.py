import sympy as sp

p, q, d, s, v, z, eps = sp.symbols("p q d s v z eps", positive=True)
D = p**2 + q**2
h = p*q + eps

x = q*s + p*v
y = p*s - q*v

fx = h*y - p**2*x - y*z
fy = h*x - q**2*y + x*z
fz = x*y - d*z

sdot = sp.factor((q*fx + p*fy)/D)
vdot = sp.factor((p*fx - q*fy)/D)
zdot = sp.expand(fz)

expected_s = v*z
expected_v = -D*v - s*z
expected_z = p*q*s**2 + (p**2-q**2)*s*v - p*q*v**2 - d*z

Edot = sp.factor(2*x*fx + 2*y*fy)
expected_Edot = -2*(p*x-q*y)**2

a3 = -p*q/(d*D)
b2 = p*q/d
v_cm = a3*s**3
z_cm = b2*s**2

cm_v_residual = sp.series(
    sp.diff(v_cm, s)*(v_cm*z_cm)
    - (-D*v_cm - s*z_cm), s, 0, 5
).removeO()
cm_z_residual = sp.series(
    sp.diff(z_cm, s)*(v_cm*z_cm)
    - (p*q*s**2 + (p**2-q**2)*s*v_cm - p*q*v_cm**2 - d*z_cm),
    s, 0, 4
).removeO()

reduced = sp.expand(v_cm*z_cm)
quintic_coeff = sp.simplify(reduced.coeff(s, 5))
expected_quintic = -p**2*q**2/(d**2*D)

checks = {
    "critical_s_equation": sp.simplify(sdot.subs(eps, 0)-expected_s),
    "critical_v_equation": sp.simplify(vdot.subs(eps, 0)-expected_v),
    "critical_z_equation": sp.simplify(zdot-expected_z),
    "critical_energy_identity": sp.simplify(Edot.subs(eps, 0)-expected_Edot),
    "center_v_invariance_through_s3": sp.expand(cm_v_residual),
    "center_z_invariance_through_s2": sp.expand(cm_z_residual),
    "quintic_coefficient": sp.simplify(quintic_coeff-expected_quintic),
}

for name, residual in checks.items():
    print(f"{name}: {sp.simplify(residual)}")

print("quintic coefficient:", expected_quintic)
print("linear center coefficient derivative:", sp.simplify(2*p*q/D))
