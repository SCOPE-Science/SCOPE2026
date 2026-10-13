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

The proof is analytic. The accompanying checker performs an exact-rational exhaustive replay over every Prüfer word for
\[
3\le n\le8.
\]

For each word it reconstructs the occupancy of the distinguished label and the total number of absent labels, which are exactly the fixed-vertex degree minus one and the tree leaf count.

It verifies the marginal leaf mean, exact zero first covariance, every admissible factorial covariance, the full conditional-mean profile, and the mixed generating identity at several rational values of \(z\).

The exhaustive replay covers \(280391\) Prüfer words.

Finite enumeration is supplementary. The all-\(n\) theorem is the exact Prüfer/multinomial calculation in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK words_checked=280391 leaf_mean_checks=6 first_cov_checks=6 factorial_cov_checks=21 conditional_checks=27 pgf_checks=24 sign_checks=15`.
