---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

Run `python3 verify.py` in this directory. The program constructs the finite digit sets and enumerates ordered pairs directly for cutoffs \(4^k\), \(0\le k\le7\). It tests the exact singleton and adjacent-pair counts against \(3^k\). These finite tests do not establish the all-\(k\) claim; that follows from the adjacent-pair recurrence in `RESULT.md`.
