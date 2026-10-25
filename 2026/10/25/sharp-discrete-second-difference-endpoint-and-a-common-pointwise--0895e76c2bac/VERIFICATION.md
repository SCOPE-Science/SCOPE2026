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

# Reproducibility and verification

Run `python checks/verify.py` with Python 3 (only the standard library is needed). The script checks all support lengths from 1 through 160 using exact rational arithmetic. It reports 26,880 successful assertions. The calculations verify both boundary moments, the second-difference reconstruction, symmetry, positivity, each individual convex-chord certificate, and all four closed forms. They corroborate but do not replace the all-dimension convexity and polynomial-summation proof in `RESULT.md`.

No independent scientific audit or external certification has been performed. Priority is not conclusively certified against all unindexed earlier literature; the proof addresses only second differences with zero boundary extension and a coefficient sup norm.
