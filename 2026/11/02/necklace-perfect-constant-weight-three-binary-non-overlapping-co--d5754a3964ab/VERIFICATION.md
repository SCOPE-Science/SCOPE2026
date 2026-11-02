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

# Reproducibility

Run `python3 verify.py` with Python 3 and no external libraries. It directly enumerates the specified weight-three binary code and all primitive rotation classes for lengths 4 through 40, compares proper-prefix and proper-suffix sets, and checks bijection of the constructed words to primitive necklace classes. The expected terminal marker is `VERIFY_OK`.

The published mathematical proof handles arbitrary lengths; the finite run verifies definitions and selected arithmetic, not unbounded quantifiers. No independent mathematical audit or external certification is represented.
