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

The proof in `RESULT.md` is analytic.

`artifacts/verify_persistent_debiasing.py` exhaustively enumerates all fresh subsets of a rational vector population and checks the expectation, finite-population variance, interpolation MSE, oracle interpolation weight, and a \(50\%\)-overlap variance factor in exact rational arithmetic.

The finite enumeration is supporting evidence only. The universal formulas follow from the inclusion-probability calculation and convex quadratic optimization in the proof.
