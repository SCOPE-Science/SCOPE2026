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
# Verification protocol

Run `python3 verify.py` with Python 3 and no external dependencies. The checker reconstructs the regular paperfolding sequence using the odd-part rule and tests every prefix recurrence and transition identity for all starts up to sixteen times the factor length, at factor lengths \(8,16,\ldots,4096\). It also cross-checks full ordered-bigram profiles and all twelve explicitly predicted witnesses. Successful execution prints `VERIFY_OK`.

The infinite proof is contained in `RESULT.md`. These finite tests identify possible mistakes in the construction but do not certify untested lengths or replace proof of the universal claims.
