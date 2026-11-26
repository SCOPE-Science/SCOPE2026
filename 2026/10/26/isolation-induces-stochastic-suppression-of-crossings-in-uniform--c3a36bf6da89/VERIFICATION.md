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

# Reproducibility record

Run `python verify.py` with Python 3.10 or later in the directory with the script. The checker enumerates uniform matchings, uses direct endpoint interlacing to compute counts, and checks the crossing-count distributions of the two-arc splits, the asserted tail inequalities, and strictness for the crossing-count test function for two through six chords. All checks use integer arithmetic on finite inputs; the general inequality and the strictness for every strictly increasing test function follow from the coupling proof in `RESULT.md`.
