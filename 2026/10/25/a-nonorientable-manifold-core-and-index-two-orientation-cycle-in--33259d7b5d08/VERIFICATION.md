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
# Reproduction of exact finite checks

Execute `python verify.py` with Python 3 and SymPy. The program enumerates every graph-independent vertex subset up to size five, constructs the signed simplicial boundary maps using increasing-order orientations, and computes integer Smith normal forms. All 80 tetrahedra and 144 triangles are covered. A consistent orientation is obstructed by a closed dual cycle with required sign product \(-1\). The relative matrix is generated from the exact specified tetrahedral orbit, not a hand-entered table. The full top-cycle coefficient certificate is independently recomputed by nullspace normalization and then checked directly against the boundary.

Expected result: `VERIFY_OK_EXCEPTIONAL_CIRCULANT_MANIFOLD_CORE` and all assertions successful, with detailed JSON numerical data in `verification_output.txt`. The reproduced finite data verifies the manifold, torsion, relative homology and primitive cycle. The separate previously published shellability result is used solely to identify the full complex's homotopy type. This check does not provide the core's fundamental group or identify its homeomorphism type.
