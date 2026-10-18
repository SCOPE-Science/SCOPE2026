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

Execute `python3 verify_truncated_tetra_character.py` with the standard Python 3 library. The executable reconstructs vertices, all 18 graph edges, 1009 nonempty matchings, 493 pairings and one critical vertex plus twenty-two three-cells. It verifies the complete 3558-incidence directed Hasse graph is acyclic. It evaluates the 24 tetrahedral permutations with two independently implemented exact signed Lefschetz methods and checks all five class traces and representation multiplicities.

Expected face vector: `(18, 117, 332, 390, 144, 8)`; expected class character: `(22, 0, 2, -2, -2)`; expected rational multiplicities in the implemented order: `(0, 1, 3, 2, 3)`. The code was executed successfully on the actual included source file before packaging. It proves only this finite case and supplies no higher-dimensional family classification, publication-priority guarantee or independent mathematical audit.
