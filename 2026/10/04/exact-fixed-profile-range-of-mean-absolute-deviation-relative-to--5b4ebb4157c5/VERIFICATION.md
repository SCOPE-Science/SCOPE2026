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

The proof is analytic. The accompanying checker uses exact rational arithmetic for the squared inequalities.

For random rational probability profiles and strict rational support vectors, it verifies:

- the identity splitting mean absolute deviation equally between positive and negative centered first moments;
- the lower squared bound
  \[
  D^2/\sigma^2\ge4p_1p_m/(p_1+p_m);
  \]
- the upper squared bound
  \[
  D^2/\sigma^2\le4\max_jP_j(1-P_j);
  \]
- exact two-point equality;
- exact three-point lower equality when the middle atom equals the mean;
- strict lower and upper inequalities for strict supports with at least four and at least three atoms respectively;
- rational lower- and upper-bound approach families;
- the equal-mass endpoint formulas.

Finite replay is supplementary. The universal theorem is the analytic argument in `RESULT.md`.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK balance_checks=48000 lower_checks=24000 upper_checks=24000 strict_lower_checks=17034 strict_upper_checks=20503 binary_checks=3497 triple_equality_checks=24000 lower_approach_checks=8000 upper_approach_checks=8000 equal_mass_checks=198`.
