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

The proof is analytic. The accompanying checker uses exact rational arithmetic and exhaustive permutation enumeration.

For every \(2\le n\le8\), it enumerates all permutations and computes cycle count, every ordinary inversion indicator, total inversion number, and same-cycle relations.

It checks every local covariance against
\[
-\frac{2(j-i)-1}{2n(n-1)},
\]
checks the exact total covariance, and verifies the conditional same-cycle probabilities used in the proof.

It also verifies the cycle-count and inversion variances and the exact squared correlation formula.

The finite replay is supplementary. The all-\(n\) theorem is the image-swap involution and completion count in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK permutations_checked=46232 local_cov_checks=84 completion_rule_checks=3192 total_cov_checks=7 variance_checks=14 correlation_checks=7`.
