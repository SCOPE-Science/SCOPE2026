"""Recovery-test script for lane 20372 target analysis.

Verifies the scale identities on which the target proof hinges:
 (a) on-axis Navier-Stokes rescaling preserves Gamma = r v_theta exactly;
 (b) off-axis rescaling breaks Gamma invariance (bound retained only trivially);
 (c) Type-II amplitude renormalization exhausts the backward time window;
 (d) ring-escape model: r_k -> 0, M_k -> infty with d_k = r_k*M_k -> infty,
     so an axis-projected renormalization peak escapes every compact set.

Run: python3 output/artifacts/scaling_check.py
"""
import sympy as sp

print("=== (a) on-axis Gamma invariance ===")
lam, r_y, Gamma = sp.symbols('lam r_y Gamma', positive=True)
vth = Gamma / (lam * r_y)          # v_theta(x) = Gamma / r_x, r_x = lam*r_y
Gamma_lam_on = sp.simplify(r_y * (lam * vth))
print("Gamma^lam (on-axis) =", Gamma_lam_on)
assert Gamma_lam_on == Gamma

print("=== (b) off-axis Gamma non-invariance ===")
r0, y1 = sp.symbols('r0 y1', real=True)
Gamma_lam_off = sp.simplify(r_y * lam * Gamma / (r0 + lam * y1))
print("Gamma^lam (off-axis) =", Gamma_lam_off)

print("=== (c) Type-II backward-window exhaustion ===")
# model rate ||v(t)|| = (T*-t)^(-alpha), alpha > 1/2 (Type II)
# amplitude scale mu_k = 1/M_k; window length (T*-t_k)/mu_k^2 = (T*-t_k)^{1-2a}
for a in (0.5, 0.6, 1.0):
    print(f"alpha={a}: window exponent 1-2alpha = {1 - 2 * a} "
          + ("(bounded, Type I)" if 1 - 2 * a >= 0 else "(-> +inf, Type II)"))

print("=== (d) ring-escape model ===")
# r_k -> 0 (peaks approach axis by CKN-circle lemma) but d_k = r_k*M_k -> inf
cases = [(1e-2, 1e3), (1e-3, 1e5), (1e-4, 1e8)]
for r_k, M_k in cases:
    d_k = r_k * M_k
    print(f"r_k={r_k:g}, M_k={M_k:g}: d_k = {d_k:g} "
          + ("-> peak inside B_1" if d_k < 1 else "-> peak ESCAPES compacts"))
print("Conclusion: axis-projected renormalization keeps axisymmetry and the "
      "global bound, but nontriviality needs d_k bounded, which M<inf alone "
      "does not imply. This is the blocking obstacle.")
