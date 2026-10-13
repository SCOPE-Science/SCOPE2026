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

The analytic argument proves the identities for every pair of positive integer sample sizes under the common continuous-distribution null.

The standalone checker uses exact rational arithmetic and exhaustive enumeration of every fixed-composition binary label word for every pair \((m,n)\) with \(2\le m+n\le14\). For each pair it recomputes the run count and Mann–Whitney inversion count directly from the word, then checks the exact marginal moments, \(\operatorname{Cov}(R,U)=0\), \(\operatorname{Cov}(R,(U-mn/2)^2)\), the fourth-moment variance, the standardized covariance, and the exact squared correlation when defined.

The finite enumeration is a consistency test rather than an infinite proof. No claim is verified for ties or unequal underlying distributions.
