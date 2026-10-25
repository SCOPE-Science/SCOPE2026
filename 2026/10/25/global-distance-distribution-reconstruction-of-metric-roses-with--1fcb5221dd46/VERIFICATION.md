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

# Verification record
The full density identity, loop jump formula, origin-slope identity, and distributional signed-atom induction were reconstructed symbolically. The included `rose_verifier.py` uses Python standard-library rational arithmetic to replay 4,361 exact finite configurations (including repeated lengths and cancellations) and five exact normalization checks. Piecewise-polynomial density integration was independently tested on five configurations with integral equal to one numerically. The checks cannot establish the theorem beyond the explicit analytic argument, and they do not independently certify originality.

No independent audit was performed. All graph edge lengths must be positive; the single-junction assumption is essential for the convolution decomposition.
