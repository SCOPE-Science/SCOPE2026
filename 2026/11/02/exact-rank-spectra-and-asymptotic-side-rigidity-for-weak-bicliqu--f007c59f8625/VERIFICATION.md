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

# Verification record

Run `python verify.py` in a directory containing this file and the script. The script exhaustively generates every total map in each of nine finite configurations; tests the idempotence and weak edge condition independently; and compares each complete rank distribution to the stated closed formula. A successful run prints `VERIFY_OK` after all checks. The mathematical proof, not the finite enumeration, establishes the theorem over all positive side sizes and its large balanced-size asymptotic. Independent external validation has not been performed.
