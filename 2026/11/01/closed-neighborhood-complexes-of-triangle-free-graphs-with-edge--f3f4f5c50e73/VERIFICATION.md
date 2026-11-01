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

The complete theorem and its all-size proof are in `RESULT.md`. The included `checker.py` is a standalone standard-Python finite consistency check, not an infinite proof or an independent audit. Execute `python checker.py` to reproduce tests of exact free-face conditions and mod-two simplicial boundary ranks. The executed run reported 3,430 qualifying graphs, 95,179 total initial nonempty faces, 23,172 elementary collapse pairs and 1,430 instances of four-cycles, with all comparisons passing.

The script enumerates all finite connected labeled triangle-free, square-edge-disjoint simple graphs through six vertices, plus cycles, tree paths, square bouquets and randomized qualifying graphs with seven through nine vertices. It separately constructs all simplices of the closed-neighborhood complex, constructs the proposed tetrahedral core, verifies each proposed collapse by testing unique codimension-one cofaces and maximality, then computes reduced mod-two Betti numbers from boundary matrices. It does not establish integral torsion-freeness, infinite quantification or originality; the proof supplies those mathematical steps and literature inspection addresses novelty risk.

Independent audit has not been performed.
