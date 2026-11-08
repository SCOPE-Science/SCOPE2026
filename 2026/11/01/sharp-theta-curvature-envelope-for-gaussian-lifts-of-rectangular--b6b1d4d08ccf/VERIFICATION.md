---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed quotient-Hessian as four t^2 times discrete-Gaussian shifted variance and equality at shift zero (with the established shifted-covariance inequality cited from Letwin--Reis--Rothvoss). Differentiation gives A prime=4t(2m-tv); Jacobi transform controls t<=2, cumulant comparison controls 2<=t<=3, tail bound gives negativity beyond 3, establishing one maximizer. Independent high-precision theta sums found t*=2.353015289448131648865384 and A*=3.550276615992224481628183. Product Hessian diagonal gives minimum of A(t_j)/a_j^2 and rigidity on longest sides. Numerical check does not prove the imported shift inequality or the global analytic signs; proof cites explicit inequalities.

## originality

PASS

Best-of-knowledge: statement-level comparison with identifiable published results does not show the exact asserted new contribution to be covered; non-access and unindexed-priority uncertainties are explicitly retained.

## value

PASS

A sharp constant and full equality classification for a natural periodized Gaussian construction, including sensitivity to the longest lattice side, refines a general existence theorem into a concrete optimally tuned family. Claim explicitly excludes arbitrary Gaussian covariance and arbitrary non-Gaussian lifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
