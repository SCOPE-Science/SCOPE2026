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
The bundled checker `artifacts/verify.py` reconstructs
\[
\{e_1,e_2,e_1\}=e_3,
\qquad
\alpha=\operatorname{diag}(1,-1,-1),
\]
and the product-structure integrability identity.

It symbolically verifies the two affine product-structure families and the two isolated structures \(\pm\alpha\), the perfect-product criterion, the automorphism group, and the conjugation formulas.

It exhaustively enumerates every endomorphism commuting with \(\alpha\) over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7.
\]
After imposing \(E^2=I\), excluding \(\pm I\), and testing the product identity on every ordered basis triple, the exact counts are
\[
8,\quad12,\quad16.
\]
In each field exactly two structures are perfect and exactly four automorphism-conjugacy orbits occur.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field classification is proved by the symbolic case analysis in `RESULT.md`.
