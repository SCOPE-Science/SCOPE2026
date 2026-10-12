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
# Verification scope

Run `python verify.py` with Python 3. It uses only the standard library and exact rational arithmetic. The reported `VERIFY_OK` confirms 32,059 finite-spectrum tests (including deterministic grid and pseudorandom rational examples), eight perfect-square upper-bound equality instances, and three frozen-preconditioner stationary-feedback examples.

The script cannot independently establish maximization over arbitrary real probability measures or the exact irrational condition-number limit; those are proved using the compactness/first-variation/endpoints argument and rational approximation in `RESULT.md`. No claim of independent audit or third-party certification is made.
