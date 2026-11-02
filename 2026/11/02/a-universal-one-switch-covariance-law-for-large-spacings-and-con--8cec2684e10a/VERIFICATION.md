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
# Reproducible checks

Run `python verify_spacing.py` in the same directory as this document. Python standard library only. The checker derives the thresholded first- and other-coordinate monomial mixed moments by integrating a beta density, separately from the simplex-slice derivation. It compares those routes for degrees \(2\) through \(6\), dimensions \(2\) through \(13\) and all thresholds \(j/16\) with \(1\le j\le15\), and tests the quadratic covariance and unique sign location. Further exact checks reconstruct both variance identities; asymptotic checks use floating-point evaluations at large dimension. On execution it reports `PASS 1459 independent exact-rational and asymptotic checks`.

Finite symbolic/arithmetic checks verify sampled cases, not the universal infinite theorem, which follows from the analytic convexity and moment proof in `RESULT.md`. Floating-point asymptotic comparisons use a tolerance and are diagnostics rather than certifications. The sampled zero variance at \(m=2,t=1/2\) is explicitly allowed. No external audit or independent replication is claimed.
