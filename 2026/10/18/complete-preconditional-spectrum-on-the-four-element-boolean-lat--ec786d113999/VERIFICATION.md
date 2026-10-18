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

The file `verify_boolean_preconditionals.py` is a standalone Python 3 checker requiring only the standard library. Run it with `python3 verify_boolean_preconditionals.py`. It enumerates every tuple from the proved first-four-axiom normal form and tests the original five defining inequalities directly for all element triples.

Actual result: all 144 first-four-axiom candidates were checked; exactly 41 satisfy all five axioms, with 24 atom-swap orbits. The bottom-row distribution is 4, 6, 6, 25; induced operations number 25 (15 orbits), noninduced 16 (9), the T class 4 (3), and the F class 2 (2). For every one of the 144 candidates, the direct P5 classification agreed exactly with the symbolic necessary-and-sufficient conditions. The checker also tests one explicit T-not-F witness and one F-not-Heyting witness.

The independent completeness of the finite enumeration is mathematical, not procedural: the proof shows that any operation satisfying P1–P4 lies among exactly these 144 parameter tables. No claim is made for larger Boolean lattices, or for independence of this review.
