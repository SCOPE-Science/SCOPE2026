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

The proof is analytic. The critical continuum steps are the exact radial multiplicity formula, the substitutions \(s=d-a\), \(y=s(s+2a)\), and \(z=t(t+2a)\), and the beta-kernel identity
\[
\int_z^Y\frac{dy}{\sqrt{(y-z)(Y-y)}}=\pi.
\]
Applying that identity twice forces the transformed tail to be \(F(z)=z^{-1/2}\), which reconstructs the stated \(\Gamma_a\). The derivative of \(\Gamma_a\) gives the positive density, and layer cake gives the total width.

The standalone checker `artifacts/verify_fractional_annulus.py` was executed from its packaged path. It checked representative values of the exact tail derivative and antiderivative, verified that the Abel-substituted integrand reduces to the constant \(2\) on a parameter grid, checked \(W_a=2\sqrt{1-a^2}\), and checked the specialization \(W_{1/2}=\sqrt3\). It returned `PASS: tail monotonicity derivative, Abel transform, and total-width identities checked.`

Finite numerical checks are not used to infer uniqueness or the continuum quantifiers. No unrestricted fractional optimum is verified or claimed.
