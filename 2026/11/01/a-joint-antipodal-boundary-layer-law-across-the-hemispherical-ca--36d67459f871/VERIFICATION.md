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

The accompanying `verify.py` is a self-contained Python standard-library checker. It passed **117 deterministic comparisons** covering the integral normalization for dimensions three through nine, the exact three-dimensional piecewise polynomial, low-deficit convergence against an independently implemented finite-radius angular integral, and the subhemisphere endpoint relation. Execute `python verify.py` from the directory containing this file.

The crucial analytic steps are the exact antipodal reduction, the signed-latitude cap constraints, the explicit spherical normal-coordinate Jacobian, the quadratic small-distance expansion, and dominated convergence on the compact rescaled event region. The limiting conditional law is uniform on a measurable tangent bundle with density \((\sigma_{q-1}J_q(\lambda))^{-1}\); exact integration over its latitude coordinate gives the positive-part factor and probability rate.

The numerical checks cannot establish convergence for all dimensions or prove originality. Independent scientific validation has not been performed. The regime fixes dimension \(q\) and crossover parameter \(\lambda\); the strict event is impossible at and below \(\lambda=-1/2\), so no conditional law is claimed there.
