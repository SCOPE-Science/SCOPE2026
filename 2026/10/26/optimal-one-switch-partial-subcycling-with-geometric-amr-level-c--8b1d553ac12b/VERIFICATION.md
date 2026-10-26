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

# Reproduction

Run `python verify.py` with Python 3 (standard library only) from the directory containing `verify.py`. The finite program enumerates all adjacent binary patterns and exact rational costs for 1,790 combinations of hierarchy depth, refinement ratio, geometric weights and overhead. Equality thresholds are tested directly, so the minimizer set is checked including ties. The expected first output line is `EXACT_RATIONAL_ENUMERATION_PASS 1790`. This tests finite cases only; the general all-depth claim rests on the inversion-swap and telescoping proofs in `RESULT.md`.

No independent audit or validation is represented by this report.
