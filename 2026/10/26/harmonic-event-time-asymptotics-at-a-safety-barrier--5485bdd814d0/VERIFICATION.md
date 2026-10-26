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

Run `python verify.py` with Python 3 and no third-party dependencies. The script computes 2,000 successive roots of the exact trigger equation using the exact held-flow identity, and checks that the barrier margin remains positive and decreases and that each trigger residual is small. These finite checks do not establish the asymptotic limits; those follow from the analytic argument in `RESULT.md`. No independent audit or independent validation has been performed.
