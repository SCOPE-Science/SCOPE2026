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

## Reproducibility and scope

The analytic certificate is the complete Laplacian eigenspace decomposition and strict convex minimization in `RESULT.md`. A finite independent matrix assembly implementation is provided as `verify_spectral.py`. Execute `python verify_spectral.py` with Python and NumPy; it checks \(156\) integer parameter pairs, the claimed unit gap, trace-to-budget identity, agreement of two budget expressions, and finite scalar perturbations. Full-parameter correctness follows from the analytic proof, not the finite computation.

Checks do not establish independence or full-text novelty. The mathematical scope is \(k\ge2\), \(m\ge1\), \(B>0\) with all allowed edge weights nonnegative. Literature coverage risk is stated separately in the review.
