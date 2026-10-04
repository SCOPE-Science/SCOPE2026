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

The published graph description identifies coherent paths with nonzero vectors in \(\{-1,0,1\}^m\) and flips with coordinate moves of \(\ell_1\)-length one. The general proof classifies all ways an ambient \(\ell_1\)-geodesic could be forced through the deleted origin. Exactly the opposite unit vectors have this obstruction; for them a four-edge detour is explicit.

`verifier.py` constructs the graph directly for \(m=2,3,4,5\), computes every source-to-target distance by breadth-first search, and checks the pointwise metric formula, every coefficient of \(D_m(z)\), and the closed formula for the Wiener index.

The replay output is:

`VERIFY_OK exact signohedron flip-distance enumerator`

The verifier is deliberately finite and does not serve as an exhaustive proof for arbitrary \(m\). The arbitrary-dimensional statement is supported by the coordinate-path argument and exact product enumeration in `RESULT.md`.
