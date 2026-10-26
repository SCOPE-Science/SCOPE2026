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

The conditional Gaussian identity is exact: for every fixed \(v\in(0,\tfrac12)\), the pair-sum variance is \(1-2v+2v=1\), and the pair-difference characteristic function conditional on \(V=v\) is \(e^{-vt^2}\). The script `verify_pair_sum_family.py` checks the exact rational moments, marginal variance, pair covariance, and fourth-cumulant difference for \(\rho_1=\delta_{1/4}\) and \(\rho_2=\tfrac12\delta_{1/8}+\tfrac12\delta_{3/8}\). These checks are arithmetic corroboration; the distributional claims follow from the analytic proof in `RESULT.md`.
