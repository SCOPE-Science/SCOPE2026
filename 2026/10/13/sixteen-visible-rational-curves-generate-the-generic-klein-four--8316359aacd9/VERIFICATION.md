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

The proof uses three independent layers.

First, the source quartic restricted to a coordinate line is a binary quartic in the squared ratio. A repeated root would make the source surface singular, so the six discriminants \(b_{ij}^2-4a_i a_j\) are nonzero on the smooth locus. The resulting four fixed points per source coordinate line become two quotient points per quotient coordinate edge.

Second, at such a quotient point the two missing coordinates and \(Q\) give local coordinates with equation analytically equivalent to \(uv+w^2=0\). This proves the \(A_1\) type and shows how the two coordinate-face conics separate on the minimal resolution. The coordinate hyperplane is locally twice one ruling, giving the global relation \(H=2C_i+F_i\).

Third, `verify.py` performs exact finite arithmetic on the resulting incidence data. It checks that the four face vectors have binary rank \(3\), so adjoining the four half-hyperplane classes has index \(2^3\) in \(A_1^{\oplus12}\oplus\langle4\rangle\). It obtains discriminant \(2^8\). The same script recomputes from the source's two stated gluing steps that \((M_{2,2}\oplus\langle4\rangle)'\) also has discriminant \(2^8\).

The checker does not replace the analytic quotient argument and does not attempt to certify statements for special members where the Picard rank jumps or a face conic degenerates.
