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

The proof is analytic. The accompanying checker uses exact rational arithmetic.

For random finite probability vectors and sample sizes it verifies:

- the exact diagonal and off-diagonal covariance formulas;
- strict negativity of every off-diagonal covariance;
- row-sum zero and rank \(m-1\) when \(n=1\);
- positivity of every leading principal minor when \(n\ge2\);
- strict positivity of every entry of the exact rational inverse when \(n\ge2\);
- negativity of every full-order linear partial correlation sign implied by that inverse.

For small models, the checker also enumerates the complete iid sample space, computes each occupancy pattern probability exactly, and reconstructs the covariance matrix directly. This independently verifies the closed formula used by the matrix tests.

Finite replay is supplementary. Positive definiteness and inverse positivity are proved for all finite positive probability vectors in `RESULT.md`.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK formula_checks=69126 offdiag_checks=46630 rank_one_draw_checks=3524 pd_minor_checks=19612 inverse_positive_checks=100838 partial_sign_checks=40613 enumeration_checks=4707`.
