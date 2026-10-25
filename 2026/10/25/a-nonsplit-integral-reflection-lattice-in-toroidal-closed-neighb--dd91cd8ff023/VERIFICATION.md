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

# Verification and reproducibility

`VERIFY.py` is self-contained Python 3. Execute `python3 VERIFY.py` with no external libraries. It reconstructs all closed-neighborhood simplices; checks every descending unique free-face collapse and the exact residual square-boundary complex; and independently checks oriented two-disk transformations for the two coordinate reflections and both unit translations. The six pairs of side lengths (5,5), (5,6), (6,5), (6,6), (5,7), (7,5) passed, involving 1,337 elementary collapse pair tests and 1,528 signed face/disk-action comparisons.

The general integral chain computation and the exact extension-order argument are proved in RESULT.md. The finite tests do not extrapolate or certify the infinite result. Independent validation has not been performed.
