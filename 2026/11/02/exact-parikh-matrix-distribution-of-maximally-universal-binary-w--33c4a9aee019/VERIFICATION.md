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

Run `python verification.py` using Python 3.9 or newer. The accompanying `verification_output.txt` records the exact output. The program independently compares all \(\binom{2k+s}{k}\) binary words against the coefficient formula for \(1\le k\le7\), \(0\le s\le4\) and additionally checks 160 algebraic parameter cases. The mathematical proof for arbitrary integer \(k,s\) is in `RESULT.md`.

All polynomial operations are exact integer arithmetic. The program does not verify independent publication priority, cannot replace proof of an infinite statement, and makes no independent-audit claim.
