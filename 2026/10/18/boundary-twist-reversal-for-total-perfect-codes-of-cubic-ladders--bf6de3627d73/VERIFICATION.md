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

The proof uses the two lifted recurrences, exhaustion of their binary solutions and the closing conditions. `python3 CHECK.py` uses exact covers of the vertex set by open neighborhoods to enumerate individual codes, and compares them against the classification for 26 labeled graph profiles with widths from 3 to 15. The finite computation does not prove the all-width result or establish priority.
