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

The proof is analytic. The accompanying checker uses exact rational arithmetic for the determinant identity and normalized support formula.

For random positive rational mass triples and rational ordered three-point supports it verifies
\[
\kappa-\gamma^2-1
=
\frac{
abc\,
(x_2-x_1)^2
(x_3-x_1)^2
(x_3-x_2)^2
}{
\operatorname{Var}(X)^3
}.
\]

It also verifies the variance formula after normalizing the support to \((0,r,1+r)\), checks the derivative polynomial by exact algebraic evaluation at rational \(r\), verifies its sign change around the unique positive numerical root, and checks the equal-mass value \(1/2\) for the strict Pearson gap.

Root location in the checker is numerical only and is not used as the proof of uniqueness. Uniqueness follows analytically from the coefficient sign pattern and endpoint signs in `RESULT.md`.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK determinant_checks=48000 normalized_checks=48000 derivative_checks=24000 optimizer_checks=96000 equal_mass_checks=6`.
