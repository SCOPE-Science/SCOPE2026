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

The exact Python-standard-library command is `python3 verify.py`, executed from the directory containing this file, `verify.py`, and `verification_output.txt`. The tested interpreter required no external numerical libraries. The successful run output, with final line `VERIFY_OK_GP_N_3_SCALE_TWO_WEDGE_AND_DIHEDRAL_MODULE`, appears in `verification_output.txt`.

For each of the 54 integers \(19\le n\le72\), the code independently constructs the graph, square graph, all cliques,  closed-neighborhood simplices, the 2n exceptional triangles, and the six-cycle list. It compares the full face vector with the formula. For eight representative values, it explicitly replays all \(8n\) free-face pairs collapsing the centered complex to the original graph, constructs every signed integral octahedral two-cycle, proves its chain boundary zero by exact integer coefficients, and verifies the rotation and reflection images. For nine sample values it computes all mod-two boundary ranks by exact bit-vector elimination. At \(n=18\), it enumerates the entire complex and establishes the reduced mod-two Betti vector \((0,0,23,0)\).

This finite verification cannot certify the infinitely many parameter values or the absolute originality of the theorem. The uniform cyclic-index classification, cellular homotopy argument, and integral lattice basis appear in `RESULT.md`. No independent audit was performed.
