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
Run `python3 verification/check.py` from the package root. The standard-library program uses rational arithmetic for all comparison constants, directly checks row/column sums and square counts of the explicit extremizers in all 576 dimension pairs from 2 through 25, and checks the projected-coordinate norm identity. It additionally performs a complete ternary search in size 3 by 3; this is **not** a complete search over every real matrix in the cube section.

Expected output: `VERIFY_OK witness_and_projection_checks=4033 exhaustive_ternary_3x3_maximum=6`.

The unbounded-dimensional conclusion depends on the invariant-quadratic-form and odd-length zero-sum cube-section proofs in `RESULT.md`, not on finite enumeration. No external mathematical review was performed.
