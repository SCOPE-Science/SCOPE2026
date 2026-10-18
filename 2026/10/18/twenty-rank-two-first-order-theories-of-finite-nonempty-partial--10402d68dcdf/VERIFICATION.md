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

Run `python3 verify.py` with Python 3 and no external dependencies. The program enumerates posets by adjoining a new maximal point above every order ideal, checks the natural-label counts through size six, independently computes the set of pointed one-round relation types, verifies the 20 rank-two signatures, and compares representatives by explicit two-round game responses. It prints PASS on success.

The mathematical upper bound for *all* finite nonempty posets follows from the ordinal-sum decomposition of incomparability components, proved in RESULT.md, and not from any finite computation. No independent audit has been performed.
