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

# Reproducibility and mathematical limits

Run `python verify.py` with Python 3 and no third-party dependencies. The embedded script independently enumerates multinomial allocations for small instances, derives the mixed probabilities with exact rational arithmetic, verifies the strictly decreasing adjacent ratio for many parameters, and compares finite critical sign intervals and limiting constants. It completed 10,634 deterministic assertions.

The exact multinomial joint moment, the adjacent-sample-size ratio, the classification of the double discriminant zero, and the uniform second-order expansion are the decisive mathematical steps, proved analytically in `RESULT.md`. Finite computations alone do not certify an infinite family or rule out equivalent historical statements. The statements here have not received an independent audit.
