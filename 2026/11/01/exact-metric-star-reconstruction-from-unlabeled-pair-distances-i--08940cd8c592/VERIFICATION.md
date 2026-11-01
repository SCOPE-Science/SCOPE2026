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

The exact density identity and constructive reconstruction are proved in RESULT.md. Run `python verify.py` with Python 3 standard library; the independent arm-conditioning and hinge formulas agree exactly in rational arithmetic, and reconstruction passes collision/tie tests. The program verifies density normalization, origin slope, hidden-kink recovery and seeded arclength sampling. Finite tests support implementation consistency but do not prove the all-real-length theorem. No independent audit was performed.
