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

The exact covariance is derived from the normalized-gap Dirichlet density. The one-gap moments use \(Y_1\sim\mathrm{Beta}(1,n-1)\); the two-gap moment uses \(T=Y_1+Y_2\sim\mathrm{Beta}(2,n-2)\) and an independent uniform split. The finite recurrences for \(J_m\) and \(K_m\) follow by integration by parts.

Exact algebraic checks: \(n=3\) gives \(10/(3\pi^2)\); \(n=4\) gives \(4(216-19\pi^2)/(3\pi^4)\). Numerical quadrature for \(n=3,4,5,6,7,8\) agrees with the closed recurrence. No external code or nonstandard lemma is required.

Limits: no full joint law, no all-\(n\) covariance-sign theorem, and no finite-\(n\) optimal estimator are asserted. The full text of Bélisle (2011) was not accessible, so that comparison remains a residual risk. Independent audit and independent validation remain unperformed.