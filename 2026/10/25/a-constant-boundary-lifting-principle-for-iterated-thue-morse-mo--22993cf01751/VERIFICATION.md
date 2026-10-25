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

# Verification

Run `python verify.py` using Python 3. This enumerates all factors and all occurrence intervals in the finite examples, verifies the strict two-endpoint condition for marked cuts, and tests the resulting scaled position sets on iterated images. No external packages or external files are needed.

Finite enumerations do not establish universal quantified claims. The theorem itself is proved by a block-induction argument in `RESULT.md`. In particular, the exact requirement is that an occurrence spans both sides of a cut, not merely that a factor's coverage includes a designated endpoint. No independent audit has been performed.
