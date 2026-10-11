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
# Reproducible checks and limits

The companion `verify_cycle.py` requires Python 3 standard library only and prints `CHECK_OK` after fourth-order Runge–Kutta cross-section tests for positive and negative rescaled parameters, numerical beta constants, positive multiplier sign and parity. The analytical arguments in `RESULT.md` establish the assertions for a whole punctured parameter interval; numerical checks by themselves cannot certify infinitely many parameters, the implicit-function hypotheses or publication priority.

A local analytic Poincaré map is justified by transversal return to the positive turning section of a regular quartic oval, where the original smooth polynomial vector field is nonzero. The leading energy displacement was independently derived by direct integral over this oval, and the multiplier coefficient was checked both through energy differentiation and direct divergence integration. There is no separate external/independent audit or formal theorem prover record.
