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

# Reproducible verification

Execute `python verify.py` with the Python standard library. It prints a reproducible assertion count and the exact rational bracket for the unique optimizer. The diagnostic script checks the finite coefficient exceptions, rational exponential sign enclosures, and the defining objective independently of its derivative representation.

The proof for all coefficients past the finite exceptions is the displayed analytic inequality and induction in `RESULT.md`, not an extrapolation from the diagnostic integer tests. Likewise, numerical root finding is only illustrative: the endpoint signs are enclosed by exact rational arithmetic. The computed decimal for the optimal scale is approximate, not an externally certified rounded value. Independent mathematical auditing has not been performed.
