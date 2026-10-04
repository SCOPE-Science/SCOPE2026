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

The proof is analytic. The accompanying checker uses exact rational arithmetic for all algebraic identities and squared inequalities.

For random rational probability vectors, sample sizes, and strict rational support vectors, it verifies:

- the exact gap-spanning formula for \(\mathbb ER_N\);
- the extreme-order probability formula and the equivalent range-score covariance identity;
- the lower squared inequality from the minimum cumulative-cut constant;
- the upper squared inequality from the range-score variance;
- strict increase of the range-score values;
- exact upper equality when the parent support is affine to the range score;
- strictness of the lower bound for at least three support atoms;
- convergence of one-dominant-gap families to the lower endpoint.

For small dimensions it directly enumerates all iid sample tuples and confirms the expected sample range.

Finite replay is supplementary. The universal result is the analytic argument in `RESULT.md`.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK gap_checks=18000 extreme_checks=18000 covariance_checks=18000 lower_checks=18000 upper_checks=18000 score_order_checks=18000 upper_equality_checks=18000 lower_strict_checks=15048 boundary_checks=15048 direct_enum_checks=600 binary_checks=2952`.
