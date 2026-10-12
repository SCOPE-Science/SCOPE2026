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

The proof is analytic. The accompanying checker independently reconstructs each binary search tree from its insertion permutation and uses exact rational arithmetic.

It exhaustively enumerates all permutations for
\[
1\le n\le9,
\]
which is
\[
\sum_{n=1}^{9}n!=409113
\]
insertion sequences. For each size it verifies the exact leaf and path-length means, the covariance, and the leaf variance. For every \(n\ge4\) in the exhaustive range it also verifies the least-squares slope.

A separate recurrence replay computes covariance and leaf variance recursively through size \(300\) from conditional subtree moments before comparing with the claimed closed forms.

Finite enumeration and finite recurrence replay are supplementary. The proof for arbitrary \(n\) is the split-induction argument in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK permutations_checked=409113 mean_checks=18 covariance_checks=9 variance_checks=9 slope_checks=6 recurrence_checks=598`.
