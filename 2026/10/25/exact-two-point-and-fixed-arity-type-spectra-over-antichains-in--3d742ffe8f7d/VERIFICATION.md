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
# Reproduction and scope

Run `python verify_antichain.py` in a directory containing that file. `verification_output.txt` records the actual run and can be compared with rerun stdout. The verifier enumerates full strict posets directly and independently implements two separate methods for counting compatible parameter patterns. It validates the structural inclusion-exclusion identity through all labelled three-point tuple posets, seven selected four-point tuple posets, and the two-point closed form against direct checks for base sizes zero through five and state propagation through thirty. Exact integer arithmetic is used.

These are finite tests, not an exhaustive computation over all tuple arities or all base sizes. The general theorem is mathematical and follows from the disjointness bijection and inclusion-exclusion proof in `RESULT.md`. No independent audit was performed.
