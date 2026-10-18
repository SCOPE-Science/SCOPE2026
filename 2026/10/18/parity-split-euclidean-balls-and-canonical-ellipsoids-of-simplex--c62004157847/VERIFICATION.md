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

# Verification

The proof is analytical and all-dimensional. `checker.py` is the included independently coded, reproducible finite consistency checker; it requires Python 3 standard library only. Invoke with `python3 checker.py`.

Checks for each \(m\in\{3,4,\ldots,17\}\): independently reconstruct the oriented boundary incidence Gram matrix and verify the alternating-sign Laplacian exactly. For even sizes, verify the claimed full facet-normal family and both squared-radius formulas with exact rational arithmetic. For odd sizes, verify majority vertices' equal squared distances, strictly positive and equal minority clearances, and exact rational barycentric gradients. Odd positive-radical incenter checks use floating-point tolerance.

The computational range is finite and does not establish universal quantification; the accompanying proof supplies that. No independent mathematical audit has been performed.
