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

## Reproducibility

The accompanying `verify.py` script requires Python 3 and no external libraries. Execute `python3 verify.py` to check the exact finite-ring Fourier block against a numerical derivative of the fully specified nonlinear mean-field equations, its trace and determinant, discrete-mode instability criteria, the five-site threshold and boundary examples. In the reviewed package it reported `PASS 4917 deterministic consistency assertions`.

The checker is finite and numerical: it is not an exhaustive proof across all sizes and real parameters. The analytical determinant, monotonicity and quadratic-root arguments in RESULT.md establish the universal theorem. No independent audit or external certification has been performed.
