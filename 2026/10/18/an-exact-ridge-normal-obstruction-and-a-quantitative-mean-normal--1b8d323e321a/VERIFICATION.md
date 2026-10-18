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

The embedded `verification/check_ridge.py` is a standalone Python 3 program using NumPy and the standard library. Execute it with `python verification/check_ridge.py` after extracting the embedded files. It creates 80,000 uniform interior samples for each of 15 sheared-simplex configurations in dimensions 2–6, tests facet-normal signs and ridge-foot inequalities, and compares observed probability with the exact formula using a tolerance of 0.013. It also tests all proper faces for twenty uniformly sampled points of each right-coordinate simplex in dimensions 2–6, and verifies 48 rational identities exactly. The checker printed:

`PASS: 1204808 checks; sheared ridge normal probabilities, complete right-simplex active-face census, rational identities`

These finite tests validate formulas and implementation consistency only; the all-dimensional assertion follows from the symbolic two-normal Gram identity, the Dirichlet-ratio integration, the positive-inverse Gram argument, and the explicit shear construction in RESULT.md. No independent external audit has been performed.
