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

The all-parameter proof has four critical ingredients: the common-neighbor facets of one parity component; uniqueness of a facet for every face with at least three vertices; the explicit relative collapse of each facet to its full \(1\)-skeleton plus the triangles through one chosen apex; and the reduction of the resulting fundamental group to the filled-square \((d-1)\)-cube.

`artifacts/verify.py` reconstructs the actual neighborhood components for \(4\le d\le7\). It checks facet intersections and ownership of higher faces, verifies the explicit matching covers every deleted face exactly once, and for \(4\le d\le6\) checks acyclicity of the corresponding directed Hasse graph. It then computes mod-two homology of both the original and collapsed complexes.

The replay output is stored in `artifacts/verification_output.txt` and gives degree-two ranks \(7,31,111,351\) for \(d=4,5,6,7\), with no other positive-degree homology in the tested cases.

The finite replay is corroborative only. The theorem for arbitrary \(d\ge4\) depends on the symbolic collapse and simply-connectedness proof in `RESULT.md`; no finite enumeration is presented as an infinite proof.
