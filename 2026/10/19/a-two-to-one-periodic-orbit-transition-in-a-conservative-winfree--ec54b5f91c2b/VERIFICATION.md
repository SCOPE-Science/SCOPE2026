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

# Reproducibility and verification

Use Python 3's standard library; run `python3 verify_triad.py` in the directory containing this file and the verifier. The program reconstructs both the original and transformed phase equations from independent formulas, checks their equality for 1,000 deterministic sampled phase states, checks 30 stationary-point Hessians, and verifies the key exact rational polynomial certificates at three parameter values. Its successful output begins `VERIFY_OK`.

The analytic all-parameter proof is in `RESULT.md`. Exact root exhaustiveness comes from the circle-level quadratic and the positive factor \(1+\varepsilon-2\varepsilon\cos t\); it is *not* inferred from sample grids. The 1- or 2-component result follows from the absence of other critical values and compact regular-level continuation, not from numerical contour plots. Python floating-point validation does not certify a universal identity independently of the proof.

There has been no independent audit; the listed checking is reproducibility support for the self-review.
