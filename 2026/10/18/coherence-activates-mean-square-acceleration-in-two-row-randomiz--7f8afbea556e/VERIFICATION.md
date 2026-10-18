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

# Reproducible verification

Execute `python verify.py` with Python 3, NumPy, and SymPy. The standalone script reports 285 checks. It uses exact rational calculations for the reflection-separated covariance operator, characteristic polynomials, two Taylor identities, orthogonal scalar covariance polynomial, and repeated direct finite-step covariance updates; floating-point eigenspectra are used only for supplementary numerical spot checks.

The analytic proof in RESULT.md, not a simulation or a finite-range search, establishes the infinite-step mean-square rate, sign of its first derivative, unique small-coherence global optimum, and asymptotic expansions. The source algorithm is a consistent real two-row equation system with equally likely independent sampling, zero initial velocity, and no geometric smoothing. Publication priority and independent scientific validation have not been established.
