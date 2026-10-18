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

# Verification scope

Execute `python verify.py` with a standard Python 3 interpreter. The script enumerates all labeled strict partial orders on one to five elements by assigning pair orientations and filtering transitivity. It computes the derivation and selected minimal objects directly from incidence and compares all singleton conditionals with the predicted formulas. It also checks the explicit three- and five-object orientation collisions and the short-premise lower-bound constructions at sizes three through eight.

The completed execution reported 4,473 partial orders and 139,062 directly evaluated incidence-premise cases, and returned `VERIFY_OK`. The enumeration is exhaustive only through five objects; the all-size mathematical claims are justified by the proof, not by extrapolating the enumeration. The five-point nonisomorphism is additionally established using the unique three-valent vertex in each Hasse diagram.

The arithmetic and finite code checks do not establish publication priority or independent validation. They are distinct from external audit, which has not been performed.
