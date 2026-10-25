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

# Verification evidence and limits

Execute `python3 verify_relative_collapse.py` using Python 3.10+ and the standard library. The executable reconstructs the 16 stable triple graph vertices directly from the cyclic adjacency definition; computes all faces of the independence and open-neighborhood complexes from the graph independently; verifies every dihedral generator/permutation preserves adjacency; and replays all 14 orbit representatives, expanding them into the full dihedral orbit at each current face-set stage.

Every one of the 176 collapse pairs is checked to consist of a free codimension-one simplex and its **unique current** coface, and the orbit is checked for duplicate faces. The terminal face set equals the complete independently constructed neighborhood complex. The output `relative_verification_output.txt` records the successful replay and 16 signed simplicial Lefschetz trace comparisons.

This proves a finite graph-specific collapse and an orientation-character corollary. No enumeration can alone establish a statement for all larger Schrijver parameters; no such statement is claimed. Previously established absolute sphere homotopy types are used as context, not re-certified as new discoveries. An independent scientific audit has not been performed.
