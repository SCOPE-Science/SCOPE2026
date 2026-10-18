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

The standalone `CHECK.py` uses Python standard-library numerical integration of the original planar quadratic forms, not the closed area expression; it performs 248 comparisons for several axes, scales, and orientations. Numerical checks are supportive only: the exact proof, boundaries, and singular asymptotics appear in `RESULT.md`.
