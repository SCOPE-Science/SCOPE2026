---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The published inverse-Gaussian formula is
\[
g_\kappa(x)=
\Phi\!\left(\frac{\kappa-1}{\sqrt\kappa}x\right)
+e^{2x^2}\Phi\!\left(-\frac{\kappa+1}{\sqrt\kappa}x\right).
\]
For \(z=(\kappa+1)x/\sqrt\kappa\) and \(\rho=(\kappa-1)/(\kappa+1)\), its published first-order condition reduces to
\[
zM(z)=\frac1{1+\rho}.
\]
The proof checks invertibility through the positive integral derivative
\[
\frac d{dz}\bigl(zM(z)\bigr)
=\int_0^\infty u^2e^{-zu-u^2/2}\,du.
\]

For \(\rho\downarrow0\),
\[
1-zM(z)=z^{-2}-3z^{-4}+O(z^{-6}),
\]
which gives \(z=\rho^{-1/2}(1+O(\rho))\). For \(\rho\uparrow1\), strict positivity of the same derivative permits ordinary implicit expansion about the unique root \(z_*M(z_*)=1/2\); the exact envelope derivative then yields the coefficient \(z_*\varphi(z_*)\).

The standalone `VERIFY.py` reads no external data. It computes the universal root and coefficient, verifies equality between the original and transformed probability formulas at representative values, checks that the computed optimizer is locally minimal, and checks the endpoint normalizations numerically. These finite computations are regression tests only.
