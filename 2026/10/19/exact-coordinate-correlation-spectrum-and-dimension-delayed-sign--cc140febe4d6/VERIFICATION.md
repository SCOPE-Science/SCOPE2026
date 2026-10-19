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

# Reproduction and proof boundaries

Run `python verify_twisted_baker_affine.py` with Python 3 and only its standard library. The expected count is `3483`, printed as `PASS: 3483 exact-rational identities / finite floating diagnostics`.

The script independently constructs each affine inverse branch, enumerates all binary inverse words through finite depth, and compares their averaged affine actions against the exact matrix powers, including constants. It compares the rational formal-power-series coefficients, determinant identities and the dimension-delayed first sign reversal for \(2\leq M\leq8\), and checks the planar closed form numerically.

The proof, rather than this finite replay, establishes invariance of Lebesgue measure, the transfer-covariance duality, all-dimensional determinant and resolvent formulas, cancellation-free poles, and the near-unit spectral root through a simple analytic implicit-function continuation. Finite diagnostics neither certify arbitrary dimension nor prove priority over every historical source. Independent audit has not been performed.
