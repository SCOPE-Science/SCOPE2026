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

Reproduce the supplementary finite checks with `python3 CHECK.py` (Python standard library only). The program reports **68,619 exact and finite numerical assertions passed**.

The exact rational portion separately constructs (i) the direct compression of multiplication by each analytic monomial and (ii) the iterated single-step compression. It verifies their difference on all tested angular basis indices, strict central coefficients, rank-support geometry, and reflection monotonicity for several integer weights and degrees. A separate floating-point portion compares normalized singular-value moments with the beta integrals at degree 20,000.

The all-integer-degree, all-real-weight theorem and the weak convergence of nonzero singular values are **not** finite consequences of these assertions; the proof in `RESULT.md` independently establishes them by angular orthogonality, strict moment covariance, exact weighted-shift action, gamma-ratio asymptotics, and controlled endpoint Riemann sums.

No independent mathematical audit, Lean verification, or externally certified reproducibility check has been performed.
