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

# Verification evidence

The proof uses an anchored-coordinate determinant-one transformation to rung and horizontal slopes, an exact integral kernel, differentiation of its resolvent, positivity and spectral decomposition, and strict Cauchy–Schwarz on the resulting moment sequence. All are displayed in `RESULT.md`.

The standalone `verify_ladder_volumes.py` uses two independently specified rational algorithms: coefficients of the analytic power series, and leading Ehrhart coefficients obtained from exhaustive finite integer potential counts. The latter counts all integer potentials for each dilation \(k=0,1,\ldots,2n-1\), using rung-slope dynamic programming, not partial sampling; total unimodularity ensures it returns the actual volume. The checker passes for \(n=2\) through \(7\), in dimensions \(3\) through \(13\) (odd integers). A finite checker does not establish the infinite-dimensional-family statement; its proof is independent of this check.

The spectral growth base and first two spectral roots are numerical approximations to the unambiguous roots of \(\cos\rho=\rho\sin\rho\). The symbolic claims do not depend on floating-point accuracy. No independent audit has been performed.
