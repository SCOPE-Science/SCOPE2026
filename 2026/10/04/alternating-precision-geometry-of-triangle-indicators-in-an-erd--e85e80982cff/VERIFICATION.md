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

It reconstructs the Johnson neighbor-distance counts directly from three-subsets and verifies the four rows used to reduce the matrix inverse.

For rational edge probabilities it verifies the four inverse equations, the factor signs, and the exact formulas for all three overlap-class linear partial correlations.

It also materializes the complete distance-class inverse for several graph sizes and multiplies it by \(I+rA\) exactly entry by entry.

Finite replay is supplementary. The universal theorem is the covariance calculation and four-equation derivation in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK neighbor_class_checks=160 inverse_equation_checks=1900 sign_checks=3800 partial_formula_checks=2850 full_product_checks=35451`.
