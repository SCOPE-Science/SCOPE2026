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

# Verification

The proof is in `RESULT.md`; the replay program is `artifacts/verify.py` and uses only Python's standard library. Execute `python3 artifacts/verify.py` after extraction. It passed 448491 exact assertions, checking enumerated Prüfer-word populations through order 8 and symbolic-number identities/inequalities through order 33.

Finite exhaustive checks cannot replace the infinite-size proof. The proof's nonstandard input is the strict Stirling ratio inequality established by real-rootedness and recurrence, followed by the one-crossing argument. No independent assessment has been performed.
