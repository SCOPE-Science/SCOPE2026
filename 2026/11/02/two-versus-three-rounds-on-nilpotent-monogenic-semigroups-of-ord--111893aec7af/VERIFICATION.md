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

The exact 12-class first-move atomic-profile certificate is printed by `verify_ef2.py`, which cross-checks its eight Boolean tests against the complete atomic diagram with named zero. The independent `verify_game.py` computes recursive Ehrenfeucht–Fraïssé types directly from equality and ternary multiplication for ranks 1, 2, and 3. Both scripts require Python 3 only. Their captured stdout appears in the two `.txt` files.

The three-quantifier sentence is also proved analytically: its truth in \(N_t\) is equivalent to the existence of an integer \(i\) satisfying \(5i<t\le6i\), giving witness \(i=3\) at \(t=16\) and no solution at \(t=20\). The finite enumerations are complete for the stated two structures; no infinite family classification is claimed. Independent audit has not been performed.
