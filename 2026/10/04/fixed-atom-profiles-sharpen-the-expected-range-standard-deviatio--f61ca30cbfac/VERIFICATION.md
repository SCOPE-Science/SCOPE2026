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

The theorem is analytic. The accompanying checker uses exact rational arithmetic.

For random rational probability profiles, rational strictly increasing supports, and sample sizes at least three, it verifies:

1. the maximum-minus-minimum coefficient formula for the expected range;
2. the zero-sum coefficient identity;
3. strict increase of the cell-average scores \(z_i\);
4. the sharp weighted Cauchy--Schwarz inequality;
5. exact equality on the support \(x_i=z_i\);
6. the closed form for the unrestricted squared constant;
7. the exact cellwise \(L^2\) deficit identity and its strict positivity.

The checker expands \(K_n'\) as a rational polynomial and integrates its square exactly, so the deficit verification does not rely on numerical quadrature.

Finite replay is supplementary. The proof in `RESULT.md` establishes the universal statement.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK formula_checks=18000 monotonicity_checks=71616 bound_checks=18000 equality_checks=54000 deficit_checks=125616 global_norm_checks=18000`.
