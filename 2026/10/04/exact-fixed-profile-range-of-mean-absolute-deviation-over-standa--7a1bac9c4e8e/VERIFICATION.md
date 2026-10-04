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

The proof is analytic. The accompanying checker uses exact rational arithmetic for all inequality decisions.

For random rational probability profiles and strictly increasing rational supports it computes
\[
D=\mathbb E|X-\mathbb EX|
\]
and
\[
\sigma^2=\operatorname{Var}(X)
\]
exactly, then verifies
\[
D^2\ge L(\mathbf p)^2\sigma^2
\]
and, for \(m\ge3\),
\[
D^2<U(\mathbf p)^2\sigma^2.
\]

The checker separately verifies exact equality for every tested two-point law and for the explicit three-point lower-extremal support
\[
(-p_3,0,p_1).
\]

It also checks the equal-weight even--odd formulas and follows strict-support rational collapse sequences toward the lower and upper boundary configurations.

Finite replay supports the algebra but is not used to infer the universal result.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK random_lower_checks=30000 random_upper_checks=25620 two_point_checks=4380 three_point_endpoint_checks=8000 equal_weight_checks=198 lower_path_checks=6000 upper_path_checks=6000`.
