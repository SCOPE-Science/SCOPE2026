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

The proof is analytic. The accompanying checker exhaustively enumerates every permutation for
\[
2\le n\le9.
\]

For each \(n\), every record position \(2\le j\le n\), and every fixed-point position \(1\le i\le n\), it reconstructs \(I_i\) and \(R_j\) directly and verifies the three-case covariance kernel using exact rational arithmetic.

It also verifies the aggregate covariance, the conditional mean under a record event, the total fixed-point/record-count covariance, and both marginal variances.

The exhaustive replay is supplementary. The all-\(n\) proof is the conditional exchangeability argument in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK permutations_checked=409112 local_cov_checks=240 aggregate_cov_checks=36 conditional_checks=36 total_cov_checks=8 variance_checks=16 sign_checks=33`.
