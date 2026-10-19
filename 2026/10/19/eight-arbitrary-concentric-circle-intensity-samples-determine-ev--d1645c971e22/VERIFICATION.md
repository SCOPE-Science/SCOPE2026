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

The included exact symbolic script `verify.py` constructs three exact Hermitian lifts using five unit-circle nodes and three nodes on second circles with radii \(1/2\), \(2\), and \(3\). It checks rank eight, each exact diagonal kernel and the corresponding sharp rank-two kernel-angle constants; it separately verifies rank defects for repeated points and equal radii. Its run output is in `verification-output.txt`; all symbolic comparisons use exact SymPy arithmetic.

The infinite family of angular arrangements is covered by the displayed two-stage polynomial interpolation proof, not extrapolated from the example. Global cardinality minimality follows from a real two-plane of Hermitian lift null vectors, continuity of the odd determinant and spectral decomposition. The rank-two projection bound follows from singular-value ordering, including equality. This report does not assert independent audit, a formalized proof, or stability uniformly over nearly coincident angular sites.
