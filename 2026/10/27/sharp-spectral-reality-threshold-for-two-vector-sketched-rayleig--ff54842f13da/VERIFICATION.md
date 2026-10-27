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

# Verification and limits

The self-contained `verify.py` runs with Python 3's standard library. Execute `python3 verify.py`; its final success marker is `VERIFICATION_OK`. The checker forms the sharp positive-definite witness with exact rational arithmetic, verifies the sketch Gram identity and sketched two-by-two matrix, and tests the perturbation and Gram-mixing bounds on 20,000 seeded finite cases. The proof in `RESULT.md`, not this finite test suite, establishes the general quantified theorem.

The check is exact for the displayed rational witness and floating-point for the seeded stress cases. It does not constitute finite-precision eigensolver stability, statistical probability bounds, an exhaustive sweep of all admissible matrices, or independent audit.
