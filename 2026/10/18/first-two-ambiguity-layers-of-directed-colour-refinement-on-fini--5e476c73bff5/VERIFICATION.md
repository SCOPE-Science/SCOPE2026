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

# Reproducibility and limits

Execute `python3 verify_tournaments.py` in an ordinary Python 3 environment. No external modules, downloads, or input data are required. The verifier reconstructs every unlabelled tournament up to seven vertices by complete vertex extension and degree-preserving canonization, then refines all members of each order with one global palette. Its assertions prove the claimed counts and the full list of nonsingleton classes relative to this finite exhaustive enumeration; it also verifies explicit six-vertex witnesses and their transitive-four-vertex counts.

The repeated computations returned isomorphism counts `1,1,2,4,12,56,456` and refinement-class counts `1,1,2,4,12,55,451`. The complete order-seven exception distribution is three doubletons and one tripleton. The canonical code and every integer in the table are defined in `RESULT.md` and checked by the script.

This is a reproducible computational certificate for a finite theorem, together with a mathematical argument that its search domain is exhaustive. The code does not attempt to prove results at larger orders. It is not a proof-assistant formalization, and no external or independent audit has been performed.
