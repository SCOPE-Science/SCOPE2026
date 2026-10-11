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

Run `python3 artifacts/verify.py` with Python 3. The verifier uses only the standard library. It reconstructs the four-cube edges, their line graph, all shortest-path distances, the full scale-two Rips face set, the repeated-vertex Morse matching, every Hasse cover, and a complete topological sort of the Morse-oriented Hasse diagram.

Expected decisive output includes `FACE_VECTOR [32, 336, 1568, 3672, 4512, 2848, 832, 96]`, `MATCHED_PAIRS 6943 CRITICAL {0: 1, 3: 1, 5: 8}`, `HASSE_COVERS 66304`, `DAG_VERTICES 13896`, `REDUCED_F2_BETTI [0, 0, 0, 1, 0, 8, 0, 0]`, and `VERIFY_OK`.

The finite certificate proves the integral homology through the critical-cell dimensions and acyclicity of the matching. The mod-two boundary ranks are a cross-check, not a substitute for the integral Morse argument. No computation here determines the homotopy classes of the \(5\)-cell attaching maps.
