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

# Reproducible verification

Execute `python3 verify_integral_action.py` with Python 3. The program enumerates the oriented relative-cell chains and tests the full action of every leaf permutation and both hub-swap choices, for 2 through 5 leaves. The exact coefficient comparisons pass. These finite checks verify conventions; the stated integral theorem for all parameters follows from the proof in RESULT.md. No independent mathematical audit has been performed.
