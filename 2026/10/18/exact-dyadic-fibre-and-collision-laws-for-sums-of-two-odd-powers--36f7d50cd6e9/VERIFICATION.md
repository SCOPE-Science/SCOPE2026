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

# Reproducibility

Run `python3 verify.py` from the directory containing this document and the verifier. The code depends only on the Python standard library and counts the image of the \(d\)-th power map modulo \(2^n\), then convolves the resulting exact integer counts. It independently constructs the predicted finite-depth count law and checks every target and its normalized collision count using exact rational arithmetic.

The executable replay completed with `VERIFIED 4600 exact target counts across 36 cases` for \(d\in\{3,5,7,9\}\). The infinite moment cutoff and the recurrence for arbitrary odd exponents follow from the mathematical argument, not bounded enumeration. No external certification or independent review has occurred.
