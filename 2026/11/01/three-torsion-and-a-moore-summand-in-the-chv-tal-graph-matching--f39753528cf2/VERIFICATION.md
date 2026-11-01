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

# Reproducible mathematical checks

Execute `python verify_chvatal.py` with Python 3, NetworkX and SymPy installed. The script uses the canonical twelve-vertex Chvátal graph and a fixed edge ordering. It enumerates all nonempty ordinary matchings, constructs the specified acyclic Morse face-poset matching, completely topologically sorts the directed Hasse graph, computes signed gradient-path differentials, and computes the integer Smith normal form. Independent original simplicial chain reductions over the fields of 2, 3 and 5 elements verify the expected dimension jump.

The recorded run in `verification_output.txt` gives 2,835 faces, 1,396 pairs, critical vector (one zero-cell, 35 three-cells, seven four-cells), 10,816 cover relations, integral Morse Smith diagonal six ones and one three, and terminal token `CHVATAL_MATCHING_THREE_TORSION_VERIFIED`. All checks were actually executed. The finite algorithm is exhaustive for the stated graph, not a universal proof or external verification.
