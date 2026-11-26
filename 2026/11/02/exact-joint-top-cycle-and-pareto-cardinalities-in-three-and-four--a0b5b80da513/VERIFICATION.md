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

# Verification

Run `python3 verify.py` (Python 3.10 or newer, standard library only) alongside `joint_counts.csv`. The program enumerates all 13,824 normalized four-agent profiles, uses exact signed votes and graph searches, and weights each outcome by 24. It checks equality of the complete 35-cell histogram against the CSV, Pareto inclusion at each normalized profile, and the reported aggregate counts and moments. `VERIFY_OK 35 331776` confirms those checks in a replay. The finite coverage argument is in `RESULT.md`.
