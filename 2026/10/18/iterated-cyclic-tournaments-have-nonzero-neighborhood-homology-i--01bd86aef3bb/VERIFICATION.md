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

# Verification and reproducibility

Run `python verify_neighborhood.py` and `python verify_cover.py` from the directory containing these files, using standard Python 3. The programs import no third-party libraries and require no external data. Both terminate by printing an explicit `ALL_CHECKS_PASS` marker when their assertions hold.

The first script constructs arc sets directly, verifies tournament orientation for every unordered pair, enumerates the entire out-neighborhood face sets by subset generation, computes reduced Euler characteristics, and computes mod-two boundary ranks in every degree for the small instances. It verifies the two distinct nine-vertex substitution examples and the fifteen-vertex cyclic-five-base instance. It exhaustively counts the faces and Euler characteristic of the 27-vertex instance, but does **not** claim full homology-rank or integral Smith-normal-form verification there.

The second script independently builds the face sets from the abstract three-cone formula and compares the complete face set, all pairwise intersections, and the empty geometric triple intersection to a direct adjacency-based construction. These are exact finite validations of the proof's critical cover identity.

The integral and all-parameter homotopy result is established by the mathematical three-cone, homotopy-pushout and induction argument in `RESULT.md`, not by extrapolation from finite computational observations. In particular, mod-two calculations alone do not detect odd torsion or prove a homotopy wedge.
