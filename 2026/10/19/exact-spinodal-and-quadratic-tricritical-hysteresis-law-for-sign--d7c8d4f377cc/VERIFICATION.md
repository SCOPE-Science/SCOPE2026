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

# Verification of the mean-field phase and cusp laws

The accompanying `verify.py` uses only Python 3's standard library. Running `python3 verify.py` in the containing directory produced `VERIFIED 582 assertions`. It independently evaluates the six-neighbor flip rates and the factored polynomial for many exact rational parameters, the endpoint inward drifts, key derivative identities, tricritical fifth-order polynomial, leading cusp coefficients and zero-antagonism radical benchmark. All exact-rational identities used by the code were checked in its actual packaged path.

The continuous-parameter equilibrium classification and infinite-time decay law are not justified by finite samples: they follow from the concavity/monotonicity, endpoint, implicit-function and inverse-power arguments in `RESULT.md`. The software supplies independent reproducibility checks, not a formal proof or external certification. General finite-network claims, stochastic fluctuations and direct independent audit have not been checked and are not claimed.
