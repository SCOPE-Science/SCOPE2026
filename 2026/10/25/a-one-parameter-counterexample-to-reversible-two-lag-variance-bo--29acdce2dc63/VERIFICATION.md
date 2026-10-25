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

The analytic proof in `RESULT.md` establishes the universal statement for every real parameter `0 < alpha < 1`. The standalone checker uses exact rational arithmetic for four sample parameters, confirms the transition matrix row sums and uniform stationarity, computes the first two autocorrelations directly from matrix powers, and checks the exact gap identity at those points. The sample checks are not used as a substitute for the analytic proof.

The checker does not establish novelty, and it does not certify any result independently. The stated scope does not include general nonreversible chains or finite-sample estimator guarantees.
