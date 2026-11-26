---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

# Verification

The exact value for every \(K_{3,n}\), \(n\ge3\), follows from the two arguments in `RESULT.md`. The companion `verify.py` checks the four-color star construction for \(3\le n\le100\). It also checks three-colorability on \(1\le m\le n\le6\), rejecting improper vertex colorings and testing the uniquely forced edge assignment for each proper vertex coloring that it considers. The search stops at the first successful assignment on positive instances; a negative instance exhausts all assignments. Neither finite test is used as a proof for all \(n\).
