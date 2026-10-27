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

# Reproduction

Execute `python3 check.py` from the directory containing this document. Python standard library suffices. The expected final line is `BOOLEAN_PRECONDITIONAL_REDUCT_OK`.

The script enumerates all permitted normalized antitone coordinates for one through four Boolean atoms and checks their Dedekind-number counts. It generates all negation reducts on one through three atoms and verifies, for each, every finite substitution into the five preconditional axioms, conditional identity, and semicomplementation. It compares the double-negation-inflation cases to all undirected simple-graph polarities. It also checks the four operation tables on the four-element Boolean algebra.

The finite checker does not certify a universal claim by enumeration; the induction-free symbolic proof in `RESULT.md` handles arbitrary finite carriers. No independent audit was performed.
