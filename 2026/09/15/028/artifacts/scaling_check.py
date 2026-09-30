"""Checks the repaired axis-scaling/ring-escape identities.

This script intentionally makes no universal claim about an off-axis
``Gamma``: after translation, cylindrical basis directions change and
poloidal components can contribute to the azimuthal component relative to
the new origin.

Run: python3 artifacts/scaling_check.py
"""
import sympy as sp

print("=== (a) exact on-axis Gamma invariance ===")
lam, rho, Gamma = sp.symbols("lam rho Gamma", positive=True)
vtheta = Gamma / (lam * rho)       # physical r = lam*rho
Gamma_scaled = sp.simplify(rho * (lam * vtheta))
print("Gamma_scaled =", Gamma_scaled)
assert Gamma_scaled == Gamma

print("=== (b) rotation-center geometry ===")
r0, th = sp.symbols("r0 th", real=True)
x0 = sp.Matrix([r0, 0])
R = sp.Matrix([[sp.cos(th), -sp.sin(th)],
               [sp.sin(th),  sp.cos(th)]])
delta = sp.simplify(R*x0 - x0)
print("R*x0 - x0 =", delta)
# The affine rescaling intertwines all rotations iff the horizontal
# component of the center is zero.
assert sp.simplify(delta.subs(r0, 0)) == sp.zeros(2, 1)
print("For r0 != 0 this is generically nonzero; off-axis centering does not "
      "preserve axisymmetry in general.")
print("Special-field counterexample to an 'iff for every field': a constant "
      "axial vector field remains rotationally symmetric after any translation.")

print("=== (c) Type-II backward-window exhaustion ===")
for a in (0.5, 0.6, 1.0):
    exponent = 1 - 2*a
    print(f"alpha={a}: exponent={exponent} "
          + ("(bounded Type-I scale)" if exponent >= 0 else "(window -> +inf)"))

print("=== (d) ring escape ===")
cases = [(1e-2, 1e3), (1e-3, 1e5), (1e-4, 1e8)]
for rk, Mk in cases:
    dk = rk*Mk
    print(f"r_k={rk:g}, M_k={Mk:g}, d_k={dk:g}")
assert all(rk*Mk > 1 for rk, Mk in cases)

print("Conclusion: on-axis Gamma invariance is exact; retaining a chosen "
      "axis-projected peak on compact sets requires bounded d_k. A Gamma "
      "bound alone supplies no purely kinematic bound on d_k.")
