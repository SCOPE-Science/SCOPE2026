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

The proof is analytic. The accompanying checker uses exact rational arithmetic wherever the random tests permit it.

For random rational probability profiles and rational strict support vectors normalized to \([0,1]\), it verifies:

- the Bhatia--Davis upper inequality;
- the exact conditional-variance decomposition;
- the lower endpoint inequality through the radical-free certificate
  \[
  \eta^2(1-a)(1-c)\ge(2-\eta)^2ac;
  \]
- strictness of the lower endpoint for at least four distinct atoms;
- exact equality for a rational three-point family whose optimal support ratio is rational;
- the equal-mass simplification.

It also constructs rational clustered supports approaching the lower endpoint and endpoint-collapsed supports approaching the upper endpoint.

Finite replay is supplementary. The universal theorem follows from conditional variance, the exact odds-coordinate optimization, and continuity.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK upper_checks=16000 lower_checks=13699 strict_lower_checks=11440 conditional_checks=41097 binary_checks=2301 equality_checks=8000 lower_approach_checks=48 upper_approach_checks=48 equal_mass_checks=48`.
