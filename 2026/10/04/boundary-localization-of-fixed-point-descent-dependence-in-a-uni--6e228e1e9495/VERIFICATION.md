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

The proof is analytic. The accompanying checker uses exact rational arithmetic and exhaustive enumeration.

For every \(2\le n\le9\), it enumerates all permutations and reconstructs every fixed-point indicator and every ordinary and cyclic descent indicator.

It verifies all \(240\) coordinate cross-covariances in the tested range, the endpoint/interior row sums, the equal column sums, the coordinatewise cyclic cancellations, the global covariance formulas, and the two marginal variance formulas.

The exhaustive replay covers \(409112\) permutations.

Finite replay is supplementary. The all-\(n\) theorem is the conditional symmetry calculation in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK permutations_checked=409112 local_cov_checks=240 row_sum_checks=44 column_sum_checks=36 cyclic_checks=44 global_checks=16 variance_checks=16`.
