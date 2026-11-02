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

Run `python3 verify.py` using Python 3.9 or later. It checks the exact two-step Jacobian polynomial and stability inequalities, constructs nonzero roots of the two sinusoidal orbit equations with Newton's method, verifies all four one-step orbit transitions, and recomputes the return multipliers and the predicted small-parameter amplitude laws. Tests cover six damping values and several sufficiently small positive offsets.

The program is evidence for numerical consistency only; the full range of damping parameters and the nonexistence/uniqueness assertions follow from the proof in RESULT.md. No infinite claim is certified by a finite computation. The final scientific assessment is self-review only; independent audit has not been performed.
