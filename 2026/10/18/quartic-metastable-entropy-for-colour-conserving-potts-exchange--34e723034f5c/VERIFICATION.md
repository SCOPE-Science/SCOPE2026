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

# Reproducibility checks

Run `python3 artifacts/verify.py` using Python 3 standard library. The script independently enumerates spin exchanges and re-evaluates the total Potts energy for selected small rings, reconstructs the full triple-state transfer matrix, checks exact finite traces, constructs the quotient matrix, and validates the characteristic polynomial using exact integer determinants.

The exact characteristic-polynomial tests use six distinct integer alphabet sizes and nine distinct integer spectral values. Determinant and proposed polynomial have degree at most five separately in each variable, so these values certify their formal identity by interpolation. The analytic path proof of primitivity and the Perron-Frobenius theorem establish the all-size asymptotic, not the finite tests.

No external independent audit or independent validation was performed.
