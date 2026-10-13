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

The analytic proof uses only one-step conditional expectations under degree-proportional attachment.

The packaged checker constructs the exact law recursively through size \(9\) by aggregating all reachable degree sequences with rational probabilities. For each \(n\) it reconstructs \(D_n\), \(L_n\), \(\mathbb E[D_nL_n]\), and the event that the distinguished initial vertex remains a leaf. It checks the closed marginal formulas, the covariance sum, and the increment identity.

The checker also evaluates the normalized exact recurrence for large \(n\) to confirm numerically the asymptotic coefficient. That numerical check is not used to prove the limit.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK aggregated_states_checked=2055 moment_checks=32 increment_checks=7 positive_covariance_checks=6 asymptotic_ratio_checks=3`.
