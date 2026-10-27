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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 and no third-party packages. The script evaluates the six candidate first-merge slopes and the entropy/rate values for the greedy partition and its strict dominator. Expected output begins with `VERIFY_OK`.

The script's floating-point calculations are consistency checks only. The proof in `RESULT.md` supplies the exact entropy identities, the strict inequalities, and the minimality argument. No independent audit or external validation is claimed.
