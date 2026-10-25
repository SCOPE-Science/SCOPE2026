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

# Reproducibility

Run `python3 artifacts/verify.py` from the directory containing this file; only the Python standard library is required.

The checker exhaustively enumerates 23,713 canonical binary-tree vertices across sizes \(1\) through \(10\), computes their rational barycenters and squared radii, enumerates 510 signed parallelepiped vertices across sizes \(2\) through \(9\), and independently checks 70 generating-function coefficients and 99 ordering cases. The executed output was:

`VERIFY_OK tree_vertices=23713 signed_vertices=510 gf_coefficients=70 comparison_dimensions=99`

These checks can detect implementation and algebraic errors in tested cases. The all-dimension theorem is justified by the proof and the formal power-series identities in `RESULT.md`, not by treating an enumeration cutoff as exhaustive.

The original polytope realizations and vertex barycenter are taken from the cited primary sources. The scientific novelty comparison remains limited by possible unindexed equivalent calculations. Independent mathematical assessment has not been performed.
