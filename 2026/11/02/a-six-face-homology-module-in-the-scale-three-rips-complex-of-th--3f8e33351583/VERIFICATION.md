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

# Reproducible finite checks

Run `python3 verify_subdiv_cube.py` (standard library only). This reconstructs all vertex distances, the complete Rips face poset and Hasse graph, the perfect acyclic matching, six induced octahedral three-sphere cycles, and primitive coefficient cocycles. The checker also evaluates every one of the 48 geometric automorphisms by signed simplicial Lefschetz formulas, and determines the local orientation degree of every fixed face sphere. The output should contain `SUBDIVIDED_CUBE_RIPS3_PERFECT_MORSE_SIX_FACE_SPHERES_48_SYMMETRIES_OK`.

The general mathematical inference from the checked certificates is given in `RESULT.md`. No claims are made about thresholds other than three or all points along graph edges. The program provides repeatability of the finite calculation; no independent audit has been performed.
