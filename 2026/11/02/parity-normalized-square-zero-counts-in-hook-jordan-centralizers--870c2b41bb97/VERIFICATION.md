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

# Direct verification

Command: `python verify.py` (Python standard library).

Observed successful output:

`VERIFY_OK: 13 complete hook-centralizer square censuses; 9 independent square-zero block-rank censuses; parity normalization and strict gaps over five field orders`

The verifier enumerates centralizing matrices in their module-homomorphism parametrization and tests squares by **direct full matrix multiplication** over prime fields and \(\mathbb F_4\). This path does not implement the proof's four coefficient constraints. The independent block-rank census enumerates every \(r\times r\) matrix and calculates rank by Gaussian elimination. The sample cases and ranges are specified in `RESULT.md` and the executable.

These are finite reproducible tests, not an exhaustive verification of all field orders and dimensions. The universal claim rests on the written algebraic proof. No independent mathematical audit has been performed.
