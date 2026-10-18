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
# Algebraic verification

Run `python verify.py` (Python 3, SymPy). The script reconstructs the killed-diffusion and reflecting boundary-value moment functions, verifies all boundary data, expands an independent Laplace-transform formula through order two, and checks the asserted sign transition for twelve rational parameter/holding-variability combinations. Exact symbolic identities hold in the polynomial fraction field, with analytic interpretation justified by the regenerative proof in `RESULT.md`.

Computations do not establish anything about higher-dimensional targets, dependent holds, or infinite hold variance. No independent audit has been performed.
