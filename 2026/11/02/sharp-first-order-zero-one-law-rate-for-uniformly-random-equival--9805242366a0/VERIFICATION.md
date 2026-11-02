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

Run `python3 checker.py` with Python 3 and its standard library. The script reconstructs Bell numbers two ways, exhaustively enumerates block-size profiles through eight worlds, checks exact numbers of singleton blocks against a second recurrence, and compares exact small-singleton probabilities with the predicted saddle factor for n=80,160,320. It prints `ALL_CHECKS_OK` when every assertion passes. These finite checks test only combinatorial identities and local approximations; the all-size first-order equivalence and asymptotic claims are proved analytically in `RESULT.md`.
