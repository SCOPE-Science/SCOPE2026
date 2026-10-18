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

The `verify.py` program computes the actual original PDHG steps and then independently forms the scaled updates. It checks the full block matrix, eigenvalues for specified two-row correlations (including the sharp boundary), deterministic random invertible matrices, and two-step exact termination for strictly positive projected-LP targets in an explicit sufficient basin. The checker was executed from its actual embedded source before packaging and returned all assertions successful.

These tests only cover finite examples, subject to IEEE floating-point tolerance. The general spectral statement, all dimensions, boundary nondecay, uniqueness, and exact two-step properties are established by the proof in RESULT.md. No independent audit has been performed.
