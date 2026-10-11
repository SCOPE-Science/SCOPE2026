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

Execute the self-contained script `python3 artifacts/verify.py` from the directory containing this file. It requires only the Python standard library. The script reconstructs the integral oriented three-cycle with twelve tetrahedra, checks vanishing of its full signed boundary, confirms all tetrahedra are in the Alexander dual by testing all four-subsets, verifies absence of all four possible five-vertex cofaces of the distinguished tetrahedron, and verifies the integral pairing has absolute value one. It then exhaustively checks all Alexander-dual faces under vertex clamping for each \(8\le n\le13\), verifying their images remain faces of the eight-vertex base. On success it emits `VERIFY_OK`.

The complete infinite-parameter proof does **not** rely on extrapolation from these finite enumerations: its critical steps are the four-gap connectivity equivalence, a fixed integral chain/cochain witness and graph-Lipschitz retraction valid for all \(n\ge8\), followed by combinatorial Alexander duality. Finite enumeration is only a secondary consistency test. No full homology classification, exclusion of torsion outside the exhibited summand, or independently performed audit is claimed.
