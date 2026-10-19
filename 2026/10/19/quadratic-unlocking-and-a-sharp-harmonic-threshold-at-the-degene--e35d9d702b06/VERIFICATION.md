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
# Verification and proof scope

Run `python3 verify.py` in the same directory. It requires only the standard Python library. The checker verifies the two local Taylor discriminants for exact rational parameters; verifies the exact critical-endpoint identity, the elementary frequency symmetry and the maximal coefficient; and compares finite-time translation-number estimates with the derived law for sample interior and exterior values. Expected run time is short on a standard interpreter.

The exact mathematical argument is in RESULT.md. In particular, the infinite-iteration translation number and all parameter values are **not** verified by finite numerical orbits. Those are established by the completed-square positivity, local blow-up integrals and integral-clock telescoping. Numerical tests are non-certifying diagnostics. Independently checking the proof remains outstanding.
