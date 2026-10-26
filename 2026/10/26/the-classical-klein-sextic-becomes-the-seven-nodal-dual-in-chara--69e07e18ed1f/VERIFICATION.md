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

The accompanying `CHECK.py` uses only the Python 3 standard library. It verifies over \(\mathbb F_2\) the homogeneous degree-eighteen identity \(G(\nabla f)=fQ\) by exact sparse polynomial multiplication. It constructs \(\mathbb F_8\) using \(t^3+t+1\), recovers seven singular-point coordinates and verifies that every pair lies on a line containing exactly three of those points.

The infinite-geometric assertions are established in RESULT.md by the explicit partial-derivative and Bézout arguments, not by finite-field enumeration. The smooth normalization and Frobenius assertion follow from genus, degree and Riemann–Hurwitz. Independent audit has not been performed.
