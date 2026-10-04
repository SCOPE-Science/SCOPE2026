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

For random positive rational probability profiles and strict rational supports normalized to range one, it verifies
\[
\operatorname{Var}(X)\ge L(\mathbf p)
\]
and, for at least three atoms,
\[
\operatorname{Var}(X)<U(\mathbf p).
\]

It separately verifies exact equality for all tested two-point laws and for the explicit three-point lower extremizer
\[
x_2=\frac{p_m}{p_1+p_m}
\]
under endpoint normalization.

The checker also verifies the equal-mass formulas and follows explicit strict-support rational sequences toward both the lower and upper boundary configurations.

Finite replay is supplementary. The universal theorem follows from the conditional-variance decomposition and the cumulative-cut \(L^2\) argument in `RESULT.md`.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK random_lower_checks=30000 random_upper_checks=25620 two_point_checks=4380 three_point_lower_checks=10000 equal_mass_checks=198 lower_path_checks=6000 upper_path_checks=6000`.
